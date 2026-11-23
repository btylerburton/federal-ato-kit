---
title: "AC-2.11 \u2014 Usage Conditions"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-2.11 — Usage Conditions

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Specifying and enforcing usage conditions helps to enforce the principle of least privilege, increase user accountability, and enable effective account monitoring. Account monitoring includes alerts generated if the account is used in violation of organizational parameters. Organizations can describe specific conditions or circumstances under which system accounts can be used, such as by restricting usage to certain days of the week, time of day, or specific durations of time.

### Requirements and exact statement parts

- `ac-2.11_smt`: Enforce [PARAM ac-02.11_odp.01] for [PARAM ac-02.11_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-2.11_smt — Enforce [PARAM ac-02.11_odp.01] for [PARAM ac-02.11_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-02.11_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-02.11_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-2.11_smt` — For “Enforce [PARAM ac-02.11_odp.01] for [PARAM ac-02.11_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-02.11_odp.01` — What approved value applies to **circumstances and/or usage conditions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: circumstances and/or usage conditions to be enforced for system accounts are defined;

- `ac-02.11_odp.02` — What approved value applies to **system accounts**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system accounts subject to enforcement of circumstances and/or usage conditions are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-2.11_obj` (ac-2.11_smt): [PARAM ac-02.11_odp.01] for [PARAM ac-02.11_odp.02] are enforced.

#### EXAMINE — `ac-2.11_asm-examine`

- Access control policy

- procedures addressing account management

- system design documentation

- system configuration settings and associated documentation

- system-generated list of system accounts and associated assignments of usage circumstances and/or usage conditions

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-2.11_asm-interview`

- Organizational personnel with account management responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

- system developers

#### TEST — `ac-2.11_asm-test`

- Mechanisms implementing account management functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-2.11`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
