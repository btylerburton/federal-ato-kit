"""Exercise actual repository intake, baseline selection and draft regeneration."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import baselines
import wizard
from build import load_json
from scaffold import collect_controls


class WizardTests(unittest.TestCase):
    def test_all_catalog_response_guidance_is_composable(self):
        from control_library import load_catalog
        from scaffold import response_document, parts_for
        from build import markdown
        controls = collect_controls(load_catalog()['catalog'])
        self.assertEqual(len(controls), 1196)
        for control in controls.values():
            with self.subTest(control=control['id']):
                content = response_document(control, [p for p, _ in parts_for(control)])
                rendered = markdown(content, {})
                self.assertNotIn('ILLUSTRATIVE TEMPLATE ONLY', rendered)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='wizard-test-');self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name);self.repo = self.root / 'repository';self.repo.mkdir()
        subprocess.run(['git', 'init', '-q', str(self.repo)], check=True)
        (self.repo / 'package.json').write_text('{"scripts":{"test":"exit 99"}}')
        (self.repo / '.env').write_text('SYNTHETIC_SECRET_MUST_NOT_APPEAR=value')
        subprocess.run(['git', '-C', str(self.repo), 'add', '.'], check=True)
        subprocess.run(['git', '-C', str(self.repo), '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
                        'commit', '-qm', 'synthetic fixture'], check=True)
        self.answers = self.root / 'answers.json'
        self.data = {'system_name': 'Synthetic service', 'mode': 'lato', 'scope_confirmed': True,
                     'system_owner': 'Example owner', 'environment': 'test', 'data_categories': ['synthetic'],
                     'boundary_summary': 'One proposed service', 'date': '2026-11-23',
                     'topology': {'nodes': [{'id':'browser','title':'Browser','boundary':'outside'},
                                           {'id':'service','title':'Service','boundary':'inside'}],
                                  'flows':[{'from':'browser','to':'service','data':'synthetic question',
                                            'protocol':'HTTPS','authentication':'anonymous','storage':'none'}]}}
        self.answers.write_text(json.dumps(self.data))

    def test_intake_records_questions_without_reading_secrets_or_running_code(self):
        out = self.root / 'intake'
        report = wizard.intake(self.repo, out)
        self.assertEqual(report['signals']['dependency_manifests']['count'], 1)
        self.assertEqual(report['tracked_paths_considered'], 1)
        self.assertNotIn('SYNTHETIC_SECRET_MUST_NOT_APPEAR', (out / 'repository-observations.json').read_text())
        self.assertFalse(load_json(out / 'answers.json')['scope_confirmed'])
        self.assertGreater(len(load_json(out / 'questions.json')['questions']), 5)
        with self.assertRaisesRegex(ValueError, 'new or empty'):
            wizard.intake(self.repo, out)

    def test_baselines_select_exact_controls_not_all_child_enhancements(self):
        values, _ = baselines.load_inputs()
        for mode, name, count in [('lato',None,58),('ato','low',149),('ato','moderate',287),('ato','high',370)]:
            selected, info = baselines.selected_catalog(mode, name)
            actual = collect_controls(selected['catalog'])
            self.assertEqual(len(actual), count)
            expected = values['lato-reference']['control_ids'] if mode == 'lato' else values[name]['profile']['imports'][0]['include-controls'][0]['with-ids']
            self.assertEqual(set(actual), set(expected))

    def test_generation_preserves_team_work_and_ids(self):
        out = self.root / 'draft'
        report = wizard.generate(self.repo, self.answers, out)
        self.assertEqual(report['total_controls'], 58)
        first = (out / 'scaffold-state.json').read_bytes()
        manifest = load_json(out / 'manifest.json')
        self.assertEqual(len([m for m in manifest['modules'] if m['kind'] == 'diagram']), 0)
        self.assertIn('diagram-readiness', {m['id'] for m in manifest['modules']})
        response = out / 'controls/ac/ac-2.response.md';response.write_text('Team implementation edit.\n')
        chapter = out / 'chapters/boundary.md';chapter.write_text('Owner reviewed boundary.\n')
        wizard.generate(self.repo, self.answers, out)
        self.assertEqual(first, (out / 'scaffold-state.json').read_bytes())
        self.assertEqual(response.read_text(), 'Team implementation edit.\n')
        self.assertEqual(chapter.read_text(), 'Owner reviewed boundary.\n')
        self.assertIn('chapters/boundary.md', load_json(out / 'wizard-report.json')['preserved_user_files'])

    def test_full_ato_generation_and_missing_answers(self):
        self.data.update(mode='ato', baseline='low');self.answers.write_text(json.dumps(self.data))
        out = self.root / 'full'
        self.assertEqual(wizard.generate(self.repo, self.answers, out)['total_controls'], 149)
        self.data['scope_confirmed'] = False;self.answers.write_text(json.dumps(self.data))
        with self.assertRaisesRegex(ValueError, 'explicitly confirm'):
            wizard.generate(self.repo, self.answers, self.root / 'blocked')
        self.assertFalse((self.root / 'blocked').exists())

    def test_existing_nonwizard_project_refused(self):
        out = self.root / 'owned';out.mkdir();(out / 'notes.md').write_text('User work')
        with self.assertRaisesRegex(ValueError, 'not a wizard-owned'):
            wizard.generate(self.repo, self.answers, out)
        self.assertEqual((out / 'notes.md').read_text(), 'User work')

    def test_interactive_questions_preserve_existing_answers(self):
        self.data['system_name'] = ''
        from inheritance import defaults
        self.data['inheritance'] = defaults()
        self.answers.write_text(json.dumps(self.data))
        prompts = []
        def answer(question):
            prompts.append(question)
            return 'Answered system'
        result = wizard.ask(self.answers, answer)
        self.assertEqual(result['system_name'], 'Answered system')
        self.assertEqual(result['system_owner'], 'Example owner')
        self.assertEqual(len(prompts), 1)

    def test_cli_asks_missing_inheritance_after_normalization(self):
        prompts=[]
        def answer(question):
            prompts.append(question)
            return 'unknown'
        result=wizard.ask(self.answers,answer)
        self.assertEqual(len(prompts),5)
        self.assertEqual(set(result['inheritance'].values()),{'unknown'})

    def test_intake_cannot_write_into_application(self):
        with self.assertRaisesRegex(ValueError, 'outside the application'):
            wizard.intake(self.repo, self.repo / 'intake')
        self.assertFalse((self.repo / 'intake').exists())

    def test_subdirectory_input_cannot_bypass_application_write_guard(self):
        sub = self.repo / 'src';sub.mkdir()
        with self.assertRaisesRegex(ValueError, 'outside the application'):
            wizard.intake(sub, self.repo / 'intake')
        with self.assertRaisesRegex(ValueError, 'outside the application'):
            wizard.generate(sub, self.answers, self.repo / 'draft')
        self.assertFalse((self.repo / 'draft').exists())

    def test_edited_diagram_preserves_whole_topology_unit(self):
        out = self.root / 'draft'
        wizard.generate(self.repo, self.answers, out)
        # Simulate a legacy project with previously authored diagrams. Text generation
        # must not reinterpret the legacy topology or overwrite any source/metadata.
        from diagram_starters import starters
        files, _ = starters()
        for name, content in files.items():
            target = out / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        path = out / 'diagrams/context.puml'
        path.write_text(path.read_text().replace('@enduml', "' Owner annotation\n@enduml"))
        old_metadata = (out / 'diagrams.json').read_bytes()
        old_source = path.read_bytes()
        self.data['topology']['nodes'].append({'id':'store','title':'Store','boundary':'inside'})
        self.answers.write_text(json.dumps(self.data))
        wizard.generate(self.repo, self.answers, out)
        self.assertEqual((out / 'diagrams.json').read_bytes(), old_metadata)
        self.assertEqual(path.read_bytes(), old_source)
        self.assertTrue((out / 'diagrams.json').exists())

    def test_text_generation_without_topology_composes_and_preserves_legacy_answer(self):
        from build import compose
        self.data.pop('topology')
        self.answers.write_text(json.dumps(self.data))
        out = self.root / 'text-only'
        wizard.generate(self.repo, self.answers, out)
        files = compose(out / 'manifest.json')
        self.assertIn(b'Diagrams pending separate review', files['document.md'])
        self.assertFalse((out / 'diagrams.json').exists())
        self.data['topology'] = {'legacy_unparsed': 'keep this answer'}
        self.answers.write_text(json.dumps(self.data))
        before = self.answers.read_bytes()
        wizard.generate(self.repo, self.answers, out)
        self.assertEqual(self.answers.read_bytes(), before)

    def test_cli_export_refuses_application_destination(self):
        command = [sys.executable, str(Path(wizard.__file__)), 'generate', '--repository', str(self.repo),
                   '--answers', str(self.answers), '--output', str(self.root / 'draft'),
                   '--export', str(self.repo / 'export'), '--plantuml-jar', '/missing/tool.jar', '--pandoc', '/missing/pandoc']
        result = subprocess.run(command, capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 1)
        self.assertIn('outside the application', result.stderr)
        self.assertFalse((self.repo / 'export').exists())

    def test_inheritance_is_exported_and_user_edits_preserved(self):
        self.data['inheritance'] = {'hosting_service': 'cloud-gov-pages', 'egress_proxy': 'no',
            'gsa_common_controls': 'unknown', 'org_dependency_management': 'unknown', 'sha_pinning': 'no'}
        self.answers.write_text(json.dumps(self.data))
        out = self.root / 'draft'
        wizard.generate(self.repo, self.answers, out)
        manifest = load_json(out / 'manifest.json')
        self.assertEqual(len([m for m in manifest['modules'] if m['id']=='inherited-responsibilities']), 1)
        report = load_json(out / 'inheritance/map.json')
        self.assertNotIn('cg-egress-proxy', {r['provider_id'] for r in report['mappings']})
        path = out / 'inheritance/responsibilities.md'
        path.write_text(path.read_text() + '\nOwner review note.\n')
        old = (out / 'inheritance/map.json').read_bytes()
        self.data['inheritance']['gsa_common_controls'] = 'no'
        self.answers.write_text(json.dumps(self.data))
        wizard.generate(self.repo, self.answers, out)
        self.assertEqual((out / 'inheritance/map.json').read_bytes(), old)
        self.assertIn('Owner review note.', path.read_text())
        self.assertIn('inheritance/map.json', load_json(out / 'wizard-report.json')['preserved_user_files'])


if __name__ == '__main__':
    unittest.main()
