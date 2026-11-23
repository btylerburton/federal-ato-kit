---
title: "SA-3.3 \u2014 Technology Refresh"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-3.3 — Technology Refresh

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Technology refresh planning may encompass hardware, software, firmware, processes, personnel skill sets, suppliers, service providers, and facilities. The use of obsolete or nearing obsolete technology may increase the security and privacy risks associated with unsupported components, counterfeit or repurposed components, components unable to implement security or privacy requirements, slow or inoperable components, components from untrusted sources, inadvertent personnel error, or increased complexity. Technology refreshes typically occur during the operations and maintenance stage of the system development life cycle.

### Requirements and exact statement parts

- `sa-3.3_smt`: Plan for and implement a technology refresh schedule for the system throughout the system development life cycle.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-3.3_smt — Plan for and implement a technology refresh schedule for the system throughout the system development life cycle.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sa-3.3_smt` — For “Plan for and implement a technology refresh schedule for the system throughout the system development life cycle.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-3.3_obj-1` (sa-3.3_smt): a technology refresh schedule is planned for the system throughout the system development life cycle;

- `sa-3.3_obj-2` (sa-3.3_smt): a technology refresh schedule is implemented for the system throughout the system development life cycle.

#### EXAMINE — `sa-3.3_asm-examine`

- System and services acquisition policy

- system and services acquisition procedures

- procedures addressing technology refresh planning and implementation

- system development life cycle documentation

- technology refresh schedule

- security risk assessment documentation

- privacy impact assessment

- privacy risk assessment documentation

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `sa-3.3_asm-interview`

- Organizational personnel with information security and privacy responsibilities

- organizational personnel with system life cycle development responsibilities

#### TEST — `sa-3.3_asm-test`

- Organizational processes for defining and documenting the system development life cycle

- organizational processes for identifying system development life cycle roles and responsibilities

- organizational processes for integrating security and privacy risk management into the system development life cycle

- mechanisms supporting and/or implementing the system development life cycle

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-3.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-3`.

- Catalog relationship **related**: `ma-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
