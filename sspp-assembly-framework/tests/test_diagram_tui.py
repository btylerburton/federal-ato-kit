"""Headless terminal interactions backed by real disposable diagram workspaces."""
import asyncio
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
HAS_TEXTUAL = importlib.util.find_spec('textual') is not None
HAS_DASHBOARD = importlib.util.find_spec('diagram_dashboard') is not None
if HAS_TEXTUAL and HAS_DASHBOARD:
    from textual.widgets import Button, Checkbox, Input, Select, Static, TabbedContent
    from diagram_dashboard import DiagramDashboard
    from diagram_tui import DiagramApp


@unittest.skipUnless(HAS_TEXTUAL and HAS_DASHBOARD, 'Textual and live diagram dashboard required')
class DiagramTuiTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='diagram-tui-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.repository = self.root / 'source'
        self.repository.mkdir()
        self.workspace = self.root / 'workspace'
        self.git('init', '-q')
        (self.repository / 'service.py').write_text('Client requests API\nAPI stores records\n')
        self.git('add', 'service.py')
        self.git('-c', 'user.name=Synthetic Test', '-c', 'user.email=test@example.invalid',
                 '-c', 'commit.gpgsign=false', 'commit', '-qm', 'Synthetic diagram fixture')
        evidence = [{'path': 'service.py', 'lines': [1, 2]}]
        self.proposal = {
            'schema_version': 1, 'repository_revision': self.git('rev-parse', 'HEAD').strip(),
            'system_name': 'Example service', 'environment': 'Test', 'date': '2026-11-24',
            'assumptions': [], 'unknown_fields': ['flows/request/authentication'],
            'nodes': [
                {'id': 'client', 'title': 'Client', 'boundary': 'outside', 'kind': 'actor',
                 'status': 'source-supported', 'evidence': evidence},
                {'id': 'api', 'title': 'API', 'boundary': None, 'kind': 'component',
                 'status': 'hypothesis', 'evidence': []}],
            'flows': [{'id': 'request', 'from': 'client', 'to': 'api', 'data': 'Requests',
                       'protocol': 'HTTPS', 'authentication': None, 'storage': 'None',
                       'status': 'source-supported', 'evidence': evidence}]}

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.repository), *args], capture_output=True,
                              text=True, check=True).stdout

    def dashboard(self, proposal=False):
        dashboard = DiagramDashboard(self.repository, self.workspace)
        dashboard.refresh()
        if proposal:
            dashboard.proposal_path.write_text(json.dumps(self.proposal))
        return dashboard

    async def settled(self, app, pilot):
        await app.workers.wait_for_complete()
        await pilot.pause()

    async def click(self, app, pilot, selector):
        app.query_one(selector).scroll_visible(animate=False, immediate=True)
        await pilot.pause()
        self.assertTrue(await pilot.click(selector))
        await self.settled(app, pilot)

    async def tab(self, app, pilot, name):
        app.query_one('#sections', TabbedContent).active = name
        await pilot.pause()

    async def answer(self, app, pilot, key, value):
        await self.tab(app, pilot, 'questions')
        app.query_one('#question', Select).value = key
        await pilot.pause()
        question = app.selected_question
        if question.get('choices'):
            app.query_one('#answer-choice', Select).value = value
        else:
            app.query_one('#answer-text', Input).value = value
        await pilot.pause()
        await self.click(app, pilot, '#save-answer')

    async def test_invalid_proposal_is_not_reported_as_refresh_success_and_prompt_copies(self):
        self.proposal['nodes'][0]['id'] = 'bad id'
        dashboard = self.dashboard(proposal=True)
        app = DiagramApp(dashboard)
        async with app.run_test(size=(80, 24)) as pilot:
            await self.settled(app, pilot)
            status = str(app.query_one('#status', Static).render())
            self.assertIn('Proposal needs correction:', status)
            self.assertIn('nodes[0].id', status)
            self.assertNotIn('Refresh complete', status)
            await self.click(app, pilot, '#copy-prompt')
            await pilot.click('#copy-all')
            self.assertEqual(app.clipboard, dashboard.handoff_text())

    async def test_missing_proposal_explains_handoff_at_both_terminal_sizes(self):
        for size in ((80, 24), (100, 40)):
            with self.subTest(size=size):
                dashboard = self.dashboard()
                app = DiagramApp(dashboard)
                async with app.run_test(size=size) as pilot:
                    await self.settled(app, pilot)
                    self.assertEqual(app.state['stage'], 'needs-analysis')
                    handoff = str(app.query_one('#handoff', Static).render())
                    self.assertIn(str(dashboard.request_path), handoff)
                    self.assertIn(dashboard.handoff_text(), handoff)
                    for action in ('analyze', 'generate', 'render', 'attach', 'confirm'):
                        self.assertTrue(app.query_one('#' + action, Button).disabled)
                    await self.click(app, pilot, '#runner-consent')
                    self.assertTrue(app.query_one('#analyze', Button).disabled)
                    await pilot.press('ctrl+r')
                    await self.settled(app, pilot)
                    await pilot.press('ctrl+q')

    async def test_auto_import_answers_explicit_confirmation_and_correction(self):
        dashboard = self.dashboard(proposal=True)
        app = DiagramApp(dashboard)
        async with app.run_test(size=(80, 24)) as pilot:
            await self.settled(app, pilot)
            self.assertEqual(app.state['stage'], 'clarify')
            self.assertFalse(app.state['confirmed'])
            await self.answer(app, pilot, 'nodes/api/boundary', 'inside')
            await self.answer(app, pilot, 'flows/request/authentication', 'Anonymous')
            await self.answer(app, pilot, 'nodes/api/review', 'confirmed')
            self.assertEqual(app.state['pending_count'], 0)
            self.assertFalse(app.state['confirmed'])
            self.assertTrue(app.query_one('#confirm', Button).disabled)
            app.query_one('#reviewer', Input).value = 'Synthetic reviewer'
            await pilot.pause()
            self.assertTrue(app.query_one('#confirm', Button).disabled)
            await self.click(app, pilot, '#review-consent')
            self.assertFalse(app.query_one('#confirm', Button).disabled)
            await self.click(app, pilot, '#confirm')
            self.assertTrue(app.state['confirmed'])
            self.assertFalse(app.query_one('#review-consent', Checkbox).value)
            self.assertFalse(app.query_one('#generate', Button).disabled)
            await self.click(app, pilot, '#show-known')
            await self.answer(app, pilot, 'flows/request/authentication', 'Service identity')
            self.assertFalse(app.state['confirmed'])
            self.assertFalse(app.query_one('#review-consent', Checkbox).value)
            state = json.loads((dashboard.root / 'session.json').read_text())
            self.assertEqual(state['answers']['flows/request/authentication'], 'Service identity')
        reopened = DiagramDashboard(self.repository, self.workspace)
        reopened.refresh()
        answers = {q['key']: q['value'] for q in reopened.questions()}
        self.assertEqual(answers['nodes/api/boundary'], 'inside')
        self.assertEqual(answers['flows/request/authentication'], 'Service identity')

    async def test_refresh_detects_new_proposal_and_preserves_mismatch_error(self):
        dashboard = self.dashboard()
        app = DiagramApp(dashboard)
        async with app.run_test(size=(80, 24)) as pilot:
            await self.settled(app, pilot)
            self.assertEqual(app.state['stage'], 'needs-analysis')
            dashboard.proposal_path.write_text(json.dumps(self.proposal))
            await pilot.press('ctrl+r')
            await self.settled(app, pilot)
            self.assertEqual(app.state['stage'], 'clarify')
            original = (dashboard.root / 'proposal.json').read_bytes()
            self.proposal['system_name'] = 'Different proposal'
            dashboard.proposal_path.write_text(json.dumps(self.proposal))
            await pilot.press('ctrl+r')
            await self.settled(app, pilot)
            self.assertEqual(app.state['stage'], 'blocked')
            self.assertEqual((dashboard.root / 'proposal.json').read_bytes(), original)
            self.assertTrue(app.query_one('#generate', Button).disabled)
            self.assertTrue(app.query_one('#save-answer', Button).disabled)

    async def test_structured_preview_and_generation_with_real_backend(self):
        dashboard = self.dashboard(proposal=True)
        dashboard.refresh()
        for key, value in [('nodes/api/boundary', 'inside'),
                           ('flows/request/authentication', 'Anonymous'), ('nodes/api/review', 'confirmed')]:
            dashboard.answer(key, value)
        dashboard.confirm('Synthetic reviewer')
        app = DiagramApp(dashboard)
        async with app.run_test(size=(100, 40)) as pilot:
            await self.settled(app, pilot)
            await self.tab(app, pilot, 'preview')
            preview = str(app.query_one('#preview-content', Static).render())
            self.assertIn('service.py', preview)
            self.assertIn('Client', preview)
            self.assertIn('structured preview', preview)
            await self.tab(app, pilot, 'outputs')
            await self.click(app, pilot, '#generate')
            self.assertTrue(app.state['generated'])
            self.assertTrue(app.query_one('#render', Button).disabled)
            self.assertTrue(app.query_one('#attach', Button).disabled)
            await self.tab(app, pilot, 'preview')
            app.query_one('#view', Select).value = 'data-flow'
            await pilot.pause()
            await self.settled(app, pilot)
            preview = str(app.query_one('#preview-content', Static).render())
            self.assertIn('@startuml', preview)
            self.assertIn('Anonymous', preview)

    async def test_missing_endpoints_are_answerable_through_ui(self):
        self.proposal['flows'][0].update({'from': None, 'to': None})
        dashboard = self.dashboard(proposal=True)
        app = DiagramApp(dashboard)
        async with app.run_test(size=(80, 24)) as pilot:
            await self.settled(app, pilot)
            self.assertEqual(app.state['stage'], 'clarify')
            await self.answer(app, pilot, 'flows/request/from', 'client')
            await self.answer(app, pilot, 'flows/request/to', 'api')
            saved = json.loads((dashboard.root / 'session.json').read_text())['answers']
            self.assertEqual(saved['flows/request/from'], 'client')
            self.assertEqual(saved['flows/request/to'], 'api')

    async def test_background_error_recovery_and_quit_guard(self):
        dashboard = self.dashboard(proposal=True)
        app = DiagramApp(dashboard)
        started, release = threading.Event(), threading.Event()

        def failing_answer(*args):
            started.set()
            if not release.wait(timeout=10):
                raise TimeoutError('Test did not release worker')
            raise ValueError('[red]Answer rejected[/red]')

        async with app.run_test(size=(100, 40)) as pilot:
            await self.settled(app, pilot)
            with patch.object(dashboard, 'answer', side_effect=failing_answer):
                app.start_operation('answer', 'nodes/api/boundary', 'inside')
                try:
                    self.assertTrue(await asyncio.to_thread(started.wait, 3))
                    self.assertTrue(app.busy)
                    for selector in ('#refresh', '#answer-text', '#runner-consent', '#reviewer'):
                        self.assertTrue(app.query_one(selector).disabled)
                    await pilot.press('ctrl+q', 'ctrl+r')
                    self.assertTrue(app.busy)
                    self.assertTrue(app.is_running)
                finally:
                    release.set()
                await self.settled(app, pilot)
            self.assertFalse(app.busy)
            self.assertFalse(app.query_one('#refresh', Button).disabled)
            self.assertIn('[red]Answer rejected[/red]', str(app.query_one('#status', Static).render()))
            await self.answer(app, pilot, 'nodes/api/boundary', 'inside')
            self.assertEqual(app.state['pending_count'], 2)


if __name__ == '__main__':
    unittest.main()
