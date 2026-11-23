---
title: "Modular SSPP assembly framework — working draft"
description: "Portable manifest-driven document assembly scaffold for agent-assisted ATO work"
status: draft
tier: 2
last_updated: "2026-11-16"
---

# Modular SSPP assembly framework

Build an SSPP from versioned modules with explicit provenance, predictable inclusion and
repeatable output. Prepared with OpenCode AI assistance. It lives in the consolidated portable-ato-kit repository
(see the [root README](../README.md)); no remote repository has been created and the
publication license decision is pending.

## Architecture, boundary and data-flow pipeline

New team projects include four editable PlantUML starter views and `diagrams.json` metadata.
`tools/pipeline.py` renders pinned local SVG/PNG, composes the document, exports DOCX and
checks every figure's exact PNG bytes inside the DOCX. See [diagram-pipeline.md](diagram-pipeline.md).
The [synthetic diagram example](examples/diagrams/manifest.json) runs independently of America.gov.
The example build writes its demo DOCX under the output directory you choose; `build/` is git-ignored.

Diagram tests require `PLANTUML_TEST_JAR` and `PANDOC_TEST_BIN`; without them the live cases
are skipped. Historical note: all 23 source-repository framework tests were once executed with
those tools; this repository's own live run is tracked as PKG-04 in `../docs/kit/packaging-work.json`.

## Team template and all-control shells

Use `tools/scaffold.py` to create an editable project from a hash-pinned OSCAL catalog.
The real NIST trial generated 1,196 control/enhancement shells and 20 chapter/appendix shells,
with 58 controls selected for the review manifest. Response files and UUIDv4 identities
survive regeneration. See [team-template.md](team-template.md) for commands and limits.

## Extracted Trestle, rendering and verification engine

`tools/assemble_review.py` now owns real Trestle assembly, repeat-build comparison, source
part/provider verification, review-model projection, Pandoc DOCX rendering and output content
verification. `tools/setup_assembly.py` installs pinned renderer assets from project provenance.
Both take `--project /absolute/path/to/project.json`; the framework does not infer a parent
America.gov checkout.

America.gov retains thin compatibility launchers at `docs/compliance/scripts/assemble-review.py`
and `setup-assembly.py`. Set `SSPP_ASSEMBLY_FRAMEWORK` to relocate this directory. An explicitly
configured invalid location fails rather than falling back. Project source dates, revision,
chapter ranges, tool paths, output names and catalog/profile paths live in the consuming
project's `docs/compliance/assembly/project.json`.

### Import adapter contract

`adapter` points to **trusted, reviewed Python project code**, not executable instructions
from an imported document. Its functions are:

- `load_controls(root, config)`: ordered records containing `id`, `path`, `narrative`,
  `assessment`, and `meta` (source selections/source location plus optional Trestle parameters).
- `supplement(root, config)`: current supporting review Markdown.
- `sharing_links(text)`: project-specific link projection.
- `build_full(controls_md, root, config, frontmatter)`: full Markdown and chapter provenance.
- `verify_document(text)`: project-specific acceptance checks beyond generic content checks.

The initial adapter uses the existing migrated-source `x-migration-*` metadata contract;
other source formats normalize to that intermediate shape. `lato` is currently an internal
workspace profile alias; the actual input profile/catalog are explicit project paths.
Changing selected controls requires a fresh workspace if removed controls remain on disk.
The extracted engine retains the experiment's documented limits on DOCX byte determinism and
complete supporting-document restoration. It does not yet unify the lightweight composer
and Trestle adapter into one end-to-end manifest pipeline.

### federal-ato-kit integration

In the consolidated repository the toolkit sits beside this directory and is used by default.
Set `FEDERAL_ATO_KIT` only to use a different copy; an invalid explicit value fails with no fallback.

```sh
python3 tools/kit.py check
# optional override: export FEDERAL_ATO_KIT=/absolute/path/to/other/kit
python3 tools/kit.py verify package --package /absolute/path/to/project/docs/compliance
```

The launcher delegates to the kit's existing code, preserves its exit status and keeps the
caller's working directory. Optional environment/component checks use the same interpreter
as the calling launcher. The framework adds no duplicate evidence validator or heartbeat.

### Full extraction verification

Use an environment with Trestle 5.2.0, PyYAML and defusedxml (the consuming project's existing
locked environment supplies these), and set explicit local renderer paths:

```sh
TRESTLE_TEST_BIN=/absolute/path/to/trestle \
PANDOC_TEST_BIN=/absolute/path/to/pandoc \
python3 -m unittest discover -s tests -v
```

This adds a real synthetic OSCAL-to-DOCX build through a relocated framework. Without the
two tool variables, the optional integration case reports skipped; that is not a full
integration pass. See `extraction-verification.md` for the executed run.

## Lightweight Markdown composer

