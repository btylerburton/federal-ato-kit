---
title: "AC-3.3 \u2014 Mandatory Access Control"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-3.3 — Mandatory Access Control

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Mandatory access control is a type of nondiscretionary access control. Mandatory access control policies constrain what actions subjects can take with information obtained from objects for which they have already been granted access. This prevents the subjects from passing the information to unauthorized subjects and objects. Mandatory access control policies constrain actions that subjects can take with respect to the propagation of access control privileges; that is, a subject with a privilege cannot pass that privilege to other subjects. The policy is uniformly enforced over all subjects and objects to which the system has control. Otherwise, the access control policy can be circumvented. This enforcement is provided by an implementation that meets the reference monitor concept as described in AC-25 (catalog reference: `#ac-25`) . The policy is bounded by the system (i.e., once the information is passed outside of the control of the system, additional means may be required to ensure that the constraints on the information remain in effect).

The trusted subjects described above are granted privileges consistent with the concept of least privilege (see AC-6 (catalog reference: `#ac-6`) ). Trusted subjects are only given the minimum privileges necessary for satisfying organizational mission/business needs relative to the above policy. The control is most applicable when there is a mandate that establishes a policy regarding access to controlled unclassified information or classified information and some users of the system are not authorized access to all such information resident in the system. Mandatory access control can operate in conjunction with discretionary access control as described in AC-3(4) (catalog reference: `#ac-3.4`) . A subject constrained in its operation by mandatory access control policies can still operate under the less rigorous constraints of AC-3(4), but mandatory access control policies take precedence over the less rigorous constraints of AC-3(4). For example, while a mandatory access control policy imposes a constraint that prevents a subject from passing information to another subject operating at a different impact or classification level, AC-3(4) permits the subject to pass the information to any other subject with the same impact or classification level as the subject. Examples of mandatory access control policies include the Bell-LaPadula policy to protect confidentiality of information and the Biba policy to protect the integrity of information.

### Requirements and exact statement parts

- `ac-3.3_smt`: Enforce [PARAM ac-3.3_prm_1] over the set of covered subjects and objects specified in the policy, and where the policy:

- `ac-3.3_smt.a`: Is uniformly enforced across the covered subjects and objects within the system;

- `ac-3.3_smt.b`: Specifies that a subject that has been granted access to information is constrained from doing any of the following;

- `ac-3.3_smt.b.1`: Passing the information to unauthorized subjects or objects;

- `ac-3.3_smt.b.2`: Granting its privileges to other subjects;

- `ac-3.3_smt.b.3`: Changing one or more security attributes (specified by the policy) on subjects, objects, the system, or system components;

- `ac-3.3_smt.b.4`: Choosing the security attributes and attribute values (specified by the policy) to be associated with newly created or modified objects; and

- `ac-3.3_smt.b.5`: Changing the rules governing access control; and

- `ac-3.3_smt.c`: Specifies that [PARAM ac-03.03_odp.03] may explicitly be granted [PARAM ac-03.03_odp.04] such that they are not limited by any defined subset (or all) of the above constraints.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-3.3_smt — Enforce [PARAM ac-3.3_prm_1] over the set of covered subjects and objects specified in the policy, and where the policy:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.3_smt.a — Is uniformly enforced across the covered subjects and objects within the system;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.3_smt.b — Specifies that a subject that has been granted access to information is constrained from doing any of the following;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.3_smt.b.1 — Passing the information to unauthorized subjects or objects;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.3_smt.b.2 — Granting its privileges to other subjects;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.3_smt.b.3 — Changing one or more security attributes (specified by the policy) on subjects, objects, the system, or system components;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.3_smt.b.4 — Choosing the security attributes and attribute values (specified by the policy) to be associated with newly created or modified objects; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.3_smt.b.5 — Changing the rules governing access control; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.3_smt.c — Specifies that [PARAM ac-03.03_odp.03] may explicitly be granted [PARAM ac-03.03_odp.04] such that they are not limited by any defined subset (or all) of the above constraints.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-3.3_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-03.03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-03.03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-03.03_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-03.03_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-3.3_smt` — For “Enforce [PARAM ac-3.3_prm_1] over the set of covered subjects and objects specified in the policy, and where the policy:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.3_smt.a` — For “Is uniformly enforced across the covered subjects and objects within the system;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.3_smt.b` — For “Specifies that a subject that has been granted access to information is constrained from doing any of the following;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.3_smt.b.1` — For “Passing the information to unauthorized subjects or objects;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.3_smt.b.2` — For “Granting its privileges to other subjects;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.3_smt.b.3` — For “Changing one or more security attributes (specified by the policy) on subjects, objects, the system, or system components;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.3_smt.b.4` — For “Choosing the security attributes and attribute values (specified by the policy) to be associated with newly created or modified objects; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.3_smt.b.5` — For “Changing the rules governing access control; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.3_smt.c` — For “Specifies that [PARAM ac-03.03_odp.03] may explicitly be granted [PARAM ac-03.03_odp.04] such that they are not limited by any defined subset (or all) of the above constraints.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-3.3_prm_1` — What approved value applies to **organization-defined mandatory access control policy**? Record the value, scope, approving authority, and decision source.

