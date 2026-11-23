#!/usr/bin/env python3
"""Repository intake → durable clarifications → baseline-selected SSPP review draft."""
import argparse
import json
import re
import subprocess
import tempfile
from pathlib import Path
from build import json_bytes, load_json, sha, validate
from baselines import KIT, selected_catalog
from repository_intake import inspect, questions, checkout_root
from scaffold import scaffold, markdown_file
from diagrams import validate as validate_diagram


def require_answers(answers):
    for key in ('system_name', 'system_owner', 'environment', 'boundary_summary', 'date'):
        if not isinstance(answers.get(key), str) or not answers[key].strip() or '\n' in answers[key]:
            raise ValueError(f'Clarification required: {key}')
    if answers.get('scope_confirmed') is not True:
        raise ValueError('Owner must explicitly confirm the draft selection')
    if not isinstance(answers.get('data_categories'), list) or not answers['data_categories'] or any(
            not isinstance(v, str) or not v.strip() for v in answers['data_categories']):
        raise ValueError('Clarification required: data_categories')
    if answers.get('mode') not in {'lato', 'ato'}:
        raise ValueError('Clarification required: mode')
    if answers['mode'] == 'ato' and answers.get('baseline') not in {'low', 'moderate', 'high'}:
        raise ValueError('Clarification required: baseline')
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', answers['date']):
        raise ValueError('Date must be YYYY-MM-DD')


def topology_files(answers):
    topology = answers.get('topology', {})
    if not isinstance(topology, dict):
        raise ValueError('Topology must be an object')
    nodes, flows = topology.get('nodes', []), topology.get('flows', [])
    if not isinstance(nodes, list) or not isinstance(flows, list) or not nodes:
        raise ValueError('Topology needs node and flow arrays')
    if len(nodes) > 40 or len(flows) > 100:
        raise ValueError('Split large topology into smaller reviewed diagrams')
    for node in nodes:
        if not isinstance(node, dict):
            raise ValueError('Node must be an object')
        title = node.get('title', '')
        if not isinstance(title, str) or not re.fullmatch(r'[A-Za-z0-9 ._()/:-]{1,100}', title):
            raise ValueError('Node titles must be plain display labels')
    if any(not isinstance(flow, dict) for flow in flows):
        raise ValueError('Flow must be an object')
    source = ['@startuml', 'title Proposed system view — user supplied, not verified',
              'rectangle "Proposed authorization boundary" {']
    source += [f' rectangle "{n["title"]}" as {n["id"]}' for n in nodes if n.get('boundary') == 'inside']
    source += ['}']
    source += [f'rectangle "{n["title"]}" as {n["id"]}' for n in nodes if n.get('boundary') == 'outside']
    source += [f'{f.get("from")} --> {f.get("to")} : flow {i+1}' for i, f in enumerate(flows)]
    source += ['@enduml']
    modules, files = [], {}
    for view in ['context', 'boundary', 'architecture', 'data-flow']:
        module = {'id': 'diagram-' + view, 'title': view.title() + ' view', 'kind': 'diagram',
                  'path': f'diagrams/{view}.puml', 'source': 'User-supplied clarification answers; not code-verified',
                  'view': view, 'environment': answers['environment'], 'revision': 'intake-1', 'review_status': 'draft',
                  'caption': 'Proposed ' + view + ' — review component placement and flows',
                  'alt': 'Proposed system components and directed flows', 'nodes': nodes, 'flows': flows}
        validate_diagram(module)
        modules.append(module)
        view_source = list(source)
        view_source[1] = 'title Proposed ' + view + ' view — user supplied, not verified'
        files[module['path']] = ('\n'.join(view_source) + '\n').encode()
    files['diagrams.json'] = json_bytes({'modules': modules})
    return files


def intake(repository, output):
    repository = checkout_root(repository)
    report = inspect(repository)
    if output.resolve().is_relative_to(repository.resolve()) or repository.resolve().is_relative_to(output.resolve()):
        raise ValueError('Intake output must be outside the application checkout')
    if output.exists() and any(output.iterdir()):
        raise ValueError('Intake output must be new or empty; preserve previous answers')
    output.mkdir(parents=True, exist_ok=True)
    (output / 'repository-observations.json').write_bytes(json_bytes(report))
    (output / 'questions.json').write_bytes(json_bytes({'questions': questions()}))
    (output / 'answers.json').write_bytes(json_bytes({'system_name': '', 'mode': '', 'baseline': '',
        'scope_confirmed': False, 'system_owner': '', 'environment': '', 'data_categories': [],
        'boundary_summary': '', 'date': '', 'topology': {'nodes': [], 'flows': []}}))
    return report


def ask(answer_path, prompt=input):
    answers = load_json(answer_path)
    for question in questions():
        key = question['id']
        if key == 'baseline' and answers.get('mode') != 'ato':
            continue
        if key == 'topology':
            continue
        existing = answers.get(key)
        if existing not in (None, '', [], False):
            continue
        value = prompt(question['question'] + ' ').strip()
        if question.get('type') == 'boolean':
            answers[key] = value.lower() in {'yes', 'y'}
        elif question.get('type') == 'string-list':
            answers[key] = [part.strip() for part in value.split(',') if part.strip()]
        else:
            answers[key] = value
        answer_path.write_bytes(json_bytes(answers))
    if not answers.get('topology', {}).get('nodes'):
        value = prompt('Topology JSON file (nodes and flows; see wizard guide example): ').strip()
        if value:
            answers['topology'] = load_json(Path(value))
            answer_path.write_bytes(json_bytes(answers))
    require_answers(answers)
    topology_files(answers)
    return answers


