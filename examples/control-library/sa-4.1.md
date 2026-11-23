---
title: "SA-4.1 \u2014 Functional Properties of Controls"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-4.1 — Functional Properties of Controls

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Functional properties of security and privacy controls describe the functionality (i.e., security or privacy capability, functions, or mechanisms) visible at the interfaces of the controls and specifically exclude functionality and data structures internal to the operation of the controls.

### Requirements and exact statement parts

- `sa-4.1_smt`: Require the developer of the system, system component, or system service to provide a description of the functional properties of the controls to be implemented.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-4.1_smt — Require the developer of the system, system component, or system service to provide a description of the functional properties of the controls to be implemented.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sa-4.1_smt` — For “Require the developer of the system, system component, or system service to provide a description of the functional properties of the controls to be implemented.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-4.1_obj` (sa-4.1_smt): the developer of the system, system component, or system service is required to provide a description of the functional properties of the controls to be implemented.

#### EXAMINE — `sa-4.1_asm-examine`

- System and services acquisition policy

- system and services acquisition procedures

- procedures addressing the integration of security and privacy requirements, descriptions, and criteria into the acquisition process

- solicitation documents

- acquisition documentation

- acquisition contracts for the system, system component, or system services

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `sa-4.1_asm-interview`

- Organizational personnel with acquisition/contracting responsibilities

- organizational personnel with information security and privacy responsibilities

- system developers

#### TEST — `sa-4.1_asm-test`

- Organizational processes for determining system security functional requirements

- organizational processes for developing acquisition contracts

- mechanisms supporting and/or implementing acquisitions and the inclusion of security and privacy requirements in contracts

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-4.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
