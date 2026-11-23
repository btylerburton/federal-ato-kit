---
title: "SR-4.2 \u2014 Track and Trace"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SR-4.2 — Track and Trace

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Tracking the unique identification of systems and system components during development and transport activities provides a foundational identity structure for the establishment and maintenance of provenance. For example, system components may be labeled using serial numbers or tagged using radio-frequency identification tags. Labels and tags can help provide better visibility into the provenance of a system or system component. A system or system component may have more than one unique identifier. Identification methods are sufficient to support a forensic investigation after a supply chain compromise or event.

### Requirements and exact statement parts

- `sr-4.2_smt`: Establish and maintain unique identification of the following systems and critical system components for tracking through the supply chain: [PARAM sr-04.02_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sr-4.2_smt — Establish and maintain unique identification of the following systems and critical system components for tracking through the supply chain: [PARAM sr-04.02_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sr-04.02_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sr-4.2_smt` — For “Establish and maintain unique identification of the following systems and critical system components for tracking through the supply chain: [PARAM sr-04.02_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sr-04.02_odp` — What approved value applies to **systems and critical system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems and critical system components that require unique identification for tracking through the supply chain are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sr-4.2_obj-1` (sr-4.2_smt): the unique identification of [PARAM sr-04.02_odp] is established for tracking through the supply chain;

- `sr-4.2_obj-2` (sr-4.2_smt): the unique identification of [PARAM sr-04.02_odp] is maintained for tracking through the supply chain.

#### EXAMINE — `sr-4.2_asm-examine`

- Supply chain risk management policy and procedures

- system and services acquisition policy

- procedures addressing supply chain protection

- procedures addressing the integration of information security requirements into the acquisition process

- supply chain risk management plan

- list of supply chain elements, processes, and actors (associated with the system, system component, or system service) requiring implementation of unique identification processes, procedures, tools, mechanisms, equipment, techniques, and/or configurations

- system security plan

- other relevant documents or records

#### INTERVIEW — `sr-4.2_asm-interview`

- Organizational personnel with system and services acquisition responsibilities

- organizational personnel with information security responsibilities

- organizational personnel with supply chain protection responsibilities

- organizational personnel with responsibilities for establishing and retaining the unique identification of supply chain elements, processes, and actors

#### TEST — `sr-4.2_asm-test`

- Organizational processes for defining, establishing, and retaining unique identification for supply chain elements, processes, and actors

- mechanisms supporting and/or implementing the definition, establishment, and retention of unique identification for supply chain elements, processes, and actors

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sr-4.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sr-4`.

- Catalog relationship **related**: `ia-2`.

- Catalog relationship **related**: `ia-8`.

- Catalog relationship **related**: `pe-16`.

- Catalog relationship **related**: `pl-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
