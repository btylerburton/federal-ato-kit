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


SECTIONS = ('system', 'scope', 'inheritance', 'review')
SYSTEM_FIELDS = ('system_name', 'system_owner', 'environment', 'date')
INHERITANCE_HELP = {
    'egress_proxy': (
        'Egress proxy\n\n'
        'A proxy controls outbound connections from an application. Choose yes only if '
        'cg-egress-proxy is deployed for this system and the required direct-egress restrictions apply.\n\n'
        'Look for: deployment/binding configuration, production-space application security groups '
        '(ASGs), allowed destinations, and a test that direct outbound access is restricted. '
        'Hosting on cloud.gov or having proxy code in a repository is not enough.\n\n'
        'Ask your hosting/platform administrator. Choose unknown if you cannot confirm the '
        'deployment or restrictions; no if the system does not use this proxy.'),
    'gsa_common_controls': (
        'GSA common-control scope\n\n'
        'A common-control provider performs defined responsibilities for covered systems. '
        'Choose yes when the system owner or ISSO confirms that this system is covered by '
        'the applicable GSA common-control catalog.\n\n'
        'Look for: the current catalog, applicability language, specific control/part mappings, '
        'remaining customer responsibilities, and required agreements or configurations. '
        'A GSA repository or cloud.gov hosting alone does not establish coverage.\n\n'
        'Ask your ISSO/system owner which providers and responsibility matrices apply. '
        'Choose unknown while scope is unconfirmed; no when confirmed outside that scope. '
        'Yes declares applicability, not that every system control is implemented.'),
    'org_dependency_management': (
        'Organization dependency-management enrollment\n\n'
        'This asks about enrollment in the specific shared service described by the reference '
        'component, not simply whether the repository uses dependency tools.\n\n'
        'Look for: a merged Renovate onboarding PR, the prescribed organization preset, '
        'confirmation that the organization app includes this repository, workflow scanning, '
        'and vulnerability-remediation tracking. A renovate.json, Dependabot alert, lockfile '
        'or single pinned action does not by itself prove enrollment.\n\n'
        'Ask the GitHub organization/platform administrator. Choose unknown until enrollment '
        'is confirmed; no if the repository is not enrolled. Individual practices can still '
        'support system-specific controls.'),
    'sha_pinning': (
        'SHA pinning\n\n'
        'A full commit SHA identifies immutable GitHub Action code; a version tag can move. '
        'Choose yes only after checking applicable external action and reusable-workflow '
        'references and the review process for updates.\n\n'
        'Moving reference: uses: actions/checkout@v4\n'
        'Pinned syntax: uses: actions/checkout@<VERIFIED_40_CHARACTER_COMMIT_SHA> # reviewed release\n'
        'The placeholder above is not a usable commit. Verify the real SHA against the upstream release.\n\n'
        'Look for: workflow files, reviewed update PRs, upstream release/commit verification '
        'and enforcement or scan results. A lockfile is not action SHA pinning. Choose unknown '
        'if not checked; no if applicable references still use moving tags. If there are no '
        'applicable actions, keep applicability unresolved rather than claiming evidence. '
        'This is a practice, not automatic GSA common-control inheritance.'),
}


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
    #status { height: auto; max-height: 4; padding: 0 1; }
    #navigation { height: 3; }
    #navigation Button { width: 1fr; min-width: 8; }
    #review-summary { height: auto; }
    .question-row { height: auto; margin-top: 1; }
    .question-row Label { width: 1fr; margin-top: 0; }
    .question-help { width: 8; min-width: 8; margin-left: 1; }
    .help-detail { height: auto; padding: 1; margin-bottom: 1; border-left: thick $primary; }
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
                        with Horizontal(classes='question-row'):
                            yield Label(question['question'], markup=False)
                            if key in INHERITANCE_HELP:
                                button = Button('? Help', id='help-' + key, classes='question-help')
                                # Disclosure toggles should accept an immediate second activation.
                                button.active_effect_duration = 0
                                button.tooltip = 'Explain this question and what evidence to check. Click or press Enter.'
                                yield button
                        if key in INHERITANCE_HELP:
                            detail = Static(INHERITANCE_HELP[key], id='help-detail-' + key,
                                            classes='help-detail', markup=False)
                            detail.display = False
                            yield detail
                        yield from self.choice('inheritance-' + key, question['choices'],
                                               self.session.answers.get('inheritance', {}).get(key, 'unknown'))
                with VerticalScroll(id='review', classes='panel'):
                    yield Static('Review before generating a draft', markup=False)
                    yield Static('', id='review-summary', markup=False)
                    yield Static('Generated text remains a draft requiring owner review and evidence. '
                                 'Diagrams are a separate step to complete later.',
                                 classes='hint', markup=False)
                    yield Button('Generate draft', id='generate', variant='primary')
                    yield Static('', id='generation-result', markup=False)
        yield Static('', id='status', markup=False)
        with Horizontal(id='navigation'):
            yield Button('Back', id='back')
            yield Button('Next', id='next', variant='primary')
            yield Button('Save & exit', id='save-exit')
        yield Footer()

    def on_mount(self):
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

    def on_button_pressed(self, event: Button.Pressed):
        action = event.button.id
        if self.generating:
            return
        if action.startswith('help-'):
            detail = self.query_one('#help-detail-' + action.removeprefix('help-'), Static)
            detail.display = not detail.display
            event.button.label = 'Close' if detail.display else '? Help'
        elif action.startswith('step-'):
            self.change_step(action.removeprefix('step-'))
        elif action in ('back', 'next'):
            offset = -1 if action == 'back' else 1
            index = max(0, min(len(SECTIONS) - 1, SECTIONS.index(self.step) + offset))
            self.change_step(SECTIONS[index])
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
