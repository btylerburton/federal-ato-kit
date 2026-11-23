---
title: "AC-2.2 \u2014 Automated Temporary and Emergency Account Management"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-2.2 — Automated Temporary and Emergency Account Management

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Management of temporary and emergency accounts includes the removal or disabling of such accounts automatically after a predefined time period rather than at the convenience of the system administrator. Automatic removal or disabling of accounts provides a more consistent implementation.

### Requirements and exact statement parts

- `ac-2.2_smt`: Automatically [PARAM ac-02.02_odp.01] temporary and emergency accounts after [PARAM ac-02.02_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-2.2_smt — Automatically [PARAM ac-02.02_odp.01] temporary and emergency accounts after [PARAM ac-02.02_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-02.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-02.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-2.2_smt` — For “Automatically [PARAM ac-02.02_odp.01] temporary and emergency accounts after [PARAM ac-02.02_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-02.02_odp.01` — What approved value applies to **selection; choose one from: remove; disable**? Record the value, scope, approving authority, and decision source.

- `ac-02.02_odp.02` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the time period after which to automatically remove or disable temporary or emergency accounts is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-2.2_obj` (ac-2.2_smt): temporary and emergency accounts are automatically [PARAM ac-02.02_odp.01] after [PARAM ac-02.02_odp.02].

#### EXAMINE — `ac-2.2_asm-examine`

- Access control policy

- procedures for addressing account management

- system design documentation

- system configuration settings and associated documentation

- system-generated list of temporary accounts removed and/or disabled

- system-generated list of emergency accounts removed and/or disabled

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-2.2_asm-interview`

- Organizational personnel with account management responsibilities

- system/network administrators

- organizational personnel with information security with information security responsibilities

- system developers

#### TEST — `ac-2.2_asm-test`

- Automated mechanisms for implementing account management functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-2.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
