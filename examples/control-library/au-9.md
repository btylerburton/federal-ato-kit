---
title: "AU-9 \u2014 Protection of Audit Information"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-9 — Protection of Audit Information

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Audit information includes all information needed to successfully audit system activity, such as audit records, audit log settings, audit reports, and personally identifiable information. Audit logging tools are those programs and devices used to conduct system audit and logging activities. Protection of audit information focuses on technical protection and limits the ability to access and execute audit logging tools to authorized individuals. Physical protection of audit information is addressed by both media protection controls and physical and environmental protection controls.

### Requirements and exact statement parts

- `au-9_smt`: Statement grouping; see child parts.

- `au-9_smt.a`: Protect audit information and audit logging tools from unauthorized access, modification, and deletion; and

- `au-9_smt.b`: Alert [PARAM au-09_odp] upon detection of unauthorized access, modification, or deletion of audit information.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-9_smt.a — Protect audit information and audit logging tools from unauthorized access, modification, and deletion; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for au-9_smt.b — Alert [PARAM au-09_odp] upon detection of unauthorized access, modification, or deletion of audit information.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-09_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-9_smt.a` — For “Protect audit information and audit logging tools from unauthorized access, modification, and deletion; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `au-9_smt.b` — For “Alert [PARAM au-09_odp] upon detection of unauthorized access, modification, or deletion of audit information.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-09_odp` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to be alerted upon detection of unauthorized access, modification, or deletion of audit information is/are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-9_obj.a` (au-9_smt.a): audit information and audit logging tools are protected from unauthorized access, modification, and deletion;

- `au-9_obj.b` (au-9_smt.b): [PARAM au-09_odp] are alerted upon detection of unauthorized access, modification, or deletion of audit information.

#### EXAMINE — `au-9_asm-examine`

- Audit and accountability policy

- system security plan

- privacy plan

- access control policy and procedures

- procedures addressing protection of audit information

- system design documentation

- system configuration settings and associated documentation

- system audit records

- audit tools

- other relevant documents or records

#### INTERVIEW — `au-9_asm-interview`

- Organizational personnel with audit and accountability responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

- system developers

#### TEST — `au-9_asm-test`

- Mechanisms implementing audit information protection

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-9`. The library index records the exact source revision and hash.

- [FIPS 140-3](https://doi.org/10.6028/NIST.FIPS.140-3)

- [FIPS 180-4](https://doi.org/10.6028/NIST.FIPS.180-4)

- [FIPS 202](https://doi.org/10.6028/NIST.FIPS.202)

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-6`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-11`.

- Catalog relationship **related**: `au-14`.

- Catalog relationship **related**: `au-15`.

- Catalog relationship **related**: `mp-2`.

- Catalog relationship **related**: `mp-4`.

- Catalog relationship **related**: `pe-2`.

- Catalog relationship **related**: `pe-3`.

- Catalog relationship **related**: `pe-6`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sc-8`.

- Catalog relationship **related**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
