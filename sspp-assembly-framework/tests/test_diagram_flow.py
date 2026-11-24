"""Exercise the real standalone CLI using disposable committed source fixtures."""
import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1] / 'tools'
sys.path.insert(0, str(TOOLS))
import diagram_flow as flow
import diagrams


class DiagramFlowTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='diagram-flow-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.repository = self.root / 'application'
        self.repository.mkdir()
        self.workspace = self.root / 'workspace'
        self.git('init', '-q')
        (self.repository / 'service.py').write_text('API receives requests\nAPI stores records\nDatabase retains records\n')
        (self.repository / '.env').write_text('SYNTHETIC_SECRET=do-not-read\n')
        (self.repository / 'secret-link').symlink_to('service.py')
        self.git('add', '.')
        self.git('-c', 'user.name=Synthetic Test', '-c', 'user.email=test@example.invalid',
                 '-c', 'commit.gpgsign=false', 'commit', '-qm', 'Synthetic fixture')
        self.revision = self.git('rev-parse', 'HEAD').strip()
        evidence = [{'path': 'service.py', 'lines': [1, 3]}]
        self.proposal = {'schema_version': 1, 'repository_revision': self.revision,
            'system_name': 'Example service', 'environment': 'Test', 'date': '2026-11-24',
            'assumptions': [], 'unknown_fields': ['flows/request/authentication'],
            'nodes': [
                {'id': 'client', 'title': 'Client', 'boundary': 'outside', 'kind': 'actor',
                 'status': 'source-supported', 'evidence': evidence},
                {'id': 'api', 'title': 'API', 'boundary': 'inside', 'kind': 'component',
                 'status': 'source-supported', 'evidence': evidence},
                {'id': 'db', 'title': 'Record store', 'boundary': None, 'kind': 'database',
                 'status': 'hypothesis', 'evidence': []}],
            'flows': [
                {'id': 'request', 'from': 'client', 'to': 'api', 'data': 'Search requests',
                 'protocol': 'HTTPS', 'authentication': None, 'storage': 'None',
                 'status': 'source-supported', 'evidence': evidence},
                {'id': 'persist', 'from': 'api', 'to': 'db', 'data': 'Stored records',
                 'protocol': 'TLS', 'authentication': 'Service identity', 'storage': 'Record database',
                 'status': 'source-supported', 'evidence': evidence}]}
        self.proposal_path = self.root / 'proposal.json'
        self.write_proposal()
        self.before = self.snapshot(self.repository)

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.repository), *args], capture_output=True,
                              text=True, check=True).stdout

    def cli(self, command, *extra, stdin='', success=True, workspace=None):
        result = subprocess.run([sys.executable, '-B', str(TOOLS / 'diagram_flow.py'), command,
            '--repository', str(self.repository), '--workspace', str(workspace or self.workspace), *map(str, extra)],
            input=stdin, capture_output=True, text=True, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
        if success:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
        return result

    def write_proposal(self):
        self.proposal_path.write_text(json.dumps(self.proposal))

    def state(self):
        return json.loads((self.workspace / 'diagramming/session.json').read_text())

    def snapshot(self, directory):
        return {p.relative_to(directory).as_posix(): p.read_bytes()
                for p in directory.rglob('*') if p.is_file()}

    def start_import(self):
        self.cli('start')
        self.cli('import', '--proposal', self.proposal_path)

    def complete(self):
        self.start_import()
        answers = self.root / 'answers.json'
        answers.write_text(json.dumps({'nodes/db/boundary': 'inside', 'flows/request/authentication': 'Anonymous',
                                      'nodes/db/review': 'confirmed'}))
        self.cli('review', '--answers', answers, '--confirm', '--reviewer', 'Synthetic reviewer')
        self.cli('generate')

    def test_real_cli_partial_resume_confirmation_and_distinct_views(self):
        self.start_import()
        first = self.cli('review', stdin='inside\n')
        self.assertNotIn('nodes/api/title (', first.stdout)
        self.assertEqual(self.state()['answers'], {'nodes/db/boundary': 'inside'})
        self.assertEqual(self.state()['pending'], ['flows/request/authentication', 'nodes/db/review'])
        self.cli('prepare')
        self.cli('import', '--proposal', self.proposal_path)
        second = self.cli('review', stdin='Anonymous\nconfirmed\n')
        self.assertNotIn('nodes/db/boundary (', second.stdout)
        self.assertEqual(self.state()['pending'], [])
        self.assertIn('explicitly confirm', self.cli('generate', success=False).stderr)
        self.cli('review', '--confirm', '--reviewer', 'Synthetic reviewer')
        self.cli('generate')
        project = self.workspace / 'diagramming/project'
        manifest = json.loads((project / 'manifest.json').read_text())
        sources = {}
        for module in manifest['modules']:
            if module['kind'] != 'diagram':
                continue
            content = (project / module['path']).read_bytes()
            diagrams.check_source(content, module)
            sources[module['view']] = content
        self.assertEqual(len(set(sources.values())), 4)
        self.assertNotIn(b'as db', sources['context'])
        self.assertIn(b'database "Record store" as db', sources['architecture'])
        self.assertIn(b'Proposed authorization boundary', sources['boundary'])
        self.assertIn(b'Stored records / TLS / Service identity / Record database', sources['data-flow'])
        before = self.snapshot(project)
        self.cli('generate')
        self.assertEqual(before, self.snapshot(project))
        self.assertEqual(self.before, self.snapshot(self.repository))
        self.assertFalse((self.workspace / 'intake').exists())
        self.assertEqual((self.workspace / 'diagramming/proposal.json').read_bytes(), self.proposal_path.read_bytes())

    def test_missing_proposal_explains_agent_step_and_preserves_session(self):
        prepared = self.cli('prepare')
        self.assertIn('must write proposal.json', prepared.stdout)
        before = self.state()
        refused = self.cli('import', '--proposal', self.root / 'missing.json', success=False)
        self.assertIn('prepare only creates the workspace', refused.stderr)
        self.assertEqual(self.state(), before)
        self.assertFalse((self.workspace / 'diagramming/proposal.json').exists())

    def test_revision_and_citations_rejected_before_import(self):
        self.cli('prepare')
        original = copy.deepcopy(self.proposal)
        bad_refs = [{'path': '../service.py', 'lines': [1, 1]},
                    {'path': '.env', 'lines': [1, 1]},
                    {'path': 'secret-link', 'lines': [1, 1]},
                    {'path': 'untracked.py', 'lines': [1, 1]},
                    {'path': 'service.py', 'lines': [0, 1]},
                    {'path': 'service.py', 'lines': [1, 99]},
                    {'path': 'service.py', 'lines': [True, 2]}]
        for ref in bad_refs:
            with self.subTest(ref=ref):
                self.proposal = copy.deepcopy(original)
                self.proposal['nodes'][0]['evidence'] = [ref]
                self.write_proposal()
                self.cli('import', '--proposal', self.proposal_path, success=False)
                self.assertFalse((self.workspace / 'diagramming/proposal.json').exists())
        self.proposal = original
        self.proposal['repository_revision'] = '0' * 40
        self.write_proposal()
        self.assertIn('revision mismatch', self.cli('import', '--proposal', self.proposal_path, success=False).stderr)

    def test_secret_citation_rejected_without_reading_blob(self):
        self.cli('prepare')
        self.proposal['nodes'][0]['evidence'] = [{'path': '.env', 'lines': [1, 1]}]
        real_git = flow.git
        calls = []
        def observed(repository, *args):
            calls.append(args)
            return real_git(repository, *args)
        with patch.object(flow, 'git', side_effect=observed):
            with self.assertRaisesRegex(ValueError, 'safe tracked'):
                flow.validate_proposal(self.repository, self.state(), self.proposal)
        self.assertFalse(any(args[0] == 'cat-file' for args in calls))

    def test_uses_committed_blob_not_dirty_or_missing_worktree(self):
        (self.repository / 'service.py').unlink()
        self.start_import()
        self.assertEqual(self.state()['provenance'][0]['revision'], self.revision)

    def test_same_checkout_and_symlink_workspaces_rejected(self):
        self.cli('prepare', workspace=self.repository / 'docs', success=False)
        self.assertFalse((self.repository / 'docs').exists())
        link = self.root / 'linked'
        link.symlink_to(self.repository, target_is_directory=True)
        self.cli('prepare', workspace=link / 'docs', success=False)
        self.assertEqual(self.before, self.snapshot(self.repository))

    def test_proposal_and_output_edits_preserved_on_rerun(self):
        self.complete()
        project = self.workspace / 'diagramming/project'
        (project / 'diagrams/context.puml').write_text('Team edit\n')
        before = self.snapshot(self.workspace)
        self.assertIn('modified generated output', self.cli('generate', success=False).stderr)
        self.assertEqual(before, self.snapshot(self.workspace))
        self.proposal['system_name'] = 'Changed proposal'
        self.write_proposal()
        self.assertIn('Different proposal', self.cli('import', '--proposal', self.proposal_path, success=False).stderr)
        self.assertEqual(before, self.snapshot(self.workspace))

    def test_human_correction_invalidates_confirmation_and_keeps_history(self):
        self.complete()
        answers = self.root / 'correction.json'
        answers.write_text(json.dumps({'nodes/db/boundary': 'outside'}))
        self.cli('review', '--answers', answers)
        self.assertIsNone(self.state()['confirmation'])
        self.assertEqual(self.state()['answer_history'][-1]['previous'], 'inside')
        self.cli('generate', success=False)
        self.cli('review', '--confirm', '--reviewer', 'Synthetic reviewer')
        self.cli('generate')

    def test_injection_labels_and_unresolved_confirmation_rejected(self):
        self.cli('prepare')
        self.proposal['nodes'][0]['title'] = 'Client"\n!include /etc/passwd'
        self.write_proposal()
        self.cli('import', '--proposal', self.proposal_path, success=False)
        self.proposal['nodes'][0]['title'] = 'Client'
        self.write_proposal()
        self.cli('import', '--proposal', self.proposal_path)
        self.cli('review', '--confirm', '--reviewer', 'Synthetic reviewer', success=False)

    def test_invalid_renderer_preserves_existing_project_and_output(self):
        self.complete()
        rendered = self.workspace / 'diagramming/rendered'
        rendered.mkdir()
        (rendered / 'document.md').write_text('User work')
        before = self.snapshot(self.workspace)
        self.cli('render', '--plantuml-jar', self.root / 'missing.jar', success=False)
        self.assertEqual(before, self.snapshot(self.workspace))

    def test_assumption_and_uncertain_draft_value_need_disposition(self):
        self.proposal['assumptions'] = ['Owner has not yet confirmed deployment scope']
        self.proposal['flows'][0]['authentication'] = 'Draft anonymous'
        self.write_proposal()
        self.start_import()
        self.assertIn('assumptions/0', self.state()['pending'])
        self.assertIn('flows/request/authentication', self.state()['pending'])
        answers = self.root / 'answers.json'
        answers.write_text(json.dumps({'nodes/db/boundary': 'inside'}))
        self.cli('review', '--answers', answers)
        self.assertEqual(self.state()['pending'], ['flows/request/authentication', 'nodes/db/review', 'assumptions/0'])

    def test_checkout_revision_change_and_modified_import_refused(self):
        self.start_import()
        imported = self.workspace / 'diagramming/proposal.json'
        imported.write_text('{}')
        before = self.snapshot(self.workspace)
        self.cli('review', success=False)
        self.assertEqual(before, self.snapshot(self.workspace))
        self.git('-c', 'user.name=Synthetic Test', '-c', 'user.email=test@example.invalid',
                 '-c', 'commit.gpgsign=false', 'commit', '--allow-empty', '-qm', 'Next revision')
        self.assertIn('revision mismatch', self.cli('prepare', success=False).stderr)
        self.assertEqual(before, self.snapshot(self.workspace))

    @unittest.skipUnless(os.environ.get('PLANTUML_TEST_JAR'), 'Set PLANTUML_TEST_JAR for actual offline rendering')
    def test_actual_local_renderer(self):
        self.complete()
        extra = ['--plantuml-jar', os.environ['PLANTUML_TEST_JAR']]
        if os.environ.get('PANDOC_TEST_BIN'):
            extra += ['--pandoc', os.environ['PANDOC_TEST_BIN']]
        self.cli('render', *extra)
        output = self.workspace / 'diagramming/rendered'
        self.assertEqual(len(list(output.glob('assets/*.png'))), 4)
        self.assertEqual(len(list(output.glob('assets/*.svg'))), 4)
        if os.environ.get('PANDOC_TEST_BIN'):
            self.assertTrue((output / 'document.docx').is_file())


if __name__ == '__main__':
    unittest.main()
