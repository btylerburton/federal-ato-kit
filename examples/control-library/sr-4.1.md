---
title: "SR-4.1 \u2014 Identity"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SR-4.1 — Identity

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Knowing who and what is in the supply chains of organizations is critical to gaining visibility into supply chain activities. Visibility into supply chain activities is also important for monitoring and identifying high-risk events and activities. Without reasonable visibility into supply chains elements, processes, and personnel, it is very difficult for organizations to understand and manage risk and reduce their susceptibility to adverse events. Supply chain elements include organizations, entities, or tools used for the research and development, design, manufacturing, acquisition, delivery, integration, operations, maintenance, and disposal of systems and system components. Supply chain processes include development processes for hardware, software, and firmware; shipping and handling procedures; configuration management tools, techniques, and measures to maintain provenance; personnel and physical security programs; or other programs, processes, or procedures associated with the production and distribution of supply chain elements. Supply chain personnel are individuals with specific roles and responsibilities related to the secure the research and development, design, manufacturing, acquisition, delivery, integration, operations and maintenance, and disposal of a system or system component. Identification methods are sufficient to support an investigation in case of a supply chain change (e.g. if a supply company is purchased), compromise, or event.

### Requirements and exact statement parts

- `sr-4.1_smt`: Establish and maintain unique identification of the following supply chain elements, processes, and personnel associated with the identified system and critical system components: [PARAM sr-04.01_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sr-4.1_smt — Establish and maintain unique identification of the following supply chain elements, processes, and personnel associated with the identified system and critical system components: [PARAM sr-04.01_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sr-04.01_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sr-4.1_smt` — For “Establish and maintain unique identification of the following supply chain elements, processes, and personnel associated with the identified system and critical system components: [PARAM sr-04.01_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sr-04.01_odp` — What approved value applies to **supply chain elements, processes, and personnel**? Record the value, scope, approving authority, and decision source.

  - Catalog context: supply chain elements, processes, and personnel associated with systems and critical system components that require unique identification are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sr-4.1_obj-1` (sr-4.1_smt): unique identification of [PARAM sr-04.01_odp] is established;

- `sr-4.1_obj-2` (sr-4.1_smt): unique identification of [PARAM sr-04.01_odp] is maintained.

#### EXAMINE — `sr-4.1_asm-examine`

- Supply chain risk management policy and procedures

- supply chain risk management plan

- system and services acquisition policy

- procedures addressing supply chain protection

- procedures addressing the integration of information security requirements into the acquisition process

- list of supply chain elements, processes, and actors (associated with the system, system component, or system service) requiring implementation of unique identification processes, procedures, tools, mechanisms, equipment, techniques, and/or configurations

- system security plan

- other relevant documents or records

#### INTERVIEW — `sr-4.1_asm-interview`

- Organizational personnel with system and services acquisition responsibilities

- organizational personnel with information security responsibilities

- organizational personnel with supply chain protection responsibilities

- organizational personnel with responsibilities for establishing and retaining the unique identification of supply chain elements, processes, and actors

#### TEST — `sr-4.1_asm-test`

- Organizational processes for defining, establishing, and retaining unique identification for supply chain elements, processes, and actors

- mechanisms supporting and/or implementing the definition, establishment, and retention of unique identification for supply chain elements, processes, and actors

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sr-4.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sr-4`.

- Catalog relationship **related**: `ia-2`.

- Catalog relationship **related**: `ia-8`.

- Catalog relationship **related**: `pe-16`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
