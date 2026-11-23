---
title: "CM-7.4 \u2014 Unauthorized Software \u2014 Deny-by-exception"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-7.4 — Unauthorized Software — Deny-by-exception

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Unauthorized software programs can be limited to specific versions or from a specific source. The concept of prohibiting the execution of unauthorized software may also be applied to user actions, system ports and protocols, IP addresses/ranges, websites, and MAC addresses.

### Requirements and exact statement parts

- `cm-7.4_smt`: Statement grouping; see child parts.

- `cm-7.4_smt.a`: Identify [PARAM cm-07.04_odp.01];

- `cm-7.4_smt.b`: Employ an allow-all, deny-by-exception policy to prohibit the execution of unauthorized software programs on the system; and

- `cm-7.4_smt.c`: Review and update the list of unauthorized software programs [PARAM cm-07.04_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-7.4_smt.a — Identify [PARAM cm-07.04_odp.01];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-7.4_smt.b — Employ an allow-all, deny-by-exception policy to prohibit the execution of unauthorized software programs on the system; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-7.4_smt.c — Review and update the list of unauthorized software programs [PARAM cm-07.04_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-07.04_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-07.04_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-7.4_smt.a` — For “Identify [PARAM cm-07.04_odp.01];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-7.4_smt.b` — For “Employ an allow-all, deny-by-exception policy to prohibit the execution of unauthorized software programs on the system; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-7.4_smt.c` — For “Review and update the list of unauthorized software programs [PARAM cm-07.04_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-07.04_odp.01` — What approved value applies to **software programs**? Record the value, scope, approving authority, and decision source.

  - Catalog context: software programs not authorized to execute on the system are defined;

- `cm-07.04_odp.02` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to review and update the list of unauthorized software programs is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-7.4_obj.a` (cm-7.4_smt.a): [PARAM cm-07.04_odp.01] are identified;

- `cm-7.4_obj.b` (cm-7.4_smt.b): an allow-all, deny-by-exception policy is employed to prohibit the execution of unauthorized software programs on the system;

- `cm-7.4_obj.c` (cm-7.4_smt.c): the list of unauthorized software programs is reviewed and updated [PARAM cm-07.04_odp.02].

#### EXAMINE — `cm-7.4_asm-examine`

- Configuration management policy

- procedures addressing least functionality in the system

- configuration management plan

- system design documentation

- system configuration settings and associated documentation

- list of software programs not authorized to execute on the system

- system component inventory

- common secure configuration checklists

- review and update records associated with list of unauthorized software programs

- change control records

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-7.4_asm-interview`

- Organizational personnel with responsibilities for identifying software not authorized to execute on the system

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `cm-7.4_asm-test`

- Organizational process for identifying, reviewing, and updating programs not authorized to execute on the system

- organizational process for implementing unauthorized software policy

- mechanisms supporting and/or implementing unauthorized software policy

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-7.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-7`.

- Catalog relationship **related**: `cm-6`.

- Catalog relationship **related**: `cm-8`.

- Catalog relationship **related**: `cm-10`.

- Catalog relationship **related**: `pl-9`.

- Catalog relationship **related**: `pm-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
