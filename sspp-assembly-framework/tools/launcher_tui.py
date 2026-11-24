"""Read-only workspace chooser; the caller dispatches after this app exits."""
import subprocess
from pathlib import Path

from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Footer, Header, Input, Label, Select, Static

from repository_intake import checkout_root
from workspace_paths import claim_workspace, discover_workspaces, suggest_workspace, validate_workspace


PATH_ERRORS = (OSError, ValueError, subprocess.SubprocessError)


class LauncherApp(App):
    """Choose a repository, explicitly select a workspace, and return a workflow."""

    TITLE = 'ATO workspace launcher'
    SUB_TITLE = 'AI-assisted authoring • local workspace selection'
    BINDINGS = [('ctrl+q', 'quit', 'Quit')]
    CSS = """
    #chooser { height: 1fr; padding: 0 2; }
    Label { height: auto; margin-top: 1; }
    Input, Select { width: 100%; }
    Static { height: auto; }
    .hint { color: $text-muted; }
    #error { color: $error; }
    #actions { height: 3; }
    #actions Button { width: 1fr; min-width: 8; }
    #new-workspace, #detect { margin-top: 1; }
    """

    def __init__(self, repository: Path, workspace: Path | None = None,
                 runner: Path | None = None, jar: Path | None = None,
                 pandoc: Path | None = None):
        super().__init__()
        self.repository = repository
        self.workspace = workspace
        self.runner, self.jar, self.pandoc = runner, jar, pandoc
        self.detected_repository = None
        self.suggestion = None

    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll(id='chooser'):
            yield Label('Repository Input', markup=False)
            yield Input(str(self.repository), id='repository')
            yield Button('Detect / refresh', id='detect')
            yield Label('Resume workspace', id='resume-label', markup=False)
            yield Select([], prompt='Choose a saved workspace', id='resume')
            yield Label('Workspace Input', markup=False)
            yield Input(str(self.workspace) if self.workspace is not None else '', id='workspace',
                        placeholder='Select New workspace, resume, or enter an explicit path')
            yield Button('New workspace', id='new-workspace')
            yield Static('', id='suggestion', classes='hint', markup=False)
            yield Static('', id='summary', markup=False)
            yield Static(self.tool_status(), id='tools', classes='hint', markup=False)
            yield Static('', id='error', markup=False)
        with Horizontal(id='actions'):
            yield Button('Text draft', id='text', variant='primary')
            yield Button('Diagrams', id='diagrams')
            yield Button('Quit', id='quit')
        yield Footer()

    def tool_status(self):
        lines = ['Textual: installed']
        for label, path in (('Runner config', self.runner), ('PlantUML JAR', self.jar),
                            ('Pandoc', self.pandoc)):
            state = 'not configured' if path is None else ('file present' if path.is_file() else 'file missing')
            lines.append(f'{label}: {state}')
        return '\n'.join(lines)

    def on_mount(self):
        self.detect()

    def repository_path(self):
        value = self.query_one('#repository', Input).value
        if not value.strip():
            raise ValueError('Enter a repository path.')
        return checkout_root(Path(value).expanduser())

    def workspace_path(self, repository):
        value = self.query_one('#workspace', Input).value
        if not value.strip():
            raise ValueError('Select New workspace, resume a workspace, or enter a workspace path.')
        path = Path(value).expanduser()
        return path if path.is_absolute() else repository / path

    def set_error(self, error=''):
        self.query_one('#error', Static).update(str(error))

    def detect(self):
        """Refresh path-only information; never create directories or session state."""
        self.set_error()
        try:
            repository = self.repository_path()
            discovered = discover_workspaces(repository)
            discovered = sorted(discovered, key=lambda path: (path.stat().st_mtime_ns, str(path)), reverse=True)
            self.detected_repository = repository
            self.suggestion = suggest_workspace(repository)
            resume = self.query_one('#resume', Select)
            resume.set_options([(Text(str(path)), str(path)) for path in discovered])
            resume.display = bool(discovered)
            self.query_one('#resume-label', Label).display = bool(discovered)
            field = self.query_one('#workspace', Input)
            if not field.value and discovered:
                field.value = str(discovered[0])
            selected = self.workspace_path(repository) if field.value.strip() else None
            resume.value = str(selected) if selected in discovered else Select.NULL
            self.query_one('#suggestion', Static).update(f'New workspace suggestion: {self.suggestion}')
            self.update_summary()
        except PATH_ERRORS as error:
            self.detected_repository = None
            self.suggestion = None
            self.query_one('#summary', Static).update('Repository could not be detected.')
            self.set_error(error)

    def update_summary(self):
        self.set_error()
        try:
            repository = self.repository_path()
            if not self.query_one('#workspace', Input).value.strip():
                self.query_one('#summary', Static).update(
                    f'Repository: {repository}\nWorkspace: not selected; click New workspace to use the suggestion.')
                return
            workspace = self.workspace_path(repository)
            exists = workspace.exists()
            label = 'Resume workspace' if exists else 'New workspace (created only on launch)'
            self.query_one('#summary', Static).update('\n'.join((
                f'Repository: {repository}', f'{label}: {workspace}',
                f'Exists: {"yes" if exists else "no"}',
                f'Intake answers: {"present" if (workspace / "intake/answers.json").is_file() else "absent"}',
                f'Diagram session: {"present" if (workspace / "diagramming/session.json").is_file() else "absent"}',
            )))
            if exists:
                if not workspace.is_dir():
                    raise ValueError('Workspace path exists but is not a directory. Choose New workspace or another path.')
                if any(workspace.iterdir()):
                    validate_workspace(repository, workspace)
        except PATH_ERRORS as error:
            self.set_error(error)

    def on_input_changed(self, event: Input.Changed):
        if event.input.id in ('repository', 'workspace') and self.is_mounted:
            self.update_summary()

    def on_select_changed(self, event: Select.Changed):
        if event.select.id == 'resume' and event.value is not Select.NULL and event.value == event.select.value:
            self.query_one('#workspace', Input).value = str(event.value)
            self.update_summary()

    def on_button_pressed(self, event: Button.Pressed):
        action = event.button.id
        if action == 'quit':
            self.exit()
        elif action == 'detect':
            self.detect()
        elif action == 'new-workspace':
            try:
                self.suggestion = suggest_workspace(self.repository_path())
                self.query_one('#workspace', Input).value = str(self.suggestion)
                self.query_one('#resume', Select).value = Select.NULL
                self.update_summary()
            except PATH_ERRORS as error:
                self.set_error(error)
        elif action in ('text', 'diagrams'):
            self.launch(action)

    def launch(self, workflow):
        """Claim only an unoccupied path, then hand control back to the dispatcher."""
        try:
            repository = self.repository_path()
            workspace = self.workspace_path(repository)
            if not workspace.exists() or (workspace.is_dir() and not any(workspace.iterdir())):
                workspace = claim_workspace(repository, workspace)
            else:
                workspace = validate_workspace(repository, workspace)
        except PATH_ERRORS as error:
            self.set_error(error)
            return
        self.exit({'repository': repository, 'workspace': workspace, 'workflow': workflow})
