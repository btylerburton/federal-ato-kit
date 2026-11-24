#!/usr/bin/env python3
"""Attach an explicitly reviewed diagram project to a separately authored text project."""
import argparse
import copy
import tempfile
from pathlib import Path

from build import load_json, sha, json_bytes, validate
from diagram_flow import read_session, proposal_for, pending, check_generated
from scaffold import previous_state, scaffold
from wizard_session import atomic_json


def attach(repository, workspace, project):
    repository, root, state = read_session(repository, workspace)
    proposal = proposal_for(root, state)
    expected = sha(json_bytes({'proposal': proposal, 'answers': state['answers']}))
    if pending(proposal, state['answers']) or not state['confirmation'] or state['confirmation']['digest'] != expected:
        raise ValueError('Diagram proposal requires current explicit review before attachment')
    check_generated(root, state)
    source = root / 'project'
    if not (source / 'manifest.json').is_file():
        raise ValueError('Generate the reviewed diagram project before attachment')
    generated_review = load_json(source / 'review-record.json')
    if generated_review.get('confirmation') != state['confirmation']:
        raise ValueError('Generated diagrams predate the current review; regenerate before attachment')
    project = project.absolute()
    if any(p.is_symlink() for p in [project, *project.parents]) or any(p.is_symlink() for p in project.rglob('*')):
        raise ValueError('Attachment target cannot contain symlinks')
    project = project.resolve()
    if project.is_relative_to(repository) or repository.is_relative_to(project):
        raise ValueError('Attachment target must be outside the application checkout')
    if root.is_relative_to(project) or project.is_relative_to(root):
        raise ValueError('Diagram session and text project must be separate directories')
    previous_state(project)  # Check generated manifest/input ownership before mutation.
    config = load_json(project / 'project.json')
    support = load_json(project / 'supporting.json')
    current_manifest = load_json(project / 'manifest.json')
    diagram_manifest = load_json(source / 'manifest.json')
    prefix = 'supporting/diagram-review'
    owned = project / prefix
    entries = []
    for module in diagram_manifest['modules']:
        entry = copy.deepcopy(module)
        entry['path'] = prefix + '/' + entry['path']
        entry['sha256'] = sha((source / module['path']).read_bytes())
        entries.append(entry)
    ids = {m['id'] for m in entries}
    existing = [m for m in support['modules'] if m.get('id') in ids]
    if existing:
        if existing != entries:
            raise ValueError('Conflicting existing diagram modules; preserve and reconcile them explicitly')
    else:
        if any(m['id'] in ids for m in current_manifest['modules']):
            raise ValueError('Existing diagram IDs conflict; legacy diagrams remain untouched')
        support['modules'].extend(entries)
    files = {name: (source / name).read_bytes() for name in state['generated']}
    if owned.exists():
        actual = {p.relative_to(owned).as_posix(): p.read_bytes() for p in owned.rglob('*') if p.is_file()}
        if actual != files:
            raise ValueError('Attached diagram files changed; nothing overwritten')
    # Validate resulting composition before copying any files.
    proposed = dict(current_manifest, modules=[m for m in current_manifest['modules']
                    if m['id'] != 'diagram-readiness' and m['id'] not in ids] + entries)
    validate(proposed)
    catalog = project / 'inputs/catalog.json'
    selected = project / 'inputs/selected-catalog.json'
    for name, content in files.items():
        target = owned / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    atomic_json(project / 'supporting.json', support)
    with tempfile.TemporaryDirectory(prefix='diagram-attach-') as temporary:
        copied = Path(temporary) / 'catalog.json'
        copied.write_bytes(catalog.read_bytes())
        chosen = Path(temporary) / 'selected.json'
        if selected.exists():
            chosen.write_bytes(selected.read_bytes())
        scaffold(copied, sha(copied.read_bytes()), project, config['title'], config['date'],
                 chosen if chosen.exists() else None, sha(chosen.read_bytes()) if chosen.exists() else None,
                 include_diagrams=False)
    return len(entries)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository', type=Path, required=True)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--project', type=Path, required=True)
    args = parser.parse_args()
    try:
        count = attach(args.repository, args.workspace, args.project)
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f'Attachment refused: {error}\n')
    print(f'ATTACHED: {count} reviewed diagram/provenance modules; text responses preserved')


if __name__ == '__main__':
    main()
