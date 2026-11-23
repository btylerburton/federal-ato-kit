---
title: "AC-2 \u2014 Account Management"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-2 — Account Management

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Examples of system account types include individual, shared, group, system, guest, anonymous, emergency, developer, temporary, and service. Identification of authorized system users and the specification of access privileges reflect the requirements in other controls in the security plan. Users requiring administrative privileges on system accounts receive additional scrutiny by organizational personnel responsible for approving such accounts and privileged access, including system owner, mission or business owner, senior agency information security officer, or senior agency official for privacy. Types of accounts that organizations may wish to prohibit due to increased risk include shared, group, emergency, anonymous, temporary, and guest accounts.

Where access involves personally identifiable information, security programs collaborate with the senior agency official for privacy to establish the specific conditions for group and role membership; specify authorized users, group and role membership, and access authorizations for each account; and create, adjust, or remove system accounts in accordance with organizational policies. Policies can include such information as account expiration dates or other factors that trigger the disabling of accounts. Organizations may choose to define access privileges or other attributes by account, type of account, or a combination of the two. Examples of other attributes required for authorizing access include restrictions on time of day, day of week, and point of origin. In defining other system account attributes, organizations consider system-related requirements and mission/business requirements. Failure to consider these factors could affect system availability.

Temporary and emergency accounts are intended for short-term use. Organizations establish temporary accounts as part of normal account activation procedures when there is a need for short-term accounts without the demand for immediacy in account activation. Organizations establish emergency accounts in response to crisis situations and with the need for rapid account activation. Therefore, emergency account activation may bypass normal account authorization processes. Emergency and temporary accounts are not to be confused with infrequently used accounts, including local logon accounts used for special tasks or when network resources are unavailable (may also be known as accounts of last resort). Such accounts remain available and are not subject to automatic disabling or removal dates. Conditions for disabling or deactivating accounts include when shared/group, emergency, or temporary accounts are no longer required and when individuals are transferred or terminated. Changing shared/group authenticators when members leave the group is intended to ensure that former group members do not retain access to the shared or group account. Some types of system accounts may require specialized training.

### Requirements and exact statement parts

- `ac-2_smt`: Statement grouping; see child parts.

- `ac-2_smt.a`: Define and document the types of accounts allowed and specifically prohibited for use within the system;

- `ac-2_smt.b`: Assign account managers;

- `ac-2_smt.c`: Require [PARAM ac-02_odp.01] for group and role membership;

- `ac-2_smt.d`: Specify:

- `ac-2_smt.d.1`: Authorized users of the system;

- `ac-2_smt.d.2`: Group and role membership; and

- `ac-2_smt.d.3`: Access authorizations (i.e., privileges) and [PARAM ac-02_odp.02] for each account;

- `ac-2_smt.e`: Require approvals by [PARAM ac-02_odp.03] for requests to create accounts;

- `ac-2_smt.f`: Create, enable, modify, disable, and remove accounts in accordance with [PARAM ac-02_odp.04];

- `ac-2_smt.g`: Monitor the use of accounts;

- `ac-2_smt.h`: Notify account managers and [PARAM ac-02_odp.05] within:

- `ac-2_smt.h.1`: [PARAM ac-02_odp.06] when accounts are no longer required;

- `ac-2_smt.h.2`: [PARAM ac-02_odp.07] when users are terminated or transferred; and

- `ac-2_smt.h.3`: [PARAM ac-02_odp.08] when system usage or need-to-know changes for an individual;

- `ac-2_smt.i`: Authorize access to the system based on:

- `ac-2_smt.i.1`: A valid access authorization;

- `ac-2_smt.i.2`: Intended system usage; and

- `ac-2_smt.i.3`: [PARAM ac-02_odp.09];

- `ac-2_smt.j`: Review accounts for compliance with account management requirements [PARAM ac-02_odp.10];

- `ac-2_smt.k`: Establish and implement a process for changing shared or group account authenticators (if deployed) when individuals are removed from the group; and

