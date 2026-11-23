---
title: "PE-8 \u2014 Visitor Access Records"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PE-8 — Visitor Access Records

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Visitor access records include the names and organizations of individuals visiting, visitor signatures, forms of identification, dates of access, entry and departure times, purpose of visits, and the names and organizations of individuals visited. Access record reviews determine if access authorizations are current and are still required to support organizational mission and business functions. Access records are not required for publicly accessible areas.

### Requirements and exact statement parts

- `pe-8_smt`: Statement grouping; see child parts.

- `pe-8_smt.a`: Maintain visitor access records to the facility where the system resides for [PARAM pe-08_odp.01];

- `pe-8_smt.b`: Review visitor access records [PARAM pe-08_odp.02] ; and

- `pe-8_smt.c`: Report anomalies in visitor access records to [PARAM pe-08_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pe-8_smt.a — Maintain visitor access records to the facility where the system resides for [PARAM pe-08_odp.01];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pe-8_smt.b — Review visitor access records [PARAM pe-08_odp.02] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pe-8_smt.c — Report anomalies in visitor access records to [PARAM pe-08_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pe-08_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pe-08_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pe-08_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pe-8_smt.a` — For “Maintain visitor access records to the facility where the system resides for [PARAM pe-08_odp.01];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pe-8_smt.b` — For “Review visitor access records [PARAM pe-08_odp.02] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pe-8_smt.c` — For “Report anomalies in visitor access records to [PARAM pe-08_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pe-08_odp.01` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period for which to maintain visitor access records for the facility where the system resides is defined;

- `pe-08_odp.02` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which to review visitor access records is defined;

- `pe-08_odp.03` — What approved value applies to **personnel**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel to whom visitor access records anomalies are reported to is/are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pe-8_obj.a` (pe-8_smt.a): visitor access records for the facility where the system resides are maintained for [PARAM pe-08_odp.01];

- `pe-8_obj.b` (pe-8_smt.b): visitor access records are reviewed [PARAM pe-08_odp.02];

- `pe-8_obj.c` (pe-8_smt.c): visitor access records anomalies are reported to [PARAM pe-08_odp.03].

#### EXAMINE — `pe-8_asm-examine`

- Physical and environmental protection policy

- procedures addressing visitor access records

- visitor access control logs or records

- visitor access record or log reviews

- system security plan

- privacy plan

- privacy impact assessment

- privacy risk assessment documentation

- other relevant documents or records

#### INTERVIEW — `pe-8_asm-interview`

- Organizational personnel with visitor access record responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `pe-8_asm-test`

- Organizational processes for maintaining and reviewing visitor access records

- mechanisms supporting and/or implementing the maintenance and review of visitor access records

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pe-8`. The library index records the exact source revision and hash.

- Catalog relationship **related**: `pe-2`.

- Catalog relationship **related**: `pe-3`.

- Catalog relationship **related**: `pe-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
