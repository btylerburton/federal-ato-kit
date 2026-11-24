#!/usr/bin/env python3
"""Offline, source-cited diagram proposal → clarification → reviewed draft project."""
import argparse
import copy
import datetime
import os
import re
import subprocess
from pathlib import Path, PurePosixPath

from build import json_bytes, load_json, sha, validate
from diagrams import check_source, validate as validate_diagram
from repository_intake import checkout_root
from workspace_paths import validate_workspace, excluded_workspaces

FORMAT = 'diagram-review-v1'
NODE_FIELDS = ('title', 'boundary')
FLOW_FIELDS = ('from', 'to', 'data', 'protocol', 'authentication', 'storage')
TOP_FIELDS = ('system_name', 'environment', 'date')
LABEL = re.compile(r'[A-Za-z0-9][A-Za-z0-9 ._()/,:+@-]{0,159}')
IDENTIFIER = re.compile(r'[a-z][a-z0-9_]{0,59}')


def git(repository, *args):
    result = subprocess.run(['git', '-C', str(repository), *args], capture_output=True,
                            timeout=30, check=False)
    if result.returncode:
        raise ValueError('Git revision/blob inspection failed')
    return result.stdout


def safe_source(name):
    if not isinstance(name, str) or not name or '\\' in name or ':' in name:
        return False
    path = PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or path.as_posix() != name:
        return False
    forbidden = {'.git', '.ssh', '.aws', '.azure', '.gnupg', 'secrets', 'credentials',
                 '.netrc', '.npmrc', '.pypirc', 'auth.json', 'terraform.tfstate'}
    for part in path.parts:
        lower = part.lower()
        if lower in forbidden or lower.startswith(('.env', '.dev.vars')):
            return False
        if any(word in lower for word in ('secret', 'credential', 'id_rsa', 'id_ed25519')):
            return False
    return path.suffix.lower() not in {'.pem', '.key', '.p12', '.pfx', '.jks', '.keystore'}


def source_tree(repository, revision):
    records = {}
    excluded = excluded_workspaces(repository)
    for entry in git(repository, 'ls-tree', '-rz', revision).split(b'\0'):
        if not entry:
            continue
        header, raw_name = entry.split(b'\t', 1)
        mode, kind, oid = header.decode().split()
        name = raw_name.decode('utf-8')
        if kind == 'blob' and mode in {'100644', '100755'} and safe_source(name) and PurePosixPath(name).parts[0] not in excluded:
            records[name] = oid
    return records


def workspace_root(repository, workspace):
    repository = checkout_root(repository)
    workspace = validate_workspace(repository, workspace)
    root = workspace / 'diagramming'
    if root.is_symlink() or (root.exists() and any(p.is_symlink() for p in root.rglob('*'))):
        raise ValueError('Diagram workspace contains a symlink')
    return repository, root


def save(path, value):
    temporary = path.with_suffix(path.suffix + '.tmp')
    if temporary.exists() or temporary.is_symlink():
        raise ValueError('Interrupted state write exists; preserve it before retrying')
    with temporary.open('xb') as stream:
        stream.write(json_bytes(value))
    os.replace(temporary, path)


def prepare(repository, workspace):
    repository, root = workspace_root(repository, workspace)
    revision = git(repository, 'rev-parse', 'HEAD').decode().strip()
    if (root / 'session.json').exists():
        read_session(repository, workspace)
        return root
    if root.exists() and any(root.iterdir()):
        raise ValueError('Existing diagramming directory is not owned by this flow')
    paths = sorted(source_tree(repository, revision))
    root.mkdir(parents=True, exist_ok=True)
    save(root / 'session.json', {'format': FORMAT, 'repository': str(repository),
         'repository_revision': revision, 'source_paths': paths, 'proposal_sha256': None,
         'answers': {}, 'answer_history': [], 'pending': [], 'confirmation': None, 'generated': {}})
    return root


def read_session(repository, workspace):
    repository, root = workspace_root(repository, workspace)
    state = load_json(root / 'session.json')
    if state.get('format') != FORMAT or state.get('repository') != str(repository):
        raise ValueError('Workspace repository/format mismatch')
    revision = git(repository, 'rev-parse', 'HEAD').decode().strip()
    if state.get('repository_revision') != revision:
        raise ValueError('Repository revision mismatch; use a new workspace for a new revision')
    return repository, root, state


