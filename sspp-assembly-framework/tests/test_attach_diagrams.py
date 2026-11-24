"""Attach actual reviewed synthetic diagram output without changing text responses."""
import json
import sys
import tempfile
import subprocess
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import diagram_flow
from attach_diagrams import attach
from scaffold import scaffold
from build import sha, load_json


class AttachmentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='diagram-attach-test-');self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name);self.repo = self.root / 'app';self.repo.mkdir()
        subprocess.run(['git','init','-q',str(self.repo)],check=True)
        (self.repo / 'source.txt').write_text('Client calls service.\n')
        subprocess.run(['git','-C',str(self.repo),'add','.'],check=True)
        subprocess.run(['git','-C',str(self.repo),'-c','user.name=Fixture','-c','user.email=fixture@example.invalid',
                        'commit','-qm','fixture'],check=True)
        revision=subprocess.check_output(['git','-C',str(self.repo),'rev-parse','HEAD'],text=True).strip()
        evidence=[{'path':'source.txt','lines':[1,1]}]
        proposal={'schema_version':1,'repository_revision':revision,'system_name':'Example','environment':'test',
                  'date':'2026-11-24','assumptions':[],'unknown_fields':[],
                  'nodes':[{'id':key,'title':title,'boundary':boundary,'status':'source-supported','evidence':evidence}
                           for key,title,boundary in [('client','Client','outside'),('service','Service','inside')]],
                  'flows':[{'id':'request','from':'client','to':'service','data':'Query','protocol':'HTTPS',
                            'authentication':'Anonymous','storage':'None','status':'source-supported','evidence':evidence}]}
        self.workspace=self.root/'docs';self.proposal=self.root/'proposal.json';self.proposal.write_text(json.dumps(proposal))
        diagram_flow.prepare(self.repo,self.workspace)
        diagram_flow.import_proposal(self.repo,self.workspace,self.proposal)
        diagram_flow.review(self.repo,self.workspace,None,True,'Synthetic reviewer')
        diagram_flow.generate(self.repo,self.workspace)
        catalog=self.root/'catalog.json';catalog.write_text(json.dumps({'catalog':{'controls':[{'id':'ac-1','title':'Policy'}]}}))
        self.project=self.workspace/'project'
        scaffold(catalog,sha(catalog.read_bytes()),self.project,'Example','2026-11-24',include_diagrams=False)

    def test_attachment_regeneration_preserves_response_and_registers_provenance(self):
        response=self.project/'controls/ac/ac-1.response.md'
        response.write_text('Team response must survive.\n');before=response.read_bytes()
        self.assertEqual(attach(self.repo,self.workspace,self.project),5)
        manifest=load_json(self.project/'manifest.json')
        self.assertEqual(len([m for m in manifest['modules'] if m['kind']=='diagram']),4)
        self.assertNotIn('diagram-readiness',{m['id'] for m in manifest['modules']})
        self.assertIn('diagram-review-record',{m['id'] for m in manifest['modules']})
        self.assertEqual(response.read_bytes(),before)
        self.assertEqual(attach(self.repo,self.workspace,self.project),5)
        changed=self.project/'supporting/diagram-review/diagrams/context.puml'
        changed.write_text(changed.read_text()+"' Team edit\n")
        with self.assertRaisesRegex(ValueError,'changed'):
            attach(self.repo,self.workspace,self.project)
        self.assertTrue(changed.read_text().endswith("' Team edit\n"))

    def test_reconfirmed_correction_requires_regeneration_before_attach(self):
        answers = self.root / 'correction.json'
        answers.write_text(json.dumps({'nodes/service/boundary': 'outside'}))
        diagram_flow.review(self.repo, self.workspace, answers, True, 'Synthetic reviewer')
        before = (self.project / 'supporting.json').read_bytes()
        with self.assertRaisesRegex(ValueError, 'predate the current review'):
            attach(self.repo, self.workspace, self.project)
        self.assertEqual((self.project / 'supporting.json').read_bytes(), before)
        diagram_flow.generate(self.repo, self.workspace)
        self.assertEqual(attach(self.repo, self.workspace, self.project), 5)


if __name__ == '__main__':
    unittest.main()
