---
title: "SR-4.4 \u2014 Supply Chain Integrity \u2014 Pedigree"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SR-4.4 — Supply Chain Integrity — Pedigree

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Authoritative information regarding the internal composition of system components and the provenance of technology, products, and services provides a strong basis for trust. The validation of the internal composition and provenance of technologies, products, and services is referred to as the pedigree. For microelectronics, this includes material composition of components. For software this includes the composition of open-source and proprietary code, including the version of the component at a given point in time. Pedigrees increase the assurance that the claims suppliers assert about the internal composition and provenance of the products, services, and technologies they provide are valid. The validation of the internal composition and provenance can be achieved by various evidentiary artifacts or records that manufacturers and suppliers produce during the research and development, design, manufacturing, acquisition, delivery, integration, operations and maintenance, and disposal of technology, products, and services. Evidentiary artifacts include, but are not limited to, software identification (SWID) tags, software component inventory, the manufacturers’ declarations of platform attributes (e.g., serial numbers, hardware component inventory), and measurements (e.g., firmware hashes) that are tightly bound to the hardware itself.

### Requirements and exact statement parts

- `sr-4.4_smt`: Employ [PARAM sr-04.04_odp.01] and conduct [PARAM sr-04.04_odp.02] to ensure the integrity of the system and system components by validating the internal composition and provenance of critical or mission-essential technologies, products, and services.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sr-4.4_smt — Employ [PARAM sr-04.04_odp.01] and conduct [PARAM sr-04.04_odp.02] to ensure the integrity of the system and system components by validating the internal composition and provenance of critical or mission-essential technologies, products, and services.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sr-04.04_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sr-04.04_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sr-4.4_smt` — For “Employ [PARAM sr-04.04_odp.01] and conduct [PARAM sr-04.04_odp.02] to ensure the integrity of the system and system components by validating the internal composition and provenance of critical or mission-essential technologies, products, and services.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sr-04.04_odp.01` — What approved value applies to **controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controls employed to ensure that the integrity of the system and system component are defined;

- `sr-04.04_odp.02` — What approved value applies to **analysis method**? Record the value, scope, approving authority, and decision source.

  - Catalog context: an analysis method to be conducted to validate the internal composition and provenance of critical or mission-essential technologies, products, and services to ensure the integrity of the system and system component is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sr-4.4_obj-1` (sr-4.4_smt): [PARAM sr-04.04_odp.01] are employed to ensure the integrity of the system and system components;

- `sr-4.4_obj-2` (sr-4.4_smt): [PARAM sr-04.04_odp.02] is conducted to ensure the integrity of the system and system components.

#### EXAMINE — `sr-4.4_asm-examine`

- Supply chain risk management policy and procedures

- supply chain risk management plan

- system and services acquisition policy

- procedures addressing supply chain protection

- bill of materials for critical systems or system components

- acquisition documentation

- software identification tags

- manufacturer declarations of platform attributes (e.g., serial numbers, hardware component inventory) and measurements (e.g., firmware hashes) that are tightly bound to the hardware itself

- system security plan

- other relevant documents or records

#### INTERVIEW — `sr-4.4_asm-interview`

- Organizational personnel with system and services acquisition responsibilities

- organizational personnel with information security responsibilities

- organizational personnel with supply chain risk management responsibilities

#### TEST — `sr-4.4_asm-test`

- Organizational processes for identifying pedigree information

- organizational processes to determine and validate the integrity of the internal composition of critical systems and critical system components

- mechanisms to determine and validate the integrity of the internal composition of critical systems and critical system components

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sr-4.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sr-4`.

- Catalog relationship **related**: `ra-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
