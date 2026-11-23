---
title: "AC-2.7 \u2014 Privileged User Accounts"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-2.7 — Privileged User Accounts

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Privileged roles are organization-defined roles assigned to individuals that allow those individuals to perform certain security-relevant functions that ordinary users are not authorized to perform. Privileged roles include key management, account management, database administration, system and network administration, and web administration. A role-based access scheme organizes permitted system access and privileges into roles. In contrast, an attribute-based access scheme specifies allowed system access and privileges based on attributes.

### Requirements and exact statement parts

- `ac-2.7_smt`: Statement grouping; see child parts.

- `ac-2.7_smt.a`: Establish and administer privileged user accounts in accordance with [PARAM ac-02.07_odp];

- `ac-2.7_smt.b`: Monitor privileged role or attribute assignments;

- `ac-2.7_smt.c`: Monitor changes to roles or attributes; and

- `ac-2.7_smt.d`: Revoke access when privileged role or attribute assignments are no longer appropriate.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-2.7_smt.a — Establish and administer privileged user accounts in accordance with [PARAM ac-02.07_odp];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2.7_smt.b — Monitor privileged role or attribute assignments;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2.7_smt.c — Monitor changes to roles or attributes; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2.7_smt.d — Revoke access when privileged role or attribute assignments are no longer appropriate.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-02.07_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-2.7_smt.a` — For “Establish and administer privileged user accounts in accordance with [PARAM ac-02.07_odp];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2.7_smt.b` — For “Monitor privileged role or attribute assignments;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2.7_smt.c` — For “Monitor changes to roles or attributes; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2.7_smt.d` — For “Revoke access when privileged role or attribute assignments are no longer appropriate.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-02.07_odp` — What approved value applies to **selection; choose one from: a role-based access scheme; an attribute-based access scheme**? Record the value, scope, approving authority, and decision source.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-2.7_obj.a` (ac-2.7_smt.a): privileged user accounts are established and administered in accordance with [PARAM ac-02.07_odp];

- `ac-2.7_obj.b` (ac-2.7_smt.b): privileged role or attribute assignments are monitored;

- `ac-2.7_obj.c` (ac-2.7_smt.c): changes to roles or attributes are monitored;

- `ac-2.7_obj.d` (ac-2.7_smt.d): access is revoked when privileged role or attribute assignments are no longer appropriate.

#### EXAMINE — `ac-2.7_asm-examine`

- Access control policy

- procedures addressing account management

- system design documentation

- system configuration settings and associated documentation

- system-generated list of privileged user accounts and associated roles

- records of actions taken when privileged role assignments are no longer appropriate

- system audit records

- audit tracking and monitoring reports

- system monitoring records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-2.7_asm-interview`

- Organizational personnel with account management responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

#### TEST — `ac-2.7_asm-test`

- Mechanisms implementing account management functions

- mechanisms monitoring privileged role assignments

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-2.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
