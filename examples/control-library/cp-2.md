---
title: "CP-2 \u2014 Contingency Plan"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-2 — Contingency Plan

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Contingency planning for systems is part of an overall program for achieving continuity of operations for organizational mission and business functions. Contingency planning addresses system restoration and implementation of alternative mission or business processes when systems are compromised or breached. Contingency planning is considered throughout the system development life cycle and is a fundamental part of the system design. Systems can be designed for redundancy, to provide backup capabilities, and for resilience. Contingency plans reflect the degree of restoration required for organizational systems since not all systems need to fully recover to achieve the level of continuity of operations desired. System recovery objectives reflect applicable laws, executive orders, directives, regulations, policies, standards, guidelines, organizational risk tolerance, and system impact level.

Actions addressed in contingency plans include orderly system degradation, system shutdown, fallback to a manual mode, alternate information flows, and operating in modes reserved for when systems are under attack. By coordinating contingency planning with incident handling activities, organizations ensure that the necessary planning activities are in place and activated in the event of an incident. Organizations consider whether continuity of operations during an incident conflicts with the capability to automatically disable the system, as specified in IR-4(5) (catalog reference: `#ir-4.5`) . Incident response planning is part of contingency planning for organizations and is addressed in the IR (catalog reference: `#ir`) (Incident Response) family.

### Requirements and exact statement parts

- `cp-2_smt`: Statement grouping; see child parts.

- `cp-2_smt.a`: Develop a contingency plan for the system that:

- `cp-2_smt.a.1`: Identifies essential mission and business functions and associated contingency requirements;

- `cp-2_smt.a.2`: Provides recovery objectives, restoration priorities, and metrics;

- `cp-2_smt.a.3`: Addresses contingency roles, responsibilities, assigned individuals with contact information;

- `cp-2_smt.a.4`: Addresses maintaining essential mission and business functions despite a system disruption, compromise, or failure;

- `cp-2_smt.a.5`: Addresses eventual, full system restoration without deterioration of the controls originally planned and implemented;

- `cp-2_smt.a.6`: Addresses the sharing of contingency information; and

- `cp-2_smt.a.7`: Is reviewed and approved by [PARAM cp-2_prm_1];

- `cp-2_smt.b`: Distribute copies of the contingency plan to [PARAM cp-2_prm_2];

- `cp-2_smt.c`: Coordinate contingency planning activities with incident handling activities;

- `cp-2_smt.d`: Review the contingency plan for the system [PARAM cp-02_odp.05];

- `cp-2_smt.e`: Update the contingency plan to address changes to the organization, system, or environment of operation and problems encountered during contingency plan implementation, execution, or testing;

- `cp-2_smt.f`: Communicate contingency plan changes to [PARAM cp-2_prm_4];

- `cp-2_smt.g`: Incorporate lessons learned from contingency plan testing, training, or actual contingency activities into contingency testing and training; and

