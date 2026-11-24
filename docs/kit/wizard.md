---
title: "Repository-to-SSPP draft wizard"
description: "Guided intake, selected control library and diagrams for LATO or full ATO preparation"
status: draft
tier: 2
last_updated: "2026-11-24"
---

# Repository-to-SSPP draft wizard

Point the wizard at a Git repository, answer the missing system-context questions, and generate
a LATO-reference or full-ATO-baseline **text review draft** with control guidance. Diagramming
is a separate source-proposal and clarification flow; it does not block text generation.
An authorization decision, signed approval, and verified operational evidence are not generated
by software. The workflow automates inventory, selection, scaffolding and export while keeping
those missing facts visible.

## Run it

### Recommended: resumable terminal UI

```sh
bash setup-tui.sh
.venv-tui/bin/python sspp-assembly-framework/tools/wizard.py tui \
  --repository /path/to/application --workspace /path/to/application-ato
```

Use the same command every time. The UI creates `intake/` for a new workspace or adopts existing
wizard intake, retaining a byte-for-byte backup before normalization. Existing answers and
document dates are preserved; empty dates default to today and uppercase choices normalize.
System name defaults to a clearly labeled repository-name suggestion. Baseline, owner approval,
data categories and topology are never guessed. Repository association is persisted after
legacy adoption; a mismatched session or concurrent disk edit refuses overwrite.

System → Scope → Inheritance → Review panels show remaining errors.
The Inheritance panel has a `? Help` button beside the four yes/no/unknown questions (egress
proxy, GSA common controls, organization dependency management and SHA pinning). Click or
keyboard-activate it to expand guidance beside the question; activate Close to collapse it.
Guidance explains qualifying evidence, who to ask and when unknown is appropriate. Opening
help does not change saved answers or confirm scope.

Fields autosave even when incomplete, and generation stays disabled until required text
answers are valid. Ctrl+S saves and Ctrl+Q
saves/exits. Background generation disables editing and reports the project path or failure.
This UI creates the text review project; optional DOCX rendering uses `pipeline.py` with Pandoc.
A fresh text project does not require PlantUML. Existing attached diagrams remain preserved.

The previous `boundary_summary: "default"` input is retained but flagged for clarification.
The UI does not ask for topology or invent one to make generation pass. Owner placeholders
must be explicit decisions, not inferred facts. Legacy topology answers stay in their saved
file without being validated or overwritten by the text workflow.

### Dependency-free CLI and agent use

```sh
KIT=/absolute/path/to/federal-ato-kit
python3 "$KIT/sspp-assembly-framework/tools/wizard.py" intake \
  --repository /path/to/application --output /path/to/intake
python3 "$KIT/sspp-assembly-framework/tools/wizard.py" ask \
  --answers /path/to/intake/answers.json
python3 "$KIT/sspp-assembly-framework/tools/wizard.py" generate \
  --repository /path/to/application --answers /path/to/intake/answers.json \
  --output /path/to/sspp-project

python3 "$KIT/sspp-assembly-framework/tools/pipeline.py" /path/to/sspp-project/manifest.json \
  --output /path/to/export --pandoc /path/to/pandoc
```

The `ask` command is interactive. Agents can instead read `questions.json`, ask the user in their
own interface and write `answers.json`. Answers are saved incrementally. Generation is offline;
Pandoc is provisioned separately for DOCX. Java/fonts and pinned PlantUML are needed only
when rendering diagram source modules. Outputs live outside the application checkout; no
source code is modified.

## Clarifications that cannot be inferred from repository paths

Once answers and renderer paths are available, `generate` also accepts `--export /path/to/export`,
and `--pandoc` to perform generation and DOCX rendering in one command. `--plantuml-jar`
is needed only if diagrams have already been registered in the project.
If a renderer is unavailable, it reports a blocker rather than claiming the document was exported.

- System mission/name, owner, assessed environment and fixed document date.
- LATO reference or full ATO baseline, and owner confirmation of the draft selection.
- Data categories, proposed boundary and external services.
- Nodes and relationships are reviewed later in the separate diagramming flow.
- Later control-specific questions: accountable role, parameter decisions, inherited scope,
  implementation mechanism, evidence and assessment results.

