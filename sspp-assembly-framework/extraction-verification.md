---
title: "Reusable assembly extraction verification"
description: "Observed launcher, relocated synthetic project and America.gov assembly results"
status: draft
tier: 2
last_updated: "2026-11-16"
---

# Extraction verification

> **Historical record.** Results below were observed in the source repository before consolidation into
> portable-ato-kit, with paths and tools of that environment. They do not verify this repository; live
> reruns are tracked as PKG-04 in `../docs/kit/packaging-work.json`.

OpenCode AI agent; user-approved scoped extraction. Reusable assembly/render/content-check
logic moved into `tools/assemble_review.py`; pinned asset setup moved into `tools/setup_assembly.py`.
America.gov retains its source adapter and project configuration. `tools/kit.py` delegates to
the separately maintained federal-ato-kit. The five-minute timer records this session in
`heartbeat.jsonl`; disposable integration-test directories are cleaned by the test fixture.

## Executed verification

| Command / check | Observed result |
| --- | --- |
| Existing America.gov `.venv-ato/bin/python docs/compliance/scripts/assemble-review.py` | PASS: 58 controls, 528 exact part/component responses, two DOCX exports |
| Existing project `test_assemble_review.py` suite | PASS: 4 tests through compatibility launcher |
| Framework tests with `TRESTLE_TEST_BIN` and `PANDOC_TEST_BIN` supplied | PASS: 12 tests, including real synthetic OSCAL-to-DOCX through a copied framework from unrelated working directory |
| Synthetic engine repeat assembly | PASS: identical SSP JSON on unchanged second assembly |
| Synthetic project configuration with escaping adapter path | Rejected as expected |
| Shared-kit launcher with invalid explicit relative location | Rejected as expected; no fallback |
| `FEDERAL_ATO_KIT="$PWD/federal-ato-kit" .venv-ato/bin/python tmp/sspp-assembly-framework/tools/kit.py check` | PASS: 12 shared toolkit tests and real CLI evidence-contract checks |
| `python3 tools/ato/check.py` | PASS: 12 shared tests, 10 project tests and 58-control importer validation |
| Framework source scan for America.gov names/revision/date | No such literals in extracted assembly engine |
| Bandit JSON report | Exit 1: 4 low subprocess warnings and 1 medium URL-open warning; reviewed below |

The final America.gov check completed at 2026-11-16T23:50:27Z. Its actual Trestle/Pandoc
command records remain in `docs/compliance/assembly/commands.json`; current artifact/source
hashes remain in `result.json`. Updated headings/metadata in regenerated documents reflect
configuration-driven descriptions; this is a semantic-preservation check, not a claim of
byte-identical DOCX files across the refactor. All 586 response/assessment blocks were verified
inside each output by the extracted engine.

## Failures discovered and corrected

- One initial extraction patch failed context verification without modifying files; smaller
  patches completed the move.
- The first relocated synthetic build exposed invalid empty component definitions for a
  system with no providers. The engine now omits that optional definition and `-cd` argument;
  the same real integration test passed after correction.
- The engine refuses stale controls in a reused workspace when the selected inventory shrinks;
  it requires a fresh workspace instead of silently leaving removed controls in the output.

## Security scan disposition

`extraction-bandit.json` retains the full report without suppressions. B404/B603 identify
subprocess use in the engine and kit launcher. Commands use argument lists, no shell; the
engine permits only its explicit configured tool executables, and the kit selects from four
fixed entrypoints in the explicit shared-kit directory. Project configuration and Python
adapters are trusted, reviewed code inputs, not arbitrary imported-document instructions.

B310 flags setup's URL-open API. Setup checks approved HTTPS hosts, excludes URL credentials
and non-TLS ports, verifies release hashes before extraction and uses the archive data filter.
This is the previously reviewed setup behavior, not a clean external advisory scan. Existing
ASM-15 tracks the unavailable advisory lookup. No dependencies or network downloads were
needed to verify this extraction; setup help/configuration was inspected rather than reinstalling
the existing renderer.

## Remaining scope

- FW-03: restore and modularize all source chapters/supporting materials.
- FW-05/06: unified composer/render pipeline, complete document fidelity and DOCX/PDF
  determinism/Google Docs acceptance.
- FW-09: next phase, team template with shells for all pinned catalog controls/enhancements,
  profile-selected exports, explicit unfilled fields and preservation of team edits/IDs.
- FW-07: repository/license selection and release packaging.

The extraction has a portable executable core and a tested adapter boundary. It is not a
claim that the entire future framework, supporting-document importer or catalog-shell generator
has been completed.
