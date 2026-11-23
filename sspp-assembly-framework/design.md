---
title: "Use manifest-driven offline SSPP composition"
description: "Draft architecture decision for reusable modular SSPP generation"
status: draft
tier: 2
date: "2026-11-16"
decision_status: proposed
decision_makers: ["Requesting repository owner"]
category: "Deployment and Infrastructure"
nist_controls: ["CM-2", "CM-3", "SA-5", "SA-11", "PL-2"]
ato_relevance: yes-internal
risk_treatment: mitigate
---

# Use manifest-driven offline SSPP composition

## Context and problem

The first America.gov assembly preserved control responses but omitted source appendices,
linked attachments and image definitions. Chapter line slicing and current-assessment injection
are project-specific, fragile build inputs. A reusable framework needs explicit modules and
proof of complete assembly, not only a valid output file.

## Decision drivers

- Preserve meaning, provenance and supporting material from the imported template.
- Support different systems without editing builder code.
- Keep assessment conclusions separate from implementation claims and inheritance assertions.
- Make missing modules visible; avoid runtime network dependence and silent omissions.
- Demonstrate fresh-build and repeated-build equivalence.

## Considered options

1. Copy the existing America.gov script and replace system names.
2. Compose ordered, versioned modules through a validated project manifest and adapters.
3. Maintain one manually edited monolithic SSPP.

## Proposed outcome

Use option 2. Implement generic document composition first, then integrate the existing
Trestle-based control adapter through a small contract. Keep system content in project-owned
directories. The prototype is executable Markdown composition; complete OSCAL/DOCX/PDF
integration remains tracked work.

## Manifest contract (prototype version 1)

The manifest is JSON with `schema_version`, `document` and ordered `modules`.
The document names `title`, `revision`, `date` and `edition` (`review` or `publication`).
Every module has a unique lowercase stable `id`, `title`, `kind`, and human-readable `source`.

- `inline`: `path` to UTF-8 Markdown, optionally `sha256`.
- `asset`: local `path`, `alt`, optionally `sha256`. Copied to `assets/` and rendered inline.
- `attachment`: local `path`, optionally `sha256`. Copied to `attachments/` and indexed.
- `reference`: `url` (HTTPS) and `verification` (`not-reviewed` or `reviewed`). This records
  a supplied review state; it does not independently prove that review happened.
- `gap`: `tracking`, `owner`, `reason`; visibly included only in review builds. Publication
  builds fail when an explicit gap is present.

Paths resolve under the manifest directory, never by searching the working directory. Symlinks
that resolve outside the project are rejected. The builder does not execute embedded source
commands or evaluate source Jinja. Local Markdown links use explicit `module:<id>` targets,
which resolve to registered anchors or packaged files. External links remain HTTPS references.
Arbitrary relative links and reference-style images fail rather than disappearing unnoticed.
Initial ingestion must convert source reference definitions into registered modules.

An inventory lists each module's input hash (if local), output path/anchor and source. Output
hashes cover the generated document and copied resources; the inventory excludes its own hash.
Only outputs owned by a prior builder inventory may be replaced or removed. User-modified or
unregistered files cause a refusal. Audit logs are outside the owned artifact directory.

## Extraction decision — implemented slice

Reusable Trestle/render/verification and renderer-setup code lives under framework `tools/`.
Project launchers resolve `SSPP_ASSEMBLY_FRAMEWORK`; project configuration locates the inputs,
tools and trusted import adapter. `FEDERAL_ATO_KIT` independently resolves shared verification
through `tools/kit.py`, preserving ownership of that implementation. A real relocated synthetic
project validates the adapter boundary. The full modular pipeline below still requires the
remaining integration work tracked in the work register.

The next template phase generates every control/enhancement shell from a pinned catalog,
with profile selection controlling document inclusion. Empty sections remain unfilled; stable
identities and team edits survive regeneration. This is FW-09, not an inferred implemented feature.

## Full pipeline contract (planned)

1. **Acquire:** import an approved document and record immutable source identity. Extract
   sections, references and embedded images once; preserve original bytes separately.
2. **Author:** edit modular chapters and control responses. Store provider attribution,
   implementation status, evidence availability and assessment conclusion as separate fields.
3. **Resolve controls:** pinned catalog → profile → part/component responses → OSCAL SSP.
   Validate all expected controls and nested part IDs; preserve a versioned UUID map.
4. **Compose:** select a project/template manifest and edition, combine chapters, control
   output, figures, reference appendix and attachment index with explicit anchors.
5. **Render:** pinned local Pandoc and reference style → DOCX; optional PDF with pinned fonts
   and engine. Do not borrow classification markings from another project's reference DOCX.
6. **Verify:** compare expected sections, part/provider text, figures, links and attachments
   with actual output, plus fresh-build and repeat-build identity.
7. **Package:** output document, linked local evidence, inventory and verification report.
   Review gaps remain visible until resolved by their owners; generation does not confer ATO.

## Consequences

### Diagram stage — November 19

The manifest now supports `diagram` modules. PlantUML 1.2026.2 runs as a pinned local tool
with bundled Smetana, producing SVG and PNG. A separate `pipeline.py` connects composition to
Pandoc 3.8.2 and verifies expected PNG hashes in DOCX media. This complements the existing
Trestle adapter and federal-ato-kit launchers; it does not copy evidence validation into the
renderer. Java/fonts are explicit environment dependencies. Rendering repeatability is scoped
to the same environment, and owner acceptance is tracked separately from structural checks.

Positive: portable inputs, explicit document completeness, repeatability and testable failure
paths. Negative: initial import needs deliberate section/asset mapping, and external evidence
needs owner-managed snapshots or accurately labeled references. A generic manifest cannot
resolve legal, boundary, provider or operational assurance questions automatically.

The common playbook's documentation size target is a review aid here: keep the prototype in
small functions and split adapters at real boundaries as OSCAL/rendering integration lands.
No additional runtime dependency or new external service is introduced by this draft.
