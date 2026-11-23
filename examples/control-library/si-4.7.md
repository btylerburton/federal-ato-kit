---
title: "SI-4.7 \u2014 Automated Response to Suspicious Events"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-4.7 — Automated Response to Suspicious Events

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Least-disruptive actions include initiating requests for human responses.

### Requirements and exact statement parts

- `si-4.7_smt`: Statement grouping; see child parts.

- `si-4.7_smt.a`: Notify [PARAM si-04.07_odp.01] of detected suspicious events; and

- `si-4.7_smt.b`: Take the following actions upon detection: [PARAM si-04.07_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-4.7_smt.a — Notify [PARAM si-04.07_odp.01] of detected suspicious events; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-4.7_smt.b — Take the following actions upon detection: [PARAM si-04.07_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-04.07_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-04.07_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-4.7_smt.a` — For “Notify [PARAM si-04.07_odp.01] of detected suspicious events; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-4.7_smt.b` — For “Take the following actions upon detection: [PARAM si-04.07_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-04.07_odp.01` — What approved value applies to **incident response personnel**? Record the value, scope, approving authority, and decision source.

  - Catalog context: incident response personnel (identified by name and/or by role) to be notified of detected suspicious events is/are defined;

- `si-04.07_odp.02` — What approved value applies to **least-disruptive actions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: least-disruptive actions to terminate suspicious events are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-4.7_obj.a` (si-4.7_smt.a): [PARAM si-04.07_odp.01] are notified of detected suspicious events;

- `si-4.7_obj.b` (si-4.7_smt.b): [PARAM si-04.07_odp.02] are taken upon the detection of suspicious events.

#### EXAMINE — `si-4.7_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing system monitoring tools and techniques

- system design documentation

- system monitoring tools and techniques documentation

- system configuration settings and associated documentation

- alerts and notifications generated based on detected suspicious events

- records of actions taken to terminate suspicious events

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-4.7_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developers

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for monitoring the system

- organizational personnel responsible for the intrusion detection system

#### TEST — `si-4.7_asm-test`

- Organizational processes for intrusion detection and system monitoring

- mechanisms supporting and/or implementing intrusion detection and system monitoring capabilities

- mechanisms supporting and/or implementing notifications to incident response personnel

- mechanisms supporting and/or implementing actions to terminate suspicious events

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-4.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
