---
title: "SA-8.28 \u2014 Acceptable Security"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-8.28 — Acceptable Security

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The principle of acceptable security requires that the level of privacy and performance that the system provides is consistent with the users’ expectations. The perception of personal privacy may affect user behavior, morale, and effectiveness. Based on the organizational privacy policy and the system design, users should be able to restrict their actions to protect their privacy. When systems fail to provide intuitive interfaces or meet privacy and performance expectations, users may either choose to completely avoid the system or use it in ways that may be inefficient or even insecure.

### Requirements and exact statement parts

- `sa-8.28_smt`: Implement the security design principle of acceptable security in [PARAM sa-08.28_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-8.28_smt — Implement the security design principle of acceptable security in [PARAM sa-08.28_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sa-08.28_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sa-8.28_smt` — For “Implement the security design principle of acceptable security in [PARAM sa-08.28_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sa-08.28_odp` — What approved value applies to **systems or system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems or system components that implement the security design principle of acceptable security are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-8.28_obj` (sa-8.28_smt): [PARAM sa-08.28_odp] implement the security design principle of acceptable security.

#### EXAMINE — `sa-8.28_asm-examine`

- System and services acquisition policy

- system and services acquisition procedures

- procedures addressing the security design principle of acceptable security used in the specification, design, development, implementation, and modification of the system

- system design documentation

- security and privacy requirements and specifications for the system

- system security and privacy architecture

- personally identifiable information processing policy

- privacy notifications provided to users

- system security plan

- privacy plan

- privacy impact assessment

- privacy risk assessment documentation

- other relevant documents or records

#### INTERVIEW — `sa-8.28_asm-interview`

- Organizational personnel with information security and privacy responsibilities

- organizational personnel with system specification, design, development, implementation, and modification responsibilities

- system developers

#### TEST — `sa-8.28_asm-test`

- Organizational processes for applying the security design principle of acceptable security in system specification, design, development, implementation, and modification

- mechanisms supporting the application of the security design principle of acceptable security in system specification, design, development, implementation, and modification

- mechanisms that enforce security policies

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-8.28`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
