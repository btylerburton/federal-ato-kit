---
title: "PE-3.5 \u2014 Tamper Protection"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PE-3.5 — Tamper Protection

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations can implement tamper detection and prevention at selected hardware components or implement tamper detection at some components and tamper prevention at other components. Detection and prevention activities can employ many types of anti-tamper technologies, including tamper-detection seals and anti-tamper coatings. Anti-tamper programs help to detect hardware alterations through counterfeiting and other supply chain-related risks.

### Requirements and exact statement parts

- `pe-3.5_smt`: Employ [PARAM pe-03.05_odp.01] to [PARAM pe-03.05_odp.02] physical tampering or alteration of [PARAM pe-03.05_odp.03] within the system.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pe-3.5_smt — Employ [PARAM pe-03.05_odp.01] to [PARAM pe-03.05_odp.02] physical tampering or alteration of [PARAM pe-03.05_odp.03] within the system.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pe-03.05_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pe-03.05_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pe-03.05_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pe-3.5_smt` — For “Employ [PARAM pe-03.05_odp.01] to [PARAM pe-03.05_odp.02] physical tampering or alteration of [PARAM pe-03.05_odp.03] within the system.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pe-03.05_odp.01` — What approved value applies to **anti-tamper technologies**? Record the value, scope, approving authority, and decision source.

  - Catalog context: anti-tamper technologies to be employed are defined;

- `pe-03.05_odp.02` — What approved value applies to **selection; choose one-or-more from: detect; prevent**? Record the value, scope, approving authority, and decision source.

- `pe-03.05_odp.03` — What approved value applies to **hardware components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: hardware components to be protected from physical tampering or alteration are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pe-3.5_obj` (pe-3.5_smt): [PARAM pe-03.05_odp.01] are employed to [PARAM pe-03.05_odp.02] physical tampering or alteration of [PARAM pe-03.05_odp.03] within the system.

#### EXAMINE — `pe-3.5_asm-examine`

- Physical and environmental protection policy

- procedures addressing physical access control

- list of security safeguards to detect/prevent physical tampering or alteration of system hardware components

- system security plan

- other relevant documents or records

#### INTERVIEW — `pe-3.5_asm-interview`

- Organizational personnel with physical access control responsibilities

- organizational personnel with information security responsibilities

#### TEST — `pe-3.5_asm-test`

- Organizational processes to detect/prevent physical tampering or alteration of system hardware components

- mechanisms/security safeguards supporting and/or implementing the detection/prevention of physical tampering/alternation of system hardware components

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pe-3.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pe-3`.

- Catalog relationship **related**: `sa-16`.

- Catalog relationship **related**: `sr-9`.

- Catalog relationship **related**: `sr-11`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
