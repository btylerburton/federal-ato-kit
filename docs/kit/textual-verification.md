---
title: "Textual wizard verification"
description: "Observed session recovery, headless interaction and dependency checks"
status: draft
tier: 2
last_updated: "2026-11-24"
---

# Verification record

## All-field help and wrapped text — November 24

OpenCode AI agent, scoped continuation requested by the user. Verification observed at
2026-11-24T23:28:15Z using Python 3.14.4 and the existing Textual 8.2.8 hash lock.

Every text-wizard field has mouse/keyboard help, including environment and hosting.
Free-form editors wrap and accept line breaks; data categories split on commas/newlines.
Saved multiline names remain intact while document-title whitespace is flattened.

- Initial local `bash setup-tui.sh`: failed because the existing environment had broken
  interpreter links. Prepared `/tmp/opencode/wizard-field-help-env` with `uv venv` and
  `uv pip sync --require-hashes --only-binary :all:` using the unchanged TUI lockfile.
- Expanded regression caught a document-title single-line constraint during real generation;
  fixed both scaffold calls to use the flattened title. The saved answer remains multiline.
- `TMPDIR=/tmp/opencode PYTHONDONTWRITEBYTECODE=1 /tmp/opencode/wizard-field-help-env/bin/python check.py`:
  PASS, 12 toolkit tests; 133 framework tests run, 129 passed and four optional renderer/Trestle
  tests skipped. All eight wizard UI tests ran. Output: `/tmp/opencode/wizard-field-help-check.log`.
- UI coverage includes all 14 help disclosures at 80×24 without answer changes, vertical
  wrapping without horizontal scrolling, Enter/Tab, autosave/reopen, real generation with
  multiline identity/environment/boundary, category parsing and generation-time edit blocking.
- `git diff --check`, Python syntax parsing, and wizard-guide local-link checks: PASS.
- Third-party security scans and live renderer/Trestle checks were not run for this UI change.
  No dependencies were changed. Human Ghostty interaction was not exercised in this Linux session.

## Question help update — November 24

Added adjacent clickable/keyboard-operable help for egress proxy, GSA common-control scope,
organization dependency-management enrollment and SHA pinning. The inline disclosure includes
meaning, evidence, responsible contacts and unknown/no guidance; hover also indicates how to
open it. No dependency change.

All seven Textual interaction tests passed in 15.130 seconds, including opening each disclosure
by mouse, closing via Enter at 80×24, and byte-comparing saved answers before/after. Existing
autosave, topology and real-generation tests also passed. The first test revealed Textual's
button active-animation interval ignored immediate reactivation; help disclosures now disable
that animation interval, and the same interaction test passes without sleeps. Whitespace check
passed. This tests the actual UI event behavior, not just the presence of help strings.

OpenCode AI coordinator, delegated UI implementation and independent read-only review.
User approved the optional Textual UI, local dependency downloads, legacy-answer backup and
small durable work increments. Application source remained read-only.

## Dependency preparation

Textual 8.2.8 and eight dependencies were resolved with `uv pip compile --generate-hashes`.
`uv pip sync --require-hashes --only-binary :all:` installed them into ignored `.venv-tui`.
PyPI exact-version metadata for all nine reported no vulnerability advisories at retrieval;
license metadata/files were inspected (see textual-decision.md). The filesystem did not support
hardlinks across the package-cache boundary, so uv explicitly fell back to copying. Installation
succeeded. No system-wide package or web service was added.

`setup-tui.sh` is the portable pip/venv equivalent for users; shell syntax validation passed.
The actual session installation used uv, not this shell wrapper. The existing core check remains
usable without Textual. Optional TUI tests report skips when it is absent.

## Executed tests

```sh
TMPDIR=/tmp/opencode PYTHONDONTWRITEBYTECODE=1 .venv-tui/bin/python -m unittest discover \
  -s sspp-assembly-framework/tests -p 'test_wizard*.py' -v
```

Final focused run: **28 tests passed** in 18.105 seconds. This includes:

- The user's missing-date/uppercase-choice/default-boundary legacy pattern.
- Byte-preserved legacy backups, saved date retained across subsequent days, and resumed step.
- No automatic approval, impact baseline, provider applicability or topology inference.
- Invalid calendar dates and incomplete boundary/topology block generation while remaining editable.
- Refusal of unrelated sessions, symlinked intake and external concurrent edits.
- Atomic write failure and partial second-write failure, with reopen required and saved edits preserved.
- Missing inheritance questions remain unanswered until asked; explicit unknown/no persists.
- Textual Pilot interaction at 80×24 and 100×40: autosave, navigation, save/exit, reopen,
  field errors, provider choices, topology add/remove forms and generation failure recovery.
- Actual LATO generation from the Textual Review screen; 58 selected shells and manifest produced.
- No Rich markup interpretation of supplied field text in the review summary.

An earlier root `check.py` run passed 12 toolkit tests and 75 framework tests with two explicitly
skipped renderer/Trestle cases; Textual cases ran. After review fixes, focused tests above were
rerun. No claim of a new full diagram/PDF/production-provider verification is made.

## Real saved-session recovery

The existing consumer intake was resumed through `WizardSession` and mounted in Textual's
headless test mode. Its original answers were backed up before normalization. The substantive
owner/system/environment/data/boundary/topology answers matched the original. Uppercase LATO
normalized and the empty date defaulted. Session reopened at Scope with boundary and topology
errors; generation was not invoked. Screenshots of synthetic and resumed UI were saved only
under ignored `tmp/`, not published with consumer answers.

This is actual state recovery and headless event-loop execution, not a claim that a human
reviewed the UI in every terminal. User's terminal is the final interactive acceptance check.

## Review findings and corrections

The first UI test referenced a nonpublic Textual attribute; it now checks actual rendered
literal text. A legacy CLI error-message capitalization mismatch was corrected without
weakening the approval gate. Independent review then reproduced two substantive blockers:
normalization skipped unanswered provider questions, and a partial session save could discard
an edit on a later save. Missing inheritance now stays distinct from explicit unknown. A failed
partial save blocks subsequent writes until reopening, preserving the persisted edit. Both have
dedicated regressions.

Known scope remains unchanged: the initial CLI inventory is path-only, diagram projections
still require the separately tracked semantics work, and the TUI Generate action creates an
editable review project rather than automatically rendering a final signed authorization.

## Final check

Independent re-review cleared both blockers and independently reran 28 focused tests.
The subsequent root check passed **12 toolkit tests plus 78 framework tests**, with exactly
two optional renderer/Trestle tests skipped; all six Textual tests ran. Framework run time:
23.877 seconds. `git diff --check` passed.

Bandit on the new session/UI modules reported three low findings (B404/B607/B603), all for the
fixed Git `cat-file -e <validated-hex-revision>^{commit}` legacy association check. It uses an
argument list, no shell and a 15-second timeout; Git resolves from the operator's PATH.
No findings were suppressed or reported as a zero-finding scan. The source application is
not executed by this check. A generic Git ancestry match cannot distinguish two clones of the
same history; after legacy adoption, the explicit repository path is persisted in session state.
