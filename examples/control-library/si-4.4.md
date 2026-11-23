---
title: "SI-4.4 \u2014 Inbound and Outbound Communications Traffic"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-4.4 — Inbound and Outbound Communications Traffic

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Unusual or unauthorized activities or conditions related to system inbound and outbound communications traffic includes internal traffic that indicates the presence of malicious code or unauthorized use of legitimate code or credentials within organizational systems or propagating among system components, signaling to external systems, and the unauthorized exporting of information. Evidence of malicious code or unauthorized use of legitimate code or credentials is used to identify potentially compromised systems or system components.

### Requirements and exact statement parts

- `si-4.4_smt`: Statement grouping; see child parts.

- `si-4.4_smt.a`: Determine criteria for unusual or unauthorized activities or conditions for inbound and outbound communications traffic;

- `si-4.4_smt.b`: Monitor inbound and outbound communications traffic [PARAM si-4.4_prm_1] for [PARAM si-4.4_prm_2].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-4.4_smt.a — Determine criteria for unusual or unauthorized activities or conditions for inbound and outbound communications traffic;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-4.4_smt.b — Monitor inbound and outbound communications traffic [PARAM si-4.4_prm_1] for [PARAM si-4.4_prm_2].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-4.4_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-4.4_prm_2: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-04.04_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-04.04_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-04.04_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-04.04_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-4.4_smt.a` — For “Determine criteria for unusual or unauthorized activities or conditions for inbound and outbound communications traffic;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-4.4_smt.b` — For “Monitor inbound and outbound communications traffic [PARAM si-4.4_prm_1] for [PARAM si-4.4_prm_2].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-4.4_prm_1` — What approved value applies to **organization-defined frequency**? Record the value, scope, approving authority, and decision source.

- `si-4.4_prm_2` — What approved value applies to **organization-defined unusual or unauthorized activities or conditions**? Record the value, scope, approving authority, and decision source.

- `si-04.04_odp.01` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which to monitor inbound communications traffic for unusual or unauthorized activities or conditions is defined;

- `si-04.04_odp.02` — What approved value applies to **unusual or unauthorized activities or conditions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: unusual or unauthorized activities or conditions that are to be monitored in inbound communications traffic are defined;

- `si-04.04_odp.03` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which to monitor outbound communications traffic for unusual or unauthorized activities or conditions is defined;

- `si-04.04_odp.04` — What approved value applies to **unusual or unauthorized activities or conditions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: unusual or unauthorized activities or conditions that are to be monitored in outbound communications traffic are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-4.4_obj.a-1` (si-4.4_smt.a): criteria for unusual or unauthorized activities or conditions for inbound communications traffic are defined;

- `si-4.4_obj.a-2` (si-4.4_smt.a): criteria for unusual or unauthorized activities or conditions for outbound communications traffic are defined;

- `si-4.4_obj.b-1` (si-4.4_smt.b): inbound communications traffic is monitored [PARAM si-04.04_odp.01] for [PARAM si-04.04_odp.02];

- `si-4.4_obj.b-2` (si-4.4_smt.b): outbound communications traffic is monitored [PARAM si-04.04_odp.03] for [PARAM si-04.04_odp.04].

#### EXAMINE — `si-4.4_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing system monitoring tools and techniques

- system design documentation

- system monitoring tools and techniques documentation

- system configuration settings and associated documentation

- system protocols

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-4.4_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for monitoring the system

- organizational personnel responsible for the intrusion detection system

#### TEST — `si-4.4_asm-test`

- Organizational processes for intrusion detection and system monitoring

- mechanisms supporting and/or implementing intrusion detection and system monitoring capabilities

- mechanisms supporting and/or implementing the monitoring of inbound and outbound communications traffic

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-4.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
