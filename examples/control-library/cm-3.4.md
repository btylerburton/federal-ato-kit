---
title: "CM-3.4 \u2014 Security and Privacy Representatives"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-3.4 — Security and Privacy Representatives

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Information security and privacy representatives include system security officers, senior agency information security officers, senior agency officials for privacy, or system privacy officers. Representation by personnel with information security and privacy expertise is important because changes to system configurations can have unintended side effects, some of which may be security- or privacy-relevant. Detecting such changes early in the process can help avoid unintended, negative consequences that could ultimately affect the security and privacy posture of systems. The configuration change control element referred to in the second organization-defined parameter reflects the change control elements defined by organizations in CM-3g (catalog reference: `#cm-3_smt.g`).

### Requirements and exact statement parts

- `cm-3.4_smt`: Require [PARAM cm-3.4_prm_1] to be members of the [PARAM cm-03.04_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-3.4_smt — Require [PARAM cm-3.4_prm_1] to be members of the [PARAM cm-03.04_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-3.4_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-03.04_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-03.04_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-03.04_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-3.4_smt` — For “Require [PARAM cm-3.4_prm_1] to be members of the [PARAM cm-03.04_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-3.4_prm_1` — What approved value applies to **organization-defined security and privacy representatives**? Record the value, scope, approving authority, and decision source.

- `cm-03.04_odp.01` — What approved value applies to **security representatives**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security representatives required to be members of the change control element are defined;

- `cm-03.04_odp.02` — What approved value applies to **privacy representatives**? Record the value, scope, approving authority, and decision source.

  - Catalog context: privacy representatives required to be members of the change control element are defined;

- `cm-03.04_odp.03` — What approved value applies to **configuration change control element**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the configuration change control element of which the security and privacy representatives are to be members is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-3.4_obj-1` (cm-3.4_smt): [PARAM cm-03.04_odp.01] are required to be members of the [PARAM cm-03.04_odp.03];

- `cm-3.4_obj-2` (cm-3.4_smt): [PARAM cm-03.04_odp.02] are required to be members of the [PARAM cm-03.04_odp.03].

#### EXAMINE — `cm-3.4_asm-examine`

- Configuration management policy

- procedures addressing system configuration change control

- configuration management plan

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `cm-3.4_asm-interview`

- Organizational personnel with configuration change control responsibilities

- organizational personnel with information security and privacy responsibilities

- members of change control board or similar

#### TEST — `cm-3.4_asm-test`

- Organizational processes for configuration change control

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-3.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
