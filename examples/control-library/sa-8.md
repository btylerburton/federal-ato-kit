---
title: "SA-8 \u2014 Security and Privacy Engineering Principles"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-8 — Security and Privacy Engineering Principles

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Systems security and privacy engineering principles are closely related to and implemented throughout the system development life cycle (see SA-3 (catalog reference: `#sa-3`) ). Organizations can apply systems security and privacy engineering principles to new systems under development or to systems undergoing upgrades. For existing systems, organizations apply systems security and privacy engineering principles to system upgrades and modifications to the extent feasible, given the current state of hardware, software, and firmware components within those systems.

The application of systems security and privacy engineering principles helps organizations develop trustworthy, secure, and resilient systems and reduces the susceptibility to disruptions, hazards, threats, and the creation of privacy problems for individuals. Examples of system security engineering principles include: developing layered protections; establishing security and privacy policies, architecture, and controls as the foundation for design and development; incorporating security and privacy requirements into the system development life cycle; delineating physical and logical security boundaries; ensuring that developers are trained on how to build secure software; tailoring controls to meet organizational needs; and performing threat modeling to identify use cases, threat agents, attack vectors and patterns, design patterns, and compensating controls needed to mitigate risk.

Organizations that apply systems security and privacy engineering concepts and principles can facilitate the development of trustworthy, secure systems, system components, and system services; reduce risk to acceptable levels; and make informed risk management decisions. System security engineering principles can also be used to protect against certain supply chain risks, including incorporating tamper-resistant hardware into a design.

### Requirements and exact statement parts

- `sa-8_smt`: Apply the following systems security and privacy engineering principles in the specification, design, development, implementation, and modification of the system and system components: [PARAM sa-8_prm_1].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-8_smt — Apply the following systems security and privacy engineering principles in the specification, design, development, implementation, and modification of the system and system components: [PARAM sa-8_prm_1].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sa-8_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sa-08_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sa-08_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sa-8_smt` — For “Apply the following systems security and privacy engineering principles in the specification, design, development, implementation, and modification of the system and system components: [PARAM sa-8_prm_1].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sa-8_prm_1` — What approved value applies to **organization-defined systems security and privacy engineering principles**? Record the value, scope, approving authority, and decision source.

- `sa-08_odp.01` — What approved value applies to **systems security engineering principles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems security engineering principles are defined;

- `sa-08_odp.02` — What approved value applies to **privacy engineering principles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: privacy engineering principles are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-8_obj-1` (sa-8_smt): [PARAM sa-08_odp.01] are applied in the specification of the system and system components;

- `sa-8_obj-2` (sa-8_smt): [PARAM sa-08_odp.01] are applied in the design of the system and system components;

- `sa-8_obj-3` (sa-8_smt): [PARAM sa-08_odp.01] are applied in the development of the system and system components;

- `sa-8_obj-4` (sa-8_smt): [PARAM sa-08_odp.01] are applied in the implementation of the system and system components;

- `sa-8_obj-5` (sa-8_smt): [PARAM sa-08_odp.01] are applied in the modification of the system and system components;

- `sa-8_obj-6` (sa-8_smt): [PARAM sa-08_odp.02] are applied in the specification of the system and system components;

- `sa-8_obj-7` (sa-8_smt): [PARAM sa-08_odp.02] are applied in the design of the system and system components;

- `sa-8_obj-8` (sa-8_smt): [PARAM sa-08_odp.02] are applied in the development of the system and system components;

- `sa-8_obj-9` (sa-8_smt): [PARAM sa-08_odp.02] are applied in the implementation of the system and system components;

- `sa-8_obj-10` (sa-8_smt): [PARAM sa-08_odp.02] are applied in the modification of the system and system components.

#### EXAMINE — `sa-8_asm-examine`

- System and services acquisition policy

- system and services acquisition procedures

- assessment and authorization procedures

- procedures addressing security and privacy engineering principles used in the specification, design, development, implementation, and modification of the system

- system design documentation

- security and privacy requirements and specifications for the system

- system security plan

- privacy plan

- privacy impact assessment

- privacy risk assessment documentation

- other relevant documents or records

#### INTERVIEW — `sa-8_asm-interview`

- Organizational personnel with acquisition/contracting responsibilities

- organizational personnel with information security and privacy responsibilities

- organizational personnel with system specification, design, development, implementation, and modification responsibilities

- system developers

#### TEST — `sa-8_asm-test`

- Organizational processes for applying security and privacy engineering principles in system specification, design, development, implementation, and modification

- mechanisms supporting the application of security and privacy engineering principles in system specification, design, development, implementation, and modification

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-8`. The library index records the exact source revision and hash.

- [PRIVACT](https://www.govinfo.gov/content/pkg/STATUTE-88/pdf/STATUTE-88-Pg1896.pdf)

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [FIPS 199](https://doi.org/10.6028/NIST.FIPS.199)

- [FIPS 200](https://doi.org/10.6028/NIST.FIPS.200)

- [SP 800-37](https://doi.org/10.6028/NIST.SP.800-37r2)

- [SP 800-53A](https://doi.org/10.6028/NIST.SP.800-53Ar4)

- [SP 800-60-1](https://doi.org/10.6028/NIST.SP.800-60v1r1)

- [SP 800-60-2](https://doi.org/10.6028/NIST.SP.800-60v2r1)

- [SP 800-160-1](https://doi.org/10.6028/NIST.SP.800-160v1)

- [IR 8062](https://doi.org/10.6028/NIST.IR.8062)

- [SP 800-160-2](https://doi.org/10.6028/NIST.SP.800-160v2)

- Catalog relationship **related**: `pl-8`.

- Catalog relationship **related**: `pm-7`.

- Catalog relationship **related**: `ra-2`.

- Catalog relationship **related**: `ra-3`.

- Catalog relationship **related**: `ra-9`.

- Catalog relationship **related**: `sa-3`.

- Catalog relationship **related**: `sa-4`.

- Catalog relationship **related**: `sa-15`.

- Catalog relationship **related**: `sa-17`.

- Catalog relationship **related**: `sa-20`.

- Catalog relationship **related**: `sc-2`.

- Catalog relationship **related**: `sc-3`.

- Catalog relationship **related**: `sc-32`.

- Catalog relationship **related**: `sc-39`.

- Catalog relationship **related**: `sr-2`.

- Catalog relationship **related**: `sr-3`.

- Catalog relationship **related**: `sr-4`.

- Catalog relationship **related**: `sr-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
