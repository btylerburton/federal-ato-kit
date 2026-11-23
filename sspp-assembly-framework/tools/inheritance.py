"""Map declared provider references to selected controls without asserting inheritance."""
from pathlib import Path
from build import load_json, sha, json_bytes
from scaffold import collect_controls, markdown_file

ROOT = Path(__file__).resolve().parents[2]
REFERENCES = ROOT / 'examples/component-definitions'
CHOICES = {'yes', 'no', 'unknown'}
QUESTIONS = [
    {'id': 'hosting_service', 'question': 'Hosting service (cloud-gov-paas, cloud-gov-pages, other, unknown)?',
     'choices': ['cloud-gov-paas', 'cloud-gov-pages', 'other', 'unknown']},
    {'id': 'egress_proxy', 'question': 'Do you actually deploy cg-egress-proxy and restrict direct outbound access? (yes/no/unknown)', 'choices': sorted(CHOICES)},
    {'id': 'gsa_common_controls', 'question': 'Does your system fall within the supplied GSA common-control catalog scope? (yes/no/unknown)', 'choices': sorted(CHOICES)},
    {'id': 'org_dependency_management', 'question': 'Is this repository enrolled in the organization dependency-management service? (yes/no/unknown)', 'choices': sorted(CHOICES)},
    {'id': 'sha_pinning', 'question': 'Are external GitHub Actions pinned to verified full commit SHAs (not moving tags), with reviewed updates? (yes/no/unknown)', 'choices': sorted(CHOICES)},
]


def defaults():
    return {q['id']: 'unknown' for q in QUESTIONS}


def answers_for(answers):
    supplied = answers.get('inheritance', {})
    if not isinstance(supplied, dict) or set(supplied) - set(defaults()):
        raise ValueError('Invalid inheritance answer fields')
    result = dict(defaults(), **supplied)
    for q in QUESTIONS:
        if result[q['id']] not in q['choices']:
            raise ValueError(f"Invalid inheritance answer: {q['id']}")
    return result


def ask(answers, prompt, save):
    values = answers_for(answers)
    for q in QUESTIONS:
        # An explicit unknown is a durable answer, not permission to infer applicability.
        if q['id'] in answers.get('inheritance', {}):
            continue
        while True:
            value = prompt(q['question'] + ' ').strip().lower()
            if value in q['choices']:
                break
            print('Choose one of: ' + ', '.join(q['choices']))
        values[q['id']] = value
        answers.setdefault('inheritance', {})[q['id']] = value
        save()
    return values


def properties(holder, name):
    return [p['value'] for p in holder.get('props', []) if p.get('name') == name]


def rules(component):
    identifiers = {p.get('remarks'): p['value'] for p in component.get('props', []) if p.get('name') == 'Rule_Id'}
    return {identifiers[p.get('remarks')]: p['value'] for p in component.get('props', [])
            if p.get('name') == 'Rule_Description' and p.get('remarks') in identifiers}


def reference(name):
    entry = load_json(REFERENCES / 'index.json')['components'][name]
    path = REFERENCES / entry['path']
    if sha(path.read_bytes()) != entry['sha256']:
        raise ValueError(f'Component reference hash mismatch: {name}')
    return entry, load_json(path)['component-definition']


def candidates(answers):
    values = answers_for(answers)
    selections = {'cloud_gov': 'yes' if values['hosting_service'] in {'cloud-gov-paas', 'cloud-gov-pages'}
                  else ('no' if values['hosting_service'] == 'other' else 'unknown'),
                  'cg-egress-proxy': values['egress_proxy'], 'gsa_common_controls': values['gsa_common_controls'],
                  'org-dependency-management': values['org_dependency_management']}
    return values, selections


