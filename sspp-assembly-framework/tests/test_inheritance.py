"""Preserve source claims and prerequisite rules without inventing inherited completion."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import inheritance
from baselines import selected_catalog
from build import markdown


class InheritanceTests(unittest.TestCase):
    def test_all_four_pinned_references_load(self):
        for name in ['cloud_gov', 'cg-egress-proxy', 'gsa_common_controls', 'org-dependency-management']:
            record, definition = inheritance.reference(name)
            self.assertTrue(definition['components'])
            self.assertEqual(record['version'], definition['metadata']['version'])

    def test_pages_caveat_no_automatic_completion(self):
        catalog, _ = selected_catalog('lato', None)
        report = inheritance.mapping({'inheritance': {'hosting_service':'cloud-gov-pages',
            'egress_proxy':'yes', 'gsa_common_controls':'yes', 'org_dependency_management':'yes', 'sha_pinning':'yes'}}, catalog)
        cloud = next(s for s in report['sources'] if s['id']=='cloud_gov')
        self.assertTrue(any('Pages' in c for c in cloud['caveats']))
        self.assertGreater(len(report['mappings']), 10)
        self.assertTrue(any(r['statement_id'] for r in report['mappings']))
        self.assertTrue(any(r['provider_asserted_status'] for r in report['mappings']))
        self.assertTrue(all(r['inheritance_decision']=='UNRESOLVED' and r['system_implementation_status']=='UNFILLED' for r in report['mappings']))
        text = markdown(inheritance.report_markdown(report), {})
        self.assertIn('NOT_ASSESSED', text)
        self.assertIn('full 40-character commit SHA', text)

    def test_no_answers_exclude_and_unknowns_remain_candidates(self):
        catalog, _ = selected_catalog('lato', None)
        no = {'hosting_service':'other','egress_proxy':'no','gsa_common_controls':'no','org_dependency_management':'no','sha_pinning':'no'}
        self.assertEqual(inheritance.mapping({'inheritance':no}, catalog)['mappings'], [])
        unknown = inheritance.mapping({}, catalog)
        self.assertEqual(len(unknown['sources']),4)
        self.assertTrue(all(r['user_declaration']=='unknown' for r in unknown['mappings']))

    def test_selection_and_rule_descriptions_are_preserved(self):
        catalog = {'catalog': {'controls':[{'id':'sc-7','title':'Boundary'}]}}
        report = inheritance.mapping({'inheritance': {'hosting_service':'other','egress_proxy':'yes',
            'gsa_common_controls':'no','org_dependency_management':'no'}}, catalog)
        self.assertTrue(report['mappings'])
        self.assertEqual({r['control_id'] for r in report['mappings']}, {'sc-7'})
        rules = [value for r in report['mappings'] for value in r['provider_rule_descriptions'].values()]
        self.assertTrue(any('public-networks-egress' in text for text in rules))

    def test_ask_skips_durable_no_and_unknown(self):
        answers = {'inheritance': inheritance.defaults()}
        def fail(_): raise AssertionError('Should preserve explicit unknown')
        inheritance.ask(answers, fail, lambda: None)
        with self.assertRaisesRegex(ValueError, 'Invalid inheritance answer'):
            inheritance.answers_for({'inheritance': {'sha_pinning': True}})


if __name__ == '__main__':
    unittest.main()
