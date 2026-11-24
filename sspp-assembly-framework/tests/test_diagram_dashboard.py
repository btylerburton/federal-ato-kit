"""Actual dashboard state transitions and bounded explicit runner execution."""
import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from diagram_dashboard import DiagramDashboard
from diagram_runner import load_runner
from scaffold import scaffold
from build import json_bytes, sha, load_json


class DashboardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='dashboard-test-'); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name); self.repo = self.root / 'app'; self.repo.mkdir()
        subprocess.run(['git', 'init', '-q', str(self.repo)], check=True)
        (self.repo / 'source.txt').write_text('Client requests service.\n')
        subprocess.run(['git', '-C', str(self.repo), 'add', '.'], check=True)
        subprocess.run(['git', '-C', str(self.repo), '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
                        '-c', 'commit.gpgsign=false', 'commit', '-qm', 'fixture'], check=True)
        revision = subprocess.check_output(['git','-C',str(self.repo),'rev-parse','HEAD'],text=True).strip()
        evidence = [{'path':'source.txt','lines':[1,1]}]
        self.proposal = {'schema_version':1,'repository_revision':revision, 'system_name':'Example service',
            'environment':'Test','date':'2026-11-24','assumptions':[], 'unknown_fields':['nodes/api/boundary'],
            'nodes':[{'id':'client','title':'Client','boundary':'outside','status':'source-supported','evidence':evidence},
                     {'id':'api','title':'API','boundary':None,'status':'source-supported','evidence':evidence}],
            'flows':[{'id':'request','from':'client','to':'api','data':'Query','protocol':'HTTPS',
                      'authentication':'Anonymous','storage':'None','status':'source-supported','evidence':evidence}]}
        self.workspace = self.root / 'authoring'

    def ready(self):
        dashboard = DiagramDashboard(self.repo,self.workspace)
        dashboard.proposal_path.write_bytes(json_bytes(self.proposal))
        self.assertEqual(dashboard.refresh()['stage'], 'clarify')
        dashboard.answer('nodes/api/boundary','inside')
        dashboard.confirm('Synthetic reviewer')
        return dashboard

    def runner(self, code, timeout=10):
        script = self.root / 'runner.py'; script.write_text(code)
        config = self.root / 'runner.json'
        config.write_bytes(json_bytes({'schema_version':1,'argv':[sys.executable,str(script),'{request}','{proposal}'],
                                       'timeout_seconds':timeout}))
        return config

    def test_start_missing_then_auto_import_human_question_and_resume(self):
        dashboard = DiagramDashboard(self.repo,self.workspace)
        self.assertEqual(dashboard.refresh()['stage'],'needs-analysis')
        self.assertFalse(dashboard.refresh()['can_analyze'])
        self.assertIn(self.proposal['repository_revision'],dashboard.handoff_text())
        dashboard.proposal_path.write_bytes(json_bytes(self.proposal))
        self.assertEqual(dashboard.refresh()['pending_count'],1)
        question = next(q for q in dashboard.questions() if q['pending'])
        self.assertEqual(question['key'],'nodes/api/boundary')
        self.assertIn('API',question['label'])
        self.assertIn('source.txt',question['help'])
        dashboard.answer(question['key'],'inside')
        reopened = DiagramDashboard(self.repo,self.workspace)
        self.assertEqual(reopened.refresh()['stage'],'review')
        reopened.confirm('Synthetic reviewer')
        self.assertEqual(reopened.refresh()['stage'],'generate')
        reopened.generate()
        self.assertTrue(reopened.refresh()['generated'])
        self.assertIn('@startuml',reopened.preview('boundary'))

    def test_invalid_new_proposal_never_imported_or_replaced(self):
        dashboard = DiagramDashboard(self.repo,self.workspace)
        bad = copy.deepcopy(self.proposal); bad['repository_revision']='0'*40
        dashboard.proposal_path.write_bytes(json_bytes(bad))
        self.assertEqual(dashboard.refresh()['stage'],'blocked')
        self.assertIsNone(load_json(dashboard.root/'session.json')['proposal_sha256'])
        dashboard.proposal_path.write_bytes(json_bytes(self.proposal))
        self.assertEqual(dashboard.refresh()['stage'],'clarify')
        imported = (dashboard.root/'proposal.json').read_bytes()
        dashboard.proposal_path.write_bytes(json_bytes(bad))
        self.assertEqual(dashboard.refresh()['stage'],'blocked')
        self.assertEqual((dashboard.root/'proposal.json').read_bytes(),imported)

    def test_explicit_runner_only_and_success_requires_valid_file(self):
        marker = self.root/'executed'
        code = ('import pathlib,sys\n'
                f'pathlib.Path({str(marker)!r}).write_text("ran")\n'
                f'pathlib.Path(sys.argv[2]).write_bytes({json_bytes(self.proposal)!r})\n')
        dashboard = DiagramDashboard(self.repo,self.workspace,runner=self.runner(code))
        self.assertTrue(dashboard.refresh()['can_analyze'])
        self.assertFalse(marker.exists())
        self.assertEqual(dashboard.analyze()['stage'],'clarify')
        self.assertTrue(marker.exists())
        self.assertEqual(len(list((dashboard.root/'runs').glob('*.json'))),1)
        with self.assertRaisesRegex(ValueError,'already exists'):
            dashboard.analyze()

    def test_runner_failure_missing_output_and_timeout_have_durable_receipts(self):
        for name, code, timeout, expected in [('nonzero','raise SystemExit(7)',10,'exited 7'),
                                             ('empty','pass',10,'did not write'),
                                             ('timeout','import time; time.sleep(10)',1,'timed out')]:
            with self.subTest(name=name):
                config = self.runner(code,timeout)
                dashboard = DiagramDashboard(self.repo,self.root/name,runner=config)
                with self.assertRaisesRegex(ValueError,expected): dashboard.analyze()
                self.assertEqual(len(list((dashboard.root/'runs').glob('*.json'))),1)
                self.assertIsNone(load_json(dashboard.root/'session.json')['proposal_sha256'])

    def test_runner_config_refuses_shell_string_and_application_config(self):
        config = self.root/'bad-runner.json'; config.write_text('{"schema_version":1,"argv":"echo bad"}')
        with self.assertRaisesRegex(ValueError,'argument array'):load_runner(config,self.repo)
        config = self.repo/'runner.json';config.write_text('{}')
        with self.assertRaisesRegex(ValueError,'outside the application'):load_runner(config,self.repo)

    def test_failed_valid_proposal_is_quarantined_not_auto_imported(self):
        for label, ending, timeout in [('failed','raise SystemExit(7)',10),('timeout','import time; time.sleep(10)',1)]:
            config=self.runner('import pathlib,sys\n' + f'pathlib.Path(sys.argv[2]).write_bytes({json_bytes(self.proposal)!r})\n' + ending,timeout)
            dashboard=DiagramDashboard(self.repo,self.root/label,runner=config)
            with self.assertRaises(ValueError): dashboard.analyze()
            reopened=DiagramDashboard(self.repo,self.root/label,runner=config)
            self.assertEqual(reopened.refresh()['stage'],'needs-analysis')
            self.assertTrue(reopened.refresh()['warnings'])
            self.assertIsNone(load_json(reopened.root/'session.json')['proposal_sha256'])
            self.assertEqual(len(list((reopened.root/'runs').glob('*-unaccepted-proposal.json'))),1)

    def test_null_relationship_endpoints_can_be_answered(self):
        dashboard=DiagramDashboard(self.repo,self.workspace)
        self.proposal['flows'][0].update({'from':None,'to':None})
        dashboard.proposal_path.write_bytes(json_bytes(self.proposal))
        self.assertEqual(dashboard.refresh()['stage'],'clarify')
        self.assertTrue(any('unknown source' in q['label'] for q in dashboard.questions()))
        dashboard.answer('flows/request/from','client');dashboard.answer('flows/request/to','api')
        self.assertFalse(any(q['pending'] for q in dashboard.questions() if q['key'] in {'flows/request/from','flows/request/to'}))

    def test_stale_dashboard_and_missing_reviewer_do_not_confirm(self):
        first = self.ready(); second=DiagramDashboard(self.repo,self.workspace);second.refresh()
        first.answer('flows/request/authentication','Service identity')
        with self.assertRaisesRegex(ValueError,'changed since displayed'): second.confirm('Other reviewer')
        second.refresh()
        with self.assertRaisesRegex(ValueError,'Human reviewer'):second.confirm('')
        self.assertFalse(second.refresh()['confirmed'])

    def test_attach_detection_checks_source_and_text_registration(self):
        dashboard = self.ready(); dashboard.generate();dashboard.refresh()
        catalog = self.root/'catalog.json'
        catalog.write_bytes(json_bytes({'catalog':{'controls':[{'id':'ac-1','title':'Policy'}]}}))
        project = self.workspace/'project'
        scaffold(catalog,sha(catalog.read_bytes()),project,'Example','2026-11-24',include_diagrams=False)
        dashboard.attach()
        self.assertTrue(dashboard.refresh()['attached'])
        for name in ['supporting.json','manifest.json']:
            document=load_json(project/name)
            next(m for m in document['modules'] if m['id']=='diagram-context')['path']='missing-context.puml'
            (project/name).write_bytes(json_bytes(document))
        self.assertFalse(dashboard.refresh()['attached'])
        support=load_json(project/'supporting.json');support['modules']=[]
        (project/'supporting.json').write_bytes(json_bytes(support))
        self.assertFalse(dashboard.refresh()['attached'])

    @unittest.skipUnless(os.environ.get('PLANTUML_TEST_JAR'), 'Set PLANTUML_TEST_JAR for actual rendering')
    def test_real_render_receipt_becomes_stale_after_correction(self):
        dashboard=self.ready();dashboard.jar=Path(os.environ['PLANTUML_TEST_JAR'])
        if os.environ.get('PANDOC_TEST_BIN'):dashboard.pandoc=Path(os.environ['PANDOC_TEST_BIN'])
        dashboard.render()
        self.assertTrue(dashboard.refresh()['rendered'])
        dashboard.answer('flows/request/data','New query')
        dashboard.confirm('Synthetic reviewer');dashboard.generate()
        self.assertFalse(dashboard.refresh()['rendered'])


if __name__ == '__main__':
    unittest.main()
