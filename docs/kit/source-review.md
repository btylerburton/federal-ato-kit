---
title: "Optional source review before SSPP drafting"
description: "Manual or approved-agent findings shared by text drafting and diagrams"
status: draft
tier: 2
last_updated: "2026-11-25"
---

# Start with source review, or continue manually

Run `./ato-wizard /path/to/repository` and select **Text draft**. Before system questions,
the launcher offers optional source review. **Continue to text questions** skips analysis;
no model, network, runner or findings file is required. **Source review / LLM assist** on
the launcher returns to findings later. Direct `wizard.py tui` opens text questions directly.

## Approved agent or manual handoff

1. Choose **View / copy LLM request**, then **Copy all**. The exact request is saved as
   `<workspace>/source-review/agent-request.md` for file-based/offline handoff.
2. Give it to an approved tool with access to permitted source, or author findings manually
   using the same schema and `method: "manual"`. No provider is chosen automatically.
3. Write `<workspace>/source-review/findings.json`, then **Refresh findings**.
4. On **Intake suggestions**, tick the replacements you want on the scrollable sheet. Choose
   **Preview selected intake replacements** to compare current and proposed answers together.
   Only **Replace selected answers** applies them; closing the preview leaves answers unchanged.
   Select at most one suggestion per intake field. Applying answers does not include source findings.
5. Open **Source findings** for the scrollable cards with descriptions and citations. Tick
   **Include in draft**, enter a human reviewer name, and **Save inclusion choices**. Untouched
   unchecked findings remain deferred; unchecking a previously included finding excludes it.
   **Include all** checks every source finding; you can uncheck individual cards before saving.
   Saved choices are restored on refresh/reopen. Inclusion does not replace intake answers.
6. Continue to text questions, confirm required scope choices, and generate.

An explicit `--runner /path/outside/application/runner.json` can run analysis after consent
and **Run source analysis**. The existing argv contract applies: `{request}` is the saved
request and `{proposal}` is the findings output path. The wrapper owns credentials, model
setup and policy. It is a trusted subprocess, not filesystem/network isolation. Failed output
is quarantined in `source-review/runs/`. See [agent/offline limits](agent-offline-assessment.md).

## Findings contract

The saved request contains a JSON example. Required top-level fields:

- `schema_version: 1`, exact `repository_revision`, `method: "manual" | "llm-assisted"`, `author`.
- `findings`: up to 300 records, each with unique lowercase `id`, `section`, `status`, `text`,
  and `evidence: [{"path": "README.md", "lines": [1, 4]}]`.
- Sections: `system`, `data`, `deployment`, `boundary`, `control`.
- Status: `source-supported` (citations required) or `hypothesis` (empty evidence allowed).
- Control records include an exact lowercase catalog `control_id` (for example `sc-8`)
  and optionally its exact `part_id`.
- Optional `suggested_field`: `system_name`, `environment`, `data_categories`, `boundary_summary`.
  Text supplies the suggestion; commas/newlines separate data categories. Approval, owners,
  baseline and inheritance cannot be inferred through suggestions.
- Optional `diagram_proposal`: the existing [diagram proposal contract](diagram-review.md).
  **Send proposed topology to diagram review** validates and writes workspace `proposal.json`
  only if absent. Diagram confirmation remains separate. Invalid optional topology does not
  prevent text findings from being reviewed.

IDs allow lowercase letters, digits, underscores and hyphens, start with a letter, and have
at most 60 characters. Imported findings are immutable: restore the original or create a new
workspace for revised analysis. Dispositions can change with history. Exact committed citation
existence is checked; semantic support and production applicability require human review.
Generated workspaces are excluded as source evidence.

## Findings in the SSPP

Only **Include** findings enter the draft. Generation registers `source-review/findings.md`
and `source-review/provenance.json`, adds system context, and seeds candidate narratives in
matching selected control responses. Part-specific candidates retain their target part ID.
Controls outside the baseline remain in the findings report for tailoring review.

Statuses remain `UNFILLED` / `NOT_ASSESSED`. Narratives retain method, author, commit, citations
and inclusion attribution. Authored responses/chapters are preserved and reported in
`wizard-report.json`; the report retains candidates that could not be inserted. Modified
findings or revision block reuse. Exclusion removes candidates from unchanged managed output
on regeneration; human-edited output requires manual reconciliation.

## Copying throughout the TUI

- Select displayed text and use **Ctrl+Shift+C**.
- Focus a field, editor or choice and press **F4** to view/copy its complete value.
- With a button focused, **F4** opens a selectable snapshot of visible text, including help
  and errors. **Copy all** sends the exact text to the terminal clipboard.
- Diagram Overview includes **Copy prompt** for the complete saved request.

Clipboard delivery uses terminal OSC 52 and may be disabled by terminal policy. The UI cannot
confirm system clipboard delivery. Prompts remain saved for copying through an editor; no
clipboard helper is downloaded or executed.

## Checklist UI verification — 2026-11-25

OpenCode AI agent (GPT 6 Astra), user-approved rapid-prototype scope:

```sh
TMPDIR=/tmp/opencode PYTHONDONTWRITEBYTECODE=1 \
  /tmp/opencode/wizard-field-help-env/bin/python -m unittest discover \
  -s sspp-assembly-framework/tests -p test_source_review_tui.py -v
```

PASS: seven headless UI cases in 17.185 seconds. Covers separate checklist/card lists,
combined replacement and cancellation, data-category parsing, independent draft inclusion,
unchecked/deferred and removal behavior, restored saved checkboxes, empty/conflicting choices,
missing reviewer, concurrent intake/review changes, malformed findings, and manual continuation.
The integration case generates a draft from saved human decisions. Tests exposed and corrected
tab focus reverting to the intake sheet and insufficient review space at 80×24. Repeated-click
tests wait for Textual's button active effect. Existing tests were retained.

The repository `.venv-tui/bin/python` launcher was unavailable; the existing documented
Textual environment above was used. Full-suite, live renderer, SAST and SCA runs were not
performed for this focused UI iteration. No dependency or application-source changes were needed.
