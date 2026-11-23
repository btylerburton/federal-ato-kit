---
title: "AU-5 \u2014 Response to Audit Logging Process Failures"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-5 — Response to Audit Logging Process Failures

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Audit logging process failures include software and hardware errors, failures in audit log capturing mechanisms, and reaching or exceeding audit log storage capacity. Organization-defined actions include overwriting oldest audit records, shutting down the system, and stopping the generation of audit records. Organizations may choose to define additional actions for audit logging process failures based on the type of failure, the location of the failure, the severity of the failure, or a combination of such factors. When the audit logging process failure is related to storage, the response is carried out for the audit log storage repository (i.e., the distinct system component where the audit logs are stored), the system on which the audit logs reside, the total audit log storage capacity of the organization (i.e., all audit log storage repositories combined), or all three. Organizations may decide to take no additional actions after alerting designated roles or personnel.

### Requirements and exact statement parts

- `au-5_smt`: Statement grouping; see child parts.

- `au-5_smt.a`: Alert [PARAM au-05_odp.01] within [PARAM au-05_odp.02] in the event of an audit logging process failure; and

- `au-5_smt.b`: Take the following additional actions: [PARAM au-05_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-5_smt.a — Alert [PARAM au-05_odp.01] within [PARAM au-05_odp.02] in the event of an audit logging process failure; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for au-5_smt.b — Take the following additional actions: [PARAM au-05_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-05_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter au-05_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter au-05_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-5_smt.a` — For “Alert [PARAM au-05_odp.01] within [PARAM au-05_odp.02] in the event of an audit logging process failure; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `au-5_smt.b` — For “Take the following additional actions: [PARAM au-05_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-05_odp.01` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles receiving audit logging process failure alerts are defined;

- `au-05_odp.02` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period for personnel or roles receiving audit logging process failure alerts is defined;

- `au-05_odp.03` — What approved value applies to **additional actions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: additional actions to be taken in the event of an audit logging process failure are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-5_obj.a` (au-5_smt.a): [PARAM au-05_odp.01] are alerted in the event of an audit logging process failure within [PARAM au-05_odp.02];

- `au-5_obj.b` (au-5_smt.b): [PARAM au-05_odp.03] are taken in the event of an audit logging process failure.

#### EXAMINE — `au-5_asm-examine`

- Audit and accountability policy

- procedures addressing response to audit processing failures

- system design documentation

- system security plan

- privacy plan

- system configuration settings and associated documentation

- list of personnel to be notified in case of an audit processing failure

- system audit records

- other relevant documents or records

#### INTERVIEW — `au-5_asm-interview`

- Organizational personnel with audit and accountability responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

- system developers

#### TEST — `au-5_asm-test`

- Mechanisms implementing system response to audit processing failures

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-5`. The library index records the exact source revision and hash.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-4`.

- Catalog relationship **related**: `au-7`.

- Catalog relationship **related**: `au-9`.

- Catalog relationship **related**: `au-11`.

- Catalog relationship **related**: `au-12`.

- Catalog relationship **related**: `au-14`.

- Catalog relationship **related**: `si-4`.

- Catalog relationship **related**: `si-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
