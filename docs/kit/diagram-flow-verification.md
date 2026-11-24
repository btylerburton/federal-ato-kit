---
title: "Independent text and diagram flow verification"
description: "Observed topology-free text generation, source proposal review, rendering and attachment checks"
status: draft
tier: 2
last_updated: "2026-11-24"
---

# Verification record

OpenCode AI coordinator with bounded UI and diagram-flow implementation delegates and an
independent blocker reviewer. User approved removing topology from text configuration and
introducing a separate flow after an agent/LLM source extraction pass. No new dependency,
remote model call or application modification was performed.

## Delivered behavior

- Text navigation: System → Scope → Inheritance → Review. Existing four help disclosures remain.
- Text CLI and TUI generate without topology. New projects contain a diagram-readiness gap;
  legacy topology answers and authored diagram files remain untouched.
- Sessions saved on the old topology step resume at Review. Invalid legacy topology does
  not block editing unrelated text answers.
- Diagram proposal/clarification state lives under `diagramming/`, separately from intake.
- Exact source revision/blob/path/line provenance is validated; only missing/uncertain fields,
  hypotheses and assumptions require clarification. Prior answers and corrections are retained.
- Human confirmation binds the proposal and answer digest. Context, architecture, boundary
  and data-flow views use distinct projections/labels rather than title-only copies.
- Attachment verifies current review, copied hashes and no conflicts, then regenerates the
  text manifest with four diagram modules and review provenance while preserving responses.

## Executed checks

| Check | Result |
| --- | --- |
| Text/session/UI focused suite after split | 31 tests passed, including actual LATO generation without topology |
| Real standalone diagram flow with PlantUML/Pandoc | 12 tests passed; actual rendering and embedded media checks ran |
| Attachment suite | 2 tests passed: repeat attach, authored-response preservation, edited-output refusal and stale-review rejection |
| Full authoring-environment root check | 12 toolkit tests passed; 95 framework tests completed successfully with 7 Textual tests explicitly skipped |
| Separate locked Textual environment run | All 7 skipped Textual tests passed in 10.800 seconds |
| Text-only smoke export | 58-control DOCX generated with Pandoc alone; no PlantUML argument needed |
| Whitespace | `git diff --check` passed |

The first full attempt used the TUI-only environment with Trestle variables; its relocated
authoring test failed because that interpreter lacked defusedxml. The prepared authoring
environment passed the full authoring/render checks, and the Textual environment passed the
seven UI cases separately. No failed test was suppressed or called a pass.

## Review and scan

Independent review found stale attachment possible after a corrected/reconfirmed proposal
without regeneration. Attachment now compares the generated provenance confirmation with
the current session confirmation before copying. Regression reproduces refusal and confirms
success after regeneration. Independent re-review cleared the blocker.

Bandit on `diagram_flow.py`/`attach_diagrams.py` reported only three low subprocess/PATH
warnings for bounded Git calls using argument arrays without a shell. Report retained locally
in ignored tmp. Citation validation demonstrates where a claim came from, not that it is true.
The prior diagramming request's architecture completeness and provider-boundary applicability
still require owner review; the CLI cannot certify those from source alone.

## Limits

The standalone flow consumes an agent-generated proposal; it does not automatically call an
LLM. Diagram review is a separate dependency-free CLI in this increment, not another tab in
the text TUI. Renderer layout and final Google Docs acceptance remain separate. Consumers
with legacy duplicate diagram IDs must reconcile them explicitly before attaching new views.
