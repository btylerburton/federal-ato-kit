---
title: "AC-3.7 \u2014 Role-based Access Control"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-3.7 — Role-based Access Control

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Role-based access control (RBAC) is an access control policy that enforces access to objects and system functions based on the defined role (i.e., job function) of the subject. Organizations can create specific roles based on job functions and the authorizations (i.e., privileges) to perform needed operations on the systems associated with the organization-defined roles. When users are assigned to specific roles, they inherit the authorizations or privileges defined for those roles. RBAC simplifies privilege administration for organizations because privileges are not assigned directly to every user (which can be a large number of individuals) but are instead acquired through role assignments. RBAC can also increase privacy and security risk if individuals assigned to a role are given access to information beyond what they need to support organizational missions or business functions. RBAC can be implemented as a mandatory or discretionary form of access control. For organizations implementing RBAC with mandatory access controls, the requirements in AC-3(3) (catalog reference: `#ac-3.3`) define the scope of the subjects and objects covered by the policy.

### Requirements and exact statement parts

- `ac-3.7_smt`: Enforce a role-based access control policy over defined subjects and objects and control access based upon [PARAM ac-3.7_prm_1].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-3.7_smt — Enforce a role-based access control policy over defined subjects and objects and control access based upon [PARAM ac-3.7_prm_1].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-3.7_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-03.07_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-03.07_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-3.7_smt` — For “Enforce a role-based access control policy over defined subjects and objects and control access based upon [PARAM ac-3.7_prm_1].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-3.7_prm_1` — What approved value applies to **organization-defined roles and users authorized to assume such roles**? Record the value, scope, approving authority, and decision source.

- `ac-03.07_odp.01` — What approved value applies to **roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: roles upon which to base control of access are defined;

- `ac-03.07_odp.02` — What approved value applies to **users authorized to assume such roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: users authorized to assume roles (defined in AC-03(07)_ODP[01]) are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-3.7_obj-1` (ac-3.7_smt): a role-based access control policy is enforced over defined subjects;

- `ac-3.7_obj-2` (ac-3.7_smt): a role-based access control policy is enforced over defined objects;

- `ac-3.7_obj-3` (ac-3.7_smt): access is controlled based on [PARAM ac-03.07_odp.01] and [PARAM ac-03.07_odp.02].

#### EXAMINE — `ac-3.7_asm-examine`

- Access control policy

- role-based access control policies

- procedures addressing access enforcement

- system design documentation

- system configuration settings and associated documentation

- list of roles, users, and associated privileges required to control system access

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ac-3.7_asm-interview`

- Organizational personnel with access enforcement responsibilities

- system/network administrators

- organizational personnel with information security and privacy responsibilities

- system developers

#### TEST — `ac-3.7_asm-test`

- Mechanisms implementing role-based access control policy

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-3.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
