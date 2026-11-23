---
title: "AC-3.11 \u2014 Restrict Access to Specific Information Types"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-3.11 — Restrict Access to Specific Information Types

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Restricting access to specific information is intended to provide flexibility regarding access control of specific information types within a system. For example, role-based access could be employed to allow access to only a specific type of personally identifiable information within a database rather than allowing access to the database in its entirety. Other examples include restricting access to cryptographic keys, authentication information, and selected system information.

### Requirements and exact statement parts

- `ac-3.11_smt`: Restrict access to data repositories containing [PARAM ac-03.11_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-3.11_smt — Restrict access to data repositories containing [PARAM ac-03.11_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-03.11_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-3.11_smt` — For “Restrict access to data repositories containing [PARAM ac-03.11_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-03.11_odp` — What approved value applies to **information types**? Record the value, scope, approving authority, and decision source.

  - Catalog context: information types requiring restricted access to data repositories are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-3.11_obj` (ac-3.11_smt): access to data repositories containing [PARAM ac-03.11_odp] is restricted.

#### EXAMINE — `ac-3.11_asm-examine`

- Access control policy

- procedures addressing access enforcement

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-3.11_asm-interview`

- Organizational personnel with access enforcement responsibilities

- organizational personnel with responsibilities for data repositories

- system/network administrators

- organizational personnel with information security responsibilities

#### TEST — `ac-3.11_asm-test`

- Mechanisms implementing access enforcement functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-3.11`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-3`.

- Catalog relationship **related**: `cm-8`.

- Catalog relationship **related**: `cm-12`.

- Catalog relationship **related**: `cm-13`.

- Catalog relationship **related**: `pm-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
