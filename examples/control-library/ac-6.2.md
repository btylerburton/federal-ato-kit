---
title: "AC-6.2 \u2014 Non-privileged Access for Nonsecurity Functions"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-6.2 — Non-privileged Access for Nonsecurity Functions

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Requiring the use of non-privileged accounts when accessing nonsecurity functions limits exposure when operating from within privileged accounts or roles. The inclusion of roles addresses situations where organizations implement access control policies, such as role-based access control, and where a change of role provides the same degree of assurance in the change of access authorizations for the user and the processes acting on behalf of the user as would be provided by a change between a privileged and non-privileged account.

### Requirements and exact statement parts

- `ac-6.2_smt`: Require that users of system accounts (or roles) with access to [PARAM ac-06.02_odp] use non-privileged accounts or roles, when accessing nonsecurity functions.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-6.2_smt — Require that users of system accounts (or roles) with access to [PARAM ac-06.02_odp] use non-privileged accounts or roles, when accessing nonsecurity functions.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-06.02_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-6.2_smt` — For “Require that users of system accounts (or roles) with access to [PARAM ac-06.02_odp] use non-privileged accounts or roles, when accessing nonsecurity functions.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-06.02_odp` — What approved value applies to **security functions or security-relevant information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security functions or security-relevant information, the access to which requires users to use non-privileged accounts to access non-security functions, are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-6.2_obj` (ac-6.2_smt): users of system accounts (or roles) with access to [PARAM ac-06.02_odp] are required to use non-privileged accounts or roles when accessing non-security functions.

#### EXAMINE — `ac-6.2_asm-examine`

- Access control policy

- procedures addressing least privilege

- list of system-generated security functions or security-relevant information assigned to system accounts or roles

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-6.2_asm-interview`

- Organizational personnel with responsibilities for defining least privileges necessary to accomplish specified tasks

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ac-6.2_asm-test`

- Mechanisms implementing least privilege functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-6.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-6`.

- Catalog relationship **related**: `ac-17`.

- Catalog relationship **related**: `ac-18`.

- Catalog relationship **related**: `ac-19`.

- Catalog relationship **related**: `pl-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
