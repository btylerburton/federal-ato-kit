---
title: "SI-4.13 \u2014 Analyze Traffic and Event Patterns"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-4.13 — Analyze Traffic and Event Patterns

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Identifying and understanding common communications traffic and event patterns help organizations provide useful information to system monitoring devices to more effectively identify suspicious or anomalous traffic and events when they occur. Such information can help reduce the number of false positives and false negatives during system monitoring.

### Requirements and exact statement parts

- `si-4.13_smt`: Statement grouping; see child parts.

- `si-4.13_smt.a`: Analyze communications traffic and event patterns for the system;

- `si-4.13_smt.b`: Develop profiles representing common traffic and event patterns; and

- `si-4.13_smt.c`: Use the traffic and event profiles in tuning system-monitoring devices.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-4.13_smt.a — Analyze communications traffic and event patterns for the system;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-4.13_smt.b — Develop profiles representing common traffic and event patterns; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-4.13_smt.c — Use the traffic and event profiles in tuning system-monitoring devices.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `si-4.13_smt.a` — For “Analyze communications traffic and event patterns for the system;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-4.13_smt.b` — For “Develop profiles representing common traffic and event patterns; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-4.13_smt.c` — For “Use the traffic and event profiles in tuning system-monitoring devices.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-4.13_obj.a-1` (si-4.13_smt.a): communications traffic for the system is analyzed;

- `si-4.13_obj.a-2` (si-4.13_smt.a): event patterns for the system are analyzed;

- `si-4.13_obj.b-1` (si-4.13_smt.b): profiles representing common traffic are developed;

- `si-4.13_obj.b-2` (si-4.13_smt.b): profiles representing event patterns are developed;

- `si-4.13_obj.c-1` (si-4.13_smt.c): traffic profiles are used in tuning system-monitoring devices;

- `si-4.13_obj.c-2` (si-4.13_smt.c): event profiles are used in tuning system-monitoring devices.

#### EXAMINE — `si-4.13_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing system monitoring tools and techniques

- system design documentation

- system monitoring tools and techniques documentation

- system configuration settings and associated documentation

- list of profiles representing common traffic patterns and/or events

- system protocols documentation

- list of acceptable thresholds for false positives and false negatives

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-4.13_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for monitoring the system

- organizational personnel responsible for the intrusion detection system

#### TEST — `si-4.13_asm-test`

- Organizational processes for intrusion detection and system monitoring

- mechanisms supporting and/or implementing intrusion detection and system monitoring capabilities

- mechanisms supporting and/or implementing the analysis of communications traffic and event patterns

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-4.13`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
