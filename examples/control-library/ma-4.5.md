---
title: "MA-4.5 \u2014 Approvals and Notifications"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-4.5 — Approvals and Notifications

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Notification may be performed by maintenance personnel. Approval of nonlocal maintenance is accomplished by personnel with sufficient information security and system knowledge to determine the appropriateness of the proposed maintenance.

### Requirements and exact statement parts

- `ma-4.5_smt`: Statement grouping; see child parts.

- `ma-4.5_smt.a`: Require the approval of each nonlocal maintenance session by [PARAM ma-04.05_odp.01] ; and

- `ma-4.5_smt.b`: Notify the following personnel or roles of the date and time of planned nonlocal maintenance: [PARAM ma-04.05_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-4.5_smt.a — Require the approval of each nonlocal maintenance session by [PARAM ma-04.05_odp.01] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-4.5_smt.b — Notify the following personnel or roles of the date and time of planned nonlocal maintenance: [PARAM ma-04.05_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ma-04.05_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ma-04.05_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ma-4.5_smt.a` — For “Require the approval of each nonlocal maintenance session by [PARAM ma-04.05_odp.01] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-4.5_smt.b` — For “Notify the following personnel or roles of the date and time of planned nonlocal maintenance: [PARAM ma-04.05_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ma-04.05_odp.01` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles required to approve each nonlocal maintenance session is/are defined;

- `ma-04.05_odp.02` — What approved value applies to **personnel and roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel and roles to be notified of the date and time of planned nonlocal maintenance is/are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-4.5_obj.a` (ma-4.5_smt.a): the approval of each nonlocal maintenance session is required by [PARAM ma-04.05_odp.01];

- `ma-4.5_obj.b` (ma-4.5_smt.b): [PARAM ma-04.05_odp.02] is/are notified of the date and time of planned nonlocal maintenance.

#### EXAMINE — `ma-4.5_asm-examine`

- Maintenance policy

- procedures addressing nonlocal system maintenance

- notifications supporting nonlocal maintenance sessions

- maintenance records

- audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-4.5_asm-interview`

- Organizational personnel with system maintenance responsibilities

- organizational personnel with notification responsibilities

- organizational personnel with approval responsibilities

- organizational personnel with information security responsibilities

#### TEST — `ma-4.5_asm-test`

- Organizational processes for approving and notifying personnel regarding nonlocal maintenance

- mechanisms supporting the notification and approval of nonlocal maintenance

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-4.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ma-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
