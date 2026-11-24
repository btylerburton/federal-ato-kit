#!/usr/bin/env python3
"""Repository intake → durable clarifications → baseline-selected SSPP review draft."""
import argparse
import json
import subprocess
import tempfile
from pathlib import Path
from build import json_bytes, load_json, sha
from baselines import selected_catalog
from repository_intake import inspect, questions, checkout_root
from scaffold import scaffold, markdown_file
from inheritance import generated_files, ask as ask_inheritance
from wizard_session import answer_issues, normalize, atomic_json, field_issue
from workspace_paths import validate_output


def require_answers(answers):
    answers.update(normalize(answers))
    issues = answer_issues(answers, include_topology=False)
    if issues:
        raise ValueError('; '.join(f'{key}: {value}' for key, value in issues.items()))


def intake(repository, output):
    repository = checkout_root(repository)
    report = inspect(repository)
    output = validate_output(repository, output, 'intake')
    if output.exists() and any(output.iterdir()):
        raise ValueError('Intake output must be new or empty; preserve previous answers. '
                         'Resume with tui --repository <repo> --workspace <parent-of-intake>, '
                         'or ask --answers <intake>/answers.json')
    output.mkdir(parents=True, exist_ok=True)
    (output / 'repository-observations.json').write_bytes(json_bytes(report))
    (output / 'questions.json').write_bytes(json_bytes({'questions': questions()}))
    (output / 'answers.json').write_bytes(json_bytes({'system_name': '', 'mode': '', 'baseline': '',
        'scope_confirmed': False, 'system_owner': '', 'environment': '', 'data_categories': [],
        'boundary_summary': '', 'date': '', 'topology': {'nodes': [], 'flows': []}}))
    return report


def ask(answer_path, prompt=input):
    answers = normalize(load_json(answer_path))
    atomic_json(answer_path, answers)
    for question in questions():
        key = question['id']
        if key == 'baseline' and answers.get('mode') != 'ato':
            continue
        if key == 'topology' or question.get('section') == 'inheritance':
            continue
        existing = answers.get(key)
        if not field_issue(key, existing, answers):
            continue
        while True:
            value = prompt(question['question'] + ' ').strip()
            if question.get('type') == 'boolean':
                value = value.lower() in {'yes', 'y'}
            elif question.get('type') == 'string-list':
                value = [part.strip() for part in value.split(',') if part.strip()]
            elif key in {'mode', 'baseline'}:
                value = value.lower()
            elif key == 'date' and not value:
                value = normalize({'date': ''})['date']
            error = field_issue(key, value, answers)
            if not error:
                answers[key] = value
                atomic_json(answer_path, answers)
                break
            print(error)
    require_answers(answers)
    ask_inheritance(answers, prompt, lambda: answer_path.write_bytes(json_bytes(answers)))
    return answers


