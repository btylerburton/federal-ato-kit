---
title: "CM-8.8 \u2014 Automated Location Tracking"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-8.8 — Automated Location Tracking

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The use of automated mechanisms to track the location of system components can increase the accuracy of component inventories. Such capability may help organizations rapidly identify the location and responsible individuals of system components that have been compromised, breached, or are otherwise in need of mitigation actions. The use of tracking mechanisms can be coordinated with senior agency officials for privacy if there are implications that affect individual privacy.

### Requirements and exact statement parts

- `cm-8.8_smt`: Support the tracking of system components by geographic location using [PARAM cm-08.08_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-8.8_smt — Support the tracking of system components by geographic location using [PARAM cm-08.08_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-08.08_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-8.8_smt` — For “Support the tracking of system components by geographic location using [PARAM cm-08.08_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-08.08_odp` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms for tracking components are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-8.8_obj` (cm-8.8_smt): [PARAM cm-08.08_odp] are used to support the tracking of system components by geographic location.

#### EXAMINE — `cm-8.8_asm-examine`

- Configuration management policy

- procedures addressing system component inventory

- configuration management plan

- system design documentation

- system component inventory

- system configuration settings and associated documentation

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `cm-8.8_asm-interview`

- Organizational personnel with component inventory management responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

- system developers

#### TEST — `cm-8.8_asm-test`

- Organizational processes for managing the system component inventory

- automated mechanisms supporting and/or implementing system component inventory

- automated mechanisms supporting and/or implementing tracking of components by geographic locations

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-8.8`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
