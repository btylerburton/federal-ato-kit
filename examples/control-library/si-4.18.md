---
title: "SI-4.18 \u2014 Analyze Traffic and Covert Exfiltration"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-4.18 — Analyze Traffic and Covert Exfiltration

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organization-defined interior points include subnetworks and subsystems. Covert means that can be used to exfiltrate information include steganography.

### Requirements and exact statement parts

- `si-4.18_smt`: Analyze outbound communications traffic at external interfaces to the system and at the following interior points to detect covert exfiltration of information: [PARAM si-04.18_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-4.18_smt — Analyze outbound communications traffic at external interfaces to the system and at the following interior points to detect covert exfiltration of information: [PARAM si-04.18_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-04.18_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-4.18_smt` — For “Analyze outbound communications traffic at external interfaces to the system and at the following interior points to detect covert exfiltration of information: [PARAM si-04.18_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-04.18_odp` — What approved value applies to **interior points**? Record the value, scope, approving authority, and decision source.

  - Catalog context: interior points within the system where communications traffic is to be analyzed are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-4.18_obj-1` (si-4.18_smt): outbound communications traffic is analyzed at interfaces external to the system to detect covert exfiltration of information;

- `si-4.18_obj-2` (si-4.18_smt): outbound communications traffic is analyzed at [PARAM si-04.18_odp] to detect covert exfiltration of information.

#### EXAMINE — `si-4.18_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing system monitoring tools and techniques

- system design documentation

- network diagram

- system monitoring tools and techniques documentation

- system configuration settings and associated documentation

- system monitoring logs or records

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-4.18_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for monitoring the system

- organizational personnel responsible for the intrusion detection system

#### TEST — `si-4.18_asm-test`

- Organizational processes for intrusion detection and system monitoring

- mechanisms supporting and/or implementing intrusion detection and system monitoring capabilities

- mechanisms supporting and/or implementing an analysis of outbound communications traffic

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-4.18`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
