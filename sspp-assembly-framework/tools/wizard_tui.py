"""Optional Textual interface for the durable SSPP wizard session."""
import asyncio
import re
from pathlib import Path

from rich.text import Text
from textual import work
from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Checkbox, ContentSwitcher, Footer, Header, Input, Label, Select, Static

from inheritance import QUESTIONS
from wizard_session import WizardSession


SECTIONS = ('system', 'scope', 'inheritance', 'topology', 'review')
SYSTEM_FIELDS = ('system_name', 'system_owner', 'environment', 'date')
FLOW_FIELDS = ('from', 'to', 'data', 'protocol', 'authentication', 'storage')


class WizardApp(App):
    """Autosave user declarations without inferring approval or inheritance."""

    TITLE = 'SSPP draft wizard'
    SUB_TITLE = 'AI-assisted authoring • owner review required'
    BINDINGS = [('ctrl+s', 'save', 'Save'), ('ctrl+q', 'save_exit', 'Save & exit')]
    CSS = """
    Screen { background: $surface; }
    #body { height: 1fr; }
    #sidebar { width: 20; padding: 1; border-right: solid $primary; }
    #sidebar Button { width: 100%; min-width: 0; }
    ContentSwitcher { width: 1fr; }
    .panel { padding: 1 2; }
    Label { margin-top: 1; height: auto; }
    Input, Select { width: 100%; }
    .error { color: $error; height: auto; }
    .hint { color: $text-muted; height: auto; }
    .inventory { height: auto; border: solid $primary; padding: 1; }
    #status { height: auto; max-height: 4; padding: 0 1; }
    #navigation { height: 3; }
    #navigation Button { width: 1fr; min-width: 8; }
    #review-summary { height: auto; }
    """

    def __init__(self, session: WizardSession):
        super().__init__()
        self.session = session
        self.ready = False
        self.generating = False
        self.step = session.current_step if session.current_step in SECTIONS else 'system'

    def field(self, key, title=None):
        yield Label(title or key.replace('_', ' ').title(), markup=False)
        value = self.session.answers.get(key, '')
        if isinstance(value, list):
            value = ', '.join(value)
        yield Input(str(value or ''), id=key)
        yield Static('', id='error-' + key, classes='error', markup=False)

    def choice(self, key, options, value):
        yield Select([(Text(label), label) for label in options], value=value if value in options else Select.NULL,
                     id=key, prompt='Choose explicitly')
        yield Static('', id='error-' + key, classes='error', markup=False)

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(id='body'):
            with VerticalScroll(id='sidebar'):
                for step in SECTIONS:
                    yield Button(step.title(), id='step-' + step)
            with ContentSwitcher(initial=self.step, id='sections'):
                with VerticalScroll(id='system', classes='panel'):
                    yield Static('System identity', markup=False)
                    for field in SYSTEM_FIELDS:
                        yield from self.field(field)
                with VerticalScroll(id='scope', classes='panel'):
                    yield Label('Authorization track', markup=False)
                    yield from self.choice('mode', ('lato', 'ato'), self.session.answers.get('mode'))
                    yield Label('Baseline (required for ATO)', markup=False)
                    yield from self.choice('baseline', ('low', 'moderate', 'high'), self.session.answers.get('baseline'))
                    yield from self.field('data_categories', 'Data categories (comma-separated)')
                    yield from self.field('boundary_summary', 'Proposed boundary (describe the actual scope)')
                    yield Checkbox('I confirm this draft scope and selection',
                                   value=self.session.answers.get('scope_confirmed') is True, id='scope_confirmed')
                    yield Static('', id='error-scope_confirmed', classes='error', markup=False)
                with VerticalScroll(id='inheritance', classes='panel'):
                    yield Static('Declarations are not verified inheritance. Unknown keeps applicability open.',
                                 classes='hint', markup=False)
                    for question in QUESTIONS:
                        key = question['id']
                        yield Label(question['question'], markup=False)
                        yield from self.choice('inheritance-' + key, question['choices'],
                                               self.session.answers.get('inheritance', {}).get(key, 'unknown'))
                with VerticalScroll(id='topology', classes='panel'):
                    yield from self.topology_form()
                with VerticalScroll(id='review', classes='panel'):
                    yield Static('Review before generating a draft', markup=False)
                    yield Static('', id='review-summary', markup=False)
                    yield Static('Generated controls and diagrams remain drafts requiring owner review and evidence.',
                                 classes='hint', markup=False)
                    yield Button('Generate draft', id='generate', variant='primary')
                    yield Static('', id='generation-result', markup=False)
        yield Static('', id='status', markup=False)
        with Horizontal(id='navigation'):
            yield Button('Back', id='back')
            yield Button('Next', id='next', variant='primary')
            yield Button('Save & exit', id='save-exit')
        yield Footer()

    def topology_form(self):
        yield Static('Proposed components and directed data flows', markup=False)
        yield Static('', id='error-topology', classes='error', markup=False)
        yield Static('', id='nodes-list', classes='inventory', markup=False)
        for key in ('id', 'title'):
            yield Label('Node ' + key, markup=False)
            yield Input(id='node-' + key)
        yield Label('Boundary placement', markup=False)
        yield Select([('Inside', 'inside'), ('Outside', 'outside')], id='node-boundary')
        yield Button('Add node', id='add-node')
        yield Label('Remove node (also removes connected flows)', markup=False)
        yield Select([], id='remove-node-choice')
        yield Button('Remove node', id='remove-node', variant='warning')
        yield Static('', id='flows-list', classes='inventory', markup=False)
        for key in FLOW_FIELDS:
            yield Label('Flow ' + key, markup=False)
            if key in ('from', 'to'):
                yield Select([], id='flow-' + key)
            else:
                yield Input(id='flow-' + key)
        yield Button('Add flow', id='add-flow')
        yield Label('Remove flow', markup=False)
        yield Select([], id='remove-flow-choice')
        yield Button('Remove flow', id='remove-flow', variant='warning')

    def on_mount(self):
        self.refresh_topology()
        self.refresh_validation()
        self.set_status('\n'.join(self.session.notices) or 'Edits save automatically. Ctrl+S saves; Ctrl+Q saves and exits.')
        self.call_after_refresh(self.enable_autosave)

    def enable_autosave(self):
        self.ready = True

    def set_status(self, message):
        self.query_one('#status', Static).update(str(message))

    def refresh_validation(self):
        issues = self.session.issues()
        for widget in self.query('.error'):
            key = widget.id.removeprefix('error-')
            inheritance_key = key.replace('inheritance-', 'inheritance.', 1)
            widget.update(str(issues.get(key, issues.get(inheritance_key, ''))))
        for step in SECTIONS:
            pending = len(self.session.section_issues(step))
            self.query_one('#step-' + step, Button).label = Text(f'{step.title()} ({pending})' if pending else f'{step.title()} ✓')
        summary = [f'Answers: {self.session.answers_path}', f'Output: {self.session.workspace / "project"}', '']
        for field in (*SYSTEM_FIELDS, 'mode', 'baseline', 'data_categories', 'boundary_summary', 'scope_confirmed'):
            summary.append(f'{field.replace("_", " ").title()}: {self.session.answers.get(field, "")}')
        summary += ['', 'Provider declarations (unverified):']
        for question in QUESTIONS:
            key = question['id']
            value = self.session.answers.get('inheritance', {}).get(key, 'unknown')
            summary.append(f'{key.replace("_", " ").title()}: {value}')
        topology = self.session.answers.get('topology', {})
        summary += ['', f'Topology: {len(topology.get("nodes", []))} nodes, {len(topology.get("flows", []))} flows.']
        summary += ['', 'Resolve before generation:' if issues else 'Required answers complete. Ready to generate.']
        summary += [f'• {key}: {error}' for key, error in issues.items()]
        self.query_one('#review-summary', Static).update('\n'.join(summary))
        self.query_one('#generate', Button).disabled = bool(issues) or self.generating
        self.query_one('#back', Button).disabled = self.step == SECTIONS[0] or self.generating
        self.query_one('#next', Button).disabled = self.step == SECTIONS[-1] or self.generating

    def save_field(self, field, value):
        if not self.ready or self.generating:
            return
        try:
            if field.startswith('inheritance-'):
                inheritance = dict(self.session.answers.get('inheritance', {}))
                inheritance[field.removeprefix('inheritance-')] = value
                field, value = 'inheritance', inheritance
            if self.session.answers.get(field) == value:
                return
            self.session.update(field, value)
            self.set_status('Saved. Answers remain editable; approval is never inferred.')
        except Exception as error:
            self.set_status(f'Could not save: {error}')
        self.refresh_validation()

    def on_input_changed(self, event: Input.Changed):
        field = event.input.id
        if field in (*SYSTEM_FIELDS, 'data_categories', 'boundary_summary'):
            value = event.value
            if field == 'data_categories':
                value = [part.strip() for part in re.split(r'[,\n]', value) if part.strip()]
            self.save_field(field, value)

    def on_select_changed(self, event: Select.Changed):
        field = event.select.id or ''
        if field in ('mode', 'baseline') or field.startswith('inheritance-'):
            self.save_field(field, '' if event.value is Select.NULL else event.value)

    def on_checkbox_changed(self, event: Checkbox.Changed):
        self.save_field('scope_confirmed', event.value)

    def change_step(self, step):
        if self.generating:
            return
        try:
            self.session.record_step(step)
        except Exception as error:
            self.set_status(f'Could not save progress: {error}')
            return
        self.step = step
        self.query_one('#sections', ContentSwitcher).current = step
        self.refresh_validation()

    def refresh_topology(self):
        topology = self.session.answers.get('topology', {})
        nodes, flows = topology.get('nodes', []), topology.get('flows', [])
        self.query_one('#nodes-list', Static).update('\n'.join(
            f'{node["id"]}: {node["title"]} ({node["boundary"]})' for node in nodes) or 'No nodes yet.')
        self.query_one('#flows-list', Static).update('\n'.join(
            f'{i + 1}. {flow["from"]} → {flow["to"]}: {flow["data"]}; {flow["protocol"]}; '
            f'auth: {flow["authentication"]}; storage: {flow["storage"]}'
            for i, flow in enumerate(flows)) or 'No flows yet.')
        options = [(Text(f'{node["id"]}: {node["title"]}'), node['id']) for node in nodes]
        for key in ('remove-node-choice', 'flow-from', 'flow-to'):
            self.query_one('#' + key, Select).set_options(options)
        self.query_one('#remove-flow-choice', Select).set_options([
            (Text(f'{i + 1}. {flow["from"]} → {flow["to"]}'), i) for i, flow in enumerate(flows)])

    def form_value(self, key):
        widget = self.query_one('#' + key)
        return '' if widget.value is Select.NULL else widget.value

    def edit_topology(self, action):
        try:
            if action == 'add-node':
                self.session.add_node({key: self.form_value('node-' + key) for key in ('id', 'title', 'boundary')})
            elif action == 'add-flow':
                self.session.add_flow({key: self.form_value('flow-' + key) for key in FLOW_FIELDS})
            elif action == 'remove-node':
                self.session.remove_node(self.form_value('remove-node-choice'))
            else:
                index = self.form_value('remove-flow-choice')
                if index == '':
                    raise ValueError('Choose a flow to remove')
                self.session.remove_flow(index)
            self.refresh_topology()
            self.set_status('Topology saved.')
        except Exception as error:
            self.set_status(f'Topology not saved: {error}')
        self.refresh_validation()

    def on_button_pressed(self, event: Button.Pressed):
        action = event.button.id
        if self.generating:
            return
        if action.startswith('step-'):
            self.change_step(action.removeprefix('step-'))
        elif action in ('back', 'next'):
            offset = -1 if action == 'back' else 1
            index = max(0, min(len(SECTIONS) - 1, SECTIONS.index(self.step) + offset))
            self.change_step(SECTIONS[index])
        elif action in ('add-node', 'add-flow', 'remove-node', 'remove-flow'):
            self.edit_topology(action)
        elif action == 'save-exit':
            self.action_save_exit()
        elif action == 'generate':
            self.generate_draft()

    def action_save(self):
        if self.generating:
            self.set_status('Generation in progress. Please wait before saving or exiting.')
            return False
        try:
            self.session.save()
            self.set_status(f'Saved to {self.session.answers_path}')
            return True
        except Exception as error:
            self.set_status(f'Could not save: {error}')
            return False

    def action_save_exit(self):
        if self.action_save():
            self.exit()

    @work(exclusive=True)
    async def generate_draft(self):
        if self.generating:
            return
        self.refresh_validation()
        if self.session.issues():
            self.set_status('Resolve the listed issues before generating.')
            return
        self.generating = True
        for widget in self.query('Input, Select, Checkbox, Button'):
            widget.disabled = True
        self.set_status('Generating the review draft…')
        result = self.query_one('#generation-result', Static)
        result.update('Generating…')
        try:
            report = await asyncio.to_thread(self.session.generate)
            message = f'Draft generated: {self.session.workspace / "project"}'
            if isinstance(report, dict) and 'total_controls' in report:
                message += f'\nControls: {report["total_controls"]}'
            result.update(message)
            self.set_status('Generation complete. Review the output and supply implementation evidence.')
        except Exception as error:
            result.update(f'Generation failed: {error}')
            self.set_status('Generation failed. Review the error, correct the answers, and retry.')
        finally:
            self.generating = False
            for widget in self.query('Input, Select, Checkbox, Button'):
                widget.disabled = False
            self.refresh_validation()


def launch(repository: Path, workspace: Path):
    """Open or resume an external authoring workspace."""
    WizardApp(WizardSession(repository, workspace)).run()
