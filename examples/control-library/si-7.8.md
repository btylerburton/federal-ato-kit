---
title: "SI-7.8 \u2014 Auditing Capability for Significant Events"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-7.8 — Auditing Capability for Significant Events

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations select response actions based on types of software, specific software, or information for which there are potential integrity violations.

### Requirements and exact statement parts

- `si-7.8_smt`: Upon detection of a potential integrity violation, provide the capability to audit the event and initiate the following actions: [PARAM si-07.08_odp.01].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-7.8_smt — Upon detection of a potential integrity violation, provide the capability to audit the event and initiate the following actions: [PARAM si-07.08_odp.01].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-07.08_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07.08_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07.08_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-7.8_smt` — For “Upon detection of a potential integrity violation, provide the capability to audit the event and initiate the following actions: [PARAM si-07.08_odp.01].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-07.08_odp.01` — What approved value applies to **selection; choose one-or-more from: generate an audit record; alert current user; alert [PARAM si-07.08_odp.02]; [PARAM si-07.08_odp.03]**? Record the value, scope, approving authority, and decision source.

- `si-07.08_odp.02` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to be alerted upon the detection of a potential integrity violation is/are defined (if selected);

- `si-07.08_odp.03` — What approved value applies to **other actions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: other actions to be taken upon the detection of a potential integrity violation are defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-7.8_obj-1` (si-7.8_smt): the capability to audit an event upon the detection of a potential integrity violation is provided;

- `si-7.8_obj-2` (si-7.8_smt): [PARAM si-07.08_odp.01] is/are initiated upon the detection of a potential integrity violation.

#### EXAMINE — `si-7.8_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing software, firmware, and information integrity

- system design documentation

- system configuration settings and associated documentation

- integrity verification tools and associated documentation

- records of integrity scans

- incident response records

- list of security-relevant changes to the system

- automated tools supporting alerts and notifications if unauthorized security changes are detected

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-7.8_asm-interview`

- Organizational personnel responsible for software, firmware, and/or information integrity

- organizational personnel with information security responsibilities

- system/network administrators

- system developer

#### TEST — `si-7.8_asm-test`

- Software, firmware, and information integrity verification tools

- mechanisms supporting and/or implementing the capability to audit potential integrity violations

- mechanisms supporting and/or implementing alerts about potential integrity violations

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-7.8`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-7`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