def plain(value, label):
    if not isinstance(value, str) or not LABEL.fullmatch(value):
        raise ValueError(f'{label} needs a plain single-line label (maximum 160 characters)')


def field_value(proposal, key, value):
    if value is None or value == '' or value == 'unknown':
        return
    plain(value, key)
    field = key.split('/')[-1]
    if field == 'boundary' and value not in {'inside', 'outside'}:
        raise ValueError('Boundary must be inside or outside')
    if field in {'from', 'to'} and value not in {n['id'] for n in proposal['nodes']}:
        raise ValueError('Flow references an unknown node')
    if field == 'date':
        datetime.date.fromisoformat(value)


def fields(proposal):
    result = {key: proposal.get(key) for key in TOP_FIELDS}
    for group, names in [('nodes', NODE_FIELDS), ('flows', FLOW_FIELDS)]:
        for item in proposal[group]:
            result.update({f'{group}/{item["id"]}/{name}': item.get(name) for name in names})
    return result


def citation(repository, revision, tree, cache, ref, item_key):
    if not isinstance(ref, dict):
        raise ValueError('Invalid citation')
    name, lines = ref.get('path'), ref.get('lines')
    if not safe_source(name) or name not in tree:
        raise ValueError('Citation must reference a safe tracked source blob path')
    if not isinstance(lines, list) or len(lines) != 2 or any(type(n) is not int for n in lines):
        raise ValueError('Citation lines must be [first, last] integers')
    if name not in cache:
        oid = tree[name]
        if int(git(repository, 'cat-file', '-s', oid)) > 1024 * 1024:
            raise ValueError('Cited source blob exceeds 1 MiB')
        content = git(repository, 'cat-file', 'blob', oid)
        if b'\0' in content:
            raise ValueError('Citations require text source blobs')
        cache[name] = content.decode('utf-8').splitlines()
    if not 1 <= lines[0] <= lines[1] <= len(cache[name]):
        raise ValueError('Citation line range outside source blob')
    return {'item': item_key, 'path': name, 'lines': lines, 'blob': tree[name], 'revision': revision}


def validate_proposal(repository, state, proposal):
    if not isinstance(proposal, dict) or proposal.get('schema_version') != 1:
        raise ValueError('Proposal needs schema_version 1')
    revision = proposal.get('repository_revision')
    if revision != state['repository_revision'] or not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', revision):
        raise ValueError('Proposal repository revision mismatch (exact commit required)')
    tree = source_tree(repository, revision)
    cache, provenance = {}, []
    for group, limit in [('nodes', 40), ('flows', 100)]:
        items = proposal.get(group)
        if not isinstance(items, list) or not 1 <= len(items) <= limit:
            raise ValueError(f'Proposal needs 1..{limit} {group}')
        seen = set()
        for item in items:
            if not isinstance(item, dict) or not isinstance(item.get('id'), str) or not IDENTIFIER.fullmatch(item['id']):
                raise ValueError('Invalid node/flow ID')
            if item['id'] in seen:
                raise ValueError('Duplicate node/flow ID')
            seen.add(item['id'])
            if item.get('status') not in {'source-supported', 'hypothesis'}:
                raise ValueError('Every node/flow needs source-supported or hypothesis status')
            refs = item.get('evidence')
            if not isinstance(refs, list) or len(refs) > 20 or (not refs and item['status'] == 'source-supported'):
                raise ValueError('Source-supported nodes/flows need evidence citations')
            for ref in refs:
                provenance.append(citation(repository, revision, tree, cache, ref, f'{group}/{item["id"]}'))
            if group == 'nodes' and item.get('kind') not in {None, 'component', 'database', 'actor', 'queue'}:
                raise ValueError('Optional node kind must be component, database, actor or queue')
    values = fields(proposal)
    for key, value in values.items():
        field_value(proposal, key, value)
    unknown = proposal.get('unknown_fields')
    if not isinstance(unknown, list) or any(not isinstance(k, str) or k not in values for k in unknown):
        raise ValueError('unknown_fields must list field keys such as nodes/api/boundary')
    assumptions = proposal.get('assumptions')
    if not isinstance(assumptions, list) or len(assumptions) > 100:
        raise ValueError('assumptions must be an array (maximum 100)')
    for assumption in assumptions:
        plain(assumption, 'Assumption')
    return provenance