def generate(repository, answer_path, output):
    repository = checkout_root(repository)
    answers = load_json(answer_path)
    require_answers(answers)
    catalog, selection = selected_catalog(answers['mode'], answers.get('baseline'))
    diagrams = topology_files(answers)  # Fail before touching the project if answers are malformed.
    observations = inspect(repository)
    if output.resolve().is_relative_to(repository.resolve()) or repository.resolve().is_relative_to(output.resolve()):
        raise ValueError('Generate into a separate project directory, outside the application checkout')
    if output.exists() and any(output.iterdir()) and not (output / 'wizard-state.json').is_file():
        raise ValueError('Existing output is not a wizard-owned project; choose a new directory')
    # Build all selected shells; full catalog remains available from the library and scaffold tool.
    with tempfile.TemporaryDirectory(prefix='wizard-selection-') as temporary:
        selected = Path(temporary) / 'catalog.json'
        selected.write_bytes(json_bytes(catalog))
        pin = sha(selected.read_bytes())
        report, _ = scaffold(selected, pin, output, answers['system_name'], answers['date'])
    note = ('# Repository-informed draft\n\n'
            f'System: {answers["system_name"]}\n\nOwner (user supplied): {answers["system_owner"]}\n\n'
            f'Environment (user supplied): {answers["environment"]}\n\n'
            f'Proposed boundary (user supplied): {answers["boundary_summary"]}\n\n'
            f'Data categories (user supplied): {", ".join(answers["data_categories"])}\n\n'
            f'Repository revision observed: `{observations["repository_revision"]}`\n\n'
            'Repository paths are leads for assessment, not verified implementations. '
            'All generated control responses remain UNFILLED/NOT_ASSESSED until authored and reviewed.\n\n'
            'This draft does not include signed authorizations or provider attestations.\n')
    desired = dict(diagrams)
    desired['chapters/system-name.md'] = markdown_file('System intake', 'Repository and owner-supplied context', note)
    desired['chapters/boundary.md'] = markdown_file('Boundary intake', 'Proposed boundary from user answers', note)
    state_path = output / 'wizard-state.json'
    previous = load_json(state_path) if state_path.exists() else {'managed': {}}
    preserved = []
    managed = dict(previous['managed'])
    diagram_names = set(diagrams)
    diagram_edited = state_path.exists() and any(
        name not in managed or not (output / name).is_file() or sha((output / name).read_bytes()) != managed[name]
        for name in diagram_names)
    for name, content in desired.items():
        path = output / name
        if diagram_edited and name in diagram_names:
            preserved.append(name)
            continue
        if name in managed and sha(path.read_bytes()) != managed[name]:
            preserved.append(name)
            continue
        if name not in managed and state_path.exists():
            preserved.append(name)
            continue
        path.write_bytes(content)
        managed[name] = sha(content)
    # Refresh manifest after diagram answers, preserving scaffold identities and authored files.
    with tempfile.TemporaryDirectory(prefix='wizard-selection-') as temporary:
        selected = Path(temporary) / 'catalog.json';selected.write_bytes(json_bytes(catalog))
        scaffold(selected, sha(selected.read_bytes()), output, answers['system_name'], answers['date'])
    (output / 'repository-observations.json').write_bytes(json_bytes(observations))
    (output / 'wizard-report.json').write_bytes(json_bytes({'selection': selection, 'repository_revision': observations['repository_revision'],
        'selected_shells': report['total_controls'], 'preserved_user_files': preserved,
        'status': 'DRAFT_REQUIRES_IMPLEMENTATION_EVIDENCE', 'diagram_basis': 'User-supplied topology, not inferred architecture'}))
    state_path.write_bytes(json_bytes({'managed': managed, 'answers_sha256': sha(answer_path.read_bytes())}))
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ['intake', 'generate']:
        p = sub.add_parser(name);p.add_argument('--repository', type=Path, required=True);p.add_argument('--output', type=Path, required=True)
        if name == 'generate':
            p.add_argument('--answers', type=Path, required=True)
            p.add_argument('--export', type=Path, help='Also render Markdown/assets/DOCX to a separate directory')
            p.add_argument('--plantuml-jar', type=Path)
            p.add_argument('--pandoc', type=Path)
    p = sub.add_parser('ask');p.add_argument('--answers', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == 'intake':
            intake(args.repository, args.output)
            print('QUESTIONS_READY: review questions.json and fill answers.json; no application code executed')
        elif args.command == 'ask':
            ask(args.answers)
            print('ANSWERS_READY: supplied answers validated; generation remains a review draft')
        else:
            if args.export and (not args.plantuml_jar or not args.pandoc):
                raise ValueError('--export requires --plantuml-jar and --pandoc')
            if args.export:
                app_root = checkout_root(args.repository)
                if args.export.resolve().is_relative_to(app_root) or app_root.is_relative_to(args.export.resolve()):
                    raise ValueError('Export must be outside the application checkout')
            report = generate(args.repository, args.answers, args.output)
            if args.export:
                from pipeline import pipeline
                pipeline(args.output / 'manifest.json', args.export, args.plantuml_jar, args.pandoc)
                print(f'DRAFT_EXPORTED: {report["total_controls"]} selected controls; diagram bytes verified in DOCX')
            else:
                print(f'DRAFT_READY: {report["total_controls"]} selected controls with proposed diagram sources; use pipeline.py for DOCX')
    except (ValueError, OSError, KeyError, TypeError, subprocess.SubprocessError) as error:
        parser.exit(1, f'Wizard blocked: {error}\n')


if __name__ == '__main__':
    main()
