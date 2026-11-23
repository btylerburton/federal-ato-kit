---
title: "CP-9.8 \u2014 Cryptographic Protection"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-9.8 — Cryptographic Protection

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The selection of cryptographic mechanisms is based on the need to protect the confidentiality and integrity of backup information. The strength of mechanisms selected is commensurate with the security category or classification of the information. Cryptographic protection applies to system backup information in storage at both primary and alternate locations. Organizations that implement cryptographic mechanisms to protect information at rest also consider cryptographic key management solutions.

### Requirements and exact statement parts

- `cp-9.8_smt`: Implement cryptographic mechanisms to prevent unauthorized disclosure and modification of [PARAM cp-09.08_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-9.8_smt — Implement cryptographic mechanisms to prevent unauthorized disclosure and modification of [PARAM cp-09.08_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cp-09.08_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cp-9.8_smt` — For “Implement cryptographic mechanisms to prevent unauthorized disclosure and modification of [PARAM cp-09.08_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cp-09.08_odp` — What approved value applies to **backup information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: backup information to protect against unauthorized disclosure and modification is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-9.8_obj` (cp-9.8_smt): cryptographic mechanisms are implemented to prevent unauthorized disclosure and modification of [PARAM cp-09.08_odp].

#### EXAMINE — `cp-9.8_asm-examine`

- Contingency planning policy

- procedures addressing system backup

- contingency plan

- system design documentation

- system configuration settings and associated documentation

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-9.8_asm-interview`

- Organizational personnel with system backup responsibilities

- organizational personnel with information security responsibilities

#### TEST — `cp-9.8_asm-test`

- Mechanisms supporting and/or implementing cryptographic protection of backup information

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-9.8`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cp-9`.

- Catalog relationship **related**: `sc-12`.

- Catalog relationship **related**: `sc-13`.

- Catalog relationship **related**: `sc-28`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
