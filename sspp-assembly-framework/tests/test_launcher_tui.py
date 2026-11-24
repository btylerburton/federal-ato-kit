"""Exercise launcher selection against real disposable Git repositories."""
import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
HAS_TEXTUAL = importlib.util.find_spec('textual') is not None
if HAS_TEXTUAL:
    from textual.widgets import Input, Select, Static
    from launcher_tui import LauncherApp
    from workspace_paths import claim_workspace, discover_workspaces


@unittest.skipUnless(HAS_TEXTUAL, 'Optional Textual environment not installed')
class LauncherTuiTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='launcher-tui-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / 'fixture[red]'
        self.repo.mkdir()
        subprocess.run(['git', 'init', '-q', str(self.repo)], check=True)
        subprocess.run(['git', '-C', str(self.repo), '-c', 'user.name=Fixture',
                        '-c', 'user.email=fixture@example.invalid', 'commit', '--allow-empty',
                        '-qm', 'Synthetic test fixture'], check=True)

    def snapshot(self):
        return {str(path.relative_to(self.root)): path.read_bytes()
                for path in self.root.rglob('*') if path.is_file()}

    async def click_scrolled(self, app, pilot, selector):
        app.query_one(selector).scroll_visible(animate=False, immediate=True)
        await pilot.pause()
        self.assertTrue(await pilot.click(selector))
        await pilot.pause()

    async def test_mount_refresh_and_quit_do_not_write_or_select_new(self):
        before = self.snapshot()
        app = LauncherApp(self.repo)
        async with app.run_test(size=(80, 24)) as pilot:
            self.assertEqual(app.query_one('#workspace', Input).value, '')
            await self.click_scrolled(app, pilot, '#detect')
            self.assertEqual(self.snapshot(), before)
            await pilot.click('#text')
            await pilot.pause()
            self.assertIn('Select New workspace', str(app.query_one('#error', Static).render()))
            self.assertEqual(self.snapshot(), before)
            await pilot.press('ctrl+q')
        self.assertIsNone(app.return_value)

    async def test_new_workspace_click_then_launch_claims_lowercase_docs(self):
        app = LauncherApp(self.repo)
        before = self.snapshot()
        async with app.run_test(size=(80, 24)) as pilot:
            await self.click_scrolled(app, pilot, '#new-workspace')
            self.assertEqual(Path(app.query_one('#workspace', Input).value), self.repo / 'docs')
            self.assertEqual(self.snapshot(), before)
            self.assertFalse((self.repo / 'docs').exists())
            await pilot.click('#text')
            await pilot.pause()
        self.assertEqual(app.return_value, {'repository': self.repo.resolve(),
                                           'workspace': (self.repo / 'docs').resolve(), 'workflow': 'text'})
        self.assertIn((self.repo / 'docs').resolve(), discover_workspaces(self.repo))

    async def test_unrelated_docs_get_timestamp_and_collision_preserves_edits(self):
        docs = self.repo / 'docs'
        docs.mkdir()
        (docs / 'notes.md').write_text('Existing application documentation')
        app = LauncherApp(self.repo, docs)
        before = self.snapshot()
        async with app.run_test(size=(80, 24)) as pilot:
            await pilot.click('#text')
            await pilot.pause()
            self.assertIsNone(app.return_value)
            self.assertTrue(str(app.query_one('#error', Static).render()))
            self.assertEqual(self.snapshot(), before)
            await self.click_scrolled(app, pilot, '#new-workspace')
            chosen = Path(app.query_one('#workspace', Input).value)
            self.assertEqual(chosen.parent, self.repo)
            self.assertRegex(chosen.name, r'^docs-\d+(?:-\d+)?$')
            self.assertFalse(chosen.exists())
            await pilot.click('#diagrams')
            await pilot.pause()
        self.assertEqual(app.return_value['workspace'], chosen.resolve())
        self.assertEqual(app.return_value['workflow'], 'diagrams')
        self.assertEqual((docs / 'notes.md').read_text(), 'Existing application documentation')

    async def test_resume_newest_and_switch_saved_workspace_without_writes(self):
        older = claim_workspace(self.repo, self.repo / 'docs')
        newer = claim_workspace(self.repo, self.repo / 'docs-2000000000')
        (older / 'intake').mkdir()
        (older / 'intake/answers.json').write_text('{"system_owner":"User edit"}')
        os.utime(older, (100, 100))
        os.utime(newer, (200, 200))
        before = self.snapshot()
        app = LauncherApp(self.repo)
        async with app.run_test(size=(80, 24)) as pilot:
            await pilot.pause()
            self.assertEqual(Path(app.query_one('#workspace', Input).value), newer)
            self.assertIn('Resume workspace', str(app.query_one('#summary', Static).render()))
            app.query_one('#resume', Select).focus()
            await pilot.press('enter')
            await pilot.press('home', 'down', 'down', 'enter')
            await pilot.pause()
            # Textual includes its blank prompt before the two saved entries.
            self.assertEqual(app.query_one('#resume', Select).value, str(older))
            self.assertEqual(Path(app.query_one('#workspace', Input).value), older)
            self.assertEqual(self.snapshot(), before)
            await pilot.click('#text')
            await pilot.pause()
        self.assertEqual(app.return_value['workspace'], older)
        self.assertEqual(self.snapshot(), before)

    async def test_explicit_external_workspace_is_retained_and_literal(self):
        external = self.root / 'authoring[blue]'
        external.mkdir()
        (external / 'notes.md').write_text('Keep this user edit')
        claim_workspace(self.repo, self.repo / 'docs')
        runner = self.root / 'runner.json'
        runner.write_text('not parsed by launcher')
        before = self.snapshot()
        app = LauncherApp(self.repo, external, runner=runner, jar=self.root / 'missing.jar', pandoc=self.root)
        async with app.run_test(size=(80, 24)) as pilot:
            await self.click_scrolled(app, pilot, '#detect')
            self.assertEqual(Path(app.query_one('#workspace', Input).value), external)
            self.assertIn('authoring[blue]', str(app.query_one('#summary', Static).render()))
            tools = str(app.query_one('#tools', Static).render())
            self.assertIn('Textual: installed', tools)
            self.assertIn('Runner config: file present', tools)
            self.assertIn('PlantUML JAR: file missing', tools)
            self.assertIn('Pandoc: file missing', tools)
            await pilot.click('#diagrams')
            await pilot.pause()
        self.assertEqual(app.return_value['workspace'], external.resolve())
        self.assertEqual(self.snapshot(), before)

    async def test_repository_input_resolves_subdirectory_and_invalid_path(self):
        nested = self.repo / 'src'
        nested.mkdir()
        app = LauncherApp(self.root / 'not-a-repository')
        async with app.run_test(size=(80, 24)) as pilot:
            self.assertIn('Git checkout', str(app.query_one('#error', Static).render()))
            app.query_one('#repository', Input).value = str(nested)
            await self.click_scrolled(app, pilot, '#detect')
            await self.click_scrolled(app, pilot, '#new-workspace')
            await pilot.click('#text')
            await pilot.pause()
        self.assertEqual(app.return_value['repository'], self.repo.resolve())


if __name__ == '__main__':
    unittest.main()
