---
title: "AC-2.13 \u2014 Disable Accounts for High-risk Individuals"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-2.13 — Disable Accounts for High-risk Individuals

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Users who pose a significant security and/or privacy risk include individuals for whom reliable evidence indicates either the intention to use authorized access to systems to cause harm or through whom adversaries will cause harm. Such harm includes adverse impacts to organizational operations, organizational assets, individuals, other organizations, or the Nation. Close coordination among system administrators, legal staff, human resource managers, and authorizing officials is essential when disabling system accounts for high-risk individuals.

### Requirements and exact statement parts

- `ac-2.13_smt`: Disable accounts of individuals within [PARAM ac-02.13_odp.01] of discovery of [PARAM ac-02.13_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-2.13_smt — Disable accounts of individuals within [PARAM ac-02.13_odp.01] of discovery of [PARAM ac-02.13_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-02.13_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-02.13_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-2.13_smt` — For “Disable accounts of individuals within [PARAM ac-02.13_odp.01] of discovery of [PARAM ac-02.13_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-02.13_odp.01` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period within which to disable accounts of individuals who are discovered to pose significant risk is defined;

- `ac-02.13_odp.02` — What approved value applies to **significant risks**? Record the value, scope, approving authority, and decision source.

  - Catalog context: significant risks leading to disabling accounts are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-2.13_obj` (ac-2.13_smt): accounts of individuals are disabled within [PARAM ac-02.13_odp.01] of discovery of [PARAM ac-02.13_odp.02].

#### EXAMINE — `ac-2.13_asm-examine`

- Access control policy

- procedures addressing account management

- system design documentation

- system configuration settings and associated documentation

- system-generated list of disabled accounts

- list of user activities posing significant organizational risk

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-2.13_asm-interview`

- Organizational personnel with account management responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

#### TEST — `ac-2.13_asm-test`

- Mechanisms implementing account management functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-2.13`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-2`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
