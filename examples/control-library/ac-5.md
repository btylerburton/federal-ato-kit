---
title: "AC-5 \u2014 Separation of Duties"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-5 — Separation of Duties

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Separation of duties addresses the potential for abuse of authorized privileges and helps to reduce the risk of malevolent activity without collusion. Separation of duties includes dividing mission or business functions and support functions among different individuals or roles, conducting system support functions with different individuals, and ensuring that security personnel who administer access control functions do not also administer audit functions. Because separation of duty violations can span systems and application domains, organizations consider the entirety of systems and system components when developing policy on separation of duties. Separation of duties is enforced through the account management activities in AC-2 (catalog reference: `#ac-2`) , access control mechanisms in AC-3 (catalog reference: `#ac-3`) , and identity management activities in IA-2 (catalog reference: `#ia-2`), IA-4 (catalog reference: `#ia-4`) , and IA-12 (catalog reference: `#ia-12`).

### Requirements and exact statement parts

- `ac-5_smt`: Statement grouping; see child parts.

- `ac-5_smt.a`: Identify and document [PARAM ac-05_odp] ; and

- `ac-5_smt.b`: Define system access authorizations to support separation of duties.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-5_smt.a — Identify and document [PARAM ac-05_odp] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-5_smt.b — Define system access authorizations to support separation of duties.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-05_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-5_smt.a` — For “Identify and document [PARAM ac-05_odp] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-5_smt.b` — For “Define system access authorizations to support separation of duties.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-05_odp` — What approved value applies to **duties of individuals**? Record the value, scope, approving authority, and decision source.

  - Catalog context: duties of individuals requiring separation are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-5_obj.a` (ac-5_smt.a): [PARAM ac-05_odp] are identified and documented;

- `ac-5_obj.b` (ac-5_smt.b): system access authorizations to support separation of duties are defined.

#### EXAMINE — `ac-5_asm-examine`

- Access control policy

- procedures addressing divisions of responsibility and separation of duties

- system configuration settings and associated documentation

- list of divisions of responsibility and separation of duties

- system access authorizations

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-5_asm-interview`

- Organizational personnel with responsibilities for defining appropriate divisions of responsibility and separation of duties

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ac-5_asm-test`

- Mechanisms implementing separation of duties policy

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-5`. The library index records the exact source revision and hash.

- Catalog relationship **related**: `ac-2`.

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-6`.

- Catalog relationship **related**: `au-9`.

- Catalog relationship **related**: `cm-5`.

- Catalog relationship **related**: `cm-11`.

- Catalog relationship **related**: `cp-9`.

- Catalog relationship **related**: `ia-2`.

- Catalog relationship **related**: `ia-4`.

- Catalog relationship **related**: `ia-5`.

- Catalog relationship **related**: `ia-12`.

- Catalog relationship **related**: `ma-3`.

- Catalog relationship **related**: `ma-5`.

- Catalog relationship **related**: `ps-2`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sa-17`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
