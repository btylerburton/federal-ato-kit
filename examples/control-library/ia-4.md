---
title: "IA-4 \u2014 Identifier Management"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-4 — Identifier Management

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Common device identifiers include Media Access Control (MAC) addresses, Internet Protocol (IP) addresses, or device-unique token identifiers. The management of individual identifiers is not applicable to shared system accounts. Typically, individual identifiers are the usernames of the system accounts assigned to those individuals. In such instances, the account management activities of AC-2 (catalog reference: `#ac-2`) use account names provided by IA-4 (catalog reference: `#ia-4`) . Identifier management also addresses individual identifiers not necessarily associated with system accounts. Preventing the reuse of identifiers implies preventing the assignment of previously used individual, group, role, service, or device identifiers to different individuals, groups, roles, services, or devices.

### Requirements and exact statement parts

- `ia-4_smt`: Manage system identifiers by:

- `ia-4_smt.a`: Receiving authorization from [PARAM ia-04_odp.01] to assign an individual, group, role, service, or device identifier;

- `ia-4_smt.b`: Selecting an identifier that identifies an individual, group, role, service, or device;

- `ia-4_smt.c`: Assigning the identifier to the intended individual, group, role, service, or device; and

- `ia-4_smt.d`: Preventing reuse of identifiers for [PARAM ia-04_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-4_smt — Manage system identifiers by:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-4_smt.a — Receiving authorization from [PARAM ia-04_odp.01] to assign an individual, group, role, service, or device identifier;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-4_smt.b — Selecting an identifier that identifies an individual, group, role, service, or device;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-4_smt.c — Assigning the identifier to the intended individual, group, role, service, or device; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-4_smt.d — Preventing reuse of identifiers for [PARAM ia-04_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ia-04_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ia-04_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ia-4_smt` — For “Manage system identifiers by:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-4_smt.a` — For “Receiving authorization from [PARAM ia-04_odp.01] to assign an individual, group, role, service, or device identifier;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-4_smt.b` — For “Selecting an identifier that identifies an individual, group, role, service, or device;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-4_smt.c` — For “Assigning the identifier to the intended individual, group, role, service, or device; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-4_smt.d` — For “Preventing reuse of identifiers for [PARAM ia-04_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ia-04_odp.01` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles from whom authorization must be received to assign an identifier are defined;

- `ia-04_odp.02` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: a time period for preventing reuse of identifiers is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-4_obj.a` (ia-4_smt.a): system identifiers are managed by receiving authorization from [PARAM ia-04_odp.01] to assign to an individual, group, role, or device identifier;

- `ia-4_obj.b` (ia-4_smt.b): system identifiers are managed by selecting an identifier that identifies an individual, group, role, service, or device;

- `ia-4_obj.c` (ia-4_smt.c): system identifiers are managed by assigning the identifier to the intended individual, group, role, service, or device;

- `ia-4_obj.d` (ia-4_smt.d): system identifiers are managed by preventing reuse of identifiers for [PARAM ia-04_odp.02].

#### EXAMINE — `ia-4_asm-examine`

- Identification and authentication policy

- procedures addressing identifier management

- procedures addressing account management

- system security plan

- system design documentation

- system configuration settings and associated documentation

- list of system accounts

- list of identifiers generated from physical access control devices

- other relevant documents or records

#### INTERVIEW — `ia-4_asm-interview`

- Organizational personnel with identifier management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `ia-4_asm-test`

- Mechanisms supporting and/or implementing identifier management

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-4`. The library index records the exact source revision and hash.

- [FIPS 201-2](https://doi.org/10.6028/NIST.FIPS.201-2)

- [SP 800-63-3](https://doi.org/10.6028/NIST.SP.800-63-3)

- [SP 800-73-4](https://doi.org/10.6028/NIST.SP.800-73-4)

- [SP 800-76-2](https://doi.org/10.6028/NIST.SP.800-76-2)

- [SP 800-78-4](https://doi.org/10.6028/NIST.SP.800-78-4)

- Catalog relationship **related**: `ac-5`.

- Catalog relationship **related**: `ia-2`.

- Catalog relationship **related**: `ia-3`.

- Catalog relationship **related**: `ia-5`.

- Catalog relationship **related**: `ia-8`.

- Catalog relationship **related**: `ia-9`.

- Catalog relationship **related**: `ia-12`.

- Catalog relationship **related**: `ma-4`.

- Catalog relationship **related**: `pe-2`.

- Catalog relationship **related**: `pe-3`.

- Catalog relationship **related**: `pe-4`.

- Catalog relationship **related**: `pl-4`.

- Catalog relationship **related**: `pm-12`.

- Catalog relationship **related**: `ps-3`.

- Catalog relationship **related**: `ps-4`.

- Catalog relationship **related**: `ps-5`.

- Catalog relationship **related**: `sc-37`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
