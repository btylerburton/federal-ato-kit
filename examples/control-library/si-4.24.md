---
title: "SI-4.24 \u2014 Indicators of Compromise"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-4.24 — Indicators of Compromise

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Indicators of compromise (IOC) are forensic artifacts from intrusions that are identified on organizational systems at the host or network level. IOCs provide valuable information on systems that have been compromised. IOCs can include the creation of registry key values. IOCs for network traffic include Universal Resource Locator or protocol elements that indicate malicious code command and control servers. The rapid distribution and adoption of IOCs can improve information security by reducing the time that systems and organizations are vulnerable to the same exploit or attack. Threat indicators, signatures, tactics, techniques, procedures, and other indicators of compromise may be available via government and non-government cooperatives, including the Forum of Incident Response and Security Teams, the United States Computer Emergency Readiness Team, the Defense Industrial Base Cybersecurity Information Sharing Program, and the CERT Coordination Center.

### Requirements and exact statement parts

- `si-4.24_smt`: Discover, collect, and distribute to [PARAM si-04.24_odp.02] , indicators of compromise provided by [PARAM si-04.24_odp.01].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-4.24_smt — Discover, collect, and distribute to [PARAM si-04.24_odp.02] , indicators of compromise provided by [PARAM si-04.24_odp.01].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-04.24_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-04.24_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-4.24_smt` — For “Discover, collect, and distribute to [PARAM si-04.24_odp.02] , indicators of compromise provided by [PARAM si-04.24_odp.01].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-04.24_odp.01` — What approved value applies to **sources**? Record the value, scope, approving authority, and decision source.

  - Catalog context: sources that provide indicators of compromise are defined;

- `si-04.24_odp.02` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to whom indicators of compromise are to be distributed is/are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-4.24_obj-1` (si-4.24_smt): indicators of compromise provided by [PARAM si-04.24_odp.01] are discovered;

- `si-4.24_obj-2` (si-4.24_smt): indicators of compromise provided by [PARAM si-04.24_odp.01] are collected;

- `si-4.24_obj-3` (si-4.24_smt): indicators of compromise provided by [PARAM si-04.24_odp.01] are distributed to [PARAM si-04.24_odp.02].

#### EXAMINE — `si-4.24_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing system monitoring

- system design documentation

- system monitoring tools and techniques documentation

- system configuration settings and associated documentation

- system monitoring logs or records

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-4.24_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developer

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for monitoring system hosts

#### TEST — `si-4.24_asm-test`

- Organizational processes for system monitoring

- organizational processes for the discovery, collection, distribution, and use of indicators of compromise

- mechanisms supporting and/or implementing a system monitoring capability

- mechanisms supporting and/or implementing the discovery, collection, distribution, and use of indicators of compromise

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-4.24`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-4`.

- Catalog relationship **related**: `ac-18`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
