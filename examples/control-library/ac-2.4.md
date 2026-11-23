---
title: "AC-2.4 \u2014 Automated Audit Actions"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-2.4 — Automated Audit Actions

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Account management audit records are defined in accordance with AU-02 (catalog reference: `#au-2`) and reviewed, analyzed, and reported in accordance with AU-06 (catalog reference: `#au-6`).

### Requirements and exact statement parts

- `ac-2.4_smt`: Automatically audit account creation, modification, enabling, disabling, and removal actions.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-2.4_smt — Automatically audit account creation, modification, enabling, disabling, and removal actions.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ac-2.4_smt` — For “Automatically audit account creation, modification, enabling, disabling, and removal actions.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-2.4_obj-1` (ac-2.4_smt): account creation is automatically audited;

- `ac-2.4_obj-2` (ac-2.4_smt): account modification is automatically audited;

- `ac-2.4_obj-3` (ac-2.4_smt): account enabling is automatically audited;

- `ac-2.4_obj-4` (ac-2.4_smt): account disabling is automatically audited;

- `ac-2.4_obj-5` (ac-2.4_smt): account removal actions are automatically audited.

#### EXAMINE — `ac-2.4_asm-examine`

- Access control policy

- procedures addressing account management

- system design documentation

- system configuration settings and associated documentation

- notifications/alerts of account creation, modification, enabling, disabling, and removal actions

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-2.4_asm-interview`

- Organizational personnel with account management responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

#### TEST — `ac-2.4_asm-test`

- Automated mechanisms implementing account management functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-2.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-2`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