def generate(repository, answer_path, output):
    repository = checkout_root(repository)
    answers = load_json(answer_path)
    require_answers(answers)
    catalog, selection = selected_catalog(answers['mode'], answers.get('baseline'))
    inherited = generated_files(answers, catalog)
    observations = inspect(repository)
    output = validate_output(repository, output, 'project')
    if output.exists() and any(output.iterdir()) and not (output / 'wizard-state.json').is_file():
        raise ValueError('Existing output is not a wizard-owned project; choose a new directory')
    # Build all selected shells; full catalog remains available from the library and scaffold tool.
    with tempfile.TemporaryDirectory(prefix='wizard-selection-') as temporary:
        selected = Path(temporary) / 'catalog.json'
        selected.write_bytes(json_bytes(catalog))
        pin = sha(selected.read_bytes())
        report, _ = scaffold(selected, pin, output, answers['system_name'], answers['date'], include_diagrams=False)
    note = ('# Repository-informed draft\n\n'
            f'System: {answers["system_name"]}\n\nOwner (user supplied): {answers["system_owner"]}\n\n'
            f'Environment (user supplied): {answers["environment"]}\n\n'
            f'Proposed boundary (user supplied): {answers["boundary_summary"]}\n\n'
            f'Data categories (user supplied): {", ".join(answers["data_categories"])}\n\n'
            f'Repository revision observed: `{observations["repository_revision"]}`\n\n'
            'Repository paths are leads for assessment, not verified implementations. '
            'All generated control responses remain UNFILLED/NOT_ASSESSED until authored and reviewed.\n\n'
            'This draft does not include signed authorizations or provider attestations.\n')
    desired = dict(inherited)
    desired['chapters/system-name.md'] = markdown_file('System intake', 'Repository and owner-supplied context', note)
    desired['chapters/boundary.md'] = markdown_file('Boundary intake', 'Proposed boundary from user answers', note)
    state_path = output / 'wizard-state.json'
    previous = load_json(state_path) if state_path.exists() else {'managed': {}}
    preserved = []
    managed = dict(previous['managed'])
    inheritance_edited = state_path.exists() and any(
        (name in managed and (not (output / name).is_file() or sha((output / name).read_bytes()) != managed[name]))
        or ((output / name).exists() and name not in managed)
        for name in inherited)
    for name, content in desired.items():
        path = output / name
        if inheritance_edited and name in inherited:
            preserved.append(name)
            continue
        if name in managed and sha(path.read_bytes()) != managed[name]:
            preserved.append(name)
            continue
        if name not in managed and state_path.exists() and path.exists():
            preserved.append(name)
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        managed[name] = sha(content)
    # Refresh manifest after diagram answers, preserving scaffold identities and authored files.
    with tempfile.TemporaryDirectory(prefix='wizard-selection-') as temporary:
        selected = Path(temporary) / 'catalog.json';selected.write_bytes(json_bytes(catalog))
        scaffold(selected, sha(selected.read_bytes()), output, answers['system_name'], answers['date'], include_diagrams=False)
    (output / 'repository-observations.json').write_bytes(json_bytes(observations))
    (output / 'wizard-report.json').write_bytes(json_bytes({'selection': selection, 'repository_revision': observations['repository_revision'],
        'selected_shells': report['total_controls'], 'preserved_user_files': preserved,
        'status': 'DRAFT_REQUIRES_IMPLEMENTATION_EVIDENCE', 'diagram_basis': 'Separate proposal/review flow; legacy diagram files preserved'}))
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
    p = sub.add_parser('tui', help='Start or resume the optional Textual interface')
    p.add_argument('--repository', type=Path, required=True)
    p.add_argument('--workspace', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == 'tui':
            try:
                from wizard_tui import launch
            except ModuleNotFoundError as error:
                if error.name not in {'textual', 'rich'}:
                    raise
                raise ValueError('Textual UI not installed. Run bash setup-tui.sh, then use .venv-tui/bin/python.') from error
            launch(args.repository, args.workspace)
        elif args.command == 'intake':
            intake(args.repository, args.output)
            print('QUESTIONS_READY: review questions.json and fill answers.json; no application code executed')
        elif args.command == 'ask':
            ask(args.answers)
            print('ANSWERS_READY: supplied answers validated; generation remains a review draft')
        else:
            if args.export and not args.pandoc:
                raise ValueError('--export requires --pandoc; --plantuml-jar is needed only for registered diagram source modules')
            if args.export:
                app_root = checkout_root(args.repository)
                validate_output(app_root, args.export, 'export')
            report = generate(args.repository, args.answers, args.output)
            if args.export:
                from pipeline import pipeline
                pipeline(args.output / 'manifest.json', args.export, args.plantuml_jar, args.pandoc)
                print(f'DRAFT_EXPORTED: {report["total_controls"]} selected controls; see export verification.json for included figures and gaps')
            else:
                print(f'DRAFT_READY: {report["total_controls"]} selected controls; diagramming is a separate review flow')
    except (ValueError, OSError, KeyError, TypeError, subprocess.SubprocessError) as error:
        parser.exit(1, f'Wizard blocked: {error}\n')


if __name__ == '__main__':
    main()
