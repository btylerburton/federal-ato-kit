---
title: "IA-5.16 \u2014 In-person or Trusted External Party Authenticator Issuance"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-5.16 — In-person or Trusted External Party Authenticator Issuance

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Issuing authenticators in person or by a trusted external party enhances and reinforces the trustworthiness of the identity proofing process.

### Requirements and exact statement parts

- `ia-5.16_smt`: Require that the issuance of [PARAM ia-05.16_odp.01] be conducted [PARAM ia-05.16_odp.02] before [PARAM ia-05.16_odp.03] with authorization by [PARAM ia-05.16_odp.04].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-5.16_smt — Require that the issuance of [PARAM ia-05.16_odp.01] be conducted [PARAM ia-05.16_odp.02] before [PARAM ia-05.16_odp.03] with authorization by [PARAM ia-05.16_odp.04].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ia-05.16_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ia-05.16_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ia-05.16_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ia-05.16_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ia-5.16_smt` — For “Require that the issuance of [PARAM ia-05.16_odp.01] be conducted [PARAM ia-05.16_odp.02] before [PARAM ia-05.16_odp.03] with authorization by [PARAM ia-05.16_odp.04].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ia-05.16_odp.01` — What approved value applies to **types of and/or specific authenticators**? Record the value, scope, approving authority, and decision source.

  - Catalog context: types of and/or specific authenticators to be issued are defined;

- `ia-05.16_odp.02` — What approved value applies to **selection; choose one from: in person; by a trusted external party**? Record the value, scope, approving authority, and decision source.

- `ia-05.16_odp.03` — What approved value applies to **registration authority**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the registration authority that issues authenticators is defined;

- `ia-05.16_odp.04` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the personnel or roles who authorize the issuance of authenticators are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-5.16_obj` (ia-5.16_smt): the issuance of [PARAM ia-05.16_odp.01] is required to be conducted [PARAM ia-05.16_odp.02] before [PARAM ia-05.16_odp.03] with authorization by [PARAM ia-05.16_odp.04].

#### EXAMINE — `ia-5.16_asm-examine`

- Identification and authentication policy

- procedures addressing identifier management

- system security plan

- system design documentation

- mechanisms providing dynamic binding of identifiers and authenticators

- system configuration settings and associated documentation

- system audit records

- other relevant documents or records

#### INTERVIEW — `ia-5.16_asm-interview`

- Organizational personnel with identification and authentication management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ia-5.16_asm-test`

- Mechanisms supporting and/or implementing account management capability

- mechanisms supporting and/or implementing identification and authentication management capabilities for the system

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-5.16`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-5`.

- Catalog relationship **related**: `ia-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
