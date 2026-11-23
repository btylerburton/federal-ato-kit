---
title: "AC-6.7 \u2014 Review of User Privileges"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-6.7 — Review of User Privileges

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The need for certain assigned user privileges may change over time to reflect changes in organizational mission and business functions, environments of operation, technologies, or threats. A periodic review of assigned user privileges is necessary to determine if the rationale for assigning such privileges remains valid. If the need cannot be revalidated, organizations take appropriate corrective actions.

### Requirements and exact statement parts

- `ac-6.7_smt`: Statement grouping; see child parts.

- `ac-6.7_smt.a`: Review [PARAM ac-06.07_odp.01] the privileges assigned to [PARAM ac-06.07_odp.02] to validate the need for such privileges; and

- `ac-6.7_smt.b`: Reassign or remove privileges, if necessary, to correctly reflect organizational mission and business needs.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-6.7_smt.a — Review [PARAM ac-06.07_odp.01] the privileges assigned to [PARAM ac-06.07_odp.02] to validate the need for such privileges; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-6.7_smt.b — Reassign or remove privileges, if necessary, to correctly reflect organizational mission and business needs.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-06.07_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-06.07_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-6.7_smt.a` — For “Review [PARAM ac-06.07_odp.01] the privileges assigned to [PARAM ac-06.07_odp.02] to validate the need for such privileges; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-6.7_smt.b` — For “Reassign or remove privileges, if necessary, to correctly reflect organizational mission and business needs.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-06.07_odp.01` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which to review the privileges assigned to roles or classes of users is defined;

- `ac-06.07_odp.02` — What approved value applies to **roles and classes**? Record the value, scope, approving authority, and decision source.

  - Catalog context: roles or classes of users to which privileges are assigned are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-6.7_obj.a` (ac-6.7_smt.a): privileges assigned to [PARAM ac-06.07_odp.02] are reviewed [PARAM ac-06.07_odp.01] to validate the need for such privileges;

- `ac-6.7_obj.b` (ac-6.7_smt.b): privileges are reassigned or removed, if necessary, to correctly reflect organizational mission and business needs.

#### EXAMINE — `ac-6.7_asm-examine`

- Access control policy

- procedures addressing least privilege

- list of system-generated roles or classes of users and assigned privileges

- system design documentation

- system configuration settings and associated documentation

- validation reviews of privileges assigned to roles or classes or users

- records of privilege removals or reassignments for roles or classes of users

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-6.7_asm-interview`

- Organizational personnel with responsibilities for reviewing least privileges necessary to accomplish specified tasks

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ac-6.7_asm-test`

- Mechanisms implementing review of user privileges

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-6.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-6`.

- Catalog relationship **related**: `ca-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
