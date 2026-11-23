---
title: "PE-6 \u2014 Monitoring Physical Access"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PE-6 — Monitoring Physical Access

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Physical access monitoring includes publicly accessible areas within organizational facilities. Examples of physical access monitoring include the employment of guards, video surveillance equipment (i.e., cameras), and sensor devices. Reviewing physical access logs can help identify suspicious activity, anomalous events, or potential threats. The reviews can be supported by audit logging controls, such as AU-2 (catalog reference: `#au-2`) , if the access logs are part of an automated system. Organizational incident response capabilities include investigations of physical security incidents and responses to the incidents. Incidents include security violations or suspicious physical access activities. Suspicious physical access activities include accesses outside of normal work hours, repeated accesses to areas not normally accessed, accesses for unusual lengths of time, and out-of-sequence accesses.

### Requirements and exact statement parts

- `pe-6_smt`: Statement grouping; see child parts.

- `pe-6_smt.a`: Monitor physical access to the facility where the system resides to detect and respond to physical security incidents;

- `pe-6_smt.b`: Review physical access logs [PARAM pe-06_odp.01] and upon occurrence of [PARAM pe-06_odp.02] ; and

- `pe-6_smt.c`: Coordinate results of reviews and investigations with the organizational incident response capability.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pe-6_smt.a — Monitor physical access to the facility where the system resides to detect and respond to physical security incidents;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pe-6_smt.b — Review physical access logs [PARAM pe-06_odp.01] and upon occurrence of [PARAM pe-06_odp.02] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pe-6_smt.c — Coordinate results of reviews and investigations with the organizational incident response capability.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pe-06_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pe-06_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pe-6_smt.a` — For “Monitor physical access to the facility where the system resides to detect and respond to physical security incidents;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pe-6_smt.b` — For “Review physical access logs [PARAM pe-06_odp.01] and upon occurrence of [PARAM pe-06_odp.02] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pe-6_smt.c` — For “Coordinate results of reviews and investigations with the organizational incident response capability.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pe-06_odp.01` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which to review physical access logs is defined;

- `pe-06_odp.02` — What approved value applies to **events**? Record the value, scope, approving authority, and decision source.

  - Catalog context: events or potential indication of events requiring physical access logs to be reviewed are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pe-6_obj.a` (pe-6_smt.a): physical access to the facility where the system resides is monitored to detect and respond to physical security incidents;

- `pe-6_obj.b-1` (pe-6_smt.b): physical access logs are reviewed [PARAM pe-06_odp.01];

- `pe-6_obj.b-2` (pe-6_smt.b): physical access logs are reviewed upon occurrence of [PARAM pe-06_odp.02];

- `pe-6_obj.c-1` (pe-6_smt.c): results of reviews are coordinated with organizational incident response capabilities;

- `pe-6_obj.c-2` (pe-6_smt.c): results of investigations are coordinated with organizational incident response capabilities.

#### EXAMINE — `pe-6_asm-examine`

- Physical and environmental protection policy

- procedures addressing physical access monitoring

- physical access logs or records

- physical access monitoring records

- physical access log reviews

- system security plan

- other relevant documents or records

#### INTERVIEW — `pe-6_asm-interview`

- Organizational personnel with physical access monitoring responsibilities

- organizational personnel with incident response responsibilities

- organizational personnel with information security responsibilities

#### TEST — `pe-6_asm-test`

- Organizational processes for monitoring physical access

- mechanisms supporting and/or implementing physical access monitoring

- mechanisms supporting and/or implementing the review of physical access logs

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pe-6`. The library index records the exact source revision and hash.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-9`.

- Catalog relationship **related**: `au-12`.

- Catalog relationship **related**: `ca-7`.

- Catalog relationship **related**: `cp-10`.

- Catalog relationship **related**: `ir-4`.

- Catalog relationship **related**: `ir-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
