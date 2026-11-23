---
title: "CP-9.7 \u2014 Dual Authorization for Deletion or Destruction"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-9.7 — Dual Authorization for Deletion or Destruction

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Dual authorization ensures that deletion or destruction of backup information cannot occur unless two qualified individuals carry out the task. Individuals deleting or destroying backup information possess the skills or expertise to determine if the proposed deletion or destruction of information reflects organizational policies and procedures. Dual authorization may also be known as two-person control. To reduce the risk of collusion, organizations consider rotating dual authorization duties to other individuals.

### Requirements and exact statement parts

- `cp-9.7_smt`: Enforce dual authorization for the deletion or destruction of [PARAM cp-09.07_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-9.7_smt — Enforce dual authorization for the deletion or destruction of [PARAM cp-09.07_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cp-09.07_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cp-9.7_smt` — For “Enforce dual authorization for the deletion or destruction of [PARAM cp-09.07_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cp-09.07_odp` — What approved value applies to **backup information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: backup information for which to enforce dual authorization in order to delete or destroy is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-9.7_obj` (cp-9.7_smt): dual authorization for the deletion or destruction of [PARAM cp-09.07_odp] is enforced.

#### EXAMINE — `cp-9.7_asm-examine`

- Contingency planning policy

- procedures addressing system backup

- contingency plan

- system design documentation

- system configuration settings and associated documentation

- system generated list of dual authorization credentials or rules

- logs or records of deletion or destruction of backup information

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-9.7_asm-interview`

- Organizational personnel with system backup responsibilities

- organizational personnel with information security responsibilities

#### TEST — `cp-9.7_asm-test`

- Mechanisms supporting and/or implementing dual authorization

- mechanisms supporting and/or implementing the deletion/destruction of backup information

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-9.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cp-9`.

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-5`.

- Catalog relationship **related**: `mp-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
