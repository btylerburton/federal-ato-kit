---
title: "AC-3.15 \u2014 Discretionary and Mandatory Access Control"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-3.15 — Discretionary and Mandatory Access Control

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Simultaneously implementing a mandatory access control policy and a discretionary access control policy can provide additional protection against the unauthorized execution of code by users or processes acting on behalf of users. This helps prevent a single compromised user or process from compromising the entire system.

### Requirements and exact statement parts

- `ac-3.15_smt`: Statement grouping; see child parts.

- `ac-3.15_smt.a`: Enforce [PARAM ac-3.15_prm_1] over the set of covered subjects and objects specified in the policy; and

- `ac-3.15_smt.b`: Enforce [PARAM ac-3.15_prm_2] over the set of covered subjects and objects specified in the policy.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-3.15_smt.a — Enforce [PARAM ac-3.15_prm_1] over the set of covered subjects and objects specified in the policy; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.15_smt.b — Enforce [PARAM ac-3.15_prm_2] over the set of covered subjects and objects specified in the policy.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-3.15_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-3.15_prm_2: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-03.15_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-03.15_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-03.15_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-03.15_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-3.15_smt.a` — For “Enforce [PARAM ac-3.15_prm_1] over the set of covered subjects and objects specified in the policy; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.15_smt.b` — For “Enforce [PARAM ac-3.15_prm_2] over the set of covered subjects and objects specified in the policy.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-3.15_prm_1` — What approved value applies to **organization-defined mandatory access control policy**? Record the value, scope, approving authority, and decision source.

- `ac-3.15_prm_2` — What approved value applies to **organization-defined discretionary access control policy**? Record the value, scope, approving authority, and decision source.

- `ac-03.15_odp.01` — What approved value applies to **mandatory access control policy**? Record the value, scope, approving authority, and decision source.

  - Catalog context: a mandatory access control policy enforced over the set of covered subjects specified in the policy is defined;

- `ac-03.15_odp.02` — What approved value applies to **mandatory access control policy**? Record the value, scope, approving authority, and decision source.

  - Catalog context: a mandatory access control policy enforced over the set of covered objects specified in the policy is defined;

- `ac-03.15_odp.03` — What approved value applies to **discretionary access control policy**? Record the value, scope, approving authority, and decision source.

  - Catalog context: a discretionary access control policy enforced over the set of covered subjects specified in the policy is defined;

- `ac-03.15_odp.04` — What approved value applies to **discretionary access control policy**? Record the value, scope, approving authority, and decision source.

  - Catalog context: a discretionary access control policy enforced over the set of covered objects specified in the policy is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-3.15_obj.a-1` (ac-3.15_smt.a): [PARAM ac-03.15_odp.01] is enforced over the set of covered subjects specified in the policy;

- `ac-3.15_obj.a-2` (ac-3.15_smt.a): [PARAM ac-03.15_odp.02] is enforced over the set of covered objects specified in the policy;

- `ac-3.15_obj.b-1` (ac-3.15_smt.b): [PARAM ac-03.15_odp.03] is enforced over the set of covered subjects specified in the policy;

- `ac-3.15_obj.b-2` (ac-3.15_smt.b): [PARAM ac-03.15_odp.04] is enforced over the set of covered objects specified in the policy.

#### EXAMINE — `ac-3.15_asm-examine`

- Access control policy

- procedures addressing access enforcement

- system design documentation

- system configuration settings and associated documentation

- list of subjects and objects (i.e., users and resources) requiring enforcement of mandatory access control policies

- list of subjects and objects (i.e., users and resources) requiring enforcement of discretionary access control policies

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-3.15_asm-interview`

- Organizational personnel with access enforcement responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

- system developers

#### TEST — `ac-3.15_asm-test`

- Mechanisms implementing mandatory and discretionary access control policy

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-3.15`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-3`.

- Catalog relationship **related**: `sc-2`.

- Catalog relationship **related**: `sc-3`.

- Catalog relationship **related**: `ac-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
