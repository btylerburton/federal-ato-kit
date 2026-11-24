---
title: "Start and resume the diagram dashboard"
description: "One-command diagram state, source-analysis handoff, readable questions and reviewed outputs"
status: draft
tier: 2
last_updated: "2026-11-24"
---

# Diagram dashboard

From the kit root, use the same command to start or resume:

```sh
.venv-tui/bin/python sspp-assembly-framework/tools/diagram_flow.py tui \
  --repository ../searchgov-spider --workspace ../searchgov-spider-ato
```

Install the optional UI once with `bash setup-tui.sh`. The text wizard remains a separate
flow. The dashboard prepares or reopens `diagramming/`, detects a regular `proposal.json`
at the workspace root, validates/imports it, and shows the next action. No repeated manual
prepare/import/review sequence is needed. Refresh with Ctrl+R when an external agent saves
the proposal. Ctrl+Q exits; saved review answers remain on disk.

## What each screen does

- **Overview:** current state, next action, repository/revision context, runner availability,
  and an exact agent request with proposal destination. Missing analysis is explained rather
  than represented as a successful extraction.
- **Questions:** readable questions such as “Is Redis inside or outside this system boundary?”;
  sources and rationale beside the field; explicit save; known answers can be corrected.
- **Preview:** structured node/relationship and citation view. Generated PlantUML appears once
  available. This is a textual preview, not an image viewer or deployed-architecture proof.
- **Outputs:** generate, render and attach actions, enabled only when their prerequisites hold.

Answers are saved through the existing review/history mechanism. Review confirmation requires
a separate checkbox and human reviewer name. An answer change invalidates confirmation.
Existing imported proposals are never silently replaced. A differing external proposal produces
a clear conflict; preserve it and use a new workspace for a changed analysis.

## Source analysis: manual handoff or configured runner

A person can also author the proposal from source using the documented JSON contract; an LLM
is not required by the importer. The current UI does not yet provide a manual proposal builder.
See [agent/offline assessment](agent-offline-assessment.md) for the current restricted and
disconnected-operation limits and proposed first-class manual mode.

Without a runner, give your coding agent the request displayed in Overview (also saved as
`diagramming/dashboard-agent-request.md`). The agent performs the authorized source-review pass
and writes `<workspace>/proposal.json`. Refresh validates and imports it automatically.
Do not supply an example's synthetic revision as the real repository revision.

For a local installed agent wrapper, provide an operator-owned JSON config **outside the
application checkout**:

```json
{
  "schema_version": 1,
  "argv": [
    "/absolute/path/to/your-agent-wrapper",
    "--repository", "{repository}",
    "--request-file", "{request}",
    "--output-file", "{proposal}",
    "--revision", "{revision}"
  ],
  "timeout_seconds": 600
}
```

```sh
.venv-tui/bin/python sspp-assembly-framework/tools/diagram_flow.py tui \
  --repository ../searchgov-spider --workspace ../searchgov-spider-ato \
  --runner /absolute/path/to/diagram-runner.json
```

The wrapper is **your trusted executable**, not included by this config example. It must read
the request file, use its authorized provider/credentials, write proposal JSON and exit. These
flags are the wrapper contract, not a claim that a particular agent CLI already accepts them.
The dashboard does not choose a model, bypass agent permissions, or supply provider credentials.
Configure provider/network/data-handling authorization outside the kit as appropriate.

The user must enable runner execution and click **Run Analyze**. Merely opening or refreshing
the dashboard never executes it. The command uses argv without a shell, standalone supported
placeholders, an absolute executable, and a bounded timeout. On timeout its process group is
stopped. Analysis receipts contain status/exit code and hashes, not stdout, stderr, argv or
environment values that could expose credentials or source. Failed/timed-out runner proposals
are quarantined under `diagramming/runs/*-unaccepted-proposal.json`; Refresh never imports
them automatically. The dashboard retains a warning with that path. Inspect them before
retrying or explicitly copying acceptable output to the proposal destination for validation.
A zero exit without a proposal is a failure. New proposal bytes
must still pass exact-revision and citation validation before becoming review state.

This is an explicit trust boundary: the selected agent wrapper executes with the user's local
permissions and can contact its configured provider. The kit's prompt requests read-only source
review; it is not an operating-system sandbox. Review configuration rather than accepting runner
commands embedded in repository content.

## Rendering and attachment

Supply local tools at launch to enable rendering:

```sh
.venv-tui/bin/python sspp-assembly-framework/tools/diagram_flow.py tui \
  --repository ../searchgov-spider --workspace ../searchgov-spider-ato \
  --plantuml-jar /absolute/path/to/plantuml-1.2026.2.jar \
  --pandoc /absolute/path/to/pandoc
```

Generation needs no renderer. PlantUML renders SVG/PNG; optional Pandoc produces DOCX and checks
embedded media. The Outputs screen lists paths. Attach targets `<workspace>/project` after the
text wizard creates it. Current review digests and copied-file hashes are checked; stale diagrams,
edited attachments or duplicate legacy module IDs require reconciliation rather than overwrite.
Rebuild the text project's document after attachment.

States are derived from actual validated files, not remembered UI success. Corrections make old
generated/rendered outputs stale. A workspace lock prevents concurrent dashboard operations;
after a crash, verify the old operation has stopped before removing its lock. Existing CLI users
must not modify the same review concurrently; a changed session hash requires Refresh before
saving or confirming from a stale dashboard.

See [diagram-review.md](diagram-review.md) for the proposal schema and advanced CLI operations.
