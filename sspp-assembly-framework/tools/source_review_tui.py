"""Optional pre-draft source review: external handoff, explicit runner, or no AI."""
import asyncio
import re

from textual import work
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import Button, Checkbox, Footer, Header, Input, Static, TabbedContent, TabPane

from copyable_tui import CopyableApp, CopyTextScreen
from source_review import SourceReview


class SourceReviewApp(CopyableApp):
    TITLE = 'Optional source review — before drafting'
    BINDINGS = [('ctrl+q', 'quit', 'Back')]
    CSS = """
    #review-setup { height: 6; padding: 0 2; }
    TabbedContent { height: 1fr; }
    .review-sheet { padding: 0 2; }
    .finding-card { height: auto; border: solid $primary; padding: 0 1; margin-bottom: 1; }
    #intake-cards, #source-cards { height: auto; }
    Static { height: auto; }
    Button, Input, Checkbox { margin-top: 1; }
    #source-actions { height: 3; }
    #source-actions Button { width: 1fr; min-width: 8; margin: 0; }
    #source-status { height: auto; max-height: 5; }
    """

    def __init__(self, review):
        super().__init__()
        self.review = review
        self.data = None
        self.busy = False

    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll(id='review-setup'):
            yield Static('Optional: use source findings to inform system descriptions and candidate control '
                         'narratives. Continue to text questions at any time; no AI is required. '
                         'Include means use as a draft, not verified implementation.', markup=False)
            yield Static(f'Request: {self.review.request_path}\nFindings: {self.review.path}', markup=False)
            yield Button('View / copy LLM request', id='source-prompt')
            yield Button('Refresh findings', id='source-refresh')
            yield Checkbox('Enable my configured trusted runner (may contact a provider)', id='source-runner-consent')
            yield Button('Run source analysis', id='source-analyze', disabled=True)
            yield Static('Use an approved external agent with the request, or author findings manually using '
                         'the same schema and method manual. With no LLM, continue to text questions.', markup=False)
            yield Button('Send proposed topology to diagram review', id='source-diagrams')
        with TabbedContent(initial='intake-tab'):
            with TabPane('Intake suggestions', id='intake-tab'):
                with VerticalScroll(classes='review-sheet'):
                    yield Static('Tick the answers you want to replace, then preview them together. '
                                 'Applying answers is separate from including source findings in the draft.', markup=False)
                    yield Static('', id='intake-count', markup=False)
                    yield Vertical(id='intake-cards')
                    yield Button('Preview selected intake replacements', id='source-apply')
                    yield Button('Next: source findings', id='source-next')
            with TabPane('Source findings', id='findings-tab'):
                with VerticalScroll(classes='review-sheet'):
                    yield Static('Tick findings to include in the draft, then save your choices. '
                                 'Untouched unchecked findings stay deferred; unchecking a previously included '
                                 'finding excludes it. Inclusion does not verify implementation or replace intake answers.',
                                 markup=False)
                    yield Input(id='source-reviewer', placeholder='Human reviewer name (required to save choices)')
                    yield Static('', id='findings-count', markup=False)
                    yield Button('Include all', id='source-include-all')
                    yield Vertical(id='source-cards')
                    yield Button('Save inclusion choices', id='source-decide')
        yield Static('', id='source-status', markup=False)
        with Horizontal(id='source-actions'):
            yield Button('Continue to text questions', id='source-continue', variant='primary')
            yield Button('Back', id='source-back')
        yield Footer()

    def on_mount(self):
        self.operation('refresh')

    def findings(self):
        return (self.data or {}).get('findings', [])

    @staticmethod
    def finding_text(finding):
        evidence = '\n'.join(f'{e["path"]}:{e["lines"][0]}-{e["lines"][1]}' for e in finding['evidence'])
        return (f'{finding["id"]} — {finding["section"]} — {finding["status"]}\n'
                f'Control/part: {finding.get("control_id", "")} {finding.get("part_id", "")}\n\n'
                f'{finding["text"]}\n\nEvidence (existence checked; meaning needs review):\n{evidence}')

    async def render_cards(self):
        intake = self.query_one('#intake-cards', Vertical)
        sources = self.query_one('#source-cards', Vertical)
        await intake.remove_children()
        await sources.remove_children()
        intake_cards, source_cards = [], []
        for index, finding in enumerate(self.findings()):
            text = self.finding_text(finding)
            decision = self.review.state['decisions'].get(finding['id'], {}).get('disposition', 'pending')
            source_cards.append(Vertical(
                Checkbox('Include in draft', value=decision == 'include', id=f'include-{index}'),
                Static(f'Saved decision: {decision}', markup=False), Static(text, markup=False),
                classes='finding-card'))
            if finding.get('suggested_field'):
                intake_cards.append(Vertical(
                    Checkbox(f'Replace {finding["suggested_field"]}', id=f'intake-{index}'),
                    Static(text, markup=False), classes='finding-card'))
        if intake_cards:
            await intake.mount(*intake_cards)
        if source_cards:
            await sources.mount(*source_cards)
        self.query_one('#intake-count', Static).update(
            f'{len(intake_cards)} intake suggestions. Select replacements to preview.' if intake_cards else
            'No intake suggestions. Continue to source findings or text questions.')
        included = sum(d['disposition'] == 'include' for d in self.review.state['decisions'].values())
        self.query_one('#findings-count', Static).update(f'{len(source_cards)} source findings; {included} included.')

    def update_controls(self):
        for widget in self.query('Button, Input, Checkbox'):
            widget.disabled = self.busy
        if not self.busy:
            self.query_one('#source-analyze', Button).disabled = not (
                self.review.runner and self.query_one('#source-runner-consent', Checkbox).value)

    @work(exclusive=True)
    async def operation(self, action, *args):
        if self.busy:
            return
        self.busy = True
        self.update_controls()
        status = self.query_one('#source-status', Static)
        status.update(f'{action.title()} in progress…')
        try:
            if action == 'save_choices':
                for key, disposition in args[0]:
                    await asyncio.to_thread(self.review.decide, key, disposition, args[1])
            elif action != 'refresh':
                await asyncio.to_thread(getattr(self.review, action), *args)
            self.data = await asyncio.to_thread(self.review.refresh)
            await self.render_cards()
            included = sum(d['disposition'] == 'include' for d in self.review.state['decisions'].values())
            status.update(f'{len(self.findings())} findings; {included} included in draft. '
                          'Inclusion choices saved.' if action == 'save_choices' else
                          f'{len(self.findings())} findings loaded. Review intake suggestions and source findings separately.')
        except Exception as error:
            self.data = None
            await self.render_cards()
            status.update(f'Source review needs attention: {error}')
        finally:
            self.busy = False
            self.update_controls()

    def on_checkbox_changed(self, event):
        if event.checkbox.id == 'source-runner-consent':
            self.update_controls()

    def on_button_pressed(self, event):
        if self.busy:
            return
        action = event.button.id
        if action == 'source-prompt':
            self.push_screen(CopyTextScreen(self.review.request_path.read_text()))
        elif action == 'source-refresh':
            self.operation('refresh')
        elif action == 'source-analyze' and self.query_one('#source-runner-consent', Checkbox).value:
            self.operation('analyze')
        elif action == 'source-decide':
            self.save_choices()
        elif action == 'source-include-all':
            for checkbox in self.query('#source-cards Checkbox'):
                checkbox.value = True
            self.query_one('#source-status', Static).update(
                'All source findings selected. Save inclusion choices to record them.')
        elif action == 'source-diagrams':
            self.operation('send_diagrams')
        elif action == 'source-apply':
            self.preview_suggestion()
        elif action == 'source-next':
            self.query_one(TabbedContent).active = 'findings-tab'
            self.query_one('#source-reviewer', Input).focus()
        elif action == 'source-continue':
            self.exit(True)
        elif action == 'source-back':
            self.exit(False)

    def save_choices(self):
        changes = []
        for index, finding in enumerate(self.findings()):
            previous = self.review.state['decisions'].get(finding['id'], {}).get('disposition', 'pending')
            checked = self.query_one(f'#include-{index}', Checkbox).value
            if checked != (previous == 'include'):
                changes.append((finding['id'], 'include' if checked else 'exclude'))
        if not changes:
            self.query_one('#source-status', Static).update('No inclusion changes to save.')
            return
        reviewer = self.query_one('#source-reviewer', Input).value
        if not reviewer.strip():
            self.query_one('#source-status', Static).update('Enter a human reviewer name before saving choices.')
            return
        self.operation('save_choices', changes, reviewer)

    def preview_suggestion(self):
        from wizard_session import WizardSession
        try:
            values = {}
            for index, finding in enumerate(self.findings()):
                key = finding.get('suggested_field')
                if key and self.query_one(f'#intake-{index}', Checkbox).value:
                    if key in values:
                        raise ValueError(f'Select only one replacement for {key}.')
                    value = finding['text']
                    values[key] = [v.strip() for v in re.split(r'[,\n]', value) if v.strip()] if key == 'data_categories' else value
            if not values:
                raise ValueError('Select at least one intake suggestion to preview.')
            session = WizardSession(self.review.repository, self.review.workspace)
            decision_hash = self.review.seen
            self.push_screen(SuggestionScreen(session.answers, values),
                             lambda confirmed: self.apply_suggestion(session, values, decision_hash) if confirmed else None)
        except (ValueError, OSError) as error:
            self.query_one('#source-status', Static).update(str(error))

    def apply_suggestion(self, session, values, decision_hash):
        try:
            # Revalidate the reviewed finding immediately before writing an answer.
            self.review.refresh()
            if self.review.seen != decision_hash:
                raise ValueError('Review decisions changed; preview the suggestion again')
            session.answers = {**session.answers, **values}
            session.save()
            for checkbox in self.query('#intake-cards Checkbox'):
                checkbox.value = False
            message = f'{len(values)} intake replacements applied. Review remaining suggestions or open Source findings.'
            self.query_one('#intake-count', Static).update(message)
            self.query_one('#source-status', Static).update(message)
        except (ValueError, OSError) as error:
            self.query_one('#source-status', Static).update(f'Could not apply: {error}')

    def action_quit(self):
        if not self.busy:
            self.exit(False)


class SuggestionScreen(CopyTextScreen):
    def __init__(self, previous, proposed):
        super().__init__('\n\n'.join(
            f'Field: {key}\n\nCurrent answer:\n{previous.get(key)}\n\nProposed answer:\n{value}'
            for key, value in proposed.items()))

    def compose(self):
        yield from super().compose()
        yield Button('Replace selected answers', id='suggestion-confirm', variant='primary')

    def on_button_pressed(self, event):
        if event.button.id == 'suggestion-confirm':
            event.stop()
            event.prevent_default()
            self.dismiss(True)


def launch(repository, workspace, runner=None):
    return SourceReviewApp(SourceReview(repository, workspace, runner)).run()
