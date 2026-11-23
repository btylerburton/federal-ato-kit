---
name: ato-sspp
title: "Evidence-driven ATO and SSPP review"
description: "Build and review modular SSPPs by connecting requirements, boundaries, component responsibilities, source claims, and executable evidence."
status: draft
tier: 1
version: "0.1.0"
last_updated: "2026-11-06"
---

# ATO/SSPP at agentic speed

Act as an AI author and reviewer. Optimize time to trustworthy review evidence,
not pages generated. The authorizing official accepts risk; the agent prepares
traceable findings and decision-ready artifacts.

## Locate the kit

Resolve the shared kit through `FEDERAL_ATO_KIT` or this skill's containing kit
directory. Read the kit's `docs/kit/README.md` and `tools/ato/registry.json`, then
the consuming project's work register. Toolkit paths below are relative to the kit;
package/evidence paths are supplied by the project, never inferred from the kit's location.
The implementation is in `tools/ato/`; this skill owns methodology, not a second
validator. Read `references/methodology.md`, `references/standards.md`,
`references/trestle.md`, and `references/verification.md` beside this skill as
needed. Do not load the entire SSPP into context by default.

Use the consuming project's approved coordination workflow. Record ownership
before scheduling or delegating. Project permissions govern installs, live tests,
and publishing. No project session IDs or active schedules are shipped with the kit.

## Intake once, then reuse

1. Identify agency/system owner, AO/ISSO, assessment purpose, applicable template
   version, system categorization, authorization boundary, and baseline/profile.
2. Locate application/configuration repositories and exact revisions, existing
   SSPP, component definitions, CRMs, agreements, assessments, and POA&M.
3. Confirm environments, data classifications, test-data permissions, evidence
   storage/access/retention, and allowed local and live actions. Never infer a
   production boundary from a DNS suffix or a development checkout.
4. Record unresolved decisions once with owner, trigger, and blocking dependency.
   Ask only questions blocking the next slice; continue independent approved work.

## Review loop

1. **Inventory:** discover artifacts, validate provenance, identify missing local
   references, then inspect the highest-risk flows (identity, PII, egress, logs).
2. **Map:** requirement/assessment objective → control part → responsible
   component/team → implementation claim → evidence → residual gap/decision.
3. **Challenge:** write falsifiable claims with environment, revision, conditions,
   expected observable result, and a test that would detect the opposite result.
4. **Verify:** use the tool registry. Run focused checks, preserve exit codes and
   actual observations, and distinguish source review from live behavior.
5. **Author:** update modular narratives from attributable evidence. Preserve
   imported assertions and hashes separately from corrections. Never overwrite
   original source excerpts or invent checkbox/component statuses.
6. **Assemble:** resolve/pin the profile and catalog; validate component and SSP
   models; check UUID/reference integrity; assemble/render in an isolated copy.
7. **Report:** prioritize blockers, contradictions, unassessed requirements, and
   human decisions. A valid OSCAL object is not evidence of effective controls.
8. **Reflect:** during longer work, assess progress, scope drift, proof quality,
   and the next smallest slice. Record substantive reflections in the project.
   If a schedule is authorized, stop the owned schedule at completion.

## Evidence rules

- Label evidence `source-review`, `offline-test`, `live-test`, or
  `provider-attestation`. An offline test cannot establish a deployed claim.
- Evidence records need source revision, environment, observation time, expiry,
  artifact SHA-256, method, result, and observation. Hash integrity proves that a
  file matches the recorded hash, not that its contents are true.
- Report check outcomes as `PASS`, `FAIL`, `BLOCKED`, or `NOT_ASSESSED`.
  Track control implementation and assessor conclusions independently.
- Record application/browser, backend, provider, logs, backups, downloadable
  exports, and abandoned drafts. Memory-only is still processing sensitive data.
- Inheritance requires authoritative scope and shared-responsibility evidence;
  a provider name, authorization label, or component stub establishes neither.
- Cite source repository, path, immutable revision, and line range. Do not embed
  sibling-checkout or machine-specific relative hyperlinks in documents.
- Keep security findings in the authorized private evidence store. Do not publish
  vulnerability details through issue creation or report uploads by default.

## Fast path

Set `FEDERAL_ATO_KIT` to the kit's absolute directory. From the consuming project:

```sh
python3 "$FEDERAL_ATO_KIT/tools/ato/verify.py" package --package docs/compliance
python3 "$FEDERAL_ATO_KIT/tools/ato/verify.py" claims --manifest docs/compliance/assessment/claims.json --evidence-root .
python3 "$FEDERAL_ATO_KIT/tools/ato/check.py"
```

Read the machine-readable report and its coverage boundary. `check.py` verifies
the toolkit itself; it does not certify the system. Reuse fresh evidence only
when claim scope, environment, source revision, tool configuration, and artifact
hash still match. Rerun affected claims after changes; broaden only when needed.

## Completion

An iteration ends when its agreed deliverables and focused checks are complete,
all pending work has a durable tracked record, and its heartbeat is stopped.
An ATO review is ready only when the selected requirements are accounted for,
evidence and findings are reviewed, package references resolve, and the owner
has dispositioned residual risks. Neither milestone means authorization granted.
