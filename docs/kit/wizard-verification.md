---
title: "Wizard and control-library verification"
description: "Observed source pins, repository intake, draft generation and export tests"
status: draft
tier: 2
last_updated: "2026-11-23"
---

# Verification record

OpenCode AI coordinator with bounded library implementation and independent wizard review.
User approved complete catalog examples, official baseline retrieval and the 58-control LATO
reference selection. No remote publication or authorization decision is part of this work.

## Observed input and initial pipeline results

- NIST catalog and Low/Moderate/High profiles retrieved at immutable source revision
  `5006f18c8047643eaa70e35dd0d20a58bcc41856`; hashes in `data/control-library/provenance.json`.
- Exact selection tests: 58 LATO reference, 149 Low, 287 Moderate, 370 High. Enhancement inclusion
  is explicit; parent selection does not accidentally import all children.
- Real synthetic Git checkout generated into a separate workspace. Repository `.env` content
  was not read, and package scripts were not executed by intake.
- Initial LATO and Low-ATO projects rendered successfully through actual PlantUML/Pandoc:
  12 output files each; four expected diagram PNGs verified inside each DOCX.
- Direct NIST publication-page checks failed TLS certificate validation. URLs remain authoritative
  references with unverified reachability; TLS verification was not disabled.

## Review fixes

An independent reviewer reproduced two blockers: repository subdirectory inputs could bypass
the application-write guard, and edited diagram sources could be preserved alongside changed
metadata. The implementation now resolves the real Git checkout root for intake/generation/
export guards and preserves diagram source/metadata as one unit when edited. Regression tests
cover these failures. The previous focused wizard suite passed nine tests after the fixes;
final expanded results are recorded below when all library work is integrated.

The independent re-review cleared both blockers and the new export guard. Three focused
regressions passed during that re-review; it made no file modifications or network requests.
Coordinator mutation checks in disposable copies then independently disabled checkout-root
normalization and diagram-unit preservation; the matching regression failed for each mutation.
The production files were not modified by the mutation experiment.

The first library delegate stalled without durable files and was stopped; its workspace was
retained. A smaller implementation slice was delegated directly. No uncommitted user work was
discarded. One patch context mismatch caused no file changes and was reapplied in smaller form.

## Scope of claims

Path inventory, explicit answers, baseline selection, generation and document rendering are
executable CLI behavior. Semantic repository-to-control assessment is a separately scoped
agent workflow, not established by path inventory. Commented illustrative responses remain
examples, not evidence. Diagrams seed four views from declared topology; view-specific
architecture inference and agency/privacy tailoring remain WIZ-05/06.

The implementation scan at this stage reports only low subprocess/PATH warnings for fixed
Git commands and the subprocess import; the CLI uses argument arrays, no shell and bounded
timeouts. No fresh application SAST/SCA or live provider verification is claimed.

## Final library and integrated results

- Generated 1,196 per-control Markdown files: 1,014 active templates and 182 withdrawal
  dispositions. Each active file retains control-specific catalog guidance, exact requirements,
  parameter questions, HTML-commented illustrative response, assessment targets and sources.
  Standalone files also link to toolkit intake, verification, evidence-manifest and wizard examples.
- All local toolkit-document links resolve. Existing `examples/package` fixture unchanged.
- Full configured check: 12 toolkit tests plus 55 framework tests passed with zero skips,
  including actual Trestle, PlantUML and Pandoc tests. A subsequently added all-control
  composition regression passed within the expanded 11-test wizard suite.
- Real LATO and Moderate exports containing guidance passed; comments were independently
  verified absent from both Markdown and DOCX XML. Low export also passed before the final
  guidance integration; High generation selected exactly 370 controls.
- Independent final library review found two unsupported `mailto:` catalog links. They now
  render as catalog-contact text; all 1,196 scaffold response blocks pass the actual Markdown
  processor. The first new test incorrectly supplied an OSCAL wrapper instead of its catalog
  object; that test setup error was corrected before recording the pass.
- A prior Moderate build exposed catalog-local `#au-2` links. Generator normalization converts
  those to visible source-reference text, and the actual Moderate export then passed.
- Examples are generated parameterized templates, not 1,014 individually verified implementation
  narratives. No live agency systems were assessed and no authorization is claimed.
