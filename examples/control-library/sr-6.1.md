---
title: "SR-6.1 \u2014 Testing and Analysis"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SR-6.1 — Testing and Analysis

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Relationships between entities and procedures within the supply chain, including development and delivery, are considered. Supply chain elements include organizations, entities, or tools that are used for the research and development, design, manufacturing, acquisition, delivery, integration, operations, maintenance, and disposal of systems, system components, or system services. Supply chain processes include supply chain risk management programs; SCRM strategies and implementation plans; personnel and physical security programs; hardware, software, and firmware development processes; configuration management tools, techniques, and measures to maintain provenance; shipping and handling procedures; and programs, processes, or procedures associated with the production and distribution of supply chain elements. Supply chain actors are individuals with specific roles and responsibilities in the supply chain. The evidence generated and collected during analyses and testing of supply chain elements, processes, and actors is documented and used to inform organizational risk management activities and decisions.

### Requirements and exact statement parts

- `sr-6.1_smt`: Employ [PARAM sr-06.01_odp.01] of the following supply chain elements, processes, and actors associated with the system, system component, or system service: [PARAM sr-06.01_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sr-6.1_smt — Employ [PARAM sr-06.01_odp.01] of the following supply chain elements, processes, and actors associated with the system, system component, or system service: [PARAM sr-06.01_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sr-06.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sr-06.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sr-6.1_smt` — For “Employ [PARAM sr-06.01_odp.01] of the following supply chain elements, processes, and actors associated with the system, system component, or system service: [PARAM sr-06.01_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sr-06.01_odp.01` — What approved value applies to **selection; choose one-or-more from: organizational analysis; independent third-party analysis; organizational testing; independent third-party testing**? Record the value, scope, approving authority, and decision source.

- `sr-06.01_odp.02` — What approved value applies to **supply chain elements, processes, and actors**? Record the value, scope, approving authority, and decision source.

  - Catalog context: supply chain elements, processes, and actors to be analyzed and tested are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sr-6.1_obj` (sr-6.1_smt): [PARAM sr-06.01_odp.01] is/are employed on [PARAM sr-06.01_odp.02] associated with the system, system component, or system service.

#### EXAMINE — `sr-6.1_asm-examine`

- Supply chain risk management policy and procedures

- supply chain risk management plan

- system and services acquisition policy

- procedures addressing supply chain protection

- evidence of organizational analysis, independent third-party analysis, organizational penetration testing, and/or independent third-party penetration testing

- list of supply chain elements, processes, and actors (associated with the system, system component, or system service) subject to analysis and/or testing

- system security plan

- other relevant documents or records

#### INTERVIEW — `sr-6.1_asm-interview`

- Organizational personnel with system and services acquisition responsibilities

- organizational personnel with information security responsibilities

- organizational personnel with supply chain risk management responsibilities

- organizational personnel with responsibilities for analyzing and/or testing supply chain elements, processes, and actors

#### TEST — `sr-6.1_asm-test`

- Organizational processes for defining and employing methods of analysis/testing of supply chain elements, processes, and actors

- mechanisms supporting and/or implementing the analysis/testing of supply chain elements, processes, and actors

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sr-6.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sr-6`.

- Catalog relationship **related**: `ca-8`.

- Catalog relationship **related**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