def pending(proposal, answers):
    keys = [key for key, value in fields(proposal).items()
            if value in (None, '', 'unknown') or key in proposal['unknown_fields']]
    keys += [f'{group}/{item["id"]}/review' for group in ('nodes', 'flows')
             for item in proposal[group] if item['status'] == 'hypothesis']
    keys += [f'assumptions/{i}' for i in range(len(proposal['assumptions']))]
    return [key for key in keys if key not in answers]


def import_proposal(repository, workspace, path):
    repository, root, state = read_session(repository, workspace)
    if not path.is_file():
        raise ValueError('Proposal file not found: ' + str(path) + '. prepare only creates the workspace. '
                         'Ask an authorized agent to review the pinned source and write proposal.json first; '
                         'see docs/kit/diagram-review.md and examples/diagram-proposal/proposal.json.')
    if path.stat().st_size > 1024 * 1024:
        raise ValueError('Proposal exceeds 1 MiB')
    content = path.read_bytes()
    proposal = load_json(path)
    provenance = validate_proposal(repository, state, proposal)
    target = root / 'proposal.json'
    if state['proposal_sha256']:
        if sha(content) != state['proposal_sha256']:
            raise ValueError('Different proposal: use a new workspace; prior human answers are preserved')
        if not target.is_file() or sha(target.read_bytes()) != state['proposal_sha256']:
            raise ValueError('Imported proposal modified or missing')
        return state
    if target.exists():
        raise ValueError('Unowned proposal file exists')
    target.write_bytes(content)
    state.update(proposal_sha256=sha(content), provenance=provenance, pending=pending(proposal, {}))
    save(root / 'session.json', state)
    return state


def proposal_for(root, state):
    path = root / 'proposal.json'
    if not state['proposal_sha256'] or sha(path.read_bytes()) != state['proposal_sha256']:
        raise ValueError('Import a proposal first; imported proposal must remain unmodified')
    return load_json(path)


def resolved(proposal, answers):
    result = copy.deepcopy(proposal)
    for key, value in answers.items():
        parts = key.split('/')
        if key in TOP_FIELDS:
            result[key] = value
        elif len(parts) == 3 and parts[0] in {'nodes', 'flows'} and parts[2] != 'review':
            next(item for item in result[parts[0]] if item['id'] == parts[1])[parts[2]] = value
    return result


def review(repository, workspace, answer_path=None, confirm=False, reviewer=None, prompt=input):
    _, root, state = read_session(repository, workspace)
    proposal = proposal_for(root, state)
    answers = state['answers']
    supplied = load_json(answer_path) if answer_path else None
    allowed = set(fields(proposal)) | set(pending(proposal, {}))
    if supplied is not None and (not isinstance(supplied, dict) or set(supplied) - allowed):
        raise ValueError('Answers must map known field keys to human-supplied values')
    keys = list(supplied) if supplied is not None else pending(proposal, answers)
    for key in keys:
        try:
            description = key
            if key.startswith('assumptions/'):
                description += ': ' + proposal['assumptions'][int(key.split('/')[1])]
            elif key.endswith('/review'):
                description += ': hypothesis; enter confirmed after reviewing proposal and corrections'
            value = supplied[key] if supplied is not None else prompt(f'{description} (blank to defer): ').strip()
        except EOFError:
            break
        if value == '':
            continue
        field_value(proposal, key, value)
        if value is None or value == 'unknown':
            raise ValueError('Human answers must resolve uncertainty; blank defers a question')
        if key.endswith('/review') and value != 'confirmed':
            raise ValueError('Hypothesis review requires confirmed; correct fields via --answers first')
        if answers.get(key) != value:
            state.setdefault('answer_history', []).append({'field': key, 'previous': answers.get(key),
                'value': value, 'at': datetime.datetime.now(datetime.timezone.utc).isoformat()})
        answers[key] = value
        state.update(confirmation=None, pending=pending(proposal, answers))
        save(root / 'session.json', state)
    state['pending'] = pending(proposal, answers)
    if confirm:
        if state['pending']:
            raise ValueError('Unresolved clarification fields remain: ' + ', '.join(state['pending']))
        plain(reviewer, 'Human reviewer')
        state['confirmation'] = {'reviewer': reviewer, 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                                 'digest': sha(json_bytes({'proposal': proposal, 'answers': answers}))}
    save(root / 'session.json', state)
    return state


