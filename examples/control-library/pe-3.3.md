---
title: "PE-3.3 \u2014 Continuous Guards"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PE-3.3 — Continuous Guards

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Employing guards at selected physical access points to the facility provides a more rapid response capability for organizations. Guards also provide the opportunity for human surveillance in areas of the facility not covered by video surveillance.

### Requirements and exact statement parts

- `pe-3.3_smt`: Employ guards to control [PARAM pe-03.03_odp] to the facility where the system resides 24 hours per day, 7 days per week.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pe-3.3_smt — Employ guards to control [PARAM pe-03.03_odp] to the facility where the system resides 24 hours per day, 7 days per week.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pe-03.03_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pe-3.3_smt` — For “Employ guards to control [PARAM pe-03.03_odp] to the facility where the system resides 24 hours per day, 7 days per week.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pe-03.03_odp` — What approved value applies to **physical access points**? Record the value, scope, approving authority, and decision source.

  - Catalog context: physical access points to the facility where the system resides are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pe-3.3_obj` (pe-3.3_smt): guards are employed to control [PARAM pe-03.03_odp] to the facility where the system resides 24 hours per day, 7 days per week.

#### EXAMINE — `pe-3.3_asm-examine`

- Physical and environmental protection policy

- procedures addressing physical access control

- physical access control logs or records

- physical access control devices

- facility surveillance records

- facility layout documentation

- system entry and exit points

- system security plan

- other relevant documents or records

#### INTERVIEW — `pe-3.3_asm-interview`

- Organizational personnel with physical access control responsibilities

- organizational personnel with information security responsibilities

#### TEST — `pe-3.3_asm-test`

- Organizational processes for physical access control to the facility where the system resides

- mechanisms supporting and/or implementing physical access control for the facility where the system resides

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pe-3.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pe-3`.

- Catalog relationship **related**: `cp-6`.

- Catalog relationship **related**: `cp-7`.

- Catalog relationship **related**: `pe-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
