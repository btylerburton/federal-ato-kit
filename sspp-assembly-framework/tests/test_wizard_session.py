"""Legacy recovery, truthful defaults and durable progress, without Textual dependencies."""
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from wizard_session import WizardSession, answer_issues, atomic_json
import wizard


class SessionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='session-test-');self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name);self.repo = self.root / 'application';self.repo.mkdir()
        subprocess.run(['git','init','-q',str(self.repo)],check=True)
        subprocess.run(['git','-C',str(self.repo),'-c','user.name=Fixture','-c','user.email=fixture@example.invalid',
                        'commit','--allow-empty','-qm','fixture'],check=True)
        self.workspace = self.root / 'authoring'

    def test_legacy_user_transcript_resumes_without_losing_answers(self):
        wizard.intake(self.repo, self.workspace / 'intake')
        path = self.workspace / 'intake/answers.json'
        answers = json.loads(path.read_text())
        answers.update(system_name='spider bot for search.gov', mode='LATO', scope_confirmed=True,
                       system_owner='PT Barnum', environment='Production, 0.0.1',
                       data_categories=['public records'], date='', boundary_summary='default')
        path.write_text(json.dumps(answers));before=path.read_bytes()
        session=WizardSession(self.repo,self.workspace,today=date(2026,11,24))
        self.assertEqual(session.answers['date'],'2026-11-24')
        self.assertEqual(session.answers['mode'],'lato')
        self.assertEqual(session.answers['system_owner'],'PT Barnum')
        self.assertEqual(session.answers['boundary_summary'],'default')
        self.assertIn('boundary_summary',session.issues())
        self.assertNotIn('topology',session.issues())
        self.assertEqual(session.current_step,'scope')
        self.assertEqual(next(path.parent.glob('answers.backup-*.json')).read_bytes(),before)
        resumed=WizardSession(self.repo,self.workspace,today=date(2026,11,25))
        self.assertEqual(resumed.answers['date'],'2026-11-24')
        self.assertEqual(resumed.answers['data_categories'],['public records'])

    def test_invalid_calendar_date_saved_but_blocks_generation(self):
        session=WizardSession(self.repo,self.workspace)
        session.update('date','2026-02-30')
        self.assertIn('date',session.issues())
        self.assertEqual(json.loads(session.answers_path.read_text())['date'],'2026-02-30')
        with self.assertRaisesRegex(ValueError,'date'):
            session.generate()
        self.assertFalse((self.workspace/'project').exists())

    def test_no_inferred_scope_or_topology(self):
        session=WizardSession(self.repo,self.workspace)
        self.assertFalse(session.answers['scope_confirmed'])
        self.assertEqual(session.answers['mode'],'')
        self.assertEqual(session.answers['topology'],{'nodes':[],'flows':[]})

    def test_legacy_topology_step_resumes_review_and_keeps_topology_bytes(self):
        session=WizardSession(self.repo,self.workspace)
        answers=json.loads(session.answers_path.read_text())
        answers['topology']={'legacy_data':'preserve without requiring repair'}
        session.answers_path.write_text(json.dumps(answers))
        state=json.loads(session.state_path.read_text());state['step']='topology'
        session.state_path.write_text(json.dumps(state))
        resumed=WizardSession(self.repo,self.workspace)
        self.assertEqual(resumed.current_step,'review')
        self.assertEqual(resumed.answers['topology'],answers['topology'])
        self.assertNotIn('topology',resumed.issues())

    def test_external_answer_edit_is_not_overwritten(self):
        session=WizardSession(self.repo,self.workspace)
        other=dict(session.answers,system_owner='Another author')
        session.answers_path.write_text(json.dumps(other))
        with self.assertRaisesRegex(ValueError,'changed on disk'):
            session.update('system_owner','Stale edit')
        self.assertEqual(json.loads(session.answers_path.read_text())['system_owner'],'Another author')

    def test_wrong_repo_and_symlinked_intake_rejected(self):
        session=WizardSession(self.repo,self.workspace)
        state=json.loads(session.state_path.read_text());state['repository']='/another/repository'
        session.state_path.write_text(json.dumps(state))
        with self.assertRaisesRegex(ValueError,'another repository'):
            WizardSession(self.repo,self.workspace)
        other=self.root/'other';other.mkdir();(other/'intake').symlink_to(self.workspace/'intake')
        with self.assertRaisesRegex(ValueError,'symlink'):
            WizardSession(self.repo,other)

    def test_topology_edits_atomic_and_cascade_node_removal(self):
        session=WizardSession(self.repo,self.workspace)
        session.add_node({'id':'a','title':'A','boundary':'inside'})
        before=session.answers_path.read_bytes()
        with self.assertRaisesRegex(ValueError,'unique'):
            session.add_node({'id':'a','title':'Duplicate','boundary':'outside'})
        self.assertEqual(before,session.answers_path.read_bytes())
        session.add_node({'id':'b','title':'B','boundary':'outside'})
        session.add_flow({'from':'a','to':'b','data':'public','protocol':'HTTPS','authentication':'none','storage':'unknown'})
        session.remove_node('a')
        self.assertEqual(session.answers['topology']['flows'],[])

    def test_failed_replace_preserves_original_file(self):
        path=self.root/'answers.json';path.write_bytes(b'{"kept":true}\n')
        with patch('wizard_session.os.replace',side_effect=OSError('Synthetic disk failure')):
            with self.assertRaisesRegex(OSError,'disk failure'):
                atomic_json(path,{'kept':False})
        self.assertEqual(path.read_bytes(),b'{"kept":true}\n')
        self.assertEqual(list(self.root.glob('.wizard-*')),[])

    def test_second_write_failure_requires_reopen_and_keeps_saved_answer(self):
        session=WizardSession(self.repo,self.workspace)
        real=atomic_json
        def fail_state(path,value):
            if path == session.state_path:
                raise OSError('Synthetic progress write failure')
            return real(path,value)
        with patch('wizard_session.atomic_json',side_effect=fail_state):
            with self.assertRaisesRegex(OSError,'progress write'):
                session.update('system_owner','New owner')
        self.assertEqual(session.answers['system_owner'],'New owner')
        with self.assertRaisesRegex(ValueError,'reopen'):
            session.record_step('scope')
        reopened=WizardSession(self.repo,self.workspace)
        self.assertEqual(reopened.answers['system_owner'],'New owner')

    def test_normalization_keeps_unanswered_inheritance_missing(self):
        from wizard_session import normalize
        from inheritance import ask
        answers=normalize({'date':'2026-11-24'})
        prompts=[]
        def prompt(question):
            prompts.append(question)
            return 'unknown'
        ask(answers,prompt,lambda:None)
        self.assertEqual(len(prompts),5)
        ask(answers,prompt,lambda:None)
        self.assertEqual(len(prompts),5)


if __name__ == '__main__':
    unittest.main()
