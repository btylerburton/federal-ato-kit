---
title: "PE-5 \u2014 Access Control for Output Devices"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PE-5 — Access Control for Output Devices

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Controlling physical access to output devices includes placing output devices in locked rooms or other secured areas with keypad or card reader access controls and allowing access to authorized individuals only, placing output devices in locations that can be monitored by personnel, installing monitor or screen filters, and using headphones. Examples of output devices include monitors, printers, scanners, audio devices, facsimile machines, and copiers.

### Requirements and exact statement parts

- `pe-5_smt`: Control physical access to output from [PARAM pe-05_odp] to prevent unauthorized individuals from obtaining the output.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pe-5_smt — Control physical access to output from [PARAM pe-05_odp] to prevent unauthorized individuals from obtaining the output.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pe-05_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pe-5_smt` — For “Control physical access to output from [PARAM pe-05_odp] to prevent unauthorized individuals from obtaining the output.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pe-05_odp` — What approved value applies to **output devices**? Record the value, scope, approving authority, and decision source.

  - Catalog context: output devices that require physical access control to output are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pe-5_obj` (pe-5_smt): physical access to output from [PARAM pe-05_odp] is controlled to prevent unauthorized individuals from obtaining the output.

#### EXAMINE — `pe-5_asm-examine`

- Physical and environmental protection policy

- procedures addressing access control for display medium

- facility layout of system components

- actual displays from system components

- list of output devices and associated outputs requiring physical access controls

- physical access control logs or records for areas containing output devices and related outputs

- system security plan

- other relevant documents or records

#### INTERVIEW — `pe-5_asm-interview`

- Organizational personnel with physical access control responsibilities

- organizational personnel with information security responsibilities

#### TEST — `pe-5_asm-test`

- Organizational processes for access control to output devices

- mechanisms supporting and/or implementing access control to output devices

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pe-5`. The library index records the exact source revision and hash.

- [IR 8023](https://doi.org/10.6028/NIST.IR.8023)

- Catalog relationship **related**: `pe-2`.

- Catalog relationship **related**: `pe-3`.

- Catalog relationship **related**: `pe-4`.

- Catalog relationship **related**: `pe-18`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
