---
title: "AC-7.4 \u2014 Use of Alternate Authentication Factor"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-7.4 — Use of Alternate Authentication Factor

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The use of alternate authentication factors supports the objective of availability and allows a user who has inadvertently been locked out to use additional authentication factors to bypass the lockout.

### Requirements and exact statement parts

- `ac-7.4_smt`: Statement grouping; see child parts.

- `ac-7.4_smt.a`: Allow the use of [PARAM ac-07.04_odp.01] that are different from the primary authentication factors after the number of organization-defined consecutive invalid logon attempts have been exceeded; and

- `ac-7.4_smt.b`: Enforce a limit of [PARAM ac-07.04_odp.02] consecutive invalid logon attempts through use of the alternative factors by a user during a [PARAM ac-07.04_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-7.4_smt.a — Allow the use of [PARAM ac-07.04_odp.01] that are different from the primary authentication factors after the number of organization-defined consecutive invalid logon attempts have been exceeded; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-7.4_smt.b — Enforce a limit of [PARAM ac-07.04_odp.02] consecutive invalid logon attempts through use of the alternative factors by a user during a [PARAM ac-07.04_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-07.04_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-07.04_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-07.04_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-7.4_smt.a` — For “Allow the use of [PARAM ac-07.04_odp.01] that are different from the primary authentication factors after the number of organization-defined consecutive invalid logon attempts have been exceeded; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-7.4_smt.b` — For “Enforce a limit of [PARAM ac-07.04_odp.02] consecutive invalid logon attempts through use of the alternative factors by a user during a [PARAM ac-07.04_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-07.04_odp.01` — What approved value applies to **authentication factors**? Record the value, scope, approving authority, and decision source.

  - Catalog context: authentication factors allowed to be used that are different from the primary authentication factors are defined;

- `ac-07.04_odp.02` — What approved value applies to **number**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the number of consecutive, invalid logon attempts through the use of alternative factors for which to enforce a limit by a user is defined;

- `ac-07.04_odp.03` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period during which a user can attempt logons through alternative factors is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-7.4_obj.a` (ac-7.4_smt.a): [PARAM ac-07.04_odp.01] that are different from the primary authentication factors are allowed to be used after the number of organization-defined consecutive invalid logon attempts have been exceeded;

- `ac-7.4_obj.b` (ac-7.4_smt.b): a limit of [PARAM ac-07.04_odp.02] consecutive invalid logon attempts through the use of the alternative factors by the user during a [PARAM ac-07.04_odp.03] is enforced.

#### EXAMINE — `ac-7.4_asm-examine`

- Access control policy

- procedures addressing unsuccessful logon attempts for primary and alternate authentication factors

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-7.4_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

#### TEST — `ac-7.4_asm-test`

- Mechanisms implementing access control policy for unsuccessful logon attempts

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-7.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-7`.

- Catalog relationship **related**: `ia-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