- `cp-2_smt.h`: Protect the contingency plan from unauthorized disclosure and modification.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-2_smt.a — Develop a contingency plan for the system that:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-2_smt.a.1 — Identifies essential mission and business functions and associated contingency requirements;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-2_smt.a.2 — Provides recovery objectives, restoration priorities, and metrics;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-2_smt.a.3 — Addresses contingency roles, responsibilities, assigned individuals with contact information;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-2_smt.a.4 — Addresses maintaining essential mission and business functions despite a system disruption, compromise, or failure;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-2_smt.a.5 — Addresses eventual, full system restoration without deterioration of the controls originally planned and implemented;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-2_smt.a.6 — Addresses the sharing of contingency information; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-2_smt.a.7 — Is reviewed and approved by [PARAM cp-2_prm_1];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-2_smt.b — Distribute copies of the contingency plan to [PARAM cp-2_prm_2];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-2_smt.c — Coordinate contingency planning activities with incident handling activities;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-2_smt.d — Review the contingency plan for the system [PARAM cp-02_odp.05];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-2_smt.e — Update the contingency plan to address changes to the organization, system, or environment of operation and problems encountered during contingency plan implementation, execution, or testing;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-2_smt.f — Communicate contingency plan changes to [PARAM cp-2_prm_4];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-2_smt.g — Incorporate lessons learned from contingency plan testing, training, or actual contingency activities into contingency testing and training; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-2_smt.h — Protect the contingency plan from unauthorized disclosure and modification.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cp-2_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-2_prm_2: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-2_prm_4: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-02_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-02_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-02_odp.05: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-02_odp.06: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-02_odp.07: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cp-2_smt.a` — For “Develop a contingency plan for the system that:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-2_smt.a.1` — For “Identifies essential mission and business functions and associated contingency requirements;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-2_smt.a.2` — For “Provides recovery objectives, restoration priorities, and metrics;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-2_smt.a.3` — For “Addresses contingency roles, responsibilities, assigned individuals with contact information;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-2_smt.a.4` — For “Addresses maintaining essential mission and business functions despite a system disruption, compromise, or failure;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-2_smt.a.5` — For “Addresses eventual, full system restoration without deterioration of the controls originally planned and implemented;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-2_smt.a.6` — For “Addresses the sharing of contingency information; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-2_smt.a.7` — For “Is reviewed and approved by [PARAM cp-2_prm_1];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-2_smt.b` — For “Distribute copies of the contingency plan to [PARAM cp-2_prm_2];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-2_smt.c` — For “Coordinate contingency planning activities with incident handling activities;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-2_smt.d` — For “Review the contingency plan for the system [PARAM cp-02_odp.05];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-2_smt.e` — For “Update the contingency plan to address changes to the organization, system, or environment of operation and problems encountered during contingency plan implementation, execution, or testing;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-2_smt.f` — For “Communicate contingency plan changes to [PARAM cp-2_prm_4];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-2_smt.g` — For “Incorporate lessons learned from contingency plan testing, training, or actual contingency activities into contingency testing and training; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-2_smt.h` — For “Protect the contingency plan from unauthorized disclosure and modification.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cp-2_prm_1` — What approved value applies to **organization-defined personnel or roles**? Record the value, scope, approving authority, and decision source.

- `cp-2_prm_2` — What approved value applies to **organization-defined key contingency personnel (identified by name and/or by role) and organizational elements**? Record the value, scope, approving authority, and decision source.

- `cp-2_prm_4` — What approved value applies to **organization-defined key contingency personnel (identified by name and/or by role) and organizational elements**? Record the value, scope, approving authority, and decision source.

- `cp-02_odp.01` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to review a contingency plan is/are defined;

- `cp-02_odp.02` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to approve a contingency plan is/are defined;

- `cp-02_odp.03` — What approved value applies to **key contingency personnel**? Record the value, scope, approving authority, and decision source.

  - Catalog context: key contingency personnel (identified by name and/or by role) to whom copies of the contingency plan are distributed are defined;

- `cp-02_odp.04` — What approved value applies to **organizational elements**? Record the value, scope, approving authority, and decision source.

  - Catalog context: key contingency organizational elements to which copies of the contingency plan are distributed are defined;

- `cp-02_odp.05` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency of contingency plan review is defined;

- `cp-02_odp.06` — What approved value applies to **key contingency personnel**? Record the value, scope, approving authority, and decision source.

  - Catalog context: key contingency personnel (identified by name and/or by role) to communicate changes to are defined;

