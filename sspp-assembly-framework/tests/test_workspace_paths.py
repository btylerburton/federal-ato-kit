"""Real in-repository workspace integration and collision/preservation checks."""
import json
import subprocess
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from workspace_paths import claim_workspace, discover_workspaces, suggest_workspace, validate_workspace, validate_output
from wizard_session import WizardSession
from repository_intake import inspect
import wizard
import diagram_flow
from attach_diagrams import attach
from build import load_json, json_bytes, compose


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='owned-docs-');self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);self.repo=self.root/'app';self.repo.mkdir()
        self.git('init','-q')
        # A monitor inherited from user config can create an uncopyable IPC socket.
        self.git('config','--local','core.fsmonitor','false')
        (self.repo/'source.txt').write_text('Client calls service.\n')
        self.git('add','.')
        self.git('-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','-qm','fixture')

    def git(self,*args):
        return subprocess.check_output(['git','-C',str(self.repo),*args],text=True).strip()

    def test_default_timestamp_case_and_collision(self):
        self.assertEqual(suggest_workspace(self.repo,123),self.repo/'docs')
        (self.repo/'Docs').mkdir()
        self.assertEqual(suggest_workspace(self.repo,123),self.repo/'docs-123')
        (self.repo/'docs-123').mkdir()
        self.assertEqual(suggest_workspace(self.repo,123),self.repo/'docs-123-1')
        self.assertEqual(discover_workspaces(self.repo),[])

    def test_refuse_existing_docs_root_other_dirs_and_symlinks(self):
        docs=self.repo/'docs';docs.mkdir();(docs/'manual.md').write_text('Keep')
        for path in (docs,self.repo,self.repo/'src',self.repo/'docs-1'/'nested'):
            with self.subTest(path=path),self.assertRaises(ValueError):claim_workspace(self.repo,path)
        (self.repo/'docs-2').symlink_to(self.root)
        with self.assertRaisesRegex(ValueError,'symlink'):claim_workspace(self.repo,self.repo/'docs-2')
        self.assertEqual((docs/'manual.md').read_text(),'Keep')

    def test_only_claimed_children_allowed_and_marker_identity_checked(self):
        docs=claim_workspace(self.repo,self.repo/'docs')
        self.assertEqual(claim_workspace(self.repo,docs),docs)
        self.assertEqual(discover_workspaces(self.repo),[docs])
        self.assertEqual(validate_output(self.repo,docs/'project','project'),docs/'project')
        with self.assertRaises(ValueError):validate_output(self.repo,self.repo/'source.txt','project')
        marker=docs/'.ato-workspace.json';state=load_json(marker);state['repository']='/different'
        marker.write_bytes(json_bytes(state))
        with self.assertRaises(ValueError):validate_workspace(self.repo,docs)

    def test_text_and_diagram_workflows_in_owned_docs_and_excluded_from_source(self):
        docs=claim_workspace(self.repo,self.repo/'docs')
        session=WizardSession(self.repo,docs)
        for key,value in {'system_name':'Fixture','system_owner':'Test owner','environment':'Test','date':'2026-11-24',
                          'mode':'lato','scope_confirmed':True,'data_categories':['Synthetic'],
                          'boundary_summary':'Proposed service and client'}.items():session.update(key,value)
        session.generate()
        response=docs/'project/controls/ac/ac-2.response.md';before=response.read_bytes()
        self.assertIn('diagram-readiness',{m['id'] for m in load_json(docs/'project/manifest.json')['modules']})
        # Even if a team versions generated documentation, source inventory must not recurse into it.
        self.git('add','docs')
        self.git('-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','-qm','docs')
        observed=inspect(self.repo)
        self.assertEqual(observed['tracked_paths_considered'],1)
        diagram_flow.prepare(self.repo,docs)
        state=load_json(docs/'diagramming/session.json')
        self.assertEqual(state['source_paths'],['source.txt'])
        evidence=[{'path':'source.txt','lines':[1,1]}]
        proposal={'schema_version':1,'repository_revision':state['repository_revision'],'system_name':'Fixture',
                  'environment':'Test','date':'2026-11-24','unknown_fields':[],'assumptions':[],
                  'nodes':[{'id':key,'title':key,'boundary':boundary,'status':'source-supported','evidence':evidence}
                           for key,boundary in [('client','outside'),('service','inside')]],
                  'flows':[{'id':'request','from':'client','to':'service','data':'Query','protocol':'HTTPS',
                            'authentication':'Anonymous','storage':'None','status':'source-supported','evidence':evidence}]}
        (docs/'proposal.json').write_bytes(json_bytes(proposal))
        diagram_flow.import_proposal(self.repo,docs,docs/'proposal.json')
        diagram_flow.review(self.repo,docs,confirm=True,reviewer='Synthetic test reviewer')
        diagram_flow.generate(self.repo,docs)
        self.assertEqual(attach(self.repo,docs,docs/'project'),5)
        self.assertEqual(response.read_bytes(),before)
        self.assertEqual(len([m for m in load_json(docs/'project/manifest.json')['modules'] if m['kind']=='diagram']),4)
        self.assertEqual((self.repo/'source.txt').read_text(),'Client calls service.\n')

    def test_external_old_workspace_and_subdirectory_root_resolution(self):
        external=self.root/'external';wizard.intake(self.repo,external/'intake')
        self.assertEqual(WizardSession(self.repo,external).workspace,external)
        nested=self.repo/'src';nested.mkdir()
        docs=claim_workspace(self.repo,self.repo/'docs')
        self.assertEqual(WizardSession(nested,docs).repository,self.repo)

    def test_new_directory_empty_can_be_claimed_but_nonempty_cannot(self):
        path=self.repo/'docs';path.mkdir()
        claim_workspace(self.repo,path)
        self.assertTrue((path/'.ato-workspace.json').is_file())
        occupied=self.repo/'docs-1';occupied.mkdir();(occupied/'keep').write_text('user')
        with self.assertRaisesRegex(ValueError,'unrelated'):claim_workspace(self.repo,occupied)

    def test_relocated_checkout_excludes_old_generated_docs_without_write_ownership(self):
        docs=claim_workspace(self.repo,self.repo/'docs')
        (docs/'generated.md').write_text('Generated text is not source evidence.\n')
        self.git('add','docs')
        self.git('-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','-qm','docs')
        moved=self.root/'moved'
        shutil.copytree(self.repo,moved)
        self.assertEqual(inspect(moved)['tracked_paths_considered'],1)
        revision=subprocess.check_output(['git','-C',str(moved),'rev-parse','HEAD'],text=True).strip()
        self.assertEqual(set(diagram_flow.source_tree(moved,revision)),{'source.txt'})
        with self.assertRaises(ValueError):validate_workspace(moved,moved/'docs')


if __name__ == '__main__':
    unittest.main()
