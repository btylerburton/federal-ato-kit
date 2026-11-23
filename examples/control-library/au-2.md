---
title: "AU-2 \u2014 Event Logging"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-2 — Event Logging

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

An event is an observable occurrence in a system. The types of events that require logging are those events that are significant and relevant to the security of systems and the privacy of individuals. Event logging also supports specific monitoring and auditing needs. Event types include password changes, failed logons or failed accesses related to systems, security or privacy attribute changes, administrative privilege usage, PIV credential usage, data action changes, query parameters, or external credential usage. In determining the set of event types that require logging, organizations consider the monitoring and auditing appropriate for each of the controls to be implemented. For completeness, event logging includes all protocols that are operational and supported by the system.

To balance monitoring and auditing requirements with other system needs, event logging requires identifying the subset of event types that are logged at a given point in time. For example, organizations may determine that systems need the capability to log every file access successful and unsuccessful, but not activate that capability except for specific circumstances due to the potential burden on system performance. The types of events that organizations desire to be logged may change. Reviewing and updating the set of logged events is necessary to help ensure that the events remain relevant and continue to support the needs of the organization. Organizations consider how the types of logging events can reveal information about individuals that may give rise to privacy risk and how best to mitigate such risks. For example, there is the potential to reveal personally identifiable information in the audit trail, especially if the logging event is based on patterns or time of usage.

Event logging requirements, including the need to log specific event types, may be referenced in other controls and control enhancements. These include AC-2(4) (catalog reference: `#ac-2.4`), AC-3(10) (catalog reference: `#ac-3.10`), AC-6(9) (catalog reference: `#ac-6.9`), AC-17(1) (catalog reference: `#ac-17.1`), CM-3f (catalog reference: `#cm-3_smt.f`), CM-5(1) (catalog reference: `#cm-5.1`), IA-3(3)(b) (catalog reference: `#ia-3.3_smt.b`), MA-4(1) (catalog reference: `#ma-4.1`), MP-4(2) (catalog reference: `#mp-4.2`), PE-3 (catalog reference: `#pe-3`), PM-21 (catalog reference: `#pm-21`), PT-7 (catalog reference: `#pt-7`), RA-8 (catalog reference: `#ra-8`), SC-7(9) (catalog reference: `#sc-7.9`), SC-7(15) (catalog reference: `#sc-7.15`), SI-3(8) (catalog reference: `#si-3.8`), SI-4(22) (catalog reference: `#si-4.22`), SI-7(8) (catalog reference: `#si-7.8`) , and SI-10(1) (catalog reference: `#si-10.1`) . Organizations include event types that are required by applicable laws, executive orders, directives, policies, regulations, standards, and guidelines. Audit records can be generated at various levels, including at the packet level as information traverses the network. Selecting the appropriate level of event logging is an important part of a monitoring and auditing capability and can identify the root causes of problems. When defining event types, organizations consider the logging necessary to cover related event types, such as the steps in distributed, transaction-based processes and the actions that occur in service-oriented architectures.

### Requirements and exact statement parts

- `au-2_smt`: Statement grouping; see child parts.

- `au-2_smt.a`: Identify the types of events that the system is capable of logging in support of the audit function: [PARAM au-02_odp.01];

- `au-2_smt.b`: Coordinate the event logging function with other organizational entities requiring audit-related information to guide and inform the selection criteria for events to be logged;

- `au-2_smt.c`: Specify the following event types for logging within the system: [PARAM au-2_prm_2];

- `au-2_smt.d`: Provide a rationale for why the event types selected for logging are deemed to be adequate to support after-the-fact investigations of incidents; and

