---
title: "PS-4.2 \u2014 Automated Actions"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PS-4.2 — Automated Actions

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

In organizations with many employees, not all personnel who need to know about termination actions receive the appropriate notifications, or if such notifications are received, they may not occur in a timely manner. Automated mechanisms can be used to send automatic alerts or notifications to organizational personnel or roles when individuals are terminated. Such automatic alerts or notifications can be conveyed in a variety of ways, including via telephone, electronic mail, text message, or websites. Automated mechanisms can also be employed to quickly and thoroughly disable access to system resources after an employee is terminated.

### Requirements and exact statement parts

- `ps-4.2_smt`: Use [PARAM ps-04.02_odp.01] to [PARAM ps-04.02_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ps-4.2_smt — Use [PARAM ps-04.02_odp.01] to [PARAM ps-04.02_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ps-04.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ps-04.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ps-04.02_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ps-4.2_smt` — For “Use [PARAM ps-04.02_odp.01] to [PARAM ps-04.02_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ps-04.02_odp.01` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms to notify personnel or roles of individual termination actions and/or to disable access to system resources are defined;

- `ps-04.02_odp.02` — What approved value applies to **selection; choose one-or-more from: notify [PARAM ps-04.02_odp.03] of individual termination actions; disable access to system resources**? Record the value, scope, approving authority, and decision source.

- `ps-04.02_odp.03` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to be notified upon termination of an individual is/are defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ps-4.2_obj` (ps-4.2_smt): [PARAM ps-04.02_odp.01] are used to [PARAM ps-04.02_odp.02].

#### EXAMINE — `ps-4.2_asm-examine`

- Personnel security policy

- procedures addressing personnel termination

- system design documentation

- system configuration settings and associated documentation

- records of personnel termination actions

- automated notifications of employee terminations

- system security plan

- other relevant documents or records

#### INTERVIEW — `ps-4.2_asm-interview`

- Organizational personnel with personnel security responsibilities

- organizational personnel with information security responsibilities

#### TEST — `ps-4.2_asm-test`

- Organizational processes for personnel termination

- automated mechanisms supporting and/or implementing personnel termination notifications

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ps-4.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ps-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
