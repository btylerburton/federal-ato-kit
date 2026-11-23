---
title: "Portable ATO Kit"
description: "Reusable evidence-readiness toolkit and modular SSPP assembly framework"
status: draft
tier: 1
last_updated: "2026-11-23"
---

# Portable ATO Kit

Reusable local tools for preparing traceable ATO/SSPP review artifacts. This repository
holds two parts that ship together:

| Part | Location | Purpose |
| --- | --- | --- |
| Evidence toolkit | `tools/ato/` | Offline validators for evidence integrity, freshness and package inventory; prints JSON and uses exit codes (0 PASS, 1 failure, 2 BLOCKED/NOT_ASSESSED). |
| SSPP assembly framework | `sspp-assembly-framework/` | Manifest-driven assembly of an SSPP from versioned modules; optional Trestle/Pandoc/PlantUML rendering to DOCX. See its [README](sspp-assembly-framework/README.md). |

Keep system controls, source imports, evidence, decisions, logs and assessment results in
each consuming project. Nothing here is an agency baseline, an accepted federal policy or
evidence that any control is effective; examples are synthetic.

## Quick start

For repository-guided LATO/full-ATO preparation, start with the
[draft wizard workflow](docs/kit/wizard.md). It records repository observations, asks for
missing system context, selects a pinned baseline and creates an editable draft with diagrams.
The optional `ato-wizard` agent skill adds a source/evidence review workflow; CLI path discovery
alone is not an implementation assessment.

The [control library](examples/control-library/README.md) covers the full pinned catalog with
descriptions, commented illustrative responses, questions, evidence guidance and source links.
The original `examples/package/` remains a minimal validator fixture; use the control library
and wizard for authoring guidance.

Python 3.11+ and nothing else (no installs, no network):

```sh
python3 check.py
```

This runs both focused suites (the toolkit's checks and the framework's unit tests) and
exits non-zero if either fails. It works by absolute path from any directory. Live
renderer integration tests are skipped unless `TRESTLE_TEST_BIN`, `PANDOC_TEST_BIN` and
`PLANTUML_TEST_JAR` are set; a skip is not a pass.

Try the examples from any working directory (use this repository's absolute path):

```sh
KIT=/absolute/path/to/this/repository
python3 "$KIT/tools/ato/verify.py" claims --manifest "$KIT/examples/claims.json" --evidence-root "$KIT/examples"
python3 "$KIT/sspp-assembly-framework/tools/build.py" \
  "$KIT/sspp-assembly-framework/examples/minimal/manifest.json" --output /tmp/minimal-sspp
```

The first command intentionally exits 2 (the example claims are unevidenced). The second
writes `document.md`, an inventory and copied assets to a directory you choose.

## Optional setup

Only needed for Trestle, property tests and scanners. It downloads hash-locked packages
from PyPI, so run it only after approving dependency downloads:

```sh
bash setup.sh          # delegates to tools/ato/setup.sh; creates ./.venv-ato
bash setup.sh --help   # also lists the separate optional renderer steps
```

Optional renderers are explicit, separate steps and are never run by `setup.sh`:

- Pandoc and the pinned catalog: `sspp-assembly-framework/tools/setup_assembly.py --project /abs/project.json` (Linux ARM64/AMD64, downloads pinned assets).
- PlantUML: `sspp-assembly-framework/tools/setup_diagrams.py --destination /abs/plantuml.jar` (also requires a Java runtime you provide).

The lock was resolved on Linux/Python 3.14; verify wheel availability for your platform.
Recreate `.venv-ato` after moving the repository rather than moving an installed one.

## Use from another project

Run from your project root; arguments select the project and the tools never search
neighboring directories:

```sh
python3 /path/to/this/repository/tools/ato/verify.py package --package docs/compliance
python3 /path/to/this/repository/tools/ato/verify.py claims --manifest docs/compliance/assessment/claims.json --evidence-root .
```

`sspp-assembly-framework/tools/kit.py` is a thin launcher for the toolkit
(`check`, `verify`, `environment_report`, `heartbeat`). By default it uses the toolkit in
this repository; set `FEDERAL_ATO_KIT` to an absolute directory to use another copy. An
explicitly set but invalid value fails; it never falls back to the default. It keeps the
caller's working directory and returns the toolkit's exact exit status.

## Contents

- [Workflow](docs/kit/README.md) and [input formats](docs/kit/formats.md).
- `tools/ato/`: validators, synthetic tests, optional dependency lock and setup.
- `sspp-assembly-framework/`: assembly tools, design, tests and synthetic examples.
- `examples/`: synthetic claim and package examples.
- `docs/templates/`: project intake and verification templates.
- `docs/kit/packaging-work.json`: tracked remaining work to publish this repository.
- `.agents/skills/ato-sspp/`: reusable skill source. Moving this repository does not
  register the skill with an agent harness; use your harness's own mechanism.

Files named `*verification.md` record results observed in the source repository before
consolidation. They are historical, not a verification of this repository.

## Provenance, license and review

AI-assisted extraction by OpenCode AI / GPT 6 Astra from a project-specific
implementation; this repository contains generalized methodology and synthetic fixtures,
not that project's documents, contacts, evidence or build outputs. **The publication
license and ownership decision is pending**; no license grant is inferred. Dependency
licenses and hashes are in the lock and package metadata. Human review is required
before operational adoption. Remaining work is tracked in `docs/kit/packaging-work.json`.
