---
title: "CM-7.5 \u2014 Authorized Software \u2014 Allow-by-exception"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-7.5 — Authorized Software — Allow-by-exception

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Authorized software programs can be limited to specific versions or from a specific source. To facilitate a comprehensive authorized software process and increase the strength of protection for attacks that bypass application level authorized software, software programs may be decomposed into and monitored at different levels of detail. These levels include applications, application programming interfaces, application modules, scripts, system processes, system services, kernel functions, registries, drivers, and dynamic link libraries. The concept of permitting the execution of authorized software may also be applied to user actions, system ports and protocols, IP addresses/ranges, websites, and MAC addresses. Organizations consider verifying the integrity of authorized software programs using digital signatures, cryptographic checksums, or hash functions. Verification of authorized software can occur either prior to execution or at system startup. The identification of authorized URLs for websites is addressed in CA-3(5) (catalog reference: `#ca-3.5`) and SC-7 (catalog reference: `#sc-7`).

### Requirements and exact statement parts

- `cm-7.5_smt`: Statement grouping; see child parts.

- `cm-7.5_smt.a`: Identify [PARAM cm-07.05_odp.01];

- `cm-7.5_smt.b`: Employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs on the system; and

- `cm-7.5_smt.c`: Review and update the list of authorized software programs [PARAM cm-07.05_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-7.5_smt.a — Identify [PARAM cm-07.05_odp.01];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-7.5_smt.b — Employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs on the system; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-7.5_smt.c — Review and update the list of authorized software programs [PARAM cm-07.05_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-07.05_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-07.05_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-7.5_smt.a` — For “Identify [PARAM cm-07.05_odp.01];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-7.5_smt.b` — For “Employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs on the system; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-7.5_smt.c` — For “Review and update the list of authorized software programs [PARAM cm-07.05_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-07.05_odp.01` — What approved value applies to **software programs**? Record the value, scope, approving authority, and decision source.

  - Catalog context: software programs authorized to execute on the system are defined;

- `cm-07.05_odp.02` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to review and update the list of authorized software programs is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-7.5_obj.a` (cm-7.5_smt.a): [PARAM cm-07.05_odp.01] are identified;

- `cm-7.5_obj.b` (cm-7.5_smt.b): a deny-all, permit-by-exception policy to allow the execution of authorized software programs on the system is employed;

- `cm-7.5_obj.c` (cm-7.5_smt.c): the list of authorized software programs is reviewed and updated [PARAM cm-07.05_odp.02].

#### EXAMINE — `cm-7.5_asm-examine`

- Configuration management policy

- procedures addressing least functionality in the system

- configuration management plan

- system design documentation

- system configuration settings and associated documentation

- list of software programs authorized to execute on the system

- system component inventory

- common secure configuration checklists

- review and update records associated with list of authorized software programs

- change control records

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-7.5_asm-interview`

- Organizational personnel with responsibilities for identifying software authorized to execute on the system

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `cm-7.5_asm-test`

- Organizational process for identifying, reviewing, and updating programs authorized to execute on the system

- organizational process for implementing authorized software policy

- mechanisms supporting and/or implementing authorized software policy

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-7.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-7`.

- Catalog relationship **related**: `cm-2`.

- Catalog relationship **related**: `cm-6`.

- Catalog relationship **related**: `cm-8`.

- Catalog relationship **related**: `cm-10`.

- Catalog relationship **related**: `pl-9`.

- Catalog relationship **related**: `pm-5`.

- Catalog relationship **related**: `sa-10`.

- Catalog relationship **related**: `sc-34`.

- Catalog relationship **related**: `si-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
