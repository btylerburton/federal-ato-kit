---
title: "SA-8.29 \u2014 Repeatable and Documented Procedures"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-8.29 — Repeatable and Documented Procedures

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The principle of repeatable and documented procedures states that the techniques and methods employed to construct a system component permit the same component to be completely and correctly reconstructed at a later time. Repeatable and documented procedures support the development of a component that is identical to the component created earlier, which may be in widespread use. In the case of other system artifacts (e.g., documentation and testing results), repeatability supports consistency and the ability to inspect the artifacts. Repeatable and documented procedures can be introduced at various stages within the system development life cycle and contribute to the ability to evaluate assurance claims for the system. Examples include systematic procedures for code development and review, procedures for the configuration management of development tools and system artifacts, and procedures for system delivery.

### Requirements and exact statement parts

- `sa-8.29_smt`: Implement the security design principle of repeatable and documented procedures in [PARAM sa-08.29_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-8.29_smt — Implement the security design principle of repeatable and documented procedures in [PARAM sa-08.29_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sa-08.29_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sa-8.29_smt` — For “Implement the security design principle of repeatable and documented procedures in [PARAM sa-08.29_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sa-08.29_odp` — What approved value applies to **systems or system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems or system components that implement the security design principle of repeatable and documented procedures are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-8.29_obj` (sa-8.29_smt): [PARAM sa-08.29_odp] implement the security design principle of repeatable and documented procedures.

#### EXAMINE — `sa-8.29_asm-examine`

- System and services acquisition policy

- procedures addressing the security design principle of repeatable and documented procedures used in the specification, design, development, implementation, and modification of the system

- system design documentation

- security and privacy requirements and specifications for the system

- system security and privacy architecture

- system security plan

- other relevant documents or records

#### INTERVIEW — `sa-8.29_asm-interview`

- Organizational personnel with the responsibility for determining system security and privacy requirements

- organizational personnel with system specification, design, development, implementation, and modification responsibilities

- system developers

- organizational personnel with information security responsibilities

#### TEST — `sa-8.29_asm-test`

- Organizational processes for applying the security design principle of repeatable and documented procedures in system specification, design, development, implementation, and modification

- mechanisms supporting the application of the security design principle of repeatable and documented procedures in system specification, design, development, implementation, and modification

- mechanisms that enforce security policies

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-8.29`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-8`.

- Catalog relationship **related**: `cm-1`.

- Catalog relationship **related**: `sa-1`.

- Catalog relationship **related**: `sa-10`.

- Catalog relationship **related**: `sa-11`.

- Catalog relationship **related**: `sa-15`.

- Catalog relationship **related**: `sa-17`.

- Catalog relationship **related**: `sc-1`.

- Catalog relationship **related**: `si-1`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
