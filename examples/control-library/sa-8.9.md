---
title: "SA-8.9 \u2014 Trusted Components"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-8.9 — Trusted Components

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The principle of trusted components states that a component is trustworthy to at least a level commensurate with the security dependencies it supports (i.e., how much it is trusted to perform its security functions by other components). This principle enables the composition of components such that trustworthiness is not inadvertently diminished and the trust is not consequently misplaced. Ultimately, this principle demands some metric by which the trust in a component and the trustworthiness of a component can be measured on the same abstract scale. The principle of trusted components is particularly relevant when considering systems and components in which there are complex chains of trust dependencies. A trust dependency is also referred to as a trust relationship and there may be chains of trust relationships.

The principle of trusted components also applies to a compound component that consists of subcomponents (e.g., a subsystem), which may have varying levels of trustworthiness. The conservative assumption is that the trustworthiness of a compound component is that of its least trustworthy subcomponent. It may be possible to provide a security engineering rationale that the trustworthiness of a particular compound component is greater than the conservative assumption. However, any such rationale reflects logical reasoning based on a clear statement of the trustworthiness objectives as well as relevant and credible evidence. The trustworthiness of a compound component is not the same as increased application of defense-in-depth layering within the component or a replication of components. Defense-in-depth techniques do not increase the trustworthiness of the whole above that of the least trustworthy component.

### Requirements and exact statement parts

- `sa-8.9_smt`: Implement the security design principle of trusted components in [PARAM sa-08.09_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-8.9_smt — Implement the security design principle of trusted components in [PARAM sa-08.09_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sa-08.09_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sa-8.9_smt` — For “Implement the security design principle of trusted components in [PARAM sa-08.09_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sa-08.09_odp` — What approved value applies to **systems or system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems or system components that implement the security design principle of trusted components are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-8.9_obj` (sa-8.9_smt): [PARAM sa-08.09_odp] implement the security design principle of trusted components.

#### EXAMINE — `sa-8.9_asm-examine`

- Supply chain risk management plan

- system and services acquisition policy

- procedures addressing the security design principle of trusted components used in the specification, design, development, implementation, and modification of the system

- system design documentation

- security, supply chain risk management, and privacy requirements and specifications for the system

- system security and privacy architecture

- procedures for determining component assurance

- system security plan

- other relevant documents or records

#### INTERVIEW — `sa-8.9_asm-interview`

- Organizational personnel with the responsibility for determining system security and privacy requirements

- organizational personnel with system specification, design, development, implementation, and modification responsibilities

- system developers

- organizational personnel with information security responsibilities

- organizational personnel with supply chain risk management responsibilities

#### TEST — `sa-8.9_asm-test`

- Organizational processes for applying the security design principle of trusted components in system specification, design, development, implementation, and modification

- mechanisms supporting the application of the security design principle of trusted components in system specification, design, development, implementation, and modification

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-8.9`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
