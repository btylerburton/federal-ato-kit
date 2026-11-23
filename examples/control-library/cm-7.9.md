---
title: "CM-7.9 \u2014 Prohibiting The Use of Unauthorized Hardware"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-7.9 — Prohibiting The Use of Unauthorized Hardware

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Hardware components provide the foundation for organizational systems and the platform for the execution of authorized software programs. Managing the inventory of hardware components and controlling which hardware components are permitted to be installed or connected to organizational systems is essential in order to provide adequate security.

### Requirements and exact statement parts

- `cm-7.9_smt`: Statement grouping; see child parts.

- `cm-7.9_smt.a`: Identify [PARAM cm-07.09_odp.01];

- `cm-7.9_smt.b`: Prohibit the use or connection of unauthorized hardware components;

- `cm-7.9_smt.c`: Review and update the list of authorized hardware components [PARAM cm-07.09_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-7.9_smt.a — Identify [PARAM cm-07.09_odp.01];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-7.9_smt.b — Prohibit the use or connection of unauthorized hardware components;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-7.9_smt.c — Review and update the list of authorized hardware components [PARAM cm-07.09_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-07.09_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-07.09_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-7.9_smt.a` — For “Identify [PARAM cm-07.09_odp.01];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-7.9_smt.b` — For “Prohibit the use or connection of unauthorized hardware components;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-7.9_smt.c` — For “Review and update the list of authorized hardware components [PARAM cm-07.09_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-07.09_odp.01` — What approved value applies to **hardware components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: hardware components authorized for system use are defined;

- `cm-07.09_odp.02` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to review and update the list of authorized hardware components is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-7.9_obj.a` (cm-7.9_smt.a): [PARAM cm-07.09_odp.01] are identified;

- `cm-7.9_obj.b` (cm-7.9_smt.b): the use or connection of unauthorized hardware components is prohibited;

- `cm-7.9_obj.c` (cm-7.9_smt.c): the list of authorized hardware components is reviewed and updated [PARAM cm-07.09_odp.02].

#### EXAMINE — `cm-7.9_asm-examine`

- Configuration management policy

- network connection policy and procedures

- configuration management plan

- system security plan

- system design documentation

- system component inventory

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-7.9_asm-interview`

- Organizational personnel with system hardware management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `cm-7.9_asm-test`

- Organizational process for approving execution of binary or machine-executable code

- mechanisms supporting and/or implementing the prohibition of binary or machine-executable code

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-7.9`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
