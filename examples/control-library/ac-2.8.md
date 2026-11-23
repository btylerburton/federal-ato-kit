---
title: "AC-2.8 \u2014 Dynamic Account Management"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-2.8 — Dynamic Account Management

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Approaches for dynamically creating, activating, managing, and deactivating system accounts rely on automatically provisioning the accounts at runtime for entities that were previously unknown. Organizations plan for the dynamic management, creation, activation, and deactivation of system accounts by establishing trust relationships, business rules, and mechanisms with appropriate authorities to validate related authorizations and privileges.

### Requirements and exact statement parts

- `ac-2.8_smt`: Create, activate, manage, and deactivate [PARAM ac-02.08_odp] dynamically.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-2.8_smt — Create, activate, manage, and deactivate [PARAM ac-02.08_odp] dynamically.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-02.08_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-2.8_smt` — For “Create, activate, manage, and deactivate [PARAM ac-02.08_odp] dynamically.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-02.08_odp` — What approved value applies to **system accounts**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system accounts that are dynamically created, activated, managed, and deactivated are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-2.8_obj-1` (ac-2.8_smt): [PARAM ac-02.08_odp] are created dynamically;

- `ac-2.8_obj-2` (ac-2.8_smt): [PARAM ac-02.08_odp] are activated dynamically;

- `ac-2.8_obj-3` (ac-2.8_smt): [PARAM ac-02.08_odp] are managed dynamically;

- `ac-2.8_obj-4` (ac-2.8_smt): [PARAM ac-02.08_odp] are deactivated dynamically.

#### EXAMINE — `ac-2.8_asm-examine`

- Access control policy

- procedures addressing account management

- system design documentation

- system configuration settings and associated documentation

- system-generated list of system accounts

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-2.8_asm-interview`

- Organizational personnel with account management responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

- system developers

#### TEST — `ac-2.8_asm-test`

- Automated mechanisms implementing account management functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-2.8`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-2`.

- Catalog relationship **related**: `ac-16`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