- `au-2_smt.e`: Review and update the event types selected for logging [PARAM au-02_odp.04].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-2_smt.a — Identify the types of events that the system is capable of logging in support of the audit function: [PARAM au-02_odp.01];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for au-2_smt.b — Coordinate the event logging function with other organizational entities requiring audit-related information to guide and inform the selection criteria for events to be logged;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for au-2_smt.c — Specify the following event types for logging within the system: [PARAM au-2_prm_2];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for au-2_smt.d — Provide a rationale for why the event types selected for logging are deemed to be adequate to support after-the-fact investigations of incidents; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for au-2_smt.e — Review and update the event types selected for logging [PARAM au-02_odp.04].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-2_prm_2: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter au-02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter au-02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter au-02_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter au-02_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-2_smt.a` — For “Identify the types of events that the system is capable of logging in support of the audit function: [PARAM au-02_odp.01];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `au-2_smt.b` — For “Coordinate the event logging function with other organizational entities requiring audit-related information to guide and inform the selection criteria for events to be logged;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `au-2_smt.c` — For “Specify the following event types for logging within the system: [PARAM au-2_prm_2];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `au-2_smt.d` — For “Provide a rationale for why the event types selected for logging are deemed to be adequate to support after-the-fact investigations of incidents; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `au-2_smt.e` — For “Review and update the event types selected for logging [PARAM au-02_odp.04].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-2_prm_2` — What approved value applies to **organization-defined event types (subset of the event types defined in AU-2a. (catalog reference: `#au-2_smt.a`)) along with the frequency of (or situation requiring) logging for each identified event type**? Record the value, scope, approving authority, and decision source.

- `au-02_odp.01` — What approved value applies to **event types**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the event types that the system is capable of logging in support of the audit function are defined;

- `au-02_odp.02` — What approved value applies to **event types (subset of AU-02_ODP[01])**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the event types (subset of AU-02_ODP[01]) for logging within the system are defined;

- `au-02_odp.03` — What approved value applies to **frequency or situation**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency or situation requiring logging for each specified event type is defined;

- `au-02_odp.04` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency of event types selected for logging are reviewed and updated;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-2_obj.a` (au-2_smt.a): [PARAM au-02_odp.01] that the system is capable of logging are identified in support of the audit logging function;

- `au-2_obj.b` (au-2_smt.b): the event logging function is coordinated with other organizational entities requiring audit-related information to guide and inform the selection criteria for events to be logged;

- `au-2_obj.c-1` (au-2_smt.c): [PARAM au-02_odp.02] are specified for logging within the system;

- `au-2_obj.c-2` (au-2_smt.c): the specified event types are logged within the system [PARAM au-02_odp.03];

- `au-2_obj.d` (au-2_smt.d): a rationale is provided for why the event types selected for logging are deemed to be adequate to support after-the-fact investigations of incidents;

- `au-2_obj.e` (au-2_smt.e): the event types selected for logging are reviewed and updated [PARAM au-02_odp.04].

#### EXAMINE — `au-2_asm-examine`

- Audit and accountability policy

- procedures addressing auditable events

- system security plan

- privacy plan

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system auditable events

- other relevant documents or records

#### INTERVIEW — `au-2_asm-interview`

- Organizational personnel with audit and accountability responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

#### TEST — `au-2_asm-test`

- Mechanisms implementing system auditing

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-2`. The library index records the exact source revision and hash.

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [SP 800-92](https://doi.org/10.6028/NIST.SP.800-92)

- Catalog relationship **related**: `ac-2`.

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-6`.

- Catalog relationship **related**: `ac-7`.

- Catalog relationship **related**: `ac-8`.

- Catalog relationship **related**: `ac-16`.

- Catalog relationship **related**: `ac-17`.

- Catalog relationship **related**: `au-3`.

- Catalog relationship **related**: `au-4`.

- Catalog relationship **related**: `au-5`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-7`.

- Catalog relationship **related**: `au-11`.

- Catalog relationship **related**: `au-12`.

- Catalog relationship **related**: `cm-3`.

- Catalog relationship **related**: `cm-5`.

- Catalog relationship **related**: `cm-6`.

- Catalog relationship **related**: `cm-13`.

- Catalog relationship **related**: `ia-3`.

- Catalog relationship **related**: `ma-4`.

- Catalog relationship **related**: `mp-4`.

- Catalog relationship **related**: `pe-3`.

- Catalog relationship **related**: `pm-21`.

- Catalog relationship **related**: `pt-2`.

- Catalog relationship **related**: `pt-7`.

- Catalog relationship **related**: `ra-8`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `sc-18`.

- Catalog relationship **related**: `si-3`.

- Catalog relationship **related**: `si-4`.

- Catalog relationship **related**: `si-7`.

- Catalog relationship **related**: `si-10`.

- Catalog relationship **related**: `si-11`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
