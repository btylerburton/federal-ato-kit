---
title: "Standalone source-cited diagram review"
description: "Import an agent proposal, resolve uncertainty and render a human-reviewed external diagram project"
status: draft
tier: 2
last_updated: "2026-11-24"
related_files:
  - docs/kit/wizard.md
  - examples/diagram-proposal/README.md
  - sspp-assembly-framework/tools/diagram_flow.py
---

# Standalone diagram proposal and review

Diagrams need repository-specific reasoning and human boundary decisions. The AI-assisted
`diagram_flow.py` CLI accepts an explicit proposal from an agent or person, checks its source
citations, persists unresolved questions and generates four distinct review views. It makes
no model call and does not infer topology from filenames. Source text is never executed.

## Start an external workspace

Run from the kit root, with the application and its documentation workspace as siblings:

```sh
python3 -B sspp-assembly-framework/tools/diagram_flow.py prepare \
  --repository ../application --workspace ../application-ato
```

`start` is an alias for `prepare`. Both safely resume an existing session. Use the root
`./ato-wizard <repo>` launcher to select a new owned in-repo `docs`/`docs-timestamp` workspace,
or supply an external directory outside every checkout. In-repo paths require the launcher
ownership marker; arbitrary application folders are rejected. Workspaces cannot use symlinks.
The flow owns only `<workspace>/diagramming/`; an existing `<workspace>/intake/` is independent.

`diagramming/session.json` records the checkout root, exact `HEAD` commit and a filtered list
of tracked blob paths. This is a path inventory, not a source assessment. No application
files or intake answers are written. A new commit requires a new workspace; a dirty checkout
does not change the committed source basis.

## Supply the proposal

Ask an authorized agent or reviewer to examine the relevant source and author JSON following
[`examples/diagram-proposal/proposal.json`](../../examples/diagram-proposal/proposal.json).
Use the exact full commit from `session.json`. Save the authored proposal outside the
application checkout, then import it:

```sh
python3 -B sspp-assembly-framework/tools/diagram_flow.py import \
  --repository ../application --workspace ../application-ato \
  --proposal ../application-ato/proposal.json
```

Required proposal structure:

- `schema_version: 1`, `repository_revision`: exact full commit hash.
- `system_name`, `environment`, `date` (ISO date), each optionally `null` until clarified.
- `nodes`: 1–40 objects with stable `id`, `title`, `boundary` (`inside`/`outside` or `null`),
  optional `kind` (`component`, `database`, `actor`, `queue`).
- `flows`: 1–100 objects with stable `id`, `from`, `to`, `data`, `protocol`,
  `authentication`, `storage`. Missing values, `null`, empty strings or `"unknown"`
  trigger a question. Use meaningful data labels, not numeric flow names.
- Each node and flow has `status: "source-supported"` or `"hypothesis"` and
  `evidence: [{"path": "src/service.py", "lines": [10, 25]}]`.
  Source-supported records require citations. Hypotheses may have an empty evidence array;
  each requires a separate human confirmation.
- `unknown_fields`: field keys that remain uncertain even if a draft value was supplied,
  such as `"nodes/api/boundary"` or `"flows/request/authentication"`.
- `assumptions`: plain-language strings; every assumption requires a human disposition.

IDs use lowercase letters, digits, underscores and hyphens, beginning with a letter (maximum
60 characters). Hyphenated proposal IDs get collision-safe renderer aliases; review IDs are retained.
Display labels use a deliberately small ASCII subset (letters, digits, spaces and `._()/,:;+@-`, at most 160
characters); PlantUML directives, multiline content, quotes and markup are not accepted.
Assumptions are review prose (up to 4000 characters each), never interpolated into diagram source.
The [shared source-review flow](source-review.md) can propose topology alongside text findings.
Overview includes **Copy prompt**; **F4** opens copyable field/screen text.

Import checks citations against regular tracked blobs at the exact commit with `git ls-tree`
and `git cat-file`. It rejects traversal, symlinks/submodules, excluded secret/environment
paths, nontext blobs, oversized blobs and invalid line ranges. It does not read working-tree
source, run application scripts or contact services. The excluded-path filter is conservative;
the authorized proposal author must also avoid citing sensitive files under ordinary names.
Citation existence verifies provenance, **not whether the source supports the assertion**.

The imported `diagramming/proposal.json` is preserved byte-for-byte. Reimporting identical
bytes preserves answers; importing a different proposal requires a new workspace. Verified
provenance includes commit hash, blob hash, path and line ranges without copying source text.

## Resolve only missing or uncertain fields

```sh
python3 -B sspp-assembly-framework/tools/diagram_flow.py review \
  --repository ../application --workspace ../application-ato
```

