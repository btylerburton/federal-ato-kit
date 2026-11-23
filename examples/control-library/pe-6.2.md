---
title: "PE-6.2 \u2014 Automated Intrusion Recognition and Responses"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PE-6.2 — Automated Intrusion Recognition and Responses

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Response actions can include notifying selected organizational personnel or law enforcement personnel. Automated mechanisms implemented to initiate response actions include system alert notifications, email and text messages, and activating door locking mechanisms. Physical access monitoring can be coordinated with intrusion detection systems and system monitoring capabilities to provide integrated threat coverage for the organization.

### Requirements and exact statement parts

- `pe-6.2_smt`: Recognize [PARAM pe-06.02_odp.01] and initiate [PARAM pe-06.02_odp.02] using [PARAM pe-06.02_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pe-6.2_smt — Recognize [PARAM pe-06.02_odp.01] and initiate [PARAM pe-06.02_odp.02] using [PARAM pe-06.02_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pe-06.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pe-06.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pe-06.02_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pe-6.2_smt` — For “Recognize [PARAM pe-06.02_odp.01] and initiate [PARAM pe-06.02_odp.02] using [PARAM pe-06.02_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pe-06.02_odp.01` — What approved value applies to **classes or types of intrusions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: classes or types of intrusions to be recognized by automated mechanisms are defined;

- `pe-06.02_odp.02` — What approved value applies to **response actions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: response actions to be initiated by automated mechanisms when organization-defined classes or types of intrusions are recognized are defined;

- `pe-06.02_odp.03` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used to recognize classes or types of intrusions and initiate response actions (defined in PE-06(02)_ODP (catalog reference: `#pe-06.02_odp.02`)) are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pe-6.2_obj-1` (pe-6.2_smt): [PARAM pe-06.02_odp.01] are recognized;

- `pe-6.2_obj-2` (pe-6.2_smt): [PARAM pe-06.02_odp.02] are initiated using [PARAM pe-06.02_odp.03].

#### EXAMINE — `pe-6.2_asm-examine`

- Physical and environmental protection policy

- procedures addressing physical access monitoring

- system design documentation

- system configuration settings and associated documentation

- system audit records

- list of response actions to be initiated when specific classes/types of intrusions are recognized

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `pe-6.2_asm-interview`

- Organizational personnel with physical access monitoring responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `pe-6.2_asm-test`

- Organizational processes for monitoring physical access

- automated mechanisms supporting and/or implementing physical access monitoring

- automated mechanisms supporting and/or implementing recognition of classes/types of intrusions and initiation of a response

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pe-6.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pe-6`.

- Catalog relationship **related**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
