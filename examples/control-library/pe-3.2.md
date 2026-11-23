---
title: "PE-3.2 \u2014 Facility and Systems"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PE-3.2 — Facility and Systems

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations determine the extent, frequency, and/or randomness of security checks to adequately mitigate risk associated with exfiltration.

### Requirements and exact statement parts

- `pe-3.2_smt`: Perform security checks [PARAM pe-03.02_odp] at the physical perimeter of the facility or system for exfiltration of information or removal of system components.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pe-3.2_smt — Perform security checks [PARAM pe-03.02_odp] at the physical perimeter of the facility or system for exfiltration of information or removal of system components.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pe-03.02_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pe-3.2_smt` — For “Perform security checks [PARAM pe-03.02_odp] at the physical perimeter of the facility or system for exfiltration of information or removal of system components.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pe-03.02_odp` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which to perform security checks at the physical perimeter of the facility or system for exfiltration of information or removal of system components is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pe-3.2_obj` (pe-3.2_smt): security checks are performed [PARAM pe-03.02_odp] at the physical perimeter of the facility or system for exfiltration of information or removal of system components.

#### EXAMINE — `pe-3.2_asm-examine`

- Physical and environmental protection policy

- procedures addressing physical access control

- physical access control logs or records

- records of security checks

- security audit reports

- security inspection reports

- facility layout documentation

- system entry and exit points

- system security plan

- other relevant documents or records

#### INTERVIEW — `pe-3.2_asm-interview`

- Organizational personnel with physical access control responsibilities

- organizational personnel with information security responsibilities

#### TEST — `pe-3.2_asm-test`

- Organizational processes for physical access control to the facility and/or system

- mechanisms supporting and/or implementing physical access control for the facility or system

- mechanisms supporting and/or implementing security checks for the unauthorized exfiltration of information

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pe-3.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pe-3`.

- Catalog relationship **related**: `ac-4`.

- Catalog relationship **related**: `sc-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
