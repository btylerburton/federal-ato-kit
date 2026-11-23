---
title: "SI-7.10 \u2014 Protection of Boot Firmware"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-7.10 — Protection of Boot Firmware

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Unauthorized modifications to boot firmware may indicate a sophisticated, targeted attack. These types of targeted attacks can result in a permanent denial of service or a persistent malicious code presence. These situations can occur if the firmware is corrupted or if the malicious code is embedded within the firmware. System components can protect the integrity of boot firmware in organizational systems by verifying the integrity and authenticity of all updates to the firmware prior to applying changes to the system component and preventing unauthorized processes from modifying the boot firmware.

### Requirements and exact statement parts

- `si-7.10_smt`: Implement the following mechanisms to protect the integrity of boot firmware in [PARAM si-07.10_odp.02]: [PARAM si-07.10_odp.01].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-7.10_smt — Implement the following mechanisms to protect the integrity of boot firmware in [PARAM si-07.10_odp.02]: [PARAM si-07.10_odp.01].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-07.10_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07.10_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-7.10_smt` — For “Implement the following mechanisms to protect the integrity of boot firmware in [PARAM si-07.10_odp.02]: [PARAM si-07.10_odp.01].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-07.10_odp.01` — What approved value applies to **mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: mechanisms to be implemented to protect the integrity of boot firmware in system components are defined;

- `si-07.10_odp.02` — What approved value applies to **system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system components requiring mechanisms to protect the integrity of boot firmware are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-7.10_obj` (si-7.10_smt): [PARAM si-07.10_odp.01] are implemented to protect the integrity of boot firmware in [PARAM si-07.10_odp.02].

#### EXAMINE — `si-7.10_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing software, firmware, and information integrity

- system design documentation

- system configuration settings and associated documentation

- integrity verification tools and associated documentation

- records of integrity verification scans

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-7.10_asm-interview`

- Organizational personnel responsible for software, firmware, and/or information integrity

- organizational personnel with information security responsibilities

- system/network administrators

- system developer

#### TEST — `si-7.10_asm-test`

- Software, firmware, and information integrity verification tools

- mechanisms supporting and/or implementing protection of the integrity of boot firmware

- safeguards implementing protection of the integrity of boot firmware

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-7.10`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-7`.

- Catalog relationship **related**: `si-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
