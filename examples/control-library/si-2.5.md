---
title: "SI-2.5 \u2014 Automatic Software and Firmware Updates"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-2.5 — Automatic Software and Firmware Updates

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Due to system integrity and availability concerns, organizations consider the methodology used to carry out automatic updates. Organizations balance the need to ensure that the updates are installed as soon as possible with the need to maintain configuration management and control with any mission or operational impacts that automatic updates might impose (i.e., implementing a staggered deployment strategy).

### Requirements and exact statement parts

- `si-2.5_smt`: Install [PARAM si-02.05_odp.01] automatically to [PARAM si-02.05_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-2.5_smt — Install [PARAM si-02.05_odp.01] automatically to [PARAM si-02.05_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-02.05_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-02.05_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-2.5_smt` — For “Install [PARAM si-02.05_odp.01] automatically to [PARAM si-02.05_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-02.05_odp.01` — What approved value applies to **security-relevant software and firmware updates**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security-relevant software and firmware updates to be automatically installed to system components are defined;

- `si-02.05_odp.02` — What approved value applies to **system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system components requiring security-relevant software updates to be automatically installed are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-2.5_obj` (si-2.5_smt): [PARAM si-02.05_odp.01] are installed automatically to [PARAM si-02.05_odp.02].

#### EXAMINE — `si-2.5_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing flaw remediation

- mechanisms supporting flaw remediation and automatic software/firmware updates

- system design documentation

- system configuration settings and associated documentation

- records of recent security-relevant software and firmware updates automatically installed to system components

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-2.5_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for flaw remediation

#### TEST — `si-2.5_asm-test`

- Mechanisms implementing automatic software/firmware updates

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-2.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
