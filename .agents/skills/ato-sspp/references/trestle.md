---
title: "Modular Trestle integration"
description: "Portable authoring model and compatibility acceptance checks"
status: draft
tier: 2
last_updated: "2026-11-12"
---

# Trestle integration

The optional dependency lock pins compliance-trestle 5.2.0 (Apache-2.0); upstream
identity is recorded in `tools/ato/registry.json`. Inspect the installed version
and CLI help in the environment used for the run. A lock is not an installation
or vulnerability-scan result. Preserve environment evidence in the project.

## Authoring model

Catalog → tailored profile → component definitions and system implementations →
SSP → assessment plan/results and POA&M. Keep editable controls and chapters
modular. Preserve UUIDs, control/part IDs, parameters, source versions and owner
boundaries. Component names or stubs do not establish inherited requirements.

## Adapter acceptance

1. Confirm approved immutable catalog/profile versions and agency parameters.
2. Verify dependency hashes/licenses and installed model/CLI compatibility.
3. Validate supplied models and negative fixtures on a disposable copy. Never
   change an OSCAL version string as a substitute for a reviewed migration.
4. Generate/assemble twice; check current prose, nested part IDs and UUID stability.
5. Verify old source excerpts and assessment notes do not become implementation
   assertions. Check provider attribution separately from synthetic single-system tests.
6. Render and compare selected requirements, narratives and references to inputs.

Project-specific wrapper commands are not automatically stock Trestle commands.
Query the actual CLI and document any wrapper/version dependencies in the project.
Keep source inputs outside the disposable Trestle workspace when importing them.

## Reproducible synthetic tests

From the kit, after optional setup:

```sh
.venv-ato/bin/python -m pytest tools/ato/authoring_check.py -q -p no:cacheprovider
```

Tests exercise local synthetic catalog/profile import, Markdown generation, SSP
assembly and validation, implementation prose replacement, nested statement IDs,
unchanged rebuild equality and original-excerpt exclusion. These are compatibility
checks, not evidence of any project's approved baseline or complete SSPP assembly.
