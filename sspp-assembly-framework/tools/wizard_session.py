"""Dependency-free wizard validation and durable, resumable sessions."""
import copy
import os
import re
import tempfile
from datetime import date
from pathlib import Path

from build import json_bytes, load_json, sha
from inheritance import answers_for, defaults
from repository_intake import checkout_root, inspect, questions

SECTIONS = ('system', 'scope', 'inheritance', 'topology', 'review')
SYSTEM = {'system_name', 'system_owner', 'environment', 'date'}
SCOPE = {'mode', 'baseline', 'data_categories', 'boundary_summary', 'scope_confirmed'}
PLACEHOLDERS = {'default', 'unknown', 'tbd', 'unfilled', 'n/a'}


def normalize(answers, today=None, suggested_name=None):
    result = copy.deepcopy(answers)
    if not isinstance(result, dict):
        raise ValueError('Answers must be a JSON object')
    for key in ('mode', 'baseline'):
        if isinstance(result.get(key), str):
            result[key] = result[key].strip().lower()
    if not result.get('date'):
        result['date'] = (today or date.today()).isoformat()
    if suggested_name and not result.get('system_name'):
        result['system_name'] = suggested_name
    result.setdefault('topology', {'nodes': [], 'flows': []})
    result.setdefault('inheritance', {})
    return result


def field_issue(field, value, answers):
    if field in SYSTEM | {'boundary_summary'}:
        if not isinstance(value, str) or not value.strip() or '\n' in value or '\r' in value:
            return 'Enter a nonempty single-line value.'
    if field == 'date':
        try:
            if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
                return 'Use YYYY-MM-DD.'
            date.fromisoformat(value)
        except (TypeError, ValueError):
            return 'Enter a real calendar date (YYYY-MM-DD).'
    if field == 'boundary_summary' and value.strip().lower() in PLACEHOLDERS:
        return 'Describe the proposed scope; “default” or “unknown” is not a boundary.'
    if field == 'mode' and value not in {'lato', 'ato'}:
        return 'Choose LATO reference or ATO.'
    if field == 'baseline' and answers.get('mode') == 'ato' and value not in {'low', 'moderate', 'high'}:
        return 'Choose an owner-selected Low, Moderate or High baseline.'
    if field == 'scope_confirmed' and value is not True:
        return 'Owner must explicitly confirm the draft scope and selection.'
    if field == 'data_categories' and (not isinstance(value, list) or not value or
            any(not isinstance(v, str) or not v.strip() or '\n' in v or '\r' in v for v in value)):
        return 'Enter at least one data category.'
    return None


def validate_node(node):
    if not isinstance(node, dict) or not re.fullmatch(r'[a-z][a-z0-9_]*', str(node.get('id', ''))):
        raise ValueError('Node ID: lowercase letters, digits and underscores; start with a letter.')
    if not isinstance(node.get('title'), str) or not re.fullmatch(r'[A-Za-z0-9 ._()/:-]{1,100}', node['title']):
        raise ValueError('Node title: 1–100 plain display characters (letters, digits, spaces, ._()/:-).')
    if node.get('boundary') not in {'inside', 'outside'}:
        raise ValueError('Choose inside or outside for node boundary placement.')


def validate_flow(flow, ids):
    if not isinstance(flow, dict) or flow.get('from') not in ids or flow.get('to') not in ids:
        raise ValueError('Choose existing nodes for both flow endpoints.')
    for key in ('data', 'protocol', 'authentication', 'storage'):
        value = flow.get(key)
        if not isinstance(value, str) or not value.strip() or '\n' in value or '\r' in value:
            raise ValueError(f'Flow {key} requires a nonempty single-line description.')


def topology_issue(topology, require_complete=True):
    try:
        if not isinstance(topology, dict):
            raise ValueError('Topology must contain nodes and flows.')
        nodes, flows = topology.get('nodes'), topology.get('flows')
        if not isinstance(nodes, list) or not isinstance(flows, list):
            raise ValueError('Topology needs node and flow arrays.')
        if len(nodes) > 40 or len(flows) > 100:
            raise ValueError('Use at most 40 nodes and 100 flows; split larger diagrams.')
        ids = set()
        for node in nodes:
            validate_node(node)
            if node['id'] in ids:
                raise ValueError('Node IDs must be unique.')
            ids.add(node['id'])
        for flow in flows:
            validate_flow(flow, ids)
        if require_complete and (not nodes or not flows):
            raise ValueError('Add components and at least one directed data flow.')
    except (ValueError, TypeError) as error:
        return str(error)
    return None


