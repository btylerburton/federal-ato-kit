---
title: "SI-7.16 \u2014 Time Limit on Process Execution Without Supervision"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-7.16 — Time Limit on Process Execution Without Supervision

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Placing a time limit on process execution without supervision is intended to apply to processes for which typical or normal execution periods can be determined and situations in which organizations exceed such periods. Supervision includes timers on operating systems, automated responses, and manual oversight and response when system process anomalies occur.

### Requirements and exact statement parts

- `si-7.16_smt`: Prohibit processes from executing without supervision for more than [PARAM si-07.16_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-7.16_smt — Prohibit processes from executing without supervision for more than [PARAM si-07.16_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-07.16_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-7.16_smt` — For “Prohibit processes from executing without supervision for more than [PARAM si-07.16_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-07.16_odp` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the maximum time period permitted for processes to execute without supervision is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-7.16_obj` (si-7.16_smt): processes are prohibited from executing without supervision for more than [PARAM si-07.16_odp].

#### EXAMINE — `si-7.16_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing software and information integrity

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-7.16_asm-interview`

- Organizational personnel responsible for software, firmware, and/or information integrity

- organizational personnel with information security responsibilities

- system/network administrators

- system developer

#### TEST — `si-7.16_asm-test`

- Software, firmware, and information integrity verification tools

- mechanisms supporting and/or implementing time limits on process execution without supervision

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-7.16`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
