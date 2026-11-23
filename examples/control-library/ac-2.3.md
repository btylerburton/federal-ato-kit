---
title: "AC-2.3 \u2014 Disable Accounts"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-2.3 — Disable Accounts

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Disabling expired, inactive, or otherwise anomalous accounts supports the concepts of least privilege and least functionality which reduce the attack surface of the system.

### Requirements and exact statement parts

- `ac-2.3_smt`: Disable accounts within [PARAM ac-02.03_odp.01] when the accounts:

- `ac-2.3_smt.a`: Have expired;

- `ac-2.3_smt.b`: Are no longer associated with a user or individual;

- `ac-2.3_smt.c`: Are in violation of organizational policy; or

- `ac-2.3_smt.d`: Have been inactive for [PARAM ac-02.03_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-2.3_smt — Disable accounts within [PARAM ac-02.03_odp.01] when the accounts:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2.3_smt.a — Have expired;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2.3_smt.b — Are no longer associated with a user or individual;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2.3_smt.c — Are in violation of organizational policy; or
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2.3_smt.d — Have been inactive for [PARAM ac-02.03_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-02.03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-02.03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-2.3_smt` — For “Disable accounts within [PARAM ac-02.03_odp.01] when the accounts:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2.3_smt.a` — For “Have expired;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2.3_smt.b` — For “Are no longer associated with a user or individual;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2.3_smt.c` — For “Are in violation of organizational policy; or”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2.3_smt.d` — For “Have been inactive for [PARAM ac-02.03_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-02.03_odp.01` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period within which to disable accounts is defined;

- `ac-02.03_odp.02` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period for account inactivity before disabling is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-2.3_obj.a` (ac-2.3_smt.a): accounts are disabled within [PARAM ac-02.03_odp.01] when the accounts have expired;

- `ac-2.3_obj.b` (ac-2.3_smt.b): accounts are disabled within [PARAM ac-02.03_odp.01] when the accounts are no longer associated with a user or individual;

- `ac-2.3_obj.c` (ac-2.3_smt.c): accounts are disabled within [PARAM ac-02.03_odp.01] when the accounts are in violation of organizational policy;

- `ac-2.3_obj.d` (ac-2.3_smt.d): accounts are disabled within [PARAM ac-02.03_odp.01] when the accounts have been inactive for [PARAM ac-02.03_odp.02].

#### EXAMINE — `ac-2.3_asm-examine`

- Access control policy

- procedures for addressing account management

- system security plan

- system design documentation

- system configuration settings and associated documentation

- system-generated list of accounts removed

- system-generated list of emergency accounts disabled

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-2.3_asm-interview`

- Organizational personnel with account management responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

- system developers

#### TEST — `ac-2.3_asm-test`

- Mechanisms for implementing account management functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-2.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
