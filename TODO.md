---
title: "Portable ATO Kit remaining work"
description: "Tracked follow-ups for wizard reliability, repository consolidation, offline setup and document delivery"
status: draft
tier: 2
last_updated: "2026-11-25"
related_files:
  - docs/kit/wizard-work.json
  - docs/kit/packaging-work.json
  - sspp-assembly-framework/work-items.json
---

# Remaining work

AI-authored with OpenCode assistance at the repository owner's request. This checklist
records the follow-ups accompanying the source-review and launcher changes. IDs link
the work to the existing records below, which retain detailed acceptance criteria,
owners, dependencies and historical verification results.

An unchecked item is pending completion or reconciliation. Some older planned records
overlap delivered features; review their acceptance criteria before implementing more
work or marking them complete. Historical test results do not establish current
cross-platform support.

## Work records

- [Wizard work](docs/kit/wizard-work.json): `WIZ-*`
- [Packaging work](docs/kit/packaging-work.json): `PKG-*`
- [Framework work](sspp-assembly-framework/work-items.json): `FW-*`

## Reliability and status reconciliation

- [ ] **WIZ-19 — Close diagnostic streams on reconfiguration.** Close owned logging
  handler streams before removing them. Verify repeated launcher calls in one process
  do not emit unclosed-stream `ResourceWarning` messages. Trigger: next diagnostics
  maintenance.
- [ ] **WIZ-05 — Reconcile semantic repository mapping.** Compare the planned bounded,
  revision/path-backed source adapters and per-part narratives with the delivered
  source-review workflow. Record which acceptance criteria are met and retain any
  unmet work.
- [ ] **WIZ-06 — Reconcile diagram projections and agency tailoring.** Compare delivered
  view-specific diagrams with the older planned item; retain unmet privacy/agency
  overlays and explicit tailoring requirements. Further tailoring depends on supplied
  system topology and agency requirements.
- [ ] **WIZ-13 — Reconcile manual mode and proposal authorship.** Check the delivered
  no-LLM path and authorship metadata against the planned acceptance criteria. Retain
  any gaps without assuming unavailable capabilities permit provider fallback.

## Wizard and execution capabilities

- [ ] **WIZ-08 — Assemble confirmed inheritance into OSCAL.** Map approved
  provider/common/hybrid allocations to by-component statements, preserving per-part
  evidence and remaining customer responsibilities. Depends on WIZ-07 and current
  provider scope, customer prerequisites and owner decisions.
- [ ] **WIZ-14 — Add local capability preflight and execution policy.** Detect available
  local tools without network probes or credential discovery; persist allowed modes
  and explain missing/prohibited capabilities. Trigger: owner selection of supported
  execution modes and source-transfer rules. A declaration is not OS egress enforcement.
- [ ] **WIZ-15 — Prepare an offline installation bundle.** Support explicit local
  wheelhouse/tool/catalog sources, pinned hashes and no-index installation; validate
  in a disconnected environment and fail on missing artifacts. Trigger: selection of
  target platforms and an approved acquisition process.
- [ ] **WIZ-16 — Decide runner containment and provenance requirements.** Record either
  the enforcing sandbox/egress boundary and credential scope or an approved
  trusted-process model, plus required request/executable/model and transfer metadata.
  Resolve before runner use in environments requiring filesystem, credential or
  network restrictions; do not log secrets.

## Repository consolidation and release preparation

- [ ] **PKG-01 — Reconcile license, ownership and provenance.** Review the license
  already present on GitHub's `main`, record the owner's publication decision and
  reconcile local README/provenance and packaging status with it.
- [ ] **PKG-02 — Complete repository integration and CI.** Integrate the intended local
  work with the existing GitHub repository through a reviewed PR. Configure approved CI
  to run `python3 check.py` on supported Python/platform combinations, and configure
  branch protections and review gates. Depends on PKG-01 and explicit owner approval
  for CI changes. Update the older record that still describes remote creation as pending.
- [ ] **PKG-03 — Verify fresh optional dependency installation.** Exercise hash-locked
  setup on supported operating systems and Python versions and record results, or
  regenerate platform-specific locks with advisory/license review. Required before
  claiming support beyond the original Linux/Python 3.14 resolution.
- [ ] **PKG-05 / FW-14 — Pin the complete renderer release environment.** Define and
  verify Java, fonts and native dependencies, advisory/license review, a renderer
  platform matrix and cross-platform guarantees. Depends on the recorded renderer
  pipeline work (PKG-04 / FW-12); complete before renderer releases. Historical live
  rendering does not establish fresh installation or current platform support.
- [ ] **PKG-06 — Document supported agent-skill registration.** Provide tested
  registration instructions for selected harnesses when teams request them; copying
  the repository alone does not register skills.

## Framework and document delivery

- [ ] **FW-10 — Support profile-tailored requirement display.** Explicitly select
  catalog or resolved-profile requirement prose, preserve both snapshots and detect
  changes without overwriting team assignments. Depends on FW-09; trigger: team need
  for tailored prose and parameter display.
- [ ] **FW-11 — Complete the team-shell-to-Trestle adapter.** Consume split requirement
  and response files, part/provider narratives and separately owned statuses; verify
  a real synthetic OSCAL/DOCX round trip without inventing status from UNFILLED.
  Depends on FW-09; trigger: filled team shells ready for assembly.
- [ ] **FW-05 — Complete reproducible document rendering.** Pin renderer, styles and
  fonts; verify links, images, headings and tables, and document byte determinism or
  the precise semantic-only guarantee. Depends on FW-03 / FW-04 and a complete module model.
- [ ] **FW-06 — Complete full-document fidelity acceptance.** Account for required
  sections, figures, references and attachments; verify deletion/misattribution
  rejection and Google Docs layout. Depends on FW-05 and a rendered full draft.
- [ ] **FW-13 — Obtain diagram content and sharing-renderer acceptance.** Have the
  relevant owner review boundary geometry, data inventory, environment scope,
  completeness and Google Docs layout when synthetic diagrams are replaced with
  system-specific views. Depends on FW-12; structural rendering is not owner approval.

## Legacy and consuming-project ownership reconciliation

- [ ] **FW-03 — Reconcile the America.gov import adapter record.** Confirm the current
  consuming-project owner and disposition of source-traced module coverage and the
  referenced import-construct gaps. Keep system-specific implementation and evidence
  in that project's documentation workspace. The existing record depends on FW-02.
- [ ] **FW-07 — Reconcile extraction and release documentation.** Compare its older
  repository/license/bootstrap/extraction criteria with completed separation and
  current PKG-01 / PKG-02 work; record remaining release criteria and dependencies
  rather than repeating completed extraction. The existing record depends on FW-06.
- [ ] **FW-08 — Reconcile system-narrative ownership.** Confirm where the system,
  identity and privacy owners track disposition of the referenced ICG-02–09 findings.
  Keep narrative/evidence changes with the consuming project. Owner review triggers
  this work independently of rendering; the existing record depends on FW-01.

## Closing items

When an item is completed or found already satisfied, update its linked work record
and this checklist together with the actual verification or decision reference.
Preserve historical results as dated observations. Keep deferred and dependency-blocked
items recorded with their pickup trigger until explicitly resolved or retired.
