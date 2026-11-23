---
title: "AC-4.4 \u2014 Flow Control of Encrypted Information"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4.4 — Flow Control of Encrypted Information

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Flow control mechanisms include content checking, security policy filters, and data type identifiers. The term encryption is extended to cover encoded data not recognized by filtering mechanisms.

### Requirements and exact statement parts

- `ac-4.4_smt`: Prevent encrypted information from bypassing [PARAM ac-04.04_odp.01] by [PARAM ac-04.04_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4.4_smt — Prevent encrypted information from bypassing [PARAM ac-04.04_odp.01] by [PARAM ac-04.04_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-04.04_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.04_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.04_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-4.4_smt` — For “Prevent encrypted information from bypassing [PARAM ac-04.04_odp.01] by [PARAM ac-04.04_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-04.04_odp.01` — What approved value applies to **information flow control mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: information flow control mechanisms that encrypted information is prevented from bypassing are defined;

- `ac-04.04_odp.02` — What approved value applies to **selection; choose one-or-more from: decrypting the information; blocking the flow of the encrypted information; terminating communications sessions attempting to pass encrypted information; [PARAM ac-04.04_odp.03]**? Record the value, scope, approving authority, and decision source.

- `ac-04.04_odp.03` — What approved value applies to **organization-defined procedure or method**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the organization-defined procedure or method used to prevent encrypted information from bypassing information flow control mechanisms is defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4.4_obj` (ac-4.4_smt): encrypted information is prevented from bypassing [PARAM ac-04.04_odp.01] by [PARAM ac-04.04_odp.02].

#### EXAMINE — `ac-4.4_asm-examine`

- Access control policy

- information flow control policies

- procedures addressing information flow enforcement

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-4.4_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developers

#### TEST — `ac-4.4_asm-test`

- Mechanisms implementing information flow enforcement policy

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-4`.

- Catalog relationship **related**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
