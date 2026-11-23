---
title: "SA-4.2 \u2014 Design and Implementation Information for Controls"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-4.2 — Design and Implementation Information for Controls

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations may require different levels of detail in the documentation for the design and implementation of controls in organizational systems, system components, or system services based on mission and business requirements, requirements for resiliency and trustworthiness, and requirements for analysis and testing. Systems can be partitioned into multiple subsystems. Each subsystem within the system can contain one or more modules. The high-level design for the system is expressed in terms of subsystems and the interfaces between subsystems providing security-relevant functionality. The low-level design for the system is expressed in terms of modules and the interfaces between modules providing security-relevant functionality. Design and implementation documentation can include manufacturer, version, serial number, verification hash signature, software libraries used, date of purchase or download, and the vendor or download source. Source code and hardware schematics are referred to as the implementation representation of the system.

### Requirements and exact statement parts

- `sa-4.2_smt`: Require the developer of the system, system component, or system service to provide design and implementation information for the controls that includes: [PARAM sa-04.02_odp.01] at [PARAM sa-04.02_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-4.2_smt — Require the developer of the system, system component, or system service to provide design and implementation information for the controls that includes: [PARAM sa-04.02_odp.01] at [PARAM sa-04.02_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sa-04.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sa-04.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sa-04.02_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sa-4.2_smt` — For “Require the developer of the system, system component, or system service to provide design and implementation information for the controls that includes: [PARAM sa-04.02_odp.01] at [PARAM sa-04.02_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sa-04.02_odp.01` — What approved value applies to **selection; choose one-or-more from: security-relevant external system interfaces; high-level design; low-level design; source code or hardware schematics; [PARAM sa-04.02_odp.02]**? Record the value, scope, approving authority, and decision source.

- `sa-04.02_odp.02` — What approved value applies to **design and implementation information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: design and implementation information is defined (if selected);

- `sa-04.02_odp.03` — What approved value applies to **level of detail**? Record the value, scope, approving authority, and decision source.

  - Catalog context: level of detail is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-4.2_obj` (sa-4.2_smt): the developer of the system, system component, or system service is required to provide design and implementation information for the controls that includes using [PARAM sa-04.02_odp.01] at [PARAM sa-04.02_odp.03].

#### EXAMINE — `sa-4.2_asm-examine`

- System and services acquisition policy

- system and services acquisition procedures

- procedures addressing the integration of security requirements, descriptions, and criteria into the acquisition process

- solicitation documents

- acquisition documentation

- acquisition contracts for the system, system components, or system services

- design and implementation information for controls employed in the system, system component, or system service

- system security plan

- other relevant documents or records

#### INTERVIEW — `sa-4.2_asm-interview`

- Organizational personnel with acquisition/contracting responsibilities

- organizational personnel with the responsibility to determine system security requirements

- system developers or service provider

- organizational personnel with information security responsibilities

#### TEST — `sa-4.2_asm-test`

- Organizational processes for determining the level of detail for system design and controls

- organizational processes for developing acquisition contracts

- mechanisms supporting and/or implementing the development of system design details

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-4.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