def answer_issues(answers, include_topology=True):
    result = {}
    for key in sorted(SYSTEM | SCOPE):
        error = field_issue(key, answers.get(key), answers)
        if error:
            result[key] = error
    try:
        answers_for(answers)
    except (ValueError, TypeError) as error:
        result['inheritance'] = str(error)
    if include_topology:
        error = topology_issue(answers.get('topology'))
        if error:
            result['topology'] = error
    return result


def atomic_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink():
        raise ValueError('Refusing a symlinked state file')
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix='.wizard-', delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(json_bytes(value))
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


class WizardSession:
    def __init__(self, repository, workspace, today=None):
        self.repository = checkout_root(repository)
        self.workspace = workspace.absolute()
        # Reject aliases before resolve so an existing symlink cannot redirect writes.
        if any(p.is_symlink() for p in [self.workspace, *self.workspace.parents]):
            raise ValueError('Workspace and its parents must not be symlinks')
        self.workspace = self.workspace.resolve()
        if self.workspace.is_relative_to(self.repository) or self.repository.is_relative_to(self.workspace):
            raise ValueError('Workspace must be outside the application checkout')
        self.answers_path = self.workspace / 'intake/answers.json'
        self.state_path = self.workspace / 'intake/session.json'
        intake = self.answers_path.parent
        if intake.is_symlink() or (intake.exists() and any(p.is_symlink() for p in intake.rglob('*'))):
            raise ValueError('Intake contains a symlink')
        self.notices = []
        self._save_failed = False
        self.current_step = 'system'
        self._state_hash = sha(self.state_path.read_bytes()) if self.state_path.exists() else None
        if self.state_path.exists():
            state = load_json(self.state_path)
            if state.get('schema_version') != 1 or state.get('repository') != str(self.repository):
                raise ValueError('Saved session belongs to another repository or unsupported session version')
            self.current_step = state.get('step', 'system')
        if self.answers_path.exists():
            self.answers = load_json(self.answers_path)
            self.notices.append('Resumed saved answers. Edits autosave; review suggested defaults before generating.')
            if not self.state_path.exists():
                observation_path = intake / 'repository-observations.json'
                if not observation_path.is_file() or not (intake / 'questions.json').is_file():
                    raise ValueError('Existing intake is not recognized; preserve it and choose another workspace')
                saved_revision = load_json(observation_path).get('repository_revision')
                known = subprocess_revision_exists(self.repository, saved_revision)
                if not known:
                    raise ValueError('Legacy intake revision is not in this repository; cannot safely adopt answers')
                self.notices.append('Adopted legacy intake; repository association checked against its saved revision.')
        else:
            if intake.exists() and any(intake.iterdir()):
                raise ValueError('Intake directory has unrelated or incomplete files; nothing overwritten')
            self.answers = {'system_name': '', 'system_owner': '', 'environment': '', 'date': '',
                'mode': '', 'baseline': '', 'scope_confirmed': False, 'data_categories': [],
                'boundary_summary': '', 'topology': {'nodes': [], 'flows': []}}
        self._answer_hash = sha(self.answers_path.read_bytes()) if self.answers_path.exists() else None
        before = copy.deepcopy(self.answers)
        self.answers = normalize(self.answers, today, self.repository.name)
        if not isinstance(self.answers.get('inheritance'), dict):
            raise ValueError('Saved inheritance answers must be an object; original file preserved')
        # Malformed topologies are surfaced before UI access, never silently discarded.
        structural = topology_issue(self.answers.get('topology'), require_complete=False)
        if structural:
            raise ValueError(f'Saved topology requires repair: {structural}')
        if self._answer_hash and (before != self.answers or not self.state_path.exists()):
            backup = intake / ('answers.backup-' + self._answer_hash[:16] + '.json')
            original = self.answers_path.read_bytes()
            if backup.exists() and backup.read_bytes() != original:
                raise ValueError('Backup collision; original answers preserved')
            if not backup.exists():
                backup.write_bytes(original)
            self.notices.append(f'Original answers backed up as {backup.name}.')
        if not before.get('date'):
            self.notices.append(f'Document date defaulted to {self.answers["date"]}; retained on later resumes.')
        if not before.get('system_name'):
            self.notices.append('System name is a repository-name suggestion, not a discovered mission.')
        if not self.state_path.exists():
            self.current_step = next((s for s in SECTIONS[:-1] if self.section_issues(s)), 'review')
        if self.current_step not in SECTIONS:
            self.current_step = 'system'
        self.save()
        if not (intake / 'repository-observations.json').exists():
            atomic_json(intake / 'repository-observations.json', inspect(self.repository))
        atomic_json(intake / 'questions.json', {'questions': questions()})

    def save(self):
        if self._save_failed:
            raise ValueError('Previous save failed; reopen the session before making further edits')
        for path, expected in [(self.answers_path, self._answer_hash), (self.state_path, self._state_hash)]:
            actual = sha(path.read_bytes()) if path.exists() else None
            if actual != expected:
                raise ValueError('Session changed on disk; reopen to avoid overwriting another edit')
        try:
            atomic_json(self.answers_path, self.answers)
            self._answer_hash = sha(self.answers_path.read_bytes())
            atomic_json(self.state_path, {'schema_version': 1, 'repository': str(self.repository), 'step': self.current_step})
            self._state_hash = sha(self.state_path.read_bytes())
        except OSError:
            self._save_failed = True
            raise

    def update(self, field, value):
        if field not in SYSTEM | SCOPE | {'inheritance', 'topology'}:
            raise ValueError('Unknown answer field')
        previous = copy.deepcopy(self.answers)
        self.answers[field] = value.strip().lower() if field in {'mode', 'baseline'} and isinstance(value, str) else value
        try:
            self.save()
        except Exception:
            self.answers = load_json(self.answers_path) if self._save_failed and self.answers_path.exists() else previous
            raise

    def issues(self):
        return answer_issues(self.answers)

    def section_issues(self, section):
        issues = self.issues()
        keys = SYSTEM if section == 'system' else SCOPE if section == 'scope' else {section}
        return issues if section == 'review' else {k: v for k, v in issues.items() if k in keys}

    def record_step(self, section):
        if section not in SECTIONS:
            raise ValueError('Invalid wizard section')
        previous = self.current_step
        self.current_step = section
        try:
            self.save()
        except Exception:
            self.current_step = previous
            raise

    def add_node(self, node):
        topology = copy.deepcopy(self.answers['topology'])
        topology['nodes'].append(node)
        self._topology_update(topology)

    def remove_node(self, key):
        topology = copy.deepcopy(self.answers['topology'])
        if key not in {n['id'] for n in topology['nodes']}:
            raise ValueError('Choose an existing node')
        topology['nodes'] = [n for n in topology['nodes'] if n['id'] != key]
        topology['flows'] = [f for f in topology['flows'] if key not in {f['from'], f['to']}]
        self._topology_update(topology)

    def add_flow(self, flow):
        topology = copy.deepcopy(self.answers['topology'])
        topology['flows'].append(flow)
        self._topology_update(topology)

    def remove_flow(self, index):
        topology = copy.deepcopy(self.answers['topology'])
        if type(index) is not int or not 0 <= index < len(topology['flows']):
            raise ValueError('Choose an existing flow')
        topology['flows'].pop(index)
        self._topology_update(topology)

    def _topology_update(self, topology):
        error = topology_issue(topology, require_complete=False)
        if error:
            raise ValueError(error)
        self.update('topology', topology)

    def generate(self):
        issues = self.issues()
        if issues:
            raise ValueError('; '.join(f'{key}: {value}' for key, value in issues.items()))
        self.save()
        from wizard import generate
        return generate(self.repository, self.answers_path, self.workspace / 'project')


def subprocess_revision_exists(repository, revision):
    import subprocess
    if not isinstance(revision, str) or not re.fullmatch(r'[0-9a-f]{40,64}', revision):
        return False
    result = subprocess.run(['git', '-C', str(repository), 'cat-file', '-e', revision + '^{commit}'],
                            capture_output=True, timeout=15, check=False)
    return result.returncode == 0