Full ATO choices are official NIST Low/Moderate/High security baselines. The 58-control LATO
selection is a user-approved **reference**, not universal eligibility or agency acceptance.
Privacy, overlays and organization-specific tailoring must be assessed by the owner; the entire
catalog library remains available for additional controls. A selected security baseline alone
does not settle privacy-control applicability.

## Separate diagram proposal

An LLM/agent first inspects the permitted repository source and records supposed nodes and
relationships with source revision/path/line citations, assumptions and uncertainty. The
separate flow asks about unknown relationships and boundary placements, persists corrections,
then generates diagram sources. It does not claim the path-only intake performed that review.
See [diagram review](diagram-review.md) for its contract and commands.

Legacy topology format (retained for compatibility; no longer required for text configuration):

```json
{
  "nodes": [
    {"id": "browser", "title": "Browser", "boundary": "outside"},
    {"id": "service", "title": "Application service", "boundary": "inside"}
  ],
  "flows": [
    {"from": "browser", "to": "service", "data": "Public query",
     "protocol": "HTTPS", "authentication": "Anonymous",
     "storage": "Owner must confirm retention"}
  ]
}
```

Old generated projects may contain four diagrams seeded from the same topology. Text-only
regeneration leaves them untouched. New projects receive an explicit diagram-readiness gap
until separately reviewed diagrams are attached. Rendering checks do not prove architecture.

## Inherited and shared controls

The wizard also asks whether you host on cloud.gov PaaS or Pages, deploy cg-egress-proxy,
fall within GSA common-control scope, enroll in org-dependency-management, and use verified
SHA-pinned actions. See [component reference examples](../../examples/component-definitions/README.md)
for the four imported definitions and SHA-pinning examples.

Answers are stored in an optional `inheritance` object:

```json
{
  "hosting_service": "cloud-gov-pages",
  "egress_proxy": "unknown",
  "gsa_common_controls": "unknown",
  "org_dependency_management": "unknown",
  "sha_pinning": "unknown"
}
```

Omitted legacy answers are treated as unknown, not consent to claim inheritance. `ask` requests
missing fields once and preserves explicit yes/no/unknown answers. Generation emits
`inheritance/map.json` and `inheritance/responsibilities.md`, and includes the responsibility
report in the document manifest. A yes answer identifies a candidate reference; no excludes it;
unknown lists unresolved candidates for clarification. No system status is automatically completed.

The mappings retain exact source control IDs and statement-part IDs, provider prose/status,
rule identifiers and descriptions, version/date/hash, and an unresolved applicability decision.
Controls not covered by the references remain application questions. The source definitions
are not rewritten or recertified. Pages is explicitly distinguished from the supplied PaaS CRM.
Provider-managed responsibility and authorization-boundary placement are separate decisions.

The map/report form one preservation unit: if either is edited, both are preserved and listed
for reconciliation on regeneration. Full OSCAL incorporation of these candidate mappings and
owner-confirmed inheritance decisions is not implied by this readable report integration.

## What is autonomous now

- Bounded, tracked-path repository inventory: manifests, deployments, workflow/test/doc paths.
- Durable intake questions and incremental interactive answers.
- Hash-verified offline baseline selection and selected control project generation.
- Control requirements, example guidance and unanswered status/evidence fields.
- Regeneration preserves edited responses/chapters and stable IDs; managed intake text refreshes
  only when unchanged. The text workflow never rewrites diagram sources from topology answers.
- Existing pipeline renders SVG/PNG and DOCX and verifies embedded diagram bytes.

## What still needs an agent or owner

This initial intake reads **paths**, not application file contents. It never executes repository
scripts or sends source to an external service. A coding agent can perform an explicitly scoped
semantic source review, cite exact files/revisions, and draft responses from those observations.
That deeper source-to-control mapping is not silently implied by discovering `Dockerfile` or tests.
Examples stay commented out and implementation fields remain UNFILLED until real narratives
are supplied. Provider inheritance, agency-specific tailoring and legal/operational assertions
require actual evidence. Publication readiness and full formal OSCAL authoring remain distinct
from producing a review document.

Use a staged loop: intake → answer blocking questions → generate → source/evidence review →
author responses → build/review → resolve gaps. The goal is fewer repetitive questions and
manual assembly tasks, not silently answering questions the repository cannot prove.
