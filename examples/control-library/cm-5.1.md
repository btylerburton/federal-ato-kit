---
title: "CM-5.1 \u2014 Automated Access Enforcement and Audit Records"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-5.1 — Automated Access Enforcement and Audit Records

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations log system accesses associated with applying configuration changes to ensure that configuration change control is implemented and to support after-the-fact actions should organizations discover any unauthorized changes.

### Requirements and exact statement parts

- `cm-5.1_smt`: Statement grouping; see child parts.

- `cm-5.1_smt.a`: Enforce access restrictions using [PARAM cm-05.01_odp] ; and

- `cm-5.1_smt.b`: Automatically generate audit records of the enforcement actions.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-5.1_smt.a — Enforce access restrictions using [PARAM cm-05.01_odp] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-5.1_smt.b — Automatically generate audit records of the enforcement actions.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-05.01_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-5.1_smt.a` — For “Enforce access restrictions using [PARAM cm-05.01_odp] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-5.1_smt.b` — For “Automatically generate audit records of the enforcement actions.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-05.01_odp` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: mechanisms used to automate the enforcement of access restrictions are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-5.1_obj.a` (cm-5.1_smt.a): access restrictions for change are enforced using [PARAM cm-05.01_odp];

- `cm-5.1_obj.b` (cm-5.1_smt.b): audit records of enforcement actions are automatically generated.

#### EXAMINE — `cm-5.1_asm-examine`

- Configuration management policy

- procedures addressing access restrictions for changes to the system

- system design documentation

- system architecture and configuration documentation

- system configuration settings and associated documentation

- change control records

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-5.1_asm-interview`

- Organizational personnel with logical access control responsibilities

- organizational personnel with physical access control responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `cm-5.1_asm-test`

- Organizational processes for managing access restrictions to change

- automated mechanisms implementing the enforcement of access restrictions for changes to the system

- automated mechanisms supporting auditing of enforcement actions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-5.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-5`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-7`.

- Catalog relationship **related**: `au-12`.

- Catalog relationship **related**: `cm-6`.

- Catalog relationship **related**: `cm-11`.

- Catalog relationship **related**: `si-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
