---
title: "CM-3.6 \u2014 Cryptography Management"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-3.6 — Cryptography Management

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The controls referenced in the control enhancement refer to security and privacy controls from the control catalog. Regardless of the cryptographic mechanisms employed, processes and procedures are in place to manage those mechanisms. For example, if system components use certificates for identification and authentication, a process is implemented to address the expiration of those certificates.

### Requirements and exact statement parts

- `cm-3.6_smt`: Ensure that cryptographic mechanisms used to provide the following controls are under configuration management: [PARAM cm-03.06_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-3.6_smt — Ensure that cryptographic mechanisms used to provide the following controls are under configuration management: [PARAM cm-03.06_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-03.06_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-3.6_smt` — For “Ensure that cryptographic mechanisms used to provide the following controls are under configuration management: [PARAM cm-03.06_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-03.06_odp` — What approved value applies to **controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controls provided by cryptographic mechanisms that are to be under configuration management are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-3.6_obj` (cm-3.6_smt): cryptographic mechanisms used to provide [PARAM cm-03.06_odp] are under configuration management.

#### EXAMINE — `cm-3.6_asm-examine`

- Configuration management policy

- procedures addressing system configuration change control

- configuration management plan

- system design documentation

- system architecture and configuration documentation

- system configuration settings and associated documentation

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-3.6_asm-interview`

- Organizational personnel with configuration change control responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

- members of change control board or similar

#### TEST — `cm-3.6_asm-test`

- Organizational processes for configuration change control

- cryptographic mechanisms implementing organizational security safeguards (controls)

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-3.6`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-3`.

- Catalog relationship **related**: `sc-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
