---
title: "SA-8.16 \u2014 Self-reliant Trustworthiness"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-8.16 — Self-reliant Trustworthiness

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The principle of self-reliant trustworthiness states that systems minimize their reliance on other systems for their own trustworthiness. A system is trustworthy by default, and any connection to an external entity is used to supplement its function. If a system were required to maintain a connection with another external entity in order to maintain its trustworthiness, then that system would be vulnerable to malicious and non-malicious threats that could result in the loss or degradation of that connection. The benefit of the principle of self-reliant trustworthiness is that the isolation of a system will make it less vulnerable to attack. A corollary to this principle relates to the ability of the system (or system component) to operate in isolation and then resynchronize with other components when it is rejoined with them.

### Requirements and exact statement parts

- `sa-8.16_smt`: Implement the security design principle of self-reliant trustworthiness in [PARAM sa-08.16_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-8.16_smt — Implement the security design principle of self-reliant trustworthiness in [PARAM sa-08.16_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sa-08.16_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sa-8.16_smt` — For “Implement the security design principle of self-reliant trustworthiness in [PARAM sa-08.16_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sa-08.16_odp` — What approved value applies to **systems or system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems or system components that implement the security design principle of self-reliant trustworthiness are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-8.16_obj` (sa-8.16_smt): [PARAM sa-08.16_odp] implement the security design principle of self-reliant trustworthiness.

#### EXAMINE — `sa-8.16_asm-examine`

- System and services acquisition policy

- procedures addressing the security design principle of self-reliant trustworthiness used in the specification, design, development, implementation, and modification of the system

- system design documentation

- security and privacy requirements and specifications for the system

- system security and privacy architecture

- system security plan

- other relevant documents or records

#### INTERVIEW — `sa-8.16_asm-interview`

- Organizational personnel with the responsibility for determining system security and privacy requirements

- organizational personnel with system specification, design, development, implementation, and modification responsibilities

- system developers

- organizational personnel with information security responsibilities

#### TEST — `sa-8.16_asm-test`

- Organizational processes for applying the security design principle of self-reliant trustworthiness in system specification, design, development, implementation, and modification

- mechanisms supporting the application of the security design principle of self-reliant trustworthiness in system specification, design, development, implementation, and modification

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-8.16`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
