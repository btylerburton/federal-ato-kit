"""Exercise the optional TUI with real durable sessions and terminal-sized layouts."""
import asyncio
from datetime import date
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
if HAS_TEXTUAL:
    from textual.widgets import Button, Checkbox, ContentSwitcher, Input, Select, Static
    from wizard_session import WizardSession
    from wizard_tui import WizardApp


@unittest.skipUnless(HAS_TEXTUAL, 'Optional Textual environment not installed')
class WizardTuiTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='wizard-tui-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / 'fixture-service'
        self.repo.mkdir()
        subprocess.run(['git', 'init', '-q', str(self.repo)], check=True)
        subprocess.run(['git', '-C', str(self.repo), '-c', 'user.name=Fixture',
                        '-c', 'user.email=fixture@example.invalid', 'commit', '--allow-empty',
                        '-qm', 'Synthetic test fixture'], check=True)
        self.workspace = self.root / 'authoring'

    def session(self):
        return WizardSession(self.repo, self.workspace)

    async def click_scrolled(self, app, pilot, selector):
        widget = app.query_one(selector)
        widget.scroll_visible(animate=False, immediate=True)
        await pilot.pause()
        self.assertTrue(await pilot.click(selector))
        await pilot.pause()

    def valid_answers(self, session):
        fields = {'system_owner': 'Example owner', 'environment': 'test', 'mode': 'lato',
                  'scope_confirmed': True, 'data_categories': ['synthetic'],
                  'boundary_summary': 'One service with an external browser'}
        for key, value in fields.items():
            session.update(key, value)

    async def test_defaults_autosave_quit_and_resume_at_80_columns(self):
        session = self.session()
        session.update('date', '')
        session.update('mode', 'LATO')
        session = self.session()
        app = WizardApp(session)
        async with app.run_test(size=(80, 24)) as pilot:
            self.assertEqual(app.query_one('#date', Input).value, date.today().isoformat())
            self.assertEqual(app.query_one('#system_name', Input).value, self.repo.name)
            self.assertEqual(app.query_one('#mode', Select).value, 'lato')
            self.assertFalse(app.query_one('#scope_confirmed', Checkbox).value)
            self.assertIs(app.query_one('#baseline', Select).value, Select.NULL)
            await self.click_scrolled(app, pilot, '#system_owner')
            await pilot.press(*'Example owner')
            await pilot.pause()
            saved = json.loads(session.answers_path.read_text())
            self.assertEqual(saved['system_owner'], 'Example owner')
            await pilot.click('#next')
            await pilot.pause()
            self.assertEqual(app.query_one('#sections', ContentSwitcher).current, 'scope')
            await pilot.press('ctrl+s', 'ctrl+q')
        reopened = self.session()
        self.assertEqual(reopened.current_step, 'scope')
        async with WizardApp(reopened).run_test(size=(80, 24)) as pilot:
            self.assertEqual(pilot.app.query_one('#system_owner', Input).value, 'Example owner')
            self.assertEqual(pilot.app.query_one('#sections', ContentSwitcher).current, 'scope')

    async def test_scope_validation_and_literal_user_text(self):
        session = self.session()
        app = WizardApp(session)
        async with app.run_test(size=(100, 40)) as pilot:
            await pilot.pause()
            app.query_one('#system_name', Input).value = '[red]Example[/red]'
            await pilot.click('#step-scope')
            await pilot.pause()
            app.query_one('#mode', Select).value = 'ato'
            app.query_one('#boundary_summary', Input).value = 'unknown'
            app.query_one('#data_categories', Input).value = 'public, synthetic'
            await pilot.pause()
            self.assertIn('baseline', session.issues())
            self.assertIn('boundary_summary', session.issues())
            self.assertIn('scope_confirmed', session.issues())
            self.assertEqual(session.answers['data_categories'], ['public', 'synthetic'])
            self.assertTrue(app.query_one('#generate', Button).disabled)
            self.assertIn('[red]Example[/red]', str(app.query_one('#review-summary', Static).render()))
            app.query_one('#baseline', Select).value = 'low'
            app.query_one('#boundary_summary', Input).value = 'A service and its external clients'
            app.query_one('#scope_confirmed', Checkbox).value = True
            await pilot.pause()
            self.assertNotIn('baseline', session.issues())
            self.assertNotIn('boundary_summary', session.issues())
            self.assertNotIn('scope_confirmed', session.issues())

    async def test_legacy_topology_survives_text_edits_and_resumes_at_review(self):
        session = self.session()
        topology = {'nodes': [{'id': 'service', 'title': 'Service', 'boundary': 'inside'}],
                    'flows': []}
        session.update('topology', topology)
        state = json.loads(session.state_path.read_text())
        state['step'] = 'topology'
        session.state_path.write_text(json.dumps(state))
        app = WizardApp(self.session())
        async with app.run_test(size=(80, 24)) as pilot:
            self.assertEqual(app.query_one('#sections', ContentSwitcher).current, 'review')
            await pilot.click('#step-system')
            await pilot.pause()
            app.query_one('#system_owner', Input).value = 'Updated owner'
            await pilot.pause()
            await pilot.press('ctrl+s', 'ctrl+q')
        reopened = self.session()
        self.assertEqual(reopened.answers['system_owner'], 'Updated owner')
        self.assertEqual(reopened.answers['topology'], topology)

    async def test_inheritance_autosaves_without_scope_approval(self):
        app = WizardApp(self.session())
        async with app.run_test(size=(100, 40)) as pilot:
            await pilot.click('#step-inheritance')
            await pilot.pause()
            app.query_one('#inheritance-hosting_service', Select).value = 'cloud-gov-pages'
            app.query_one('#inheritance-egress_proxy', Select).value = 'no'
            await pilot.pause()
            saved = json.loads(app.session.answers_path.read_text())
            self.assertEqual(saved['inheritance']['hosting_service'], 'cloud-gov-pages')
            self.assertEqual(saved['inheritance']['egress_proxy'], 'no')
            self.assertFalse(saved['scope_confirmed'])

    async def test_question_help_click_and_keyboard_preserve_answers(self):
        session = self.session()
        app = WizardApp(session)
        async with app.run_test(size=(80, 24)) as pilot:
            await pilot.click('#step-inheritance')
            await pilot.pause()
            before = session.answers_path.read_bytes()
            for key in ('egress_proxy', 'gsa_common_controls', 'org_dependency_management', 'sha_pinning'):
                with self.subTest(question=key):
                    detail = app.query_one('#help-detail-' + key, Static)
                    self.assertFalse(detail.display)
                    await self.click_scrolled(app, pilot, '#help-' + key)
                    self.assertTrue(detail.display)
                    self.assertEqual(session.answers_path.read_bytes(), before)
                    # Keyboard activation closes the same focused help button.
                    await pilot.press('enter')
                    await pilot.pause()
                    self.assertFalse(detail.display)
                    self.assertEqual(session.answers_path.read_bytes(), before)
            self.assertEqual(app.query_one('#sections', ContentSwitcher).current, 'inheritance')
            self.assertFalse(session.answers.get('scope_confirmed'))

    async def test_background_generation_disables_edits_and_recovers_from_error(self):
        session = self.session()
        self.valid_answers(session)
        app = WizardApp(session)
        started, release = threading.Event(), threading.Event()

        def generate():
            started.set()
            if not release.wait(timeout=10):
                raise TimeoutError('Test did not release generation')
            return {'total_controls': 58}

        async with app.run_test(size=(100, 40)) as pilot:
            await pilot.click('#step-review')
            await pilot.pause()
            with patch.object(session, 'generate', side_effect=generate):
                try:
                    await self.click_scrolled(app, pilot, '#generate')
                    self.assertTrue(await asyncio.to_thread(started.wait, 3))
                    self.assertTrue(app.generating)
                    self.assertTrue(app.query_one('#system_owner', Input).disabled)
                    await pilot.press('ctrl+q')
                    self.assertTrue(app.is_running)
                finally:
                    release.set()
                await app.workers.wait_for_complete()
            self.assertFalse(app.generating)
            self.assertFalse(app.query_one('#system_owner', Input).disabled)
            self.assertIn(str(self.workspace / 'project'), str(app.query_one('#generation-result', Static).render()))
            with patch.object(session, 'generate', side_effect=ValueError('Synthetic generation failure')):
                await self.click_scrolled(app, pilot, '#generate')
                await app.workers.wait_for_complete()
            self.assertIn('Synthetic generation failure', str(app.query_one('#generation-result', Static).render()))
            self.assertFalse(app.query_one('#generate', Button).disabled)

    async def test_text_only_navigation_generates_real_lato_draft_without_topology(self):
        session = self.session()
        self.valid_answers(session)
        self.assertEqual(session.answers['topology'], {'nodes': [], 'flows': []})
        self.assertFalse((self.workspace / 'project').exists())
        app = WizardApp(session)
        async with app.run_test(size=(100, 40)) as pilot:
            self.assertEqual([button.id for button in app.query('#sidebar Button')],
                             ['step-system', 'step-scope', 'step-inheritance', 'step-review'])
            self.assertEqual(len(app.query('#topology')), 0)
            await pilot.click('#step-inheritance')
            await pilot.pause()
            await pilot.click('#next')
            await pilot.pause()
            self.assertEqual(app.query_one('#sections', ContentSwitcher).current, 'review')
            self.assertFalse(app.query_one('#generate', Button).disabled)
            await self.click_scrolled(app, pilot, '#generate')
            await app.workers.wait_for_complete()
            report = json.loads((self.workspace / 'project' / 'wizard-report.json').read_text())
            self.assertEqual(report['selected_shells'], 58)
            manifest = json.loads((self.workspace / 'project' / 'manifest.json').read_text())
            self.assertTrue(any(module['id'] == 'diagram-readiness' and module['kind'] == 'gap'
                                for module in manifest['modules']))
            self.assertFalse(any(module['kind'] == 'diagram' for module in manifest['modules']))
            self.assertEqual(json.loads(session.answers_path.read_text())['topology'],
                             {'nodes': [], 'flows': []})
            self.assertIn('Draft generated:', str(app.query_one('#generation-result', Static).render()))


if __name__ == '__main__':
    unittest.main()
