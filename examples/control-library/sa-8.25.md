---
title: "SA-8.25 \u2014 Economic Security"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-8.25 — Economic Security

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The principle of economic security states that security mechanisms are not costlier than the potential damage that could occur from a security breach. This is the security-relevant form of the cost-benefit analyses used in risk management. The cost assumptions of cost-benefit analysis prevent the system designer from incorporating security mechanisms of greater strength than necessary, where strength of mechanism is proportional to cost. The principle of economic security also requires analysis of the benefits of assurance relative to the cost of that assurance in terms of the effort expended to obtain relevant and credible evidence as well as the necessary analyses to assess and draw trustworthiness and risk conclusions from the evidence.

### Requirements and exact statement parts

- `sa-8.25_smt`: Implement the security design principle of economic security in [PARAM sa-08.25_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-8.25_smt — Implement the security design principle of economic security in [PARAM sa-08.25_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sa-08.25_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sa-8.25_smt` — For “Implement the security design principle of economic security in [PARAM sa-08.25_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sa-08.25_odp` — What approved value applies to **systems or system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems or system components that implement the security design principle of economic security are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-8.25_obj` (sa-8.25_smt): [PARAM sa-08.25_odp] implement the security design principle of economic security.

#### EXAMINE — `sa-8.25_asm-examine`

- System and services acquisition policy

- procedures addressing the security design principle of economic security used in the specification, design, development, implementation, and modification of the system

- system design documentation

- security and privacy requirements and specifications for the system

- system security and privacy architecture

- cost-benefit analysis

- system security plan

- other relevant documents or records

#### INTERVIEW — `sa-8.25_asm-interview`

- Organizational personnel with the responsibility for determining system security and privacy requirements

- organizational personnel with system specification, design, development, implementation, and modification responsibilities

- system developers

- organizational personnel with information security responsibilities

#### TEST — `sa-8.25_asm-test`

- Organizational processes for applying the security design principle of economic security in system specification, design, development, implementation, and modification

- mechanisms supporting the application of the security design principle of economic security in system specification, design, development, implementation, and modification

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-8.25`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-8`.

- Catalog relationship **related**: `ra-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
