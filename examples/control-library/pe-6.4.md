---
title: "PE-6.4 \u2014 Monitoring Physical Access to Systems"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PE-6.4 — Monitoring Physical Access to Systems

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Monitoring physical access to systems provides additional monitoring for those areas within facilities where there is a concentration of system components, including server rooms, media storage areas, and communications centers. Physical access monitoring can be coordinated with intrusion detection systems and system monitoring capabilities to provide comprehensive and integrated threat coverage for the organization.

### Requirements and exact statement parts

- `pe-6.4_smt`: Monitor physical access to the system in addition to the physical access monitoring of the facility at [PARAM pe-06.04_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pe-6.4_smt — Monitor physical access to the system in addition to the physical access monitoring of the facility at [PARAM pe-06.04_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pe-06.04_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pe-6.4_smt` — For “Monitor physical access to the system in addition to the physical access monitoring of the facility at [PARAM pe-06.04_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pe-06.04_odp` — What approved value applies to **physical spaces**? Record the value, scope, approving authority, and decision source.

  - Catalog context: physical spaces containing one or more components of the system are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pe-6.4_obj` (pe-6.4_smt): physical access to the system is monitored in addition to the physical access monitoring of the facility at [PARAM pe-06.04_odp].

#### EXAMINE — `pe-6.4_asm-examine`

- Physical and environmental protection policy

- procedures addressing physical access monitoring

- physical access control logs or records

- physical access control devices

- access authorizations

- access credentials

- list of areas within the facility containing concentrations of system components or system components requiring additional physical access monitoring

- system security plan

- privacy plan

- privacy impact assessment

- privacy risk assessment documentation

- other relevant documents or records

#### INTERVIEW — `pe-6.4_asm-interview`

- Organizational personnel with physical access monitoring responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `pe-6.4_asm-test`

- Organizational processes for monitoring physical access to the system

- mechanisms supporting and/or implementing physical access monitoring for facility areas containing system components

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pe-6.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pe-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