- `ac-2_smt.l`: Align account management processes with personnel termination and transfer processes.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-2_smt.a — Define and document the types of accounts allowed and specifically prohibited for use within the system;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.b — Assign account managers;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.c — Require [PARAM ac-02_odp.01] for group and role membership;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.d — Specify:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.d.1 — Authorized users of the system;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.d.2 — Group and role membership; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.d.3 — Access authorizations (i.e., privileges) and [PARAM ac-02_odp.02] for each account;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.e — Require approvals by [PARAM ac-02_odp.03] for requests to create accounts;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.f — Create, enable, modify, disable, and remove accounts in accordance with [PARAM ac-02_odp.04];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.g — Monitor the use of accounts;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.h — Notify account managers and [PARAM ac-02_odp.05] within:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.h.1 — [PARAM ac-02_odp.06] when accounts are no longer required;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.h.2 — [PARAM ac-02_odp.07] when users are terminated or transferred; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.h.3 — [PARAM ac-02_odp.08] when system usage or need-to-know changes for an individual;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.i — Authorize access to the system based on:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.i.1 — A valid access authorization;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.i.2 — Intended system usage; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.i.3 — [PARAM ac-02_odp.09];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.j — Review accounts for compliance with account management requirements [PARAM ac-02_odp.10];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.k — Establish and implement a process for changing shared or group account authenticators (if deployed) when individuals are removed from the group; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2_smt.l — Align account management processes with personnel termination and transfer processes.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-02_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-02_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-02_odp.05: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-02_odp.06: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-02_odp.07: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-02_odp.08: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-02_odp.09: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-02_odp.10: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-2_smt.a` — For “Define and document the types of accounts allowed and specifically prohibited for use within the system;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.b` — For “Assign account managers;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.c` — For “Require [PARAM ac-02_odp.01] for group and role membership;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.d` — For “Specify:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.d.1` — For “Authorized users of the system;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.d.2` — For “Group and role membership; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.d.3` — For “Access authorizations (i.e., privileges) and [PARAM ac-02_odp.02] for each account;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.e` — For “Require approvals by [PARAM ac-02_odp.03] for requests to create accounts;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.f` — For “Create, enable, modify, disable, and remove accounts in accordance with [PARAM ac-02_odp.04];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.g` — For “Monitor the use of accounts;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.h` — For “Notify account managers and [PARAM ac-02_odp.05] within:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.h.1` — For “[PARAM ac-02_odp.06] when accounts are no longer required;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.h.2` — For “[PARAM ac-02_odp.07] when users are terminated or transferred; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.h.3` — For “[PARAM ac-02_odp.08] when system usage or need-to-know changes for an individual;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.i` — For “Authorize access to the system based on:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.i.1` — For “A valid access authorization;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.i.2` — For “Intended system usage; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.i.3` — For “[PARAM ac-02_odp.09];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.j` — For “Review accounts for compliance with account management requirements [PARAM ac-02_odp.10];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.k` — For “Establish and implement a process for changing shared or group account authenticators (if deployed) when individuals are removed from the group; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2_smt.l` — For “Align account management processes with personnel termination and transfer processes.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-02_odp.01` — What approved value applies to **prerequisites and criteria**? Record the value, scope, approving authority, and decision source.

  - Catalog context: prerequisites and criteria for group and role membership are defined;

- `ac-02_odp.02` — What approved value applies to **attributes (as required)**? Record the value, scope, approving authority, and decision source.

  - Catalog context: attributes (as required) for each account are defined;

- `ac-02_odp.03` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles required to approve requests to create accounts is/are defined;

- `ac-02_odp.04` — What approved value applies to **policy, procedures, prerequisites, and criteria**? Record the value, scope, approving authority, and decision source.

  - Catalog context: policy, procedures, prerequisites, and criteria for account creation, enabling, modification, disabling, and removal are defined;

- `ac-02_odp.05` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to be notified is/are defined;

- `ac-02_odp.06` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period within which to notify account managers when accounts are no longer required is defined;

- `ac-02_odp.07` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period within which to notify account managers when users are terminated or transferred is defined;

- `ac-02_odp.08` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period within which to notify account managers when system usage or the need to know changes for an individual is defined;

- `ac-02_odp.09` — What approved value applies to **attributes (as required)**? Record the value, scope, approving authority, and decision source.

  - Catalog context: attributes needed to authorize system access (as required) are defined;

