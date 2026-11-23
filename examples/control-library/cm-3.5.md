---
title: "CM-3.5 \u2014 Automated Security Response"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-3.5 — Automated Security Response

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Automated security responses include halting selected system functions, halting system processing, and issuing alerts or notifications to organizational personnel when there is an unauthorized modification of a configuration item.

### Requirements and exact statement parts

- `cm-3.5_smt`: Implement the following security responses automatically if baseline configurations are changed in an unauthorized manner: [PARAM cm-03.05_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-3.5_smt — Implement the following security responses automatically if baseline configurations are changed in an unauthorized manner: [PARAM cm-03.05_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-03.05_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-3.5_smt` — For “Implement the following security responses automatically if baseline configurations are changed in an unauthorized manner: [PARAM cm-03.05_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-03.05_odp` — What approved value applies to **security responses**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security responses to be automatically implemented are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-3.5_obj` (cm-3.5_smt): [PARAM cm-03.05_odp] are automatically implemented if baseline configurations are changed in an unauthorized manner.

#### EXAMINE — `cm-3.5_asm-examine`

- System security plan

- configuration management policy

- procedures addressing system configuration change control

- configuration management plan

- system design documentation

- system architecture and configuration documentation

- system configuration settings and associated documentation

- alerts/notifications of unauthorized baseline configuration changes

- system audit records

- other relevant documents or records

#### INTERVIEW — `cm-3.5_asm-interview`

- Organizational personnel with configuration change control responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

- members of change control board or similar

#### TEST — `cm-3.5_asm-test`

- Organizational processes for configuration change control

- automated mechanisms implementing security responses to unauthorized changes to the baseline configurations

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-3.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
