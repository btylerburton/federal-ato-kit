---
title: "SI-4.14 \u2014 Wireless Intrusion Detection"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-4.14 — Wireless Intrusion Detection

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Wireless signals may radiate beyond organizational facilities. Organizations proactively search for unauthorized wireless connections, including the conduct of thorough scans for unauthorized wireless access points. Wireless scans are not limited to those areas within facilities containing systems but also include areas outside of facilities to verify that unauthorized wireless access points are not connected to organizational systems.

### Requirements and exact statement parts

- `si-4.14_smt`: Employ a wireless intrusion detection system to identify rogue wireless devices and to detect attack attempts and potential compromises or breaches to the system.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-4.14_smt — Employ a wireless intrusion detection system to identify rogue wireless devices and to detect attack attempts and potential compromises or breaches to the system.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `si-4.14_smt` — For “Employ a wireless intrusion detection system to identify rogue wireless devices and to detect attack attempts and potential compromises or breaches to the system.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-4.14_obj-1` (si-4.14_smt): a wireless intrusion detection system is employed to identify rogue wireless devices;

- `si-4.14_obj-2` (si-4.14_smt): a wireless intrusion detection system is employed to detect attack attempts on the system;

- `si-4.14_obj-3` (si-4.14_smt): a wireless intrusion detection system is employed to detect potential compromises or breaches to the system.

#### EXAMINE — `si-4.14_asm-examine`

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

#### INTERVIEW — `si-4.14_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for monitoring the system

- organizational personnel responsible for the intrusion detection system

#### TEST — `si-4.14_asm-test`

- Organizational processes for intrusion detection

- mechanisms supporting and/or implementing a wireless intrusion detection capability

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-4.14`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-4`.

- Catalog relationship **related**: `ac-18`.

- Catalog relationship **related**: `ia-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