- `ac-03.03_odp.01` — What approved value applies to **mandatory access control policy**? Record the value, scope, approving authority, and decision source.

  - Catalog context: mandatory access control policy enforced over the set of covered subjects is defined;

- `ac-03.03_odp.02` — What approved value applies to **mandatory access control policy**? Record the value, scope, approving authority, and decision source.

  - Catalog context: mandatory access control policy enforced over the set of covered objects is defined;

- `ac-03.03_odp.03` — What approved value applies to **subjects**? Record the value, scope, approving authority, and decision source.

  - Catalog context: subjects to be explicitly granted privileges are defined;

- `ac-03.03_odp.04` — What approved value applies to **privileges**? Record the value, scope, approving authority, and decision source.

  - Catalog context: privileges to be explicitly granted to subjects are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-3.3_obj-1` (ac-3.3_smt): [PARAM ac-03.03_odp.01] is enforced over the set of covered subjects specified in the policy;

- `ac-3.3_obj-2` (ac-3.3_smt): [PARAM ac-03.03_odp.02] is enforced over the set of covered objects specified in the policy;

- `ac-3.3_obj.a-1` (ac-3.3_smt.a): [PARAM ac-03.03_odp.01] is uniformly enforced across the covered subjects within the system;

- `ac-3.3_obj.a-2` (ac-3.3_smt.a): [PARAM ac-03.03_odp.02] is uniformly enforced across the covered objects within the system;

- `ac-3.3_obj.b.1` (ac-3.3_smt.b.1): [PARAM ac-03.03_odp.01] and [PARAM ac-03.03_odp.02] specifying that a subject that has been granted access to information is constrained from passing the information to unauthorized subjects or objects are enforced;

- `ac-3.3_obj.b.2` (ac-3.3_smt.b.2): [PARAM ac-03.03_odp.01] and [PARAM ac-03.03_odp.02] specifying that a subject that has been granted access to information is constrained from granting its privileges to other subjects are enforced;

- `ac-3.3_obj.b.3` (ac-3.3_smt.b.3): [PARAM ac-03.03_odp.01] and [PARAM ac-03.03_odp.02] specifying that a subject that has been granted access to information is constrained from changing one of more security attributes (specified by the policy) on subjects, objects, the system, or system components are enforced;

- `ac-3.3_obj.b.4` (ac-3.3_smt.b.4): [PARAM ac-03.03_odp.01] and [PARAM ac-03.03_odp.02] specifying that a subject that has been granted access to information is constrained from choosing the security attributes and attribute values (specified by the policy) to be associated with newly created or modified objects are enforced;

- `ac-3.3_obj.b.5` (ac-3.3_smt.b.5): [PARAM ac-03.03_odp.01] and [PARAM ac-03.03_odp.02] specifying that a subject that has been granted access to information is constrained from changing the rules governing access control are enforced;

- `ac-3.3_obj.c` (ac-3.3_smt.c): [PARAM ac-03.03_odp.01] and [PARAM ac-03.03_odp.02] specifying that [PARAM ac-03.03_odp.03] may explicitly be granted [PARAM ac-03.03_odp.04] such that they are not limited by any defined subset (or all) of the above constraints are enforced.

#### EXAMINE — `ac-3.3_asm-examine`

- Access control policy

- mandatory access control policies

- procedures addressing access enforcement

- system design documentation

- system configuration settings and associated documentation

- list of subjects and objects (i.e., users and resources) requiring enforcement of mandatory access control policies

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-3.3_asm-interview`

- Organizational personnel with access enforcement responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

- system developers

#### TEST — `ac-3.3_asm-test`

- Automated mechanisms implementing mandatory access control

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-3.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-3`.

- Catalog relationship **related**: `sc-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
