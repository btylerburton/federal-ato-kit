---
title: "Generate a team SSPP template"
description: "Catalog-wide shells, profile-selected review documents and safe regeneration"
status: draft
tier: 2
last_updated: "2026-11-19"
---

# Team template generation

The generator is `tools/scaffold.py`. It creates a portable project with **every control and
enhancement** in a pinned OSCAL catalog, including nested enhancements. A second, resolved
catalog determines which controls enter `manifest.json`. Supply explicit SHA-256 pins; builds
never fetch a catalog automatically.

```sh
python3 tools/scaffold.py \
  --catalog /path/to/catalog.json --catalog-sha256 FULL_CATALOG_SHA256 \
  --selected-catalog /path/to/resolved-profile-catalog.json --selected-sha256 SELECTED_SHA256 \
  --output /path/to/team-project --title 'Team System SSPP' --date 2026-11-16

python3 tools/build.py /path/to/team-project/manifest.json --output /path/to/review-package
```

Omit both selection arguments to include all catalog controls in the manifest. Passing an
OSCAL profile directly fails: resolve the profile through Trestle first. The extracted Trestle
engine produces a resolved catalog; another team's existing resolver output also works.

## Generated project

Diagram-enabled scaffolds now require `--plantuml-jar /path/to/plantuml-1.2026.2.jar` on the
build command above. Use `tools/pipeline.py` with `--pandoc` for DOCX plus media verification.
See [diagram-pipeline.md](diagram-pipeline.md) for renderer setup and the complete command.

```text
project.json                         team-owned title/revision/date/edition
supporting.json                      team-owned figure/attachment/reference modules
diagrams.json                        team-owned view, node, flow and review metadata
diagrams/*.puml                       four editable synthetic diagram sources
README.md                            team workflow and preservation rules
chapters/*.md                        20 editable chapter/appendix shells
controls/<family>/<id>.requirement.md generated catalog requirements and parameters
controls/<family>/<id>.response.md    editable owner/status/part/provider/evidence/assessment fields
inputs/catalog.json                  exact full-catalog snapshot
inputs/selected-catalog.json          exact resolved selection snapshot, when supplied
control-index.json                   selected flags, paths, control and part UUIDv4 identities
manifest.json                        generated ordered review-document modules
scaffold-state.json                  ownership hashes and persistent identity map
generation-report.json               current inventory and response parts needing review
```

The 20 chapter/appendix shells include cover, revision history, guidance, approvals, system
chapters 1–12, control introduction, references, attachments and assessment notes. Figures and
reports are registered in `supporting.json` and enter the manifest on regeneration. No approval
signatures, provider attestations or implementation statuses are invented.

## Editing and regeneration

- Edit response/chapter files and the two team-owned JSON inputs. They are preserved byte-for-byte.
- Regenerate with the same pins to reproduce all file bytes. Existing UUIDv4 identities remain stable.
- New controls receive shells. Removed controls and identities stay on disk for review; the
  generated index/manifest reflects the new catalog and selection.
- If new statement parts are introduced, the preserved response is not rewritten. The report
  lists part IDs lacking response headings so the team can deliberately add narratives.
- Editing a generated requirements file causes a refusal. Missing previously authored files
  cause a refusal rather than silently recreating a blank response. Source ownership is explicit.
- Treat `scaffold-state.json` as trusted project state and keep it in version control.

**Selection versus tailoring:** requirements currently come from the full pinned catalog.
The resolved selection catalog determines inclusion, but its tailored prose/parameter values
are not merged into the shell requirements. Both exact input snapshots remain available.
The team records approved assignments explicitly; using tailored requirements as the display
source is tracked as FW-10. This scaffold is a review template, not an approved baseline.

The readiness gap always appears in generated manifests. `UNFILLED` and `NOT_ASSESSED`
are deliberate placeholders, not automated applicability or compliance decisions. Publication
readiness validation is separate from shell generation. Markdown/resource output is supported;
direct ingestion of these response shells by the extracted Trestle adapter remains FW-11.

## Actual catalog trial

Using the existing pinned NIST 800-53 Rev 5.2.0 catalog produced **1,196 control/enhancement
shells**, with **58** selected by the current LATO-resolved catalog. The trial lives in
`build/team-template/`; selected review Markdown is in `build/team-template-export/document.md`.
These are ignored synthetic team-template outputs, not America.gov implementation statements.

The generator uses the Python standard library and imports the framework's existing composer
validation. No new dependency or network download is needed.

Executed results: [template-verification.md](template-verification.md).
