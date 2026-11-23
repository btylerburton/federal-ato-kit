---
title: "IR-6.3 \u2014 Supply Chain Coordination"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-6.3 — Supply Chain Coordination

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations involved in supply chain activities include product developers, system integrators, manufacturers, packagers, assemblers, distributors, vendors, and resellers. Entities that provide supply chain governance include the Federal Acquisition Security Council (FASC). Supply chain incidents include compromises or breaches that involve information technology products, system components, development processes or personnel, distribution processes, or warehousing facilities. Organizations determine the appropriate information to share and consider the value gained from informing external organizations about supply chain incidents, including the ability to improve processes or to identify the root cause of an incident.

### Requirements and exact statement parts

- `ir-6.3_smt`: Provide incident information to the provider of the product or service and other organizations involved in the supply chain or supply chain governance for systems or system components related to the incident.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-6.3_smt — Provide incident information to the provider of the product or service and other organizations involved in the supply chain or supply chain governance for systems or system components related to the incident.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ir-6.3_smt` — For “Provide incident information to the provider of the product or service and other organizations involved in the supply chain or supply chain governance for systems or system components related to the incident.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-6.3_obj` (ir-6.3_smt): incident information is provided to the provider of the product or service and other organizations involved in the supply chain or supply chain governance for systems or system components related to the incident.

#### EXAMINE — `ir-6.3_asm-examine`

- Incident response policy

- procedures addressing supply chain coordination and supply chain risk information sharing with the Federal Acquisition Security Council

- acquisition policy

- acquisition contracts

- service-level agreements

- incident response plan

- supply chain risk management plan

- system security plan

- plans of other organizations involved in supply chain activities

- other relevant documents or records

#### INTERVIEW — `ir-6.3_asm-interview`

- Organizational personnel with incident reporting responsibilities

- organizational personnel with information security responsibilities

- organizational personnel with supply chain risk management responsibilities

- organization personnel with acquisition responsibilities

#### TEST — `ir-6.3_asm-test`

- Organizational processes for incident reporting

- organizational processes for supply chain risk information sharing

- mechanisms supporting and/or implementing the reporting of incident information involved in the supply chain

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-6.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ir-6`.

- Catalog relationship **related**: `sr-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
