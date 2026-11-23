---
title: "AC-3.4 \u2014 Discretionary Access Control"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-3.4 — Discretionary Access Control

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing the information to other subjects or objects (i.e., subjects have the discretion to pass). Discretionary access control can operate in conjunction with mandatory access control as described in AC-3(3) (catalog reference: `#ac-3.3`) and AC-3(15) (catalog reference: `#ac-3.15`) . A subject that is constrained in its operation by mandatory access control policies can still operate under the less rigorous constraints of discretionary access control. Therefore, while AC-3(3) (catalog reference: `#ac-3.3`) imposes constraints that prevent a subject from passing information to another subject operating at a different impact or classification level, AC-3(4) (catalog reference: `#ac-3.4`) permits the subject to pass the information to any subject at the same impact or classification level. The policy is bounded by the system. Once the information is passed outside of system control, additional means may be required to ensure that the constraints remain in effect. While traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this particular use of discretionary access control.

### Requirements and exact statement parts

- `ac-3.4_smt`: Enforce [PARAM ac-3.4_prm_1] over the set of covered subjects and objects specified in the policy, and where the policy specifies that a subject that has been granted access to information can do one or more of the following:

- `ac-3.4_smt.a`: Pass the information to any other subjects or objects;

- `ac-3.4_smt.b`: Grant its privileges to other subjects;

- `ac-3.4_smt.c`: Change security attributes on subjects, objects, the system, or the system’s components;

- `ac-3.4_smt.d`: Choose the security attributes to be associated with newly created or revised objects; or

- `ac-3.4_smt.e`: Change the rules governing access control.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-3.4_smt — Enforce [PARAM ac-3.4_prm_1] over the set of covered subjects and objects specified in the policy, and where the policy specifies that a subject that has been granted access to information can do one or more of the following:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.4_smt.a — Pass the information to any other subjects or objects;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.4_smt.b — Grant its privileges to other subjects;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.4_smt.c — Change security attributes on subjects, objects, the system, or the system’s components;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.4_smt.d — Choose the security attributes to be associated with newly created or revised objects; or
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.4_smt.e — Change the rules governing access control.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-3.4_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-03.04_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-03.04_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-3.4_smt` — For “Enforce [PARAM ac-3.4_prm_1] over the set of covered subjects and objects specified in the policy, and where the policy specifies that a subject that has been granted access to information can do one or more of the following:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.4_smt.a` — For “Pass the information to any other subjects or objects;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.4_smt.b` — For “Grant its privileges to other subjects;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.4_smt.c` — For “Change security attributes on subjects, objects, the system, or the system’s components;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.4_smt.d` — For “Choose the security attributes to be associated with newly created or revised objects; or”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.4_smt.e` — For “Change the rules governing access control.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-3.4_prm_1` — What approved value applies to **organization-defined discretionary access control policy**? Record the value, scope, approving authority, and decision source.

- `ac-03.04_odp.01` — What approved value applies to **discretionary access control policy**? Record the value, scope, approving authority, and decision source.

  - Catalog context: discretionary access control policy enforced over the set of covered subjects is defined;

- `ac-03.04_odp.02` — What approved value applies to **discretionary access control policy**? Record the value, scope, approving authority, and decision source.

  - Catalog context: discretionary access control policy enforced over the set of covered objects is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-3.4_obj-1` (ac-3.4_smt): [PARAM ac-03.04_odp.01] is enforced over the set of covered subjects specified in the policy;

- `ac-3.4_obj-2` (ac-3.4_smt): [PARAM ac-03.04_odp.02] is enforced over the set of covered objects specified in the policy;

- `ac-3.4_obj.a` (ac-3.4_smt.a): [PARAM ac-03.04_odp.01] and [PARAM ac-03.04_odp.02] are enforced where the policy specifies that a subject that has been granted access to information can pass the information to any other subjects or objects;

- `ac-3.4_obj.b` (ac-3.4_smt.b): [PARAM ac-03.04_odp.01] and [PARAM ac-03.04_odp.02] are enforced where the policy specifies that a subject that has been granted access to information can grant its privileges to other subjects;

- `ac-3.4_obj.c` (ac-3.4_smt.c): [PARAM ac-03.04_odp.01] and [PARAM ac-03.04_odp.02] are enforced where the policy specifies that a subject that has been granted access to information can change security attributes on subjects, objects, the system, or the system’s components;

- `ac-3.4_obj.d` (ac-3.4_smt.d): [PARAM ac-03.04_odp.01] and [PARAM ac-03.04_odp.02] are enforced where the policy specifies that a subject that has been granted access to information can choose the security attributes to be associated with newly created or revised objects;

- `ac-3.4_obj.e` (ac-3.4_smt.e): [PARAM ac-03.04_odp.01] and [PARAM ac-03.04_odp.02] are enforced where the policy specifies that a subject that has been granted access to information can change the rules governing access control.

#### EXAMINE — `ac-3.4_asm-examine`

- Access control policy

- discretionary access control policies

- procedures addressing access enforcement

- system design documentation

- system configuration settings and associated documentation

- list of subjects and objects (i.e., users and resources) requiring enforcement of discretionary access control policies

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-3.4_asm-interview`

- Organizational personnel with access enforcement responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

- system developers

#### TEST — `ac-3.4_asm-test`

- Mechanisms implementing discretionary access control policy

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-3.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
