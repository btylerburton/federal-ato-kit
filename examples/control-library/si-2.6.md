---
title: "SI-2.6 \u2014 Removal of Previous Versions of Software and Firmware"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-2.6 — Removal of Previous Versions of Software and Firmware

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Previous versions of software or firmware components that are not removed from the system after updates have been installed may be exploited by adversaries. Some products may automatically remove previous versions of software and firmware from the system.

### Requirements and exact statement parts

- `si-2.6_smt`: Remove previous versions of [PARAM si-02.06_odp] after updated versions have been installed.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-2.6_smt — Remove previous versions of [PARAM si-02.06_odp] after updated versions have been installed.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-02.06_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-2.6_smt` — For “Remove previous versions of [PARAM si-02.06_odp] after updated versions have been installed.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-02.06_odp` — What approved value applies to **software and firmware components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: software and firmware components to be removed after updated versions have been installed are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-2.6_obj` (si-2.6_smt): previous versions of [PARAM si-02.06_odp] are removed after updated versions have been installed.

#### EXAMINE — `si-2.6_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing flaw remediation

- mechanisms supporting flaw remediation

- system design documentation

- system configuration settings and associated documentation

- records of software and firmware component removals after updated versions are installed

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-2.6_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for flaw remediation

#### TEST — `si-2.6_asm-test`

- Mechanisms supporting and/or implementing the removal of previous versions of software/firmware

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-2.6`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
