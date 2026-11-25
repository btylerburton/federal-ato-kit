"""Real cited findings → human decisions → preserved, composable SSPP draft."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from source_review import SourceReview, accepted
from wizard_session import WizardSession
from build import compose, load_json


class SourceReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / 'app'
        self.repo.mkdir()
        self.git('init', '-q')
        (self.repo / 'README.md').write_text('Example public crawler\nLogs failed crawl requests\n')
        self.git('add', 'README.md')
        self.git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-qm', 'Fixture')
        self.workspace = self.root / 'docs'
        self.review = SourceReview(self.repo, self.workspace)
        evidence = [{'path': 'README.md', 'lines': [1, 2]}]
        self.data = {'schema_version': 1, 'repository_revision': self.review.revision,
                     'method': 'llm-assisted', 'author': 'Synthetic fixture', 'findings': [
            {'id': 'purpose', 'section': 'system', 'status': 'source-supported',
             'text': 'Example public crawler', 'suggested_field': 'system_name', 'evidence': evidence},
            {'id': 'logs', 'section': 'control', 'control_id': 'au-2', 'status': 'source-supported',
             'text': 'The crawler logs failures; retention requires confirmation.', 'evidence': evidence},
            {'id': 'guess', 'section': 'deployment', 'status': 'hypothesis',
             'text': 'HYPOTHESIS_MUST_NOT_EXPORT', 'evidence': []}]}

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.repo), *args], check=True, capture_output=True).stdout

    def import_findings(self):
        self.review.path.write_text(json.dumps(self.data))
        self.review.refresh()

    def session(self):
        session = WizardSession(self.repo, self.workspace)
        for key, value in {'system_owner': 'Test owner', 'environment': 'Test', 'mode': 'lato',
                           'scope_confirmed': True, 'data_categories': ['public'],
                           'boundary_summary': 'Crawler and its external websites'}.items():
            session.update(key, value)
        return session

    def test_included_findings_seed_real_draft_and_preserve_edits(self):
        self.import_findings()
        for key in ('purpose', 'logs'):
            self.review.decide(key, 'include', 'Test human')
        session = self.session()
        session.generate()
        project = self.workspace / 'project'
        response = project / 'controls/au/au-2.response.md'
        self.assertIn('The crawler logs failures', response.read_text())
        self.assertIn('Implementation status: UNFILLED', response.read_text())
        manifest = load_json(project / 'manifest.json')
        self.assertTrue(any(m['id'] == 'source-review-findings' for m in manifest['modules']))
        text = compose(project / 'manifest.json')['document.md']
        if isinstance(text, bytes):
            text = text.decode()
        self.assertIn('The crawler logs failures', text)
        self.assertNotIn('HYPOTHESIS_MUST_NOT_EXPORT', text)
        response.write_text(response.read_text() + '\nHuman-authored addition\n')
        original = response.read_bytes()
        session.generate()
        self.assertEqual(response.read_bytes(), original)
        self.assertIn('controls/au/au-2.response.md', load_json(project / 'wizard-report.json')['preserved_user_files'])

    def test_manual_no_llm_and_pending_findings(self):
        self.assertIsNone(self.review.refresh())
        self.session().generate()
        self.data['method'] = 'manual'
        self.import_findings()
        self.assertEqual(accepted(self.repo, self.workspace)['findings'], [])
        self.review.decide('purpose', 'include', 'Human')
        self.assertEqual(accepted(self.repo, self.workspace)['method'], 'manual')
        with self.assertRaisesRegex(ValueError, 'No runner'):
            self.review.analyze()

    def test_later_review_seeds_existing_pristine_shell_and_exclusion_removes_candidate(self):
        session = self.session()
        session.generate()
        self.import_findings()
        self.review.decide('logs', 'include', 'Human')
        session.generate()
        response = self.workspace / 'project/controls/au/au-2.response.md'
        self.assertIn('The crawler logs failures', response.read_text())
        self.review.decide('logs', 'exclude', 'Human')
        session.generate()
        self.assertNotIn('The crawler logs failures', response.read_text())

    def test_missing_prior_review_blocks_and_edited_report_preserves_provenance_pair(self):
        self.import_findings()
        self.review.decide('purpose', 'include', 'Human')
        session = self.session()
        session.generate()
        project = self.workspace / 'project'
        report = project / 'source-review/findings.md'
        provenance = project / 'source-review/provenance.json'
        report.write_text(report.read_text() + '\nHuman review note\n')
        original = (report.read_bytes(), provenance.read_bytes())
        self.review.decide('logs', 'include', 'Human')
        session.generate()
        self.assertEqual((report.read_bytes(), provenance.read_bytes()), original)
        self.review.root.rename(self.workspace / 'archived-source-review')
        with self.assertRaisesRegex(ValueError, 'Previously used source review is missing'):
            session.generate()

    def test_candidate_prose_stays_literal_in_assembled_output(self):
        self.data['findings'][1]['text'] = 'Observed logging.\n<!-- hidden -->\n![external](https://example.invalid/a.png)'
        self.import_findings()
        self.review.decide('logs', 'include', 'Human')
        self.session().generate()
        text = compose(self.workspace / 'project/manifest.json')['document.md'].decode()
        self.assertNotIn('<!-- hidden -->', text)
        self.assertNotIn('![external](', text)
        self.assertIn('Observed logging.', text)

    def test_optional_bad_topology_does_not_block_text_and_existing_proposal_is_preserved(self):
        self.data['diagram_proposal'] = {'schema_version': 99}
        self.import_findings()
        self.review.decide('purpose', 'include', 'Human')
        self.session().generate()
        with self.assertRaisesRegex(ValueError, 'schema_version'):
            self.review.send_diagrams()
        self.assertFalse((self.workspace / 'proposal.json').exists())

    def test_explicit_runner_writes_findings_and_failed_output_is_quarantined(self):
        script = self.root / 'runner.py'
        script.write_text('import pathlib,sys\npathlib.Path(sys.argv[2]).write_text(' + repr(json.dumps(self.data)) + ')\n')
        config = self.root / 'runner.json'
        config.write_text(json.dumps({'schema_version': 1, 'argv': [sys.executable, str(script),
                                      '{request}', '{proposal}'], 'timeout_seconds': 10}))
        self.review.runner = config
        self.assertIsNone(self.review.refresh())
        self.assertEqual(self.review.analyze()['method'], 'llm-assisted')
        self.assertEqual(self.review.state['decisions'], {})
        with self.assertRaisesRegex(ValueError, 'already exist'):
            self.review.analyze()
        other = SourceReview(self.repo, self.root / 'other', config)
        script.write_text(script.read_text() + 'sys.exit(2)\n')
        with self.assertRaisesRegex(ValueError, 'exited 2'):
            other.analyze()
        self.assertFalse(other.path.exists())
        self.assertIsNone(other.refresh())
        self.assertTrue(list((other.root / 'runs').glob('*-unaccepted-proposal.json')))

    def test_shared_diagram_proposal_is_sent_without_overwriting_existing_work(self):
        evidence = [{'path': 'README.md', 'lines': [1, 2]}]
        diagram = {'schema_version': 1, 'repository_revision': self.review.revision,
                   'system_name': 'Example', 'environment': None, 'date': None,
                   'unknown_fields': [], 'assumptions': [],
                   'nodes': [{'id': 'crawl-app', 'title': 'Crawler', 'boundary': None,
                              'status': 'source-supported', 'evidence': evidence}],
                   'flows': [{'id': 'self-call', 'from': 'crawl-app', 'to': 'crawl-app',
                              'data': 'Job state', 'protocol': None, 'authentication': None,
                              'storage': None, 'status': 'hypothesis', 'evidence': []}]}
        self.data['diagram_proposal'] = diagram
        self.import_findings()
        target = self.review.send_diagrams()
        self.assertEqual(load_json(target), diagram)
        before = target.read_bytes()
        with self.assertRaisesRegex(ValueError, 'already exists'):
            self.review.send_diagrams()
        self.assertEqual(target.read_bytes(), before)
        from diagram_dashboard import DiagramDashboard
        dashboard = DiagramDashboard(self.repo, self.workspace)
        self.assertEqual(dashboard.refresh()['stage'], 'clarify')
        self.assertIsNone(load_json(dashboard.root / 'session.json')['confirmation'])

    def test_stale_edits_and_revision_rejected_before_generation(self):
        self.import_findings()
        self.review.decide('purpose', 'include', 'Human')
        stale = SourceReview(self.repo, self.workspace)
        self.review.decide('logs', 'exclude', 'Human')
        with self.assertRaisesRegex(ValueError, 'changed on disk'):
            stale.decide('logs', 'include', 'Other')
        self.review.path.write_text(json.dumps({**self.data, 'author': 'Changed'}))
        with self.assertRaisesRegex(ValueError, 'changed'):
            self.session().generate()
        self.assertFalse((self.workspace / 'project').exists())
        self.review.path.write_text(json.dumps(self.data))
        self.git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '--allow-empty', '-qm', 'New revision')
        with self.assertRaisesRegex(ValueError, 'revision'):
            accepted(self.repo, self.workspace)

    def test_invalid_citations_controls_and_approval_suggestions_rejected(self):
        for mutation in ('citation', 'control', 'part', 'approval'):
            with self.subTest(mutation=mutation):
                data = copy.deepcopy(self.data)
                if mutation == 'citation':
                    data['findings'][0]['evidence'][0]['path'] = '.env'
                elif mutation == 'control':
                    data['findings'][1]['control_id'] = 'fake-999'
                elif mutation == 'part':
                    data['findings'][1]['part_id'] = 'ac-1_smt'
                else:
                    data['findings'][0]['suggested_field'] = 'scope_confirmed'
                self.review.path.write_text(json.dumps(data))
                with self.assertRaises(ValueError):
                    self.review.refresh()
                self.assertIsNone(load_json(self.review.state_path)['findings_sha256'])


if __name__ == '__main__':
    unittest.main()
