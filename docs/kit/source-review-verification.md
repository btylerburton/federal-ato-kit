---
title: "Shared source review verification"
description: "Observed proposal compatibility, copying, optional agent and SSPP integration checks"
status: draft
tier: 2
last_updated: "2026-11-24"
---

# Verification transcript

OpenCode AI agent implemented the user-approved scope in small saved increments on November 24,
2026. Existing uncommitted launcher/bootstrap/help work was retained. No commit or push performed.
No dependency versions changed. Tests used the existing hash-locked Textual 8.2.8 environment at
`/tmp/opencode/wizard-field-help-env` (Python 3.14.4).

## Executed checks

```sh
TMPDIR=/tmp/opencode PYTHONDONTWRITEBYTECODE=1 \
  /tmp/opencode/wizard-field-help-env/bin/python check.py \
  > /tmp/opencode/shared-source-final-check.log 2>&1
```

PASS: 12 toolkit tests; 151 framework cases, 147 passed, four skipped (68.003 seconds).
Checks include Python syntax, documentation frontmatter, entrypoint wiring and whitespace.
Live PlantUML/Pandoc/Trestle integrations were skipped: no configured local tools/JAR.
Diagram-source structural validation ran; rendered-image verification was not performed.
Third-party SAST/SCA was not run (no installed scanner); dependency files are unchanged.

Additional focused run after adding the full-screen copy assertion:

```sh
TMPDIR=/tmp/opencode PYTHONDONTWRITEBYTECODE=1 \
  /tmp/opencode/wizard-field-help-env/bin/python -m unittest discover \
  -s sspp-assembly-framework/tests -p test_source_review_tui.py -v
```

PASS: five UI cases in 5.739 seconds. A test initially expected screen copy while Refresh had
moved focus into the findings field. It now explicitly focuses a button to exercise screen copy;
field copy is tested separately. Tests cover exact prompt bytes, selection copying, manual skip,
human disposition, explicit suggestion replacement and concurrent-review invalidation. The UI
clipboard buffer is verified; physical Ghostty clipboard delivery requires terminal OSC 52 support.

Two dependency-free launcher dispatch tests passed, proving optional review precedes text
questions and Back does not open text questions. Ten source backend cases ran in the final
full check, including explicit subprocess execution, failed-output quarantine, citation/control
validation, no-LLM generation, stale revision/file refusal, literal output, exclusions, source
report/provenance pair preservation, and shared topology transfer without human confirmation.

`git diff --check`, Python AST parsing, work-register JSON and local documentation links: PASS.

## Real consumer validation

Read-only validation of the existing Search.gov spider proposal passed: 15 nodes, 30 flows,
71 citation records. IDs used hyphens, two flow labels used semicolons, and assumptions needed
review-prose validation rather than renderer-label validation. No proposal, intake or human
review state in the consumer workspace was changed. Human confirmation was not supplied.

Hyphenated IDs retain their proposal identity; deterministic injective hex aliases satisfy
the existing renderer subset. A regression verifies distinct `crawl-api` and `crawl_api`
nodes, endpoint consistency, review/generation and all generated source/inventory checks.
Malformed IDs now identify the exact JSON field; blocked refresh no longer reports success.

## Corrections found during implementation

- Corrected a new test's call to the existing compose API; real assembled output now checked.
- Prevented inherited modal button handling from dismissing a confirmation dialog twice.
- Preserved report/provenance as a pair, blocked regeneration when prior source review disappears,
  and bound suggestion application to the displayed review digest.
- Tracked unrelated repeated-logging stream ResourceWarning as WIZ-19. Dispatcher tests isolate
  logging configuration; no production diagnostics behavior was changed by this increment.

See [workflow](source-review.md), [design decision](source-review-decision.md), and
[durable work register](wizard-work.json).
