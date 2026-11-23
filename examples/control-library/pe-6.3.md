---
title: "PE-6.3 \u2014 Video Surveillance"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PE-6.3 — Video Surveillance

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Video surveillance focuses on recording activity in specified areas for the purposes of subsequent review, if circumstances so warrant. Video recordings are typically reviewed to detect anomalous events or incidents. Monitoring the surveillance video is not required, although organizations may choose to do so. There may be legal considerations when performing and retaining video surveillance, especially if such surveillance is in a public location.

### Requirements and exact statement parts

- `pe-6.3_smt`: Statement grouping; see child parts.

- `pe-6.3_smt.a`: Employ video surveillance of [PARAM pe-06.03_odp.01];

- `pe-6.3_smt.b`: Review video recordings [PARAM pe-06.03_odp.02] ; and

- `pe-6.3_smt.c`: Retain video recordings for [PARAM pe-06.03_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pe-6.3_smt.a — Employ video surveillance of [PARAM pe-06.03_odp.01];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pe-6.3_smt.b — Review video recordings [PARAM pe-06.03_odp.02] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pe-6.3_smt.c — Retain video recordings for [PARAM pe-06.03_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pe-06.03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pe-06.03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pe-06.03_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pe-6.3_smt.a` — For “Employ video surveillance of [PARAM pe-06.03_odp.01];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pe-6.3_smt.b` — For “Review video recordings [PARAM pe-06.03_odp.02] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pe-6.3_smt.c` — For “Retain video recordings for [PARAM pe-06.03_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pe-06.03_odp.01` — What approved value applies to **operational areas**? Record the value, scope, approving authority, and decision source.

  - Catalog context: operational areas where video surveillance is to be employed are defined;

- `pe-06.03_odp.02` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to review video recordings is defined;

- `pe-06.03_odp.03` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period for which to retain video recordings is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pe-6.3_obj.a` (pe-6.3_smt.a): video surveillance of [PARAM pe-06.03_odp.01] is employed;

- `pe-6.3_obj.b` (pe-6.3_smt.b): video recordings are reviewed [PARAM pe-06.03_odp.02];

- `pe-6.3_obj.c` (pe-6.3_smt.c): video recordings are retained for [PARAM pe-06.03_odp.03].

#### EXAMINE — `pe-6.3_asm-examine`

- Physical and environmental protection policy

- procedures addressing physical access monitoring

- video surveillance equipment used to monitor operational areas

- video recordings of operational areas where video surveillance is employed

- video surveillance equipment logs or records

- system security plan

- privacy plan

- privacy impact assessment

- privacy risk assessment documentation

- other relevant documents or records

#### INTERVIEW — `pe-6.3_asm-interview`

- Organizational personnel with physical access monitoring responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `pe-6.3_asm-test`

- Organizational processes for monitoring physical access

- mechanisms supporting and/or implementing physical access monitoring

- mechanisms supporting and/or implementing video surveillance

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pe-6.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pe-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
