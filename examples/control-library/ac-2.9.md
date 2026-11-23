---
title: "AC-2.9 \u2014 Restrictions on Use of Shared and Group Accounts"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-2.9 — Restrictions on Use of Shared and Group Accounts

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Before permitting the use of shared or group accounts, organizations consider the increased risk due to the lack of accountability with such accounts.

### Requirements and exact statement parts

- `ac-2.9_smt`: Only permit the use of shared and group accounts that meet [PARAM ac-02.09_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-2.9_smt — Only permit the use of shared and group accounts that meet [PARAM ac-02.09_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-02.09_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-2.9_smt` — For “Only permit the use of shared and group accounts that meet [PARAM ac-02.09_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-02.09_odp` — What approved value applies to **conditions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: conditions for establishing shared and group accounts are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-2.9_obj` (ac-2.9_smt): the use of shared and group accounts is only permitted if [PARAM ac-02.09_odp] are met.

#### EXAMINE — `ac-2.9_asm-examine`

- Access control policy

- procedures addressing account management

- system design documentation

- system configuration settings and associated documentation

- system-generated list of shared/group accounts and associated roles

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-2.9_asm-interview`

- Organizational personnel with account management responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

#### TEST — `ac-2.9_asm-test`

- Mechanisms implementing management of shared/group accounts

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-2.9`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
