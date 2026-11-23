---
title: "AC-3.13 \u2014 Attribute-based Access Control"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-3.13 — Attribute-based Access Control

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Attribute-based access control is an access control policy that restricts system access to authorized users based on specified organizational attributes (e.g., job function, identity), action attributes (e.g., read, write, delete), environmental attributes (e.g., time of day, location), and resource attributes (e.g., classification of a document). Organizations can create rules based on attributes and the authorizations (i.e., privileges) to perform needed operations on the systems associated with organization-defined attributes and rules. When users are assigned to attributes defined in attribute-based access control policies or rules, they can be provisioned to a system with the appropriate privileges or dynamically granted access to a protected resource. Attribute-based access control can be implemented as either a mandatory or discretionary form of access control. When implemented with mandatory access controls, the requirements in AC-3(3) (catalog reference: `#ac-3.3`) define the scope of the subjects and objects covered by the policy.

### Requirements and exact statement parts

- `ac-3.13_smt`: Enforce attribute-based access control policy over defined subjects and objects and control access based upon [PARAM ac-03.13_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-3.13_smt — Enforce attribute-based access control policy over defined subjects and objects and control access based upon [PARAM ac-03.13_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-03.13_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-3.13_smt` — For “Enforce attribute-based access control policy over defined subjects and objects and control access based upon [PARAM ac-03.13_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-03.13_odp` — What approved value applies to **attributes**? Record the value, scope, approving authority, and decision source.

  - Catalog context: attributes to assume access permissions are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-3.13_obj-1` (ac-3.13_smt): the attribute-based access control policy is enforced over defined subjects;

- `ac-3.13_obj-2` (ac-3.13_smt): the attribute-based access control policy is enforced over defined objects;

- `ac-3.13_obj-3` (ac-3.13_smt): access is controlled based on [PARAM ac-03.13_odp].

#### EXAMINE — `ac-3.13_asm-examine`

- Access control policy

- procedures addressing access enforcement

- system design documentation

- system configuration settings and associated documentation

- list of subjects and objects (i.e., users and resources) requiring enforcement of attribute-based access control policies

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-3.13_asm-interview`

- Organizational personnel with access enforcement responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

#### TEST — `ac-3.13_asm-test`

- Mechanisms implementing access enforcement functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-3.13`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
