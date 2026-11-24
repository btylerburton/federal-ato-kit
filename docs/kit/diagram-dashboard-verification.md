---
title: "Diagram dashboard verification"
description: "Observed Textual state recovery, runner failure handling and actual diagram rendering"
status: draft
tier: 2
last_updated: "2026-11-24"
---

# Diagram dashboard verification

OpenCode AI coordinator, delegated UI implementation and independent blocker review. User
approved a separate one-command Textual start/resume dashboard and configurable agent handoff.
No real agent provider was configured or invoked against user source during verification.

## Executed results

- Textual Pilot suite: six tests passed, covering 80×24/100×40 missing-proposal UI, automatic
  import, human-readable questions, null endpoint answers, explicit confirmation/corrections,
  real source generation, and background error/quit behavior.
- Dashboard backend suite with actual local PlantUML and Pandoc: ten tests passed in
  8.428 seconds. Includes render-receipt staleness after correction and actual artifact creation.
- Root check in the pinned TUI environment: 12 toolkit tests passed; 112 framework tests
  completed successfully with four optional renderer/Trestle tests explicitly skipped.
  Actual new-dashboard rendering was separately run as noted above; a skip is not a pass.
- Fake installed wrappers were executed as real subprocesses in disposable fixtures to test
  explicit execution, exact exit handling, missing output, timeout and partial-output quarantine.
  These prove the runner contract, not a live LLM's behavior or provider access.

## Review fixes

The first independent review reproduced three blockers. Each was fixed with a regression:

1. Schema-valid partial output from a failed/timed-out runner was auto-imported by refresh.
   Such output is now moved to a named unaccepted file under runs, with a persistent warning.
   Reopening stays at needs-analysis; no provider success is inferred.
2. Null flow endpoints caused human-question labels to fail. They now have readable unknown
   source/destination labels and can be answered through the actual TUI.
3. Attachment state compared two registrations with each other but not the expected files.
   It now reconstructs expected prefixed paths/hashes from current generated modules and
   compares both supporting and assembled manifests with those expected entries.

Independent re-review cleared all three within the scoped review and reran the backend/UI
suites (one renderer skipped in the reviewer environment). Coordinator ran the actual renderer.

## Scan and limits

Bandit on the three new modules reported only low subprocess findings: B404 on imports and
B603 on the explicit runner invocation. No findings were suppressed. The runner uses argument
arrays without a shell, explicit absolute executable paths and bounded timeouts; it is trusted
operator code and is not an OS sandbox. It inherits the invoking process's environment/access.
Network restrictions and source-read restrictions are not enforced by a prompt or by hiding
stdout. These constraints are the subject of the next agent/offline capability review.

Preview is structured text/source, not a raster-image preview. The dashboard displays current
validated state and requires explicit human review; source citation existence is not semantic
or deployment verification. Runner portability currently assumes POSIX process groups.
Consumer application/intake records were not changed for this implementation test.
