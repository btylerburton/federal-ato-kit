---
title: "Federal ATO Kit"
description: "Portable evidence-readiness tools and modular SSPP authoring guidance"
status: draft
tier: 1
last_updated: "2026-11-12"
---

# Federal ATO Kit

Reusable local tools for preparing traceable ATO/SSPP review artifacts. Keep system
controls, source imports, evidence, decisions, logs and assessment results in each
consuming project. This directory is self-contained and can be moved as a unit.

## Start

Python 3.11+ is sufficient for the offline core. No installation is needed:

```sh
python3 tools/ato/check.py
```

The command also works by absolute path from any working directory. For optional
Trestle, property tests and scanners, after approving dependency downloads:

```sh
bash tools/ato/setup.sh
```

Setup creates a kit-local `.venv-ato`; recreate it after moving the kit rather than
moving an installed virtual environment. The hash-locked wheels were originally
resolved on Linux/Python 3.14; verify wheel availability for your platform.

## Use from any project

Set `FEDERAL_ATO_KIT` to this directory's absolute path. Run from the project root:

```sh
python3 "$FEDERAL_ATO_KIT/tools/ato/verify.py" package --package docs/compliance
python3 "$FEDERAL_ATO_KIT/tools/ato/verify.py" claims --manifest docs/compliance/assessment/claims.json --evidence-root .
```

Arguments select the project; the tools never search neighboring repositories.
Reports go to stdout. Exit **0** means PASS, **1** means failure/invalid input,
and **2** means BLOCKED/NOT_ASSESSED without a failure. Save results in the project.
Package checks intentionally leave OSCAL resolution and effectiveness unassessed.

## Contents

- [Workflow](docs/kit/README.md) and [input formats](docs/kit/formats.md).
- `tools/ato/`: portable validators, synthetic tests, optional dependency lock/setup.
- `examples/`: synthetic claim and package examples, not an agency baseline.
- `docs/templates/`: project intake and verification templates.
- `.agents/skills/ato-sspp/`: reusable skill source and reference material.

To make the skill discoverable, register or copy it through your agent harness's
supported project/global skill mechanism. Moving this directory alone does not
install it into another project's agent configuration. An agent can also read the
skill source explicitly using the configured toolkit location.

## Provenance and review

AI-assisted extraction by OpenCode AI / GPT 6 Astra. The toolkit evolved from a
project-specific implementation; this distribution contains generalized methodology
and synthetic fixtures, not that project's evidence or an accepted federal policy.
Dependency licenses and hashes are recorded in package metadata and the lock;
review those obligations for your intended distribution. No new license grant is
inferred by this extraction. Human review is required before operational adoption.