def mapping(answers, catalog):
    selected = set(collect_controls(catalog.get('catalog', catalog)))
    values, selections = candidates(answers)
    records, sources = [], []
    for name, declaration in selections.items():
        if declaration == 'no':
            continue
        entry, definition = reference(name)
        caveats = ['Source assertions and historical versions; applicability and evidence require review.']
        if name == 'cloud_gov' and values['hosting_service'] == 'cloud-gov-pages':
            caveats.append('This definition describes cloud.gov PaaS, not a Pages-specific CRM. Pages inheritance is unresolved.')
        if name == 'cg-egress-proxy':
            caveats.append('Installing a proxy alone does not demonstrate removal of direct outbound access or the required ASG configuration.')
        sources.append(dict(entry, id=name, user_declaration=declaration, caveats=caveats))
        for component in definition.get('components', []):
            rule_map = rules(component)
            for implementation in component.get('control-implementations', []):
                for requirement in implementation.get('implemented-requirements', []):
                    if requirement['control-id'] not in selected:
                        continue
                    for statement in [requirement, *requirement.get('statements', [])]:
                        rule_ids = properties(statement, 'Rule_Id')
                        records.append({'provider_id': name, 'component_uuid': component['uuid'],
                            'control_id': requirement['control-id'], 'statement_id': statement.get('statement-id'),
                            'provider_statement': statement.get('description', ''),
                            'provider_asserted_status': properties(statement, 'implementation-status'),
                            'provider_rule_ids': rule_ids,
                            'provider_rule_descriptions': {key: rule_map.get(key, 'Rule description not supplied') for key in rule_ids},
                            'requirement_asserted_status': properties(requirement, 'implementation-status'),
                            'user_declaration': declaration, 'inheritance_decision': 'UNRESOLVED',
                            'system_implementation_status': 'UNFILLED', 'evidence_status': 'NOT_ASSESSED'})
    return {'schema_version': 1, 'answers': values, 'sources': sources, 'mappings': records,
            'unmapped_selected_controls': sorted(selected - {r['control_id'] for r in records}),
            'sha_pinning': {'user_declaration': values['sha_pinning'], 'classification': 'implementation practice, not automatic common-control inheritance',
                            'evidence_status': 'NOT_ASSESSED'}}


def report_markdown(report):
    rows = ['# Candidate inherited and shared responsibilities',
            'These are imported reference assertions matched to the selected controls. A yes answer declares use, '
            'not verified inheritance. Unknown answers keep applicability open. No system status is completed automatically.']
    for source in report['sources']:
        rows += [f"## {source['title']}", f"Version: `{source['version']}`; source date: `{source['last_modified']}`; "
                 f"SHA-256: `{source['sha256']}`; user declaration: **{source['user_declaration']}**."]
        rows += ['- ' + caveat for caveat in source['caveats']]
    for record in report['mappings']:
        rows += [f"### {record['control_id']} / {record['statement_id'] or 'control-level'} / {record['provider_id']}",
                 'Provider asserted status: ' + (', '.join(record['provider_asserted_status']) or 'not supplied') +
                 '. **System inheritance: UNRESOLVED; evidence: NOT_ASSESSED.**',
                 record['provider_statement'] or 'No control-level narrative; review the part mappings below.']
        rows += [f"- Source rule `{key}`: {value}" for key, value in record['provider_rule_descriptions'].items()]
        rows.append('Application owner action: confirm applicable service/scope and rule prerequisites; '
                    'document remaining customer responsibilities, approved parameters and evidence in the control response.')
    rows += ['## SHA pinning and dependency practice',
             f"User declaration: {report['answers']['sha_pinning']}. No workflow execution or provider enrollment inferred.",
             'Use a verified full 40-character commit SHA for third-party GitHub Actions, retain a version comment, '
             'and review automated updates. A moving tag such as `actions/checkout@v4` is not immutable pinning.',
             'Illustrative syntax (placeholder, not a usable verified commit): `uses: actions/checkout@<VERIFIED_40_CHARACTER_COMMIT_SHA> # reviewed release`.',
             'A lockfile records dependencies; Renovate onboarding, org preset, SLA tracking and actions scanning '
             'are separate claims needing evidence. Pinning is associated with the dependency-management reference, '
             'not proof of eligibility for the GSA common-control catalog.']
    # Provider references may contain catalog-local bookmarks; preserve as visible source text.
    import re
    content = '\n\n'.join(rows)
    content = re.sub(r'\[([^\]]+)\]\((#[^)]+)\)', r'\1 (source reference: `\2`)', content)
    return markdown_file('Candidate inherited responsibilities', 'Versioned reference assertions and unresolved application responsibilities', content)


def generated_files(answers, catalog):
    report = mapping(answers, catalog)
    return {'inheritance/map.json': json_bytes(report), 'inheritance/responsibilities.md': report_markdown(report)}
