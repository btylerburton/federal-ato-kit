"""Headless tests for optional pre-draft review and terminal copying."""
import importlib.util
import json
import unittest

import test_source_review as fixtures

HAS_TEXTUAL = importlib.util.find_spec('textual') is not None
if HAS_TEXTUAL:
    from copyable_tui import CopyTextScreen
    from source_review_tui import SourceReviewApp, SuggestionScreen
    from textual.widgets import Checkbox, Input, Static, TabbedContent, TextArea
    from wizard_session import WizardSession


@unittest.skipUnless(HAS_TEXTUAL, 'Optional Textual environment not installed')
class SourceReviewTuiTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.fixture = fixtures.SourceReviewTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.review = self.fixture.review

    async def click(self, app, pilot, selector):
        app.query_one(selector).scroll_visible(animate=False, immediate=True)
        await pilot.pause()
        self.assertTrue(await pilot.click(selector))
        # Textual suppresses repeated presses during the button's active effect.
        await pilot.pause(0.3)

    async def test_no_llm_copy_exact_prompt_and_continue(self):
        app = SourceReviewApp(self.review)
        async with app.run_test(size=(80, 24)) as pilot:
            await app.workers.wait_for_complete()
            await self.click(app, pilot, '#source-prompt')
            self.assertIsInstance(app.screen, CopyTextScreen)
            editor = app.screen.query_one('#copy-text', TextArea)
            self.assertEqual(editor.text, self.review.request_path.read_text())
            editor.focus()
            editor.action_select_all()
            await pilot.press('ctrl+shift+c')
            self.assertEqual(app.clipboard, self.review.request_path.read_text())
            await pilot.click('#copy-all')
            self.assertEqual(app.clipboard, self.review.request_path.read_text())
            await pilot.press('escape')
            await pilot.pause()
            await self.click(app, pilot, '#source-continue')
        self.assertTrue(app.return_value)
        self.assertFalse(self.review.path.exists())

    async def test_f4_screen_snapshot_includes_visible_help(self):
        app = SourceReviewApp(self.review)
        async with app.run_test(size=(80, 24)) as pilot:
            await app.workers.wait_for_complete()
            await self.click(app, pilot, '#source-refresh')
            await app.workers.wait_for_complete()
            app.query_one('#source-prompt').focus()
            app.query_one('#source-prompt').scroll_visible(animate=False, immediate=True)
            await pilot.pause()
            await pilot.press('f4')
            await pilot.pause()
            text = app.screen.query_one('#copy-text', TextArea).text
            self.assertIn('Optional:', text)
            self.assertIn(str(self.review.path), text)

    async def test_review_decisions_suggestion_confirmation_and_copy_field(self):
        self.fixture.data['findings'].append({
            'id': 'categories', 'section': 'data', 'status': 'hypothesis',
            'text': 'Public pages, Crawl logs', 'suggested_field': 'data_categories', 'evidence': []})
        self.fixture.import_findings()
        session = self.fixture.session()
        original = session.answers['system_name']
        app = SourceReviewApp(self.review)
        async with app.run_test(size=(100, 40)) as pilot:
            await app.workers.wait_for_complete()
            await pilot.pause()
            self.assertEqual(len(app.query('#intake-cards Checkbox')), 2)
            self.assertEqual(len(app.query('#source-cards Checkbox')), 4)
            app.query_one('#intake-0', Checkbox).value = True
            app.query_one('#intake-3', Checkbox).value = True
            await self.click(app, pilot, '#source-apply')
            self.assertIsInstance(app.screen, SuggestionScreen)
            self.assertEqual(WizardSession(self.fixture.repo, self.fixture.workspace).answers['system_name'], original)
            await pilot.press('escape')
            await pilot.pause()
            await self.click(app, pilot, '#source-apply')
            await pilot.click('#suggestion-confirm')
            await pilot.pause()
            self.assertEqual(WizardSession(self.fixture.repo, self.fixture.workspace).answers['system_name'],
                              'Example public crawler')
            self.assertEqual(WizardSession(self.fixture.repo, self.fixture.workspace).answers['data_categories'],
                             ['Public pages', 'Crawl logs'])
            self.assertEqual(self.review.state['decisions'], {})
            self.assertEqual(app.query_one(TabbedContent).active, 'intake-tab')
            await self.click(app, pilot, '#source-next')
            app.query_one('#source-reviewer', Input).value = 'Human reviewer'
            await self.click(app, pilot, '#source-include-all')
            self.assertTrue(all(checkbox.value for checkbox in app.query('#source-cards Checkbox')))
            self.assertEqual(self.review.state['decisions'], {})
            app.query_one('#include-2', Checkbox).value = False
            app.query_one('#include-3', Checkbox).value = False
            await self.click(app, pilot, '#source-decide')
            await app.workers.wait_for_complete()
            self.assertEqual(self.review.state['decisions']['purpose']['disposition'], 'include')
            self.assertEqual(self.review.state['decisions']['logs']['disposition'], 'include')
            self.assertNotIn('guess', self.review.state['decisions'])
            app.query_one('#include-1', Checkbox).value = False
            await self.click(app, pilot, '#source-decide')
            await app.workers.wait_for_complete()
            self.assertEqual(self.review.state['decisions']['logs']['disposition'], 'exclude')
            await self.click(app, pilot, '#source-refresh')
            await app.workers.wait_for_complete()
            self.assertTrue(app.query_one('#include-0', Checkbox).value)
            self.assertFalse(app.query_one('#include-1', Checkbox).value)
            await self.click(app, pilot, '#source-reviewer')
            await pilot.press('f4')
            await pilot.pause()
            self.assertEqual(app.screen.query_one('#copy-text', TextArea).text, 'Human reviewer')
        resumed = WizardSession(self.fixture.repo, self.fixture.workspace)
        resumed.generate()
        self.assertIn('Example public crawler',
                      (self.fixture.workspace / 'project/source-review/findings.md').read_text())

    async def test_empty_conflicting_and_unattributed_selections_do_not_save(self):
        self.fixture.data['findings'].append({
            **self.fixture.data['findings'][0], 'id': 'alternative', 'text': 'Alternative name'})
        self.fixture.import_findings()
        app = SourceReviewApp(self.review)
        async with app.run_test(size=(80, 24)) as pilot:
            await app.workers.wait_for_complete()
            await self.click(app, pilot, '#source-apply')
            self.assertIn('Select at least one', str(app.query_one('#source-status', Static).render()))
            app.query_one('#intake-0', Checkbox).value = True
            app.query_one('#intake-3', Checkbox).value = True
            await self.click(app, pilot, '#source-apply')
            self.assertIn('Select only one', str(app.query_one('#source-status', Static).render()))
            self.assertFalse((self.fixture.workspace / 'intake/answers.json').exists())
            await self.click(app, pilot, '#source-next')
            await self.click(app, pilot, '#source-decide')
            self.assertIn('No inclusion changes', str(app.query_one('#source-status', Static).render()))
            await self.click(app, pilot, '#include-0')
            await self.click(app, pilot, '#source-decide')
            self.assertIn('human reviewer', str(app.query_one('#source-status', Static).render()))
            self.assertEqual(self.review.state['decisions'], {})

    async def test_concurrent_intake_edit_is_preserved(self):
        self.fixture.import_findings()
        self.fixture.session()
        app = SourceReviewApp(self.review)
        async with app.run_test(size=(100, 40)) as pilot:
            await app.workers.wait_for_complete()
            app.query_one('#intake-0', Checkbox).value = True
            await self.click(app, pilot, '#source-apply')
            other = WizardSession(self.fixture.repo, self.fixture.workspace)
            other.update('system_name', 'Concurrent human edit')
            await pilot.click('#suggestion-confirm')
            await pilot.pause()
            self.assertEqual(WizardSession(self.fixture.repo, self.fixture.workspace).answers['system_name'],
                             'Concurrent human edit')
            self.assertIn('Session changed', str(app.query_one('#source-status', Static).render()))

    async def test_concurrent_review_invalidates_suggestion_preview(self):
        self.fixture.import_findings()
        self.review.decide('purpose', 'include', 'Human')
        self.fixture.session()
        app = SourceReviewApp(self.review)
        async with app.run_test(size=(100, 40)) as pilot:
            await app.workers.wait_for_complete()
            await pilot.pause()
            before = WizardSession(self.fixture.repo, self.fixture.workspace).answers['system_name']
            app.query_one('#intake-0', Checkbox).value = True
            await self.click(app, pilot, '#source-apply')
            other = fixtures.SourceReview(self.fixture.repo, self.fixture.workspace)
            other.refresh()
            other.decide('purpose', 'exclude', 'Other human')
            await pilot.click('#suggestion-confirm')
            await pilot.pause()
            self.assertEqual(WizardSession(self.fixture.repo, self.fixture.workspace).answers['system_name'], before)
            self.assertIn('decisions changed', str(app.query_one('#source-status', Static).render()))

    async def test_bad_findings_report_attention_and_allow_manual_continue(self):
        self.review.path.write_text('{"schema_version": 99}')
        app = SourceReviewApp(self.review)
        async with app.run_test(size=(80, 24)) as pilot:
            await app.workers.wait_for_complete()
            self.assertIn('needs attention', str(app.query_one('#source-status', Static).render()))
            self.assertIsNone(self.review.state['findings_sha256'])
            await self.click(app, pilot, '#source-continue')
        self.assertTrue(app.return_value)
