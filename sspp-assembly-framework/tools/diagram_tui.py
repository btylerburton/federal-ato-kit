"""Optional, explicitly operated Textual dashboard for source-cited diagrams."""
import asyncio
from pathlib import Path

from rich.text import Text
from textual import work
from textual.app import App, ComposeResult
from textual.widgets import Button, Checkbox, Footer, Header, Input, Label, Select, Static, TabbedContent, TabPane
from textual.containers import VerticalScroll
from copyable_tui import CopyableApp, CopyTextScreen


VIEWS = ('context', 'architecture', 'boundary', 'data-flow')


class DiagramApp(CopyableApp):
    """Keep analysis execution and human confirmation explicit and independent."""

    TITLE = 'Diagram dashboard'
    SUB_TITLE = 'AI-assisted proposals • human review required'
    BINDINGS = [('ctrl+r', 'refresh_dashboard', 'Refresh'), ('ctrl+q', 'quit', 'Quit')]
    CSS = """
    #state { height: auto; max-height: 5; padding: 0 1; border-bottom: solid $primary; }
    #status { height: auto; max-height: 4; padding: 0 1; color: $warning; }
    TabbedContent { height: 1fr; }
    TabPane { padding: 0; }
    .panel { padding: 0 1; }
    Label { height: auto; margin-top: 1; }
    Static { height: auto; }
    Input, Select { width: 100%; }
    Button { margin-top: 1; }
    .detail { margin: 1 0; }
    Checkbox { width: 100%; height: auto; }
    """

    def __init__(self, dashboard):
        super().__init__()
        self.dashboard = dashboard
        self.busy = False
        self.state = {}
        self.question_records = []
        self.selected_question = None
        self.selected_view = 'context'

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static('Loading diagram state…', id='state', markup=False)
        with TabbedContent(initial='overview', id='sections'):
            with TabPane('Overview', id='overview'):
                with VerticalScroll(classes='panel'):
                    yield Static('', id='overview-summary', classes='detail', markup=False)
                    yield Button('Refresh proposal / state', id='refresh')
                    yield Checkbox('Enable trusted runner execution (installed tool; may contact provider)',
                                   id='runner-consent')
                    yield Button('Run Analyze', id='analyze', disabled=True)
                    yield Static('Without a configured runner, give the exact request below to your authorized '
                                 'agent, then refresh after it writes proposal.json.', classes='detail', markup=False)
                    yield Static('', id='handoff', markup=False)
                    yield Button('Copy prompt', id='copy-prompt')
            with TabPane('Questions', id='questions'):
                with VerticalScroll(classes='panel'):
                    yield Checkbox('Show known answers for correction', id='show-known')
                    yield Label('Question', markup=False)
                    yield Select([], id='question', prompt='No pending questions')
                    yield Static('', id='question-help', classes='detail', markup=False)
                    yield Label('Your answer', markup=False)
                    yield Input(id='answer-text', placeholder='Enter a human-supplied answer')
                    yield Select([], id='answer-choice', prompt='Choose explicitly')
                    yield Button('Save answer', id='save-answer', disabled=True)
                    yield Label('Reviewer name', markup=False)
                    yield Input(id='reviewer', placeholder='Name of the human reviewer')
                    yield Checkbox('I reviewed the proposal and confirm its scope and relationships',
                                   id='review-consent')
                    yield Button('Confirm review', id='confirm', disabled=True)
            with TabPane('Preview', id='preview'):
                with VerticalScroll(classes='panel'):
                    yield Static('Structured source-cited summary; generated source appears when available. '
                                 'Rendered figures are separate outputs.', classes='detail', markup=False)
                    yield Select([(Text(view.title()), view) for view in VIEWS], value='context',
                                 allow_blank=False, id='view')
                    yield Static('', id='preview-content', classes='detail', markup=False)
            with TabPane('Outputs', id='outputs'):
                with VerticalScroll(classes='panel'):
                    yield Static('', id='output-summary', classes='detail', markup=False)
                    yield Button('Generate diagram sources', id='generate', disabled=True)
                    yield Button('Render figures', id='render', disabled=True)
                    yield Button('Attach to SSPP project', id='attach', disabled=True)
        yield Static('', id='status', markup=False)
        yield Footer()

    def on_mount(self):
        self.query_one('#answer-choice').display = False
        self.action_refresh_dashboard()

    def set_status(self, message):
        self.query_one('#status', Static).update(str(message))

    def update_controls(self):
        for kind in (Button, Input, Select, Checkbox):
            for widget in self.query(kind):
                widget.disabled = self.busy
        if self.busy:
            return
        consent = self.query_one('#runner-consent', Checkbox).value
        self.query_one('#analyze', Button).disabled = not (
            consent and self.state.get('runner_configured') and self.state.get('can_analyze'))
        for action in ('generate', 'render', 'attach'):
            self.query_one('#' + action, Button).disabled = not self.state.get('can_' + action, False)
        self.query_one('#save-answer', Button).disabled = (
            self.selected_question is None or self.state.get('stage') == 'blocked')
        self.query_one('#confirm', Button).disabled = not (
            self.state.get('stage') == 'review' and not self.state.get('pending_count')
            and self.query_one('#review-consent', Checkbox).value
            and self.query_one('#reviewer', Input).value.strip())

    def snapshot(self, view):
        state = self.dashboard.refresh()
        if state['stage'] == 'blocked':
            return state, [], 'Resolve the state error before previewing or reviewing.', self.dashboard.handoff_text()
        return state, self.dashboard.questions(), self.dashboard.preview(view), self.dashboard.handoff_text()

    def apply_snapshot(self, snapshot):
        self.state, self.question_records, preview, handoff = snapshot
        stage = self.state.get('stage', 'blocked')
        self.query_one('#state', Static).update(
            f'State: {stage} | Pending questions: {self.state.get("pending_count", 0)}\n'
            f'Next action: {self.state.get("message", "Refresh to inspect the current state.")}')
        warnings = '\n'.join(str(item) for item in self.state.get('warnings', []))
        self.query_one('#overview-summary', Static).update(
            f'Repository: {self.dashboard.repository}\nWorkspace: {self.dashboard.workspace}\n'
            f'Nodes: {self.state.get("nodes", 0)} | Relationships: {self.state.get("flows", 0)}\n'
            f'Trusted runner configured: {bool(self.state.get("runner_configured"))}\n{warnings}')
        self.query_one('#handoff', Static).update(
            f'Request: {self.dashboard.request_path}\nProposal destination: {self.dashboard.proposal_path}\n\n{handoff}')
        self.query_one('#preview-content', Static).update(str(preview))
        self.query_one('#output-summary', Static).update(
            f'Diagram workspace: {self.dashboard.root}\n'
            f'Human review confirmed: {bool(self.state.get("confirmed"))}\n'
            f'Sources generated: {bool(self.state.get("generated"))}\n'
            f'Figures rendered: {bool(self.state.get("rendered"))}\n'
            f'Attached to SSPP: {bool(self.state.get("attached"))}\n\n'
            'Rendering requires an explicitly configured local PlantUML JAR. '
            'Attachment requires a generated SSPP project in this workspace.\n' + warnings)
        self.populate_questions()

    def populate_questions(self):
        known = self.query_one('#show-known', Checkbox).value
        records = [q for q in self.question_records if known or q.get('pending')]
        selector = self.query_one('#question', Select)
        previous = selector.value
        selector.set_options([(Text(str(q['label'])), q['key']) for q in records])
        keys = [q['key'] for q in records]
        selector.value = previous if previous in keys else keys[0] if keys else Select.NULL
        self.show_question(selector.value)

    def show_question(self, key):
        self.selected_question = next((q for q in self.question_records if q['key'] == key), None)
        question = self.selected_question or {}
        self.query_one('#question-help', Static).update(str(question.get(
            'help', 'No pending questions. Show known answers to make a correction.')))
        choices = question.get('choices', [])
        value = question.get('value')
        choice = self.query_one('#answer-choice', Select)
        choice.set_options([(Text(str(item)), item) for item in choices])
        choice.value = value if value in choices else Select.NULL
        choice.display = bool(choices)
        text = self.query_one('#answer-text', Input)
        text.value = '' if value is None else str(value)
        text.display = not choices
        self.update_controls()

    def start_operation(self, action='refresh', *args):
        if self.busy:
            return
        self.busy = True
        self.query_one('#review-consent', Checkbox).value = False
        self.update_controls()
        self.set_status(f'{action.title()} in progress. Please wait before editing or quitting.')
        self.run_operation(action, args, self.selected_view)

    @work(exclusive=True)
    async def run_operation(self, action, args, view):
        error_message = ''
        try:
            if action != 'refresh':
                await asyncio.to_thread(getattr(self.dashboard, action), *args)
        except Exception as error:
            error_message = f'{action.title()} failed: {error}. Correct the issue and retry.'
        try:
            snapshot = await asyncio.to_thread(self.snapshot, view)
            self.apply_snapshot(snapshot)
        except Exception as error:
            error_message += f' Refresh failed: {error}. Check the workspace and refresh.'
            self.state = {'stage': 'blocked'}
            self.query_one('#state', Static).update('State: blocked\nNext action: Check the error below, then refresh.')
        finally:
            self.busy = False
            self.update_controls()
            if not error_message and self.state.get('stage') == 'blocked':
                error_message = 'Proposal needs correction: ' + self.state.get('message', '')
            self.set_status(error_message or f'{action.title()} complete. {self.state.get("message", "")}')

    def action_refresh_dashboard(self):
        self.start_operation()

    def action_quit(self):
        if self.busy:
            self.set_status('Operation in progress. Wait for completion before quitting.')
            return
        self.exit()

    def on_button_pressed(self, event: Button.Pressed):
        if self.busy or event.button.disabled:
            return
        action = event.button.id
        if action == 'copy-prompt':
            self.push_screen(CopyTextScreen(self.dashboard.handoff_text()))
        elif action == 'save-answer' and self.selected_question:
            question = self.selected_question
            value = (self.query_one('#answer-choice', Select).value if question.get('choices')
                     else self.query_one('#answer-text', Input).value)
            if value is Select.NULL or not str(value).strip():
                self.set_status('Enter or select an answer before saving.')
                return
            self.start_operation('answer', question['key'], value)
        elif action == 'confirm':
            reviewer = self.query_one('#reviewer', Input).value.strip()
            if self.query_one('#review-consent', Checkbox).value and reviewer:
                self.start_operation('confirm', reviewer)
        elif action in ('refresh', 'analyze', 'generate', 'render', 'attach'):
            self.start_operation(action)

    def on_checkbox_changed(self, event: Checkbox.Changed):
        if self.busy:
            return
        if event.checkbox.id == 'show-known':
            self.populate_questions()
        self.update_controls()

    def on_input_changed(self, event: Input.Changed):
        if self.busy:
            return
        if event.input.id in ('answer-text', 'reviewer'):
            self.query_one('#review-consent', Checkbox).value = False
        self.update_controls()

    def on_select_changed(self, event: Select.Changed):
        if self.busy:
            return
        if event.select.id == 'question':
            self.show_question(event.value)
            self.query_one('#review-consent', Checkbox).value = False
        elif event.select.id == 'answer-choice':
            self.query_one('#review-consent', Checkbox).value = False
        elif event.select.id == 'view' and event.value in VIEWS and event.value != self.selected_view:
            self.selected_view = event.value
            self.start_operation()
        self.update_controls()


def launch(repository: Path, workspace: Path, runner=None, jar=None, pandoc=None):
    """Launch only when explicitly requested; importing never starts an agent."""
    from diagram_dashboard import DiagramDashboard
    DiagramApp(DiagramDashboard(repository, workspace, runner=runner, jar=jar, pandoc=pandoc)).run()