The dependency-free prompt asks only pending questions. Blank input defers a field; EOF
ends the session without discarding answers already supplied. Answers are saved after each
response. `session.json` contains durable `pending`, `answers` and timestamped `answer_history`.
Hypotheses require the literal answer `confirmed` after reviewing/correcting their fields.
Assumptions require a human disposition; make corresponding topology corrections explicitly.

For a harness or partial noninteractive review, supply a JSON object mapping field keys to
human answers:

```json
{
  "nodes/db/boundary": "inside",
  "nodes/db/review": "confirmed",
  "flows/request/authentication": "Anonymous public access",
  "assumptions/0": "Confirmed for the review environment by the system owner"
}
```

```sh
python3 -B sspp-assembly-framework/tools/diagram_flow.py review \
  --repository ../application --workspace ../application-ato \
  --answers ../application-ato/diagram-answers.json
```

This also supports deliberate corrections to known fields. Previously supplied answers
remain until explicitly replaced, with prior values retained in history. Any answer edit
invalidates prior confirmation. Node/flow membership and evidence changes require a new
proposal/workspace; changing a field preserves the original proposal and records the override.

The human reviewer must inspect the imported proposal, citations, assumptions and saved
answers, then explicitly confirm the resolved draft:

```sh
python3 -B sspp-assembly-framework/tools/diagram_flow.py review \
  --repository ../application --workspace ../application-ato \
  --confirm --reviewer "System architecture reviewer"
python3 -B sspp-assembly-framework/tools/diagram_flow.py generate \
  --repository ../application --workspace ../application-ato
```

Confirmation fails if questions remain. Confirmation records the reviewer, timestamp and
digest of the proposal plus answers. An agent must not supply confirmation on the human's
behalf. This is draft review, not production or authorization approval.

## Four views and optional rendering

`diagramming/project/manifest.json` registers four PlantUML sources and `review-record.json`:

| View | Projection |
| --- | --- |
| Context | Collapse inside components into the named system; retain external interactions |
| Boundary | Group inside components; label flows with data and authentication |
| Architecture | Use optional component/database/actor/queue types and data/protocol labels |
| Data flow | Show named data, protocol, authentication and storage on each directed flow |

Each view's metadata matches its actual node and arrow inventory. The review record retains
the resolved topology, imported proposal hash, exact source provenance, assumptions, answers,
answer history and confirmation. This modest projection requires owner review for advanced
network zones, trust tiers, deployment multiplicity, storage semantics and layout.

Generate requires no renderer or external dependency. Render with an already-approved local
pinned PlantUML JAR; add the existing pinned Pandoc executable for DOCX:

```sh
python3 -B sspp-assembly-framework/tools/diagram_flow.py render \
  --repository ../application --workspace ../application-ato \
  --plantuml-jar /approved/tools/plantuml.jar
# Optional addition: --pandoc /approved/tools/pandoc
```

`render` uses the existing `build`/`diagrams.render` path for Markdown, PNG and SVG, or the
existing `pipeline` for DOCX and embedded-figure verification. Output is owned under
`diagramming/rendered/`. Rendering performs no downloads.

Generation preflights all prior generated hashes before writing. Missing, edited or untracked
project files cause refusal, preserving the entire project. Rendering also preflights its
existing output inventory. Preserve deliberate PlantUML edits and use the existing standalone
build/pipeline on that team-owned copy; do not remove ownership state to force an overwrite.

## Attach to the independently generated text project

After generation and explicit review:

```sh
python3 -B sspp-assembly-framework/tools/attach_diagrams.py \
  --repository ../application --workspace ../application-ato \
  --project ../application-ato/project
```

The command checks current confirmation and generated hashes, copies diagram sources and
review provenance under `supporting/diagram-review/`, adds hash-pinned entries to
`supporting.json`, and regenerates the text manifest without overwriting team responses.
The diagram-readiness gap is replaced by the four reviewed view modules and provenance
attachment. Repeat attachment is safe when unchanged; edited attached files or conflicting
legacy diagram IDs cause a refusal rather than an overwrite. Existing legacy `diagrams.json`
requires deliberate reconciliation before attaching the same IDs.

Use `pipeline.py` on the resulting text manifest for a combined DOCX. The separate diagram
proposal/history stays in `diagramming/`; intake and text answers are not rewritten.

## Verification

```sh
python3 -B -m unittest discover -s sspp-assembly-framework/tests -p 'test_diagram_flow.py' -v
```

The suite uses disposable committed repositories and exercises the real CLI, partial
clarification, confirmation, exact source references, secret-path rejection, checkout write
protection, correction history, distinct projections and output preservation. Set
`PLANTUML_TEST_JAR` for the actual offline renderer test, optionally `PANDOC_TEST_BIN` for
DOCX. The default suite needs neither network access nor additional dependencies.
