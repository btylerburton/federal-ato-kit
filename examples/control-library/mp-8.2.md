---
title: "MP-8.2 \u2014 Equipment Testing"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MP-8.2 — Equipment Testing

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

None.

### Requirements and exact statement parts

- `mp-8.2_smt`: Test downgrading equipment and procedures [PARAM mp-8.2_prm_1] to ensure that downgrading actions are being achieved.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for mp-8.2_smt — Test downgrading equipment and procedures [PARAM mp-8.2_prm_1] to ensure that downgrading actions are being achieved.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter mp-8.2_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-08.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-08.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `mp-8.2_smt` — For “Test downgrading equipment and procedures [PARAM mp-8.2_prm_1] to ensure that downgrading actions are being achieved.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `mp-8.2_prm_1` — What approved value applies to **organization-defined frequency**? Record the value, scope, approving authority, and decision source.

- `mp-08.02_odp.01` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency with which to test downgrading equipment is defined;

- `mp-08.02_odp.02` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency with which to test downgrading procedures is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `mp-8.2_obj-1` (mp-8.2_smt): downgrading equipment is tested [PARAM mp-08.02_odp.01] to ensure that downgrading actions are being achieved;

- `mp-8.2_obj-2` (mp-8.2_smt): downgrading procedures are tested [PARAM mp-08.02_odp.02] to ensure that downgrading actions are being achieved.

#### EXAMINE — `mp-8.2_asm-examine`

- System media protection policy

- procedures addressing media downgrading

- procedures addressing testing of media downgrading equipment

- results of downgrading equipment and procedures testing

- records of media downgrading

- audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `mp-8.2_asm-interview`

- Organizational personnel with system media downgrading responsibilities

- organizational personnel with information security responsibilities

#### TEST — `mp-8.2_asm-test`

- Organizational processes for media downgrading

- mechanisms supporting and/or implementing media downgrading

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `mp-8.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `mp-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
