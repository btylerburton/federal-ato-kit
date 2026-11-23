---
title: "SI-4.21 \u2014 Probationary Periods"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-4.21 — Probationary Periods

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

During probationary periods, employees do not have permanent employment status within organizations. Without such status or access to information that is resident on the system, additional monitoring can help identify any potentially malicious activity or inappropriate behavior.

### Requirements and exact statement parts

- `si-4.21_smt`: Implement the following additional monitoring of individuals during [PARAM si-04.21_odp.02]: [PARAM si-04.21_odp.01].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-4.21_smt — Implement the following additional monitoring of individuals during [PARAM si-04.21_odp.02]: [PARAM si-04.21_odp.01].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-04.21_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-04.21_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-4.21_smt` — For “Implement the following additional monitoring of individuals during [PARAM si-04.21_odp.02]: [PARAM si-04.21_odp.01].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-04.21_odp.01` — What approved value applies to **additional monitoring**? Record the value, scope, approving authority, and decision source.

  - Catalog context: additional monitoring to be implemented on individuals during probationary periods is defined;

- `si-04.21_odp.02` — What approved value applies to **probationary period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the probationary period of individuals is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-4.21_obj` (si-4.21_smt): [PARAM si-04.21_odp.01] of individuals is implemented during [PARAM si-04.21_odp.02].

#### EXAMINE — `si-4.21_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing system monitoring

- system design documentation

- system monitoring tools and techniques documentation

- system configuration settings and associated documentation

- system monitoring logs or records

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-4.21_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for monitoring the system

#### TEST — `si-4.21_asm-test`

- Organizational processes for system monitoring

- mechanisms supporting and/or implementing a system monitoring capability

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-4.21`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-4`.

- Catalog relationship **related**: `ac-18`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
