---
title: "CM-6.2 \u2014 Respond to Unauthorized Changes"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-6.2 — Respond to Unauthorized Changes

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Responses to unauthorized changes to configuration settings include alerting designated organizational personnel, restoring established configuration settings, or—in extreme cases—halting affected system processing.

### Requirements and exact statement parts

- `cm-6.2_smt`: Take the following actions in response to unauthorized changes to [PARAM cm-06.02_odp.02]: [PARAM cm-06.02_odp.01].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-6.2_smt — Take the following actions in response to unauthorized changes to [PARAM cm-06.02_odp.02]: [PARAM cm-06.02_odp.01].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-06.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-06.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-6.2_smt` — For “Take the following actions in response to unauthorized changes to [PARAM cm-06.02_odp.02]: [PARAM cm-06.02_odp.01].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-06.02_odp.01` — What approved value applies to **actions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: actions to be taken upon an unauthorized change are defined;

- `cm-06.02_odp.02` — What approved value applies to **configuration settings**? Record the value, scope, approving authority, and decision source.

  - Catalog context: configuration settings requiring action upon an unauthorized change are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-6.2_obj` (cm-6.2_smt): [PARAM cm-06.02_odp.01] are taken in response to unauthorized changes to [PARAM cm-06.02_odp.02].

#### EXAMINE — `cm-6.2_asm-examine`

- System security plan

- privacy plan

- configuration management policy

- procedures addressing configuration settings for the system

- configuration management plan

- system design documentation

- system configuration settings and associated documentation

- alerts/notifications of unauthorized changes to system configuration settings

- system component inventory

- documented responses to unauthorized changes to system configuration settings

- change control records

- system audit records

- other relevant documents or records

#### INTERVIEW — `cm-6.2_asm-interview`

- Organizational personnel with security configuration management responsibilities

- organizational personnel with security and privacy responsibilities

- system/network administrators

#### TEST — `cm-6.2_asm-test`

- Organizational process for responding to unauthorized changes to system configuration settings

- mechanisms supporting and/or implementing actions in response to unauthorized changes

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-6.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-6`.

- Catalog relationship **related**: `ir-4`.

- Catalog relationship **related**: `ir-6`.

- Catalog relationship **related**: `si-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