def projection(proposal, view):
    nodes, flows = copy.deepcopy(proposal['nodes']), copy.deepcopy(proposal['flows'])
    if view == 'context':
        inside = {n['id'] for n in nodes if n['boundary'] == 'inside'}
        system_id = 'reviewed_system'
        while any(n['id'] == system_id for n in nodes):
            system_id += '_'
        nodes = [n for n in nodes if n['boundary'] == 'outside']
        if inside:
            nodes.insert(0, {'id': system_id, 'title': proposal['system_name'], 'boundary': 'inside'})
        projected = []
        for flow in flows:
            if flow['from'] in inside and flow['to'] in inside:
                continue
            flow['from'] = system_id if flow['from'] in inside else flow['from']
            flow['to'] = system_id if flow['to'] in inside else flow['to']
            projected.append(flow)
        flows = projected
    return nodes, flows


def view_source(proposal, view, nodes, flows):
    source = ['@startuml', f'title {proposal["system_name"]} - {view} - reviewed draft',
              'left to right direction']
    def declaration(node):
        kind = (node.get('kind') or 'component') if view == 'architecture' else 'rectangle'
        return f'{kind} "{node["title"]}" as {node["id"]}'
    if view in {'boundary', 'architecture'}:
        source.append('rectangle "Proposed authorization boundary - inside" {')
        source.extend(declaration(n) for n in nodes if n['boundary'] == 'inside')
        source.append('}')
        source.extend(declaration(n) for n in nodes if n['boundary'] == 'outside')
    else:
        source.extend(declaration(n) for n in nodes)
    for flow in flows:
        if view == 'data-flow':
            label = ' / '.join(flow[k] for k in ('data', 'protocol', 'authentication', 'storage'))
        elif view == 'architecture':
            label = flow['data'] + ' / ' + flow['protocol']
        elif view == 'boundary':
            label = flow['data'] + ' / auth: ' + flow['authentication']
        else:
            label = flow['data']
        source.append(f'{flow["from"]} --> {flow["to"]} : {label}')
    return ('\n'.join(source + ['@enduml', ''])).encode()


def project_files(proposal, state):
    files, modules = {}, []
    for view in ('context', 'boundary', 'architecture', 'data-flow'):
        nodes, flows = projection(proposal, view)
        module = {'id': 'diagram-' + view, 'title': view.title() + ' view', 'kind': 'diagram',
                  'path': f'diagrams/{view}.puml', 'source': 'AI proposal and explicit human clarification; see review-record.json',
                  'view': view, 'environment': proposal['environment'], 'revision': proposal['repository_revision'],
                  'review_status': 'reviewed', 'caption': 'Human-reviewed draft ' + view + '; owner approval pending',
                  'alt': proposal['system_name'] + ' ' + view + ' view', 'nodes': nodes, 'flows': flows}
        content = view_source(proposal, view, nodes, flows)
        validate_diagram(module)
        check_source(content, module)
        files[module['path']] = content
        modules.append(module)
    files['review-record.json'] = json_bytes({'format': FORMAT, 'proposal_sha256': state['proposal_sha256'],
        'repository_revision': state['repository_revision'], 'provenance': state['provenance'],
        'human_answers': state['answers'], 'answer_history': state.get('answer_history', []),
        'confirmation': state['confirmation'],
        'assumptions': proposal['assumptions'], 'resolved_proposal': proposal,
        'limits': 'AI-assisted draft. Citation existence is checked, not semantic support. Owner approval pending.'})
    modules.append({'id': 'diagram-review-record', 'title': 'Diagram review provenance', 'kind': 'attachment',
                    'path': 'review-record.json', 'source': 'Imported proposal and human clarification history'})
    manifest = {'schema_version': 1, 'document': {'title': proposal['system_name'] + ' diagrams',
                'revision': proposal['repository_revision'], 'date': proposal['date'], 'edition': 'review'}, 'modules': modules}
    validate(manifest)
    files['manifest.json'] = json_bytes(manifest)
    return files