- `ac-02_odp.10` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency of account review is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-2_obj.a-1` (ac-2_smt.a): account types allowed for use within the system are defined and documented;

- `ac-2_obj.a-2` (ac-2_smt.a): account types specifically prohibited for use within the system are defined and documented;

- `ac-2_obj.b` (ac-2_smt.b): account managers are assigned;

- `ac-2_obj.c` (ac-2_smt.c): [PARAM ac-02_odp.01] for group and role membership are required;

- `ac-2_obj.d.1` (ac-2_smt.d.1): authorized users of the system are specified;

- `ac-2_obj.d.2` (ac-2_smt.d.2): group and role membership are specified;

- `ac-2_obj.d.3-1` (ac-2_smt.d.3): access authorizations (i.e., privileges) are specified for each account;

- `ac-2_obj.d.3-2` (ac-2_smt.d.3): [PARAM ac-02_odp.02] are specified for each account;

- `ac-2_obj.e` (ac-2_smt.e): approvals are required by [PARAM ac-02_odp.03] for requests to create accounts;

- `ac-2_obj.f-1` (ac-2_smt.f): accounts are created in accordance with [PARAM ac-02_odp.04];

- `ac-2_obj.f-2` (ac-2_smt.f): accounts are enabled in accordance with [PARAM ac-02_odp.04];

- `ac-2_obj.f-3` (ac-2_smt.f): accounts are modified in accordance with [PARAM ac-02_odp.04];

- `ac-2_obj.f-4` (ac-2_smt.f): accounts are disabled in accordance with [PARAM ac-02_odp.04];

- `ac-2_obj.f-5` (ac-2_smt.f): accounts are removed in accordance with [PARAM ac-02_odp.04];

- `ac-2_obj.g` (ac-2_smt.g): the use of accounts is monitored;

- `ac-2_obj.h.1` (ac-2_smt.h.1): account managers and [PARAM ac-02_odp.05] are notified within [PARAM ac-02_odp.06] when accounts are no longer required;

- `ac-2_obj.h.2` (ac-2_smt.h.2): account managers and [PARAM ac-02_odp.05] are notified within [PARAM ac-02_odp.07] when users are terminated or transferred;

- `ac-2_obj.h.3` (ac-2_smt.h.3): account managers and [PARAM ac-02_odp.05] are notified within [PARAM ac-02_odp.08] when system usage or the need to know changes for an individual;

- `ac-2_obj.i.1` (ac-2_smt.i.1): access to the system is authorized based on a valid access authorization;

- `ac-2_obj.i.2` (ac-2_smt.i.2): access to the system is authorized based on intended system usage;

- `ac-2_obj.i.3` (ac-2_smt.i.3): access to the system is authorized based on [PARAM ac-02_odp.09];

- `ac-2_obj.j` (ac-2_smt.j): accounts are reviewed for compliance with account management requirements [PARAM ac-02_odp.10];

- `ac-2_obj.k-1` (ac-2_smt.k): a process is established for changing shared or group account authenticators (if deployed) when individuals are removed from the group;

- `ac-2_obj.k-2` (ac-2_smt.k): a process is implemented for changing shared or group account authenticators (if deployed) when individuals are removed from the group;

- `ac-2_obj.l-1` (ac-2_smt.l): account management processes are aligned with personnel termination processes;

- `ac-2_obj.l-2` (ac-2_smt.l): account management processes are aligned with personnel transfer processes.

#### EXAMINE — `ac-2_asm-examine`

- Access control policy

- personnel termination policy and procedure

- personnel transfer policy and procedure

- procedures for addressing account management

- system design documentation

- system configuration settings and associated documentation

- list of active system accounts along with the name of the individual associated with each account

- list of recently disabled system accounts and the name of the individual associated with each account

- list of conditions for group and role membership

- notifications of recent transfers, separations, or terminations of employees

- access authorization records

- account management compliance reviews

- system monitoring records

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ac-2_asm-interview`

- Organizational personnel with account management responsibilities

- system/network administrators

- organizational personnel with information security with information security and privacy responsibilities

#### TEST — `ac-2_asm-test`

- Organizational processes for account management on the system

- mechanisms for implementing account management

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-2`. The library index records the exact source revision and hash.

- [SP 800-162](https://doi.org/10.6028/NIST.SP.800-162)

- [SP 800-178](https://doi.org/10.6028/NIST.SP.800-178)

- [SP 800-192](https://doi.org/10.6028/NIST.SP.800-192)

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-5`.

- Catalog relationship **related**: `ac-6`.

- Catalog relationship **related**: `ac-17`.

- Catalog relationship **related**: `ac-18`.

- Catalog relationship **related**: `ac-20`.

- Catalog relationship **related**: `ac-24`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-12`.

- Catalog relationship **related**: `cm-5`.

- Catalog relationship **related**: `ia-2`.

- Catalog relationship **related**: `ia-4`.

- Catalog relationship **related**: `ia-5`.

- Catalog relationship **related**: `ia-8`.

- Catalog relationship **related**: `ma-3`.

- Catalog relationship **related**: `ma-5`.

- Catalog relationship **related**: `pe-2`.

- Catalog relationship **related**: `pl-4`.

- Catalog relationship **related**: `ps-2`.

- Catalog relationship **related**: `ps-4`.

- Catalog relationship **related**: `ps-5`.

- Catalog relationship **related**: `ps-7`.

- Catalog relationship **related**: `pt-2`.

- Catalog relationship **related**: `pt-3`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `sc-12`.

- Catalog relationship **related**: `sc-13`.

- Catalog relationship **related**: `sc-37`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
