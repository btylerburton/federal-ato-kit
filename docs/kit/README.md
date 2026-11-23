---
title: "Reusable ATO evidence workflow"
description: "Project intake, control mapping, verification and review-ready outputs"
status: draft
tier: 1
last_updated: "2026-11-12"
---

# Evidence-driven ATO authoring

1. Record project identity, purpose, owners, classification, approved baseline,
   template, source revisions, environment and evidence permissions using the
   [intake template](../templates/project-intake.md).
2. Inventory controls, components and boundaries. Map each requirement/part to a
   responsible owner, implementation claim, evidence and residual gap.
3. Examine claims against source and operational evidence. Distinguish source
   review, offline tests, live tests and provider attestations.
4. Run the appropriate tool in `tools/ato/registry.json` with explicit project
   package/evidence paths. Review actual observations and preserve exit codes.
5. Author modular narratives with immutable references; keep imported assertions
   separate from corrections. Resolve the approved catalog/profile before assembly.
6. Record findings and owner decisions in the project's durable work register.
   Capture the executed checks using the [verification template](../templates/verification.md).

## Project boundary

The shared directory contains tools, methodology and synthetic examples. Each
project owns its control inventory, source excerpts, provider documents, evidence,
task IDs, sessions, schedules, decisions, installed-environment results and audit log.
No project data belongs in a shared example or toolkit test fixture.

Use [formats.md](formats.md) for the current package adapter and evidence contract.
An arbitrary Markdown SSP is not automatically compatible: import it in the project
and produce the required index/layout, or implement a reviewed format adapter.

## Optional verification

Use the Python interpreter and Trestle executable from the same isolated environment:

```sh
.venv-ato/bin/python -m pytest tools/ato/test_verify.py tools/ato/properties_check.py tools/ato/authoring_check.py -q -p no:cacheprovider
```

`environment_report.py --package PATH` inventories that interpreter's installed
distributions and validates the supplied component models. Bandit and pip-audit are
optional locked dependencies; pip-audit needs advisory-service network access.
Store scan results and license reviews with the project or environment being assessed.

Synthetic Trestle tests establish tool behavior, not complete project assembly,
approved tailoring, inherited controls or authorization.
