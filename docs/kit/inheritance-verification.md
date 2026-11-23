---
title: "Common-control inheritance integration verification"
description: "Observed import preservation, candidate mapping, questions and document export checks"
status: draft
tier: 2
last_updated: "2026-11-23"
---

# Inheritance integration verification

OpenCode AI agent; user authorized importing four named component definitions and adding
hosting/provider/practice questions to the wizard. Original source files remain unchanged.

## Actual results

- Four imported JSON files byte-compared with supplied originals and SHA-256 index: PASS.
- Five focused inheritance tests and twelve wizard tests: PASS.
- Full configured root check: 12 toolkit tests and 62 framework tests, zero skips; framework
  run completed in 26.242 seconds on November 23. Actual Trestle, PlantUML and Pandoc paths
  were supplied from the existing prepared environment.
- Synthetic LATO generation/export: PASS, 58 selected controls, four verified diagram images,
  and 121 candidate control/part mappings from four reference providers. DOCX XML inspection
  confirmed the unresolved inheritance report was included.
- Bandit on `inheritance.py`: exit 0, no findings.
- Independent read-only blocker review: no blockers. Reviewer checked exact High-baseline
  statement IDs, rule-description resolution and composition across LATO/Low/Moderate/High.
  Reviewer did not execute DOCX; coordinator performed the actual export above.

## Evidence boundaries

Imported metadata dates and OSCAL schema versions remain as supplied. JSON parsing and mapping
tests are not exact historical-schema validation, current provider attestation, or approval
of source assertions. All candidate mappings retain UNRESOLVED inheritance, UNFILLED system
implementation and NOT_ASSESSED evidence. A yes answer declares use, not effectiveness.

The cloud.gov reference describes PaaS; a Pages answer produces an explicit scope caveat.
Egress-proxy prerequisites, including direct-egress restrictions, are retained from source rules.
SHA pinning is a separately asked dependency practice, not automatic GSA common-control
inheritance. No source provider documents were assigned to PIC as approved evidence in this run.

Edited inheritance map/report files are preserved as a unit. New question fields missing from
older answers become unknown candidates; interactive ask requests missing declarations once.
Formal approved inheritance in OSCAL remains WIZ-08. Distinct diagram semantics remain WIZ-06;
this change does not resolve the existing same-topology diagram limitation or PIC boundary decision.