def check_generated(root, state, desired=None):
    project = root / 'project'
    existing = {p.relative_to(project).as_posix() for p in project.rglob('*') if p.is_file()}
    if existing != set(state['generated']):
        raise ValueError('Generated project has untracked or missing files; preserve edits before rerunning')
    for name, expected in state['generated'].items():
        if not safe_source(name) or sha((project / name).read_bytes()) != expected:
            raise ValueError('Refusing modified generated output: ' + name)
    if desired is not None and set(state['generated']) - set(desired):
        raise ValueError('Generation would remove prior output')


def generate(repository, workspace):
    repository, root, state = read_session(repository, workspace)
    proposal = proposal_for(root, state)
    validate_proposal(repository, state, proposal)
    digest = sha(json_bytes({'proposal': proposal, 'answers': state['answers']}))
    if pending(proposal, state['answers']) or not state['confirmation'] or state['confirmation']['digest'] != digest:
        raise ValueError('Resolve pending fields and explicitly confirm human review before generation')
    effective = resolved(proposal, state['answers'])
    for key, value in fields(effective).items():
        field_value(effective, key, value)
    files = project_files(effective, state)
    check_generated(root, state, files)
    for name, content in files.items():
        path = root / 'project' / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    state['generated'] = {name: sha(content) for name, content in files.items()}
    save(root / 'session.json', state)
    return root / 'project' / 'manifest.json'


def render(repository, workspace, jar, pandoc=None):
    from build import build, owned_outputs
    _, root, state = read_session(repository, workspace)
    check_generated(root, state)
    owned_outputs(root / 'rendered')
    manifest = generate(repository, workspace)
    if pandoc:
        from pipeline import pipeline
        return pipeline(manifest, root / 'rendered', jar, pandoc)
    return build(manifest, root / 'rendered', jar)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for command in ('prepare', 'start', 'import', 'review', 'generate', 'render', 'tui'):
        child = sub.add_parser(command)
        child.add_argument('--repository', type=Path, required=True)
        child.add_argument('--workspace', type=Path, required=True)
        if command == 'import':
            child.add_argument('--proposal', type=Path, required=True)
        if command == 'review':
            child.add_argument('--answers', type=Path, help='JSON field-key to human-answer map; noninteractive')
            child.add_argument('--confirm', action='store_true', help='Explicitly attest human review of the resolved proposal')
            child.add_argument('--reviewer', help='Human reviewer name; required with --confirm')
        if command in {'render', 'tui'}:
            child.add_argument('--plantuml-jar', type=Path, required=command == 'render')
            child.add_argument('--pandoc', type=Path, help='Also generate DOCX with the existing pipeline')
        if command == 'tui':
            child.add_argument('--runner', type=Path, help='Trusted operator-owned agent argv configuration; never run automatically')
    args = parser.parse_args()
    try:
        if args.command == 'tui':
            try:
                from diagram_tui import launch
            except ModuleNotFoundError as error:
                if error.name not in {'textual', 'rich'}:
                    raise
                raise ValueError('Install the optional UI with bash setup-tui.sh and use .venv-tui/bin/python.') from error
            launch(args.repository, args.workspace, args.runner, args.plantuml_jar, args.pandoc)
        elif args.command in {'prepare', 'start'}:
            print('AI-assisted diagram workspace ready:', prepare(args.repository, args.workspace))
            print('NEXT: an authorized source-review agent must write proposal.json before import. '
                  'prepare does not run an LLM or extract topology; see docs/kit/diagram-review.md.')
        elif args.command == 'import':
            state = import_proposal(args.repository, args.workspace, args.proposal)
            print('PROPOSAL_IMPORTED; pending:', ', '.join(state['pending']) or 'human confirmation')
        elif args.command == 'review':
            state = review(args.repository, args.workspace, args.answers, args.confirm, args.reviewer)
            print('REVIEW_SAVED; pending:', ', '.join(state['pending']) or ('none; confirmed' if state['confirmation'] else 'human confirmation'))
        elif args.command == 'generate':
            print('REVIEWED_DRAFT:', generate(args.repository, args.workspace))
        else:
            print('RENDERED:', render(args.repository, args.workspace, args.plantuml_jar, args.pandoc), 'files')
    except (ValueError, OSError, UnicodeError, KeyError, TypeError, subprocess.SubprocessError) as error:
        parser.exit(1, f'Diagram flow refused: {error}\n')


if __name__ == '__main__':
    main()
