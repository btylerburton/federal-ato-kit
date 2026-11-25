"""Shared local selection/copy actions; clipboard delivery depends on terminal OSC 52."""
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal
from textual.screen import ModalScreen
from textual.widgets import Button, Input, Select, Static, TextArea


class CopyTextScreen(ModalScreen):
    DEFAULT_CSS = """
    CopyTextScreen { padding: 1 2; background: $surface; }
    CopyTextScreen TextArea { height: 1fr; width: 100%; }
    CopyTextScreen Horizontal { height: 3; }
    CopyTextScreen Static { height: auto; }
    """
    BINDINGS = [('escape', 'dismiss', 'Close')]

    def __init__(self, text):
        super().__init__()
        self.text = text

    def compose(self) -> ComposeResult:
        yield Static('Select text and Ctrl+C, or Copy all. Clipboard requires terminal OSC 52 support.', markup=False)
        yield TextArea(self.text, read_only=True, soft_wrap=True, id='copy-text')
        with Horizontal():
            yield Button('Copy all', id='copy-all')
            yield Button('Close', id='copy-close')

    def on_button_pressed(self, event):
        event.stop()
        if event.button.id == 'copy-all':
            self.app.copy_to_clipboard(self.text)
            self.app.notify('Copy requested. If clipboard is unavailable, use the saved workspace files.')
        elif event.button.id == 'copy-close':
            self.dismiss()


def widget_text(widget):
    if isinstance(widget, Button):
        return ''
    if isinstance(widget, Input):
        return widget.value
    if isinstance(widget, TextArea):
        return widget.text
    if isinstance(widget, Select):
        return '' if widget.value is Select.NULL else str(widget.value)
    if isinstance(widget, Static):
        return str(widget.render())
    return ''


class CopyableApp(App):
    """F4 exposes all visible text, including labels, errors, selections and read-only prompts."""
    BINDINGS = [Binding('f4', 'copy_view', 'Copy text', priority=True),
                Binding('ctrl+shift+c', 'copy_selection', 'Copy selection', show=False, priority=True)]

    def action_copy_selection(self):
        selected = self.screen.get_selected_text()
        if not selected and isinstance(self.focused, (Input, TextArea)):
            selected = self.focused.selected_text
        if selected:
            self.copy_to_clipboard(selected)
        else:
            self.notify('Select text first, or use F4 to copy a field or the visible screen.')

    def action_copy_view(self):
        if isinstance(self.screen, CopyTextScreen):
            return
        text = widget_text(self.focused)
        if not text:
            text = '\n\n'.join(widget_text(w) for w in self.screen.query('Static, Input, TextArea, Select')
                               if w.is_on_screen and widget_text(w))
        self.push_screen(CopyTextScreen(text))
