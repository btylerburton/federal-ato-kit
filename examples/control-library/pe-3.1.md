---
title: "PE-3.1 \u2014 System Access"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PE-3.1 — System Access

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Control of physical access to the system provides additional physical security for those areas within facilities where there is a concentration of system components.

### Requirements and exact statement parts

- `pe-3.1_smt`: Enforce physical access authorizations to the system in addition to the physical access controls for the facility at [PARAM pe-03.01_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pe-3.1_smt — Enforce physical access authorizations to the system in addition to the physical access controls for the facility at [PARAM pe-03.01_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pe-03.01_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pe-3.1_smt` — For “Enforce physical access authorizations to the system in addition to the physical access controls for the facility at [PARAM pe-03.01_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pe-03.01_odp` — What approved value applies to **physical spaces**? Record the value, scope, approving authority, and decision source.

  - Catalog context: physical spaces containing one or more components of the system are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pe-3.1_obj-1` (pe-3.1_smt): physical access authorizations to the system are enforced;

- `pe-3.1_obj.2` (pe-3.1_smt): physical access controls are enforced for the facility at [PARAM pe-03.01_odp].

#### EXAMINE — `pe-3.1_asm-examine`

- Physical and environmental protection policy

- procedures addressing physical access control

- physical access control logs or records

- physical access control devices

- access authorizations

- access credentials

- system entry and exit points

- list of areas within the facility containing concentrations of system components or system components requiring additional physical protection

- system security plan

- other relevant documents or records

#### INTERVIEW — `pe-3.1_asm-interview`

- Organizational personnel with physical access authorization responsibilities

- organizational personnel with information security responsibilities

#### TEST — `pe-3.1_asm-test`

- Organizational processes for physical access control to the information system/components

- mechanisms supporting and/or implementing physical access control for facility areas containing system components

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pe-3.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pe-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
