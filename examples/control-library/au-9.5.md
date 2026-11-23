---
title: "AU-9.5 \u2014 Dual Authorization"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-9.5 — Dual Authorization

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations may choose different selection options for different types of audit information. Dual authorization mechanisms (also known as two-person control) require the approval of two authorized individuals to execute audit functions. To reduce the risk of collusion, organizations consider rotating dual authorization duties to other individuals. Organizations do not require dual authorization mechanisms when immediate responses are necessary to ensure public and environmental safety.

### Requirements and exact statement parts

- `au-9.5_smt`: Enforce dual authorization for [PARAM au-09.05_odp.01] of [PARAM au-09.05_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-9.5_smt — Enforce dual authorization for [PARAM au-09.05_odp.01] of [PARAM au-09.05_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-09.05_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter au-09.05_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-9.5_smt` — For “Enforce dual authorization for [PARAM au-09.05_odp.01] of [PARAM au-09.05_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-09.05_odp.01` — What approved value applies to **selection; choose one-or-more from: movement; deletion**? Record the value, scope, approving authority, and decision source.

- `au-09.05_odp.02` — What approved value applies to **audit information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: audit information for which dual authorization is to be enforced is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-9.5_obj` (au-9.5_smt): dual authorization is enforced for the [PARAM au-09.05_odp.01] of [PARAM au-09.05_odp.02].

#### EXAMINE — `au-9.5_asm-examine`

- Audit and accountability policy

- system security plan

- privacy plan

- access control policy and procedures

- procedures addressing protection of audit information

- system design documentation

- system configuration settings and associated documentation

- access authorizations

- system audit records

- other relevant documents or records

#### INTERVIEW — `au-9.5_asm-interview`

- Organizational personnel with audit and accountability responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

#### TEST — `au-9.5_asm-test`

- Mechanisms implementing the enforcement of dual authorization

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-9.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `au-9`.

- Catalog relationship **related**: `ac-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
