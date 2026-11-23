---
title: "SI-7.7 \u2014 Integration of Detection and Response"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-7.7 — Integration of Detection and Response

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Integrating detection and response helps to ensure that detected events are tracked, monitored, corrected, and available for historical purposes. Maintaining historical records is important for being able to identify and discern adversary actions over an extended time period and for possible legal actions. Security-relevant changes include unauthorized changes to established configuration settings or the unauthorized elevation of system privileges.

### Requirements and exact statement parts

- `si-7.7_smt`: Incorporate the detection of the following unauthorized changes into the organizational incident response capability: [PARAM si-07.07_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-7.7_smt — Incorporate the detection of the following unauthorized changes into the organizational incident response capability: [PARAM si-07.07_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-07.07_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-7.7_smt` — For “Incorporate the detection of the following unauthorized changes into the organizational incident response capability: [PARAM si-07.07_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-07.07_odp` — What approved value applies to **changes**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security-relevant changes to the system are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-7.7_obj` (si-7.7_smt): the detection of [PARAM si-07.07_odp] are incorporated into the organizational incident response capability.

#### EXAMINE — `si-7.7_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing software, firmware, and information integrity

- procedures addressing incident response

- system design documentation

- system configuration settings and associated documentation

- incident response records

- audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-7.7_asm-interview`

- Organizational personnel responsible for software, firmware, and/or information integrity

- organizational personnel with information security responsibilities

- organizational personnel with incident response responsibilities

#### TEST — `si-7.7_asm-test`

- Organizational processes for incorporating the detection of unauthorized security-relevant changes into the incident response capability

- software, firmware, and information integrity verification tools

- mechanisms supporting and/or implementing the incorporation of detection of unauthorized security-relevant changes into the incident response capability

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-7.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-7`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `ir-4`.

- Catalog relationship **related**: `ir-5`.

- Catalog relationship **related**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
