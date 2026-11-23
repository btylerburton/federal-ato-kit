---
title: "Consolidated kit verification"
description: "Observed portable entrypoint and real local renderer checks after repository consolidation"
status: draft
tier: 2
last_updated: "2026-11-23"
---

# Consolidated kit verification

OpenCode AI coordinator plus delegated packaging owner and read-only blocker reviewer.
User authorized local branches/commits only. Initial seed `487dddd1dba051af5406ba822a3a629a4e0ae226`
contains byte-verified reusable code and synthetic examples; no project source documents or
contact data were copied into the examples.

## Observed results

- Delegated `python3 check.py` from an unrelated directory: 12 evidence tests and 35 framework
  tests passed with two optional integration skips explicitly reported.
- Coordinator independently ran `check.py` using the existing approved Python/Trestle/Pandoc/
  PlantUML environment: **12 evidence tests and 35 framework tests passed, zero skips**.
  The framework suite completed in 15.540 seconds on November 23, beginning approximately
  18:21 UTC. It executes actual synthetic Trestle assembly, diagram rendering and DOCX media checks.
- Renderer prerequisites: Trestle 5.2.0, Pandoc 3.8.2, PlantUML 1.2026.2 and local Java/fonts.
  These installations were referenced explicitly; they are not bundled in this repository.
- Project consumer roundtrip from the sibling ATO checkout: 58 controls, 528 source responses,
  58 current assessments and two DOCX exports verified through the relocated framework.
- Delegated mutation proof: dropped default, empty-override fallback, swallowed/collapsed exit
  codes, ignored first failure and omitted framework suite each caused tests to fail; restored
  code passed. One agent-launched blocker-only reviewer reported no blockers/security findings.
- Claims example correctly exits 2 for NOT_ASSESSED. This is tested contract behavior, not a
  fabricated evidence pass.

The delegate initially reported Pandoc absent; coordinator filesystem inspection located the
existing binary and the full optional run above supersedes that claim.

## Reproduce

```sh
python3 check.py
# Optional actual renderer/authoring paths supplied by your environment:
TRESTLE_TEST_BIN=/absolute/path/to/trestle \
PANDOC_TEST_BIN=/absolute/path/to/pandoc \
PLANTUML_TEST_JAR=/absolute/path/to/plantuml.jar \
/path/to/prepared/python check.py
```

Missing optional tools produce explicit skips. Fresh locked dependency installation on other
platforms, publication license/ownership, remote creation and CI remain tracked in
`packaging-work.json`. These are technical local checks, not live agency/provider assurance.
