---
title: "SI-4.10 \u2014 Visibility of Encrypted Communications"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-4.10 — Visibility of Encrypted Communications

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations balance the need to encrypt communications traffic to protect data confidentiality with the need to maintain visibility into such traffic from a monitoring perspective. Organizations determine whether the visibility requirement applies to internal encrypted traffic, encrypted traffic intended for external destinations, or a subset of the traffic types.

### Requirements and exact statement parts

- `si-4.10_smt`: Make provisions so that [PARAM si-04.10_odp.01] is visible to [PARAM si-04.10_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-4.10_smt — Make provisions so that [PARAM si-04.10_odp.01] is visible to [PARAM si-04.10_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-04.10_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-04.10_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-4.10_smt` — For “Make provisions so that [PARAM si-04.10_odp.01] is visible to [PARAM si-04.10_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-04.10_odp.01` — What approved value applies to **encrypted communications traffic**? Record the value, scope, approving authority, and decision source.

  - Catalog context: encrypted communications traffic to be made visible to system monitoring tools and mechanisms is defined;

- `si-04.10_odp.02` — What approved value applies to **system monitoring tools and mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system monitoring tools and mechanisms to be provided access to encrypted communications traffic are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-4.10_obj` (si-4.10_smt): provisions are made so that [PARAM si-04.10_odp.01] is visible to [PARAM si-04.10_odp.02].

#### EXAMINE — `si-4.10_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing system monitoring tools and techniques

- system design documentation

- system monitoring tools and techniques documentation

- system configuration settings and associated documentation

- system protocols

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-4.10_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for monitoring the system

- organizational personnel responsible for the intrusion detection system

#### TEST — `si-4.10_asm-test`

- Organizational processes for intrusion detection and system monitoring

- mechanisms supporting and/or implementing intrusion detection and system monitoring capabilities

- mechanisms supporting and/or implementing the visibility of encrypted communications traffic to monitoring tools

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-4.10`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
