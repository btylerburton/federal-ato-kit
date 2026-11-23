---
title: "AC-3.12 \u2014 Assert and Enforce Application Access"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-3.12 — Assert and Enforce Application Access

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Asserting and enforcing application access is intended to address applications that need to access existing system applications and functions, including user contacts, global positioning systems, cameras, keyboards, microphones, networks, phones, or other files.

### Requirements and exact statement parts

- `ac-3.12_smt`: Statement grouping; see child parts.

- `ac-3.12_smt.a`: Require applications to assert, as part of the installation process, the access needed to the following system applications and functions: [PARAM ac-03.12_odp];

- `ac-3.12_smt.b`: Provide an enforcement mechanism to prevent unauthorized access; and

- `ac-3.12_smt.c`: Approve access changes after initial installation of the application.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-3.12_smt.a — Require applications to assert, as part of the installation process, the access needed to the following system applications and functions: [PARAM ac-03.12_odp];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.12_smt.b — Provide an enforcement mechanism to prevent unauthorized access; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.12_smt.c — Approve access changes after initial installation of the application.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-03.12_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-3.12_smt.a` — For “Require applications to assert, as part of the installation process, the access needed to the following system applications and functions: [PARAM ac-03.12_odp];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.12_smt.b` — For “Provide an enforcement mechanism to prevent unauthorized access; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.12_smt.c` — For “Approve access changes after initial installation of the application.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-03.12_odp` — What approved value applies to **system applications and functions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system applications and functions requiring access assertion are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-3.12_obj.a` (ac-3.12_smt.a): as part of the installation process, applications are required to assert the access needed to the following system applications and functions: [PARAM ac-03.12_odp];

- `ac-3.12_obj.b` (ac-3.12_smt.b): an enforcement mechanism to prevent unauthorized access is provided;

- `ac-3.12_obj.c` (ac-3.12_smt.c): access changes after initial installation of the application are approved.

#### EXAMINE — `ac-3.12_asm-examine`

- Access control policy

- procedures addressing access enforcement

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-3.12_asm-interview`

- Organizational personnel with access enforcement responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

#### TEST — `ac-3.12_asm-test`

- Mechanisms implementing access enforcement functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-3.12`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-3`.

- Catalog relationship **related**: `cm-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