- `cp-02_odp.07` — What approved value applies to **organizational elements**? Record the value, scope, approving authority, and decision source.

  - Catalog context: key contingency organizational elements to communicate changes to are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-2_obj.a.1` (cp-2_smt.a.1): a contingency plan for the system is developed that identifies essential mission and business functions and associated contingency requirements;

- `cp-2_obj.a.2-1` (cp-2_smt.a.2): a contingency plan for the system is developed that provides recovery objectives;

- `cp-2_obj.a.2-2` (cp-2_smt.a.2): a contingency plan for the system is developed that provides restoration priorities;

- `cp-2_obj.a.2-3` (cp-2_smt.a.2): a contingency plan for the system is developed that provides metrics;

- `cp-2_obj.a.3-1` (cp-2_smt.a.3): a contingency plan for the system is developed that addresses contingency roles;

- `cp-2_obj.a.3-2` (cp-2_smt.a.3): a contingency plan for the system is developed that addresses contingency responsibilities;

- `cp-2_obj.a.3-3` (cp-2_smt.a.3): a contingency plan for the system is developed that addresses assigned individuals with contact information;

- `cp-2_obj.a.4` (cp-2_smt.a.4): a contingency plan for the system is developed that addresses maintaining essential mission and business functions despite a system disruption, compromise, or failure;

- `cp-2_obj.a.5` (cp-2_smt.a.5): a contingency plan for the system is developed that addresses eventual, full-system restoration without deterioration of the controls originally planned and implemented;

- `cp-2_obj.a.6` (cp-2_smt.a.6): a contingency plan for the system is developed that addresses the sharing of contingency information;

- `cp-2_obj.a.7-1` (cp-2_smt.a.7): a contingency plan for the system is developed that is reviewed by [PARAM cp-02_odp.01];

- `cp-2_obj.a.7-2` (cp-2_smt.a.7): a contingency plan for the system is developed that is approved by [PARAM cp-02_odp.02];

- `cp-2_obj.b-1` (cp-2_smt.b): copies of the contingency plan are distributed to [PARAM cp-02_odp.03];

- `cp-2_obj.b-2` (cp-2_smt.b): copies of the contingency plan are distributed to [PARAM cp-02_odp.04];

- `cp-2_obj.c` (cp-2_smt.c): contingency planning activities are coordinated with incident handling activities;

- `cp-2_obj.d` (cp-2_smt.d): the contingency plan for the system is reviewed [PARAM cp-02_odp.05];

- `cp-2_obj.e-1` (cp-2_smt.e): the contingency plan is updated to address changes to the organization, system, or environment of operation;

- `cp-2_obj.e-2` (cp-2_smt.e): the contingency plan is updated to address problems encountered during contingency plan implementation, execution, or testing;

- `cp-2_obj.f-1` (cp-2_smt.f): contingency plan changes are communicated to [PARAM cp-02_odp.06];

- `cp-2_obj.f-2` (cp-2_smt.f): contingency plan changes are communicated to [PARAM cp-02_odp.07];

- `cp-2_obj.g-1` (cp-2_smt.g): lessons learned from contingency plan testing or actual contingency activities are incorporated into contingency testing;

- `cp-2_obj.g-2` (cp-2_smt.g): lessons learned from contingency plan training or actual contingency activities are incorporated into contingency testing and training;

- `cp-2_obj.h-1` (cp-2_smt.h): the contingency plan is protected from unauthorized disclosure;

- `cp-2_obj.h-2` (cp-2_smt.h): the contingency plan is protected from unauthorized modification.

#### EXAMINE — `cp-2_asm-examine`

- Contingency planning policy

- procedures addressing contingency operations for the system

- contingency plan

- evidence of contingency plan reviews and updates

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-2_asm-interview`

- Organizational personnel with contingency planning and plan implementation responsibilities

- organizational personnel with incident handling responsibilities

- organizational personnel with knowledge of requirements for mission and business functions

- organizational personnel with information security responsibilities

#### TEST — `cp-2_asm-test`

- Organizational processes for contingency plan development, review, update, and protection

- mechanisms for developing, reviewing, updating, and/or protecting the contingency plan

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-2`. The library index records the exact source revision and hash.

- [SP 800-34](https://doi.org/10.6028/NIST.SP.800-34r1)

- [IR 8179](https://doi.org/10.6028/NIST.IR.8179)

- Catalog relationship **related**: `cp-3`.

- Catalog relationship **related**: `cp-4`.

- Catalog relationship **related**: `cp-6`.

- Catalog relationship **related**: `cp-7`.

- Catalog relationship **related**: `cp-8`.

- Catalog relationship **related**: `cp-9`.

- Catalog relationship **related**: `cp-10`.

- Catalog relationship **related**: `cp-11`.

- Catalog relationship **related**: `cp-13`.

- Catalog relationship **related**: `ir-4`.

- Catalog relationship **related**: `ir-6`.

- Catalog relationship **related**: `ir-8`.

- Catalog relationship **related**: `ir-9`.

- Catalog relationship **related**: `ma-6`.

- Catalog relationship **related**: `mp-2`.

- Catalog relationship **related**: `mp-4`.

- Catalog relationship **related**: `mp-5`.

- Catalog relationship **related**: `pl-2`.

- Catalog relationship **related**: `pm-8`.

- Catalog relationship **related**: `pm-11`.

- Catalog relationship **related**: `sa-15`.

- Catalog relationship **related**: `sa-20`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `sc-23`.

- Catalog relationship **related**: `si-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
