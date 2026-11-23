---
title: "AC-3.2 \u2014 Dual Authorization"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-3.2 — Dual Authorization

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Dual authorization, also known as two-person control, reduces risk related to insider threats. Dual authorization mechanisms require the approval of two authorized individuals to execute. To reduce the risk of collusion, organizations consider rotating dual authorization duties. Organizations consider the risk associated with implementing dual authorization mechanisms when immediate responses are necessary to ensure public and environmental safety.

### Requirements and exact statement parts

- `ac-3.2_smt`: Enforce dual authorization for [PARAM ac-03.02_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-3.2_smt — Enforce dual authorization for [PARAM ac-03.02_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-03.02_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-3.2_smt` — For “Enforce dual authorization for [PARAM ac-03.02_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-03.02_odp` — What approved value applies to **privileged commands and/or other actions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: privileged commands and/or other actions requiring dual authorization are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-3.2_obj` (ac-3.2_smt): dual authorization is enforced for [PARAM ac-03.02_odp].

#### EXAMINE — `ac-3.2_asm-examine`

- Access control policy

- procedures addressing access enforcement and dual authorization

- system design documentation

- system configuration settings and associated documentation

- list of privileged commands requiring dual authorization

- list of actions requiring dual authorization

- list of approved authorizations (user privileges)

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-3.2_asm-interview`

- Organizational personnel with access enforcement responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

- system developers

#### TEST — `ac-3.2_asm-test`

- Dual authorization mechanisms implementing access control policy

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-3.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-3`.

- Catalog relationship **related**: `cp-9`.

- Catalog relationship **related**: `mp-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