The dependency-free Python prototype assembles local Markdown modules, copies registered
figures and attachments, emits an attachment/reference index, and records input/output hashes.
It rejects missing files, duplicate IDs, directory escapes, modified hash-pinned inputs,
undeclared Markdown images/relative links and untracked output directories. Rebuilding the
same manifest produces the same artifact bytes. A generated file manifest permits safe
replacement of owned outputs without deleting user files.

```sh
python3 tools/build.py examples/minimal/manifest.json --output build/minimal
python3 -m unittest discover -s tests -v
```

Both commands work from this directory after copying it to another location. Python 3.11+
is required. There are no packages to install for this prototype.

For environment preparation and verification in one command:

```sh
python3 -m unittest discover -s tests -v
```

Open `build/minimal/document.md`, `build/minimal/inventory.json`, and the copied `assets/`
and `attachments/`. The example is synthetic and contains no America.gov claims or credentials.

## Recommended handling of supporting documents

| Mode | Use it for | Assembly behavior |
| --- | --- | --- |
| `inline` | Editable Markdown chapters, control responses, policies or short appendices | Insert local content under a stable section ID; preserve a source note |
| `attachment` | Approved snapshots of reports, forms, PDFs, spreadsheets or signed documents | Copy the local file into the package, hash it and list it in the document's attachment index |
| `reference` | Guidance or evidence retained in an external authoritative system | Preserve HTTPS URL, title and verification state; do not fetch it during builds |
| `asset` | Diagrams and images rendered into the document | Copy registered local media and embed it under a stable ID with caption/alt text |
| `diagram` | Editable PlantUML architecture/boundary/flow views | Validate aliases/flows, render SVG/PNG locally, record tool/input/output hashes and include PNG plus flow metadata |

For Google Docs evidence, preserve the original Drive link and track the owner's approved local
export as an attachment when available. A reference-only entry says “contents not verified”
until someone actually reviews it. Do not convert signed PDFs into editable prose and imply
the resulting text is a signed original. DOCX can link to packaged attachments; it does not
turn a folder of reports into one embedded, portable signed evidence bundle.

Use **separate acquisition and build phases**. Acquisition may fetch approved sources and pin
their revision/hash. The normal build is offline and reads only manifest-listed local inputs.
An unavailable required document fails a complete build; a deliberately unresolved module is
an explicit `gap` with an owner/tracking ID and a visible placeholder in the review edition.

## Intended complete document structure

1. Cover, preparation details and document revision history.
2. Guidance and approval/signature areas (unsigned unless signed evidence is supplied).
3. System chapters: identity, categorization, ownership, responsibilities, status, type,
   description/boundary, environment, interconnections, laws and regulations.
4. Control introduction, including applicable template-level acceptance criteria.
5. Profile-selected controls, part/provider narratives and optional dated assessment overlay.
6. References appendix with stable anchors.
7. Attachment index and package files.
8. Review-only gaps and supporting analysis when selected by the edition.

The comparison driving this scaffold is
`docs/compliance/assessment/import-construct-gap.md` in the current America.gov repository.
The reusable scaffold must work without that file or this parent repository.

## Idempotence contract

- Identical manifest, local inputs and tool versions yield identical Markdown, copied files
  and inventory bytes; stable IDs come from manifest keys, not wall-clock time.
- A declared document revision/date belongs to the source manifest. Actual run timestamps
  belong to audit logs outside deterministic artifact hashes.
- Two builds in fresh output directories must match. A repeat in the same owned output
  directory must also match. Removed modules must not leave stale output attachments behind.
- DOCX/PDF byte determinism is a **future acceptance test**, not established by this Markdown
  prototype. ZIP timestamps, document properties, fonts and renderer versions need control.
- OSCAL IDs require a versioned identity map compatible with the selected tool/schema.
  Do not turn `NOT_ASSESSED` into a tool-default implementation status.

## Layout

```text
README.md                 reusable setup and usage documentation
design.md                 draft architecture decision and content contract
work-items.json           scoped work, dependencies and acceptance criteria
tools/build.py            offline manifest-to-Markdown package builder
examples/minimal/         synthetic, independently runnable project
tests/test_build.py       meaningful loss, safety and repeatability tests
verification.md           observed local results and limitations
```

The extracted Trestle/Pandoc engine and lightweight composer cover complementary pieces.
Source ranges, dates and assessment markers now belong to the project configuration/adapter.
See `work-items.json` for individually tracked remaining delivery steps, including catalog-wide
team shell generation and complete supporting-document ingestion.

## Future repository handoff

Move the generic tools, design, tests and synthetic example together. Keep system-specific
SSPP content, contacts, provider records, evidence and credentials in consuming projects.
License selection and renderer/toolchain pinning remain open (see `../docs/kit/packaging-work.json`).
The evidence toolkit in `../tools/ato/` handles integrity checks; the framework delegates to it
through `tools/kit.py` rather than copying its code.
