---
title: "AC-6.3 \u2014 Network Access to Privileged Commands"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-6.3 — Network Access to Privileged Commands

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Network access is any access across a network connection in lieu of local access (i.e., user being physically present at the device).

### Requirements and exact statement parts

- `ac-6.3_smt`: Authorize network access to [PARAM ac-06.03_odp.01] only for [PARAM ac-06.03_odp.02] and document the rationale for such access in the security plan for the system.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-6.3_smt — Authorize network access to [PARAM ac-06.03_odp.01] only for [PARAM ac-06.03_odp.02] and document the rationale for such access in the security plan for the system.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-06.03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-06.03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-6.3_smt` — For “Authorize network access to [PARAM ac-06.03_odp.01] only for [PARAM ac-06.03_odp.02] and document the rationale for such access in the security plan for the system.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-06.03_odp.01` — What approved value applies to **privileged commands**? Record the value, scope, approving authority, and decision source.

  - Catalog context: privileged commands to which network access is to be authorized only for compelling operational needs are defined;

- `ac-06.03_odp.02` — What approved value applies to **compelling operational needs**? Record the value, scope, approving authority, and decision source.

  - Catalog context: compelling operational needs necessitating network access to privileged commands are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-6.3_obj-1` (ac-6.3_smt): network access to [PARAM ac-06.03_odp.01] is authorized only for [PARAM ac-06.03_odp.02];

- `ac-6.3_obj-2` (ac-6.3_smt): the rationale for authorizing network access to privileged commands is documented in the security plan for the system.

#### EXAMINE — `ac-6.3_asm-examine`

- Access control policy

- procedures addressing least privilege

- system configuration settings and associated documentation

- system audit records

- list of operational needs for authorizing network access to privileged commands

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-6.3_asm-interview`

- Organizational personnel with responsibilities for defining least privileges necessary to accomplish specified tasks

- organizational personnel with information security responsibilities

#### TEST — `ac-6.3_asm-test`

- Mechanisms implementing least privilege functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-6.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-6`.

- Catalog relationship **related**: `ac-17`.

- Catalog relationship **related**: `ac-18`.

- Catalog relationship **related**: `ac-19`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
