---
title: "AC-7 \u2014 Unsuccessful Logon Attempts"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-7 — Unsuccessful Logon Attempts

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The need to limit unsuccessful logon attempts and take subsequent action when the maximum number of attempts is exceeded applies regardless of whether the logon occurs via a local or network connection. Due to the potential for denial of service, automatic lockouts initiated by systems are usually temporary and automatically release after a predetermined, organization-defined time period. If a delay algorithm is selected, organizations may employ different algorithms for different components of the system based on the capabilities of those components. Responses to unsuccessful logon attempts may be implemented at the operating system and the application levels. Organization-defined actions that may be taken when the number of allowed consecutive invalid logon attempts is exceeded include prompting the user to answer a secret question in addition to the username and password, invoking a lockdown mode with limited user capabilities (instead of full lockout), allowing users to only logon from specified Internet Protocol (IP) addresses, requiring a CAPTCHA to prevent automated attacks, or applying user profiles such as location, time of day, IP address, device, or Media Access Control (MAC) address. If automatic system lockout or execution of a delay algorithm is not implemented in support of the availability objective, organizations consider a combination of other actions to help prevent brute force attacks. In addition to the above, organizations can prompt users to respond to a secret question before the number of allowed unsuccessful logon attempts is exceeded. Automatically unlocking an account after a specified period of time is generally not permitted. However, exceptions may be required based on operational mission or need.

### Requirements and exact statement parts

- `ac-7_smt`: Statement grouping; see child parts.

- `ac-7_smt.a`: Enforce a limit of [PARAM ac-07_odp.01] consecutive invalid logon attempts by a user during a [PARAM ac-07_odp.02] ; and

- `ac-7_smt.b`: Automatically [PARAM ac-07_odp.03] when the maximum number of unsuccessful attempts is exceeded.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-7_smt.a — Enforce a limit of [PARAM ac-07_odp.01] consecutive invalid logon attempts by a user during a [PARAM ac-07_odp.02] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-7_smt.b — Automatically [PARAM ac-07_odp.03] when the maximum number of unsuccessful attempts is exceeded.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-07_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-07_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-07_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-07_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-07_odp.05: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-07_odp.06: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-7_smt.a` — For “Enforce a limit of [PARAM ac-07_odp.01] consecutive invalid logon attempts by a user during a [PARAM ac-07_odp.02] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-7_smt.b` — For “Automatically [PARAM ac-07_odp.03] when the maximum number of unsuccessful attempts is exceeded.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-07_odp.01` — What approved value applies to **number**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the number of consecutive invalid logon attempts by a user allowed during a time period is defined;

- `ac-07_odp.02` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the time period to which the number of consecutive invalid logon attempts by a user is limited is defined;

- `ac-07_odp.03` — What approved value applies to **selection; choose one-or-more from: lock the account or node for [PARAM ac-07_odp.04]; lock the account or node until released by an administrator; delay next logon prompt per [PARAM ac-07_odp.05]; notify system administrator; take other [PARAM ac-07_odp.06]**? Record the value, scope, approving authority, and decision source.

- `ac-07_odp.04` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period for an account or node to be locked is defined (if selected);

- `ac-07_odp.05` — What approved value applies to **delay algorithm**? Record the value, scope, approving authority, and decision source.

  - Catalog context: delay algorithm for the next logon prompt is defined (if selected);

- `ac-07_odp.06` — What approved value applies to **action**? Record the value, scope, approving authority, and decision source.

  - Catalog context: other action to be taken when the maximum number of unsuccessful attempts is exceeded is defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-7_obj.a` (ac-7_smt.a): a limit of [PARAM ac-07_odp.01] consecutive invalid logon attempts by a user during [PARAM ac-07_odp.02] is enforced;

- `ac-7_obj.b` (ac-7_smt.b): automatically [PARAM ac-07_odp.03] when the maximum number of unsuccessful attempts is exceeded.

#### EXAMINE — `ac-7_asm-examine`

- Access control policy

- procedures addressing unsuccessful logon attempts

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-7_asm-interview`

- Organizational personnel with information security responsibilities

- system developers

- system/network administrators

#### TEST — `ac-7_asm-test`

- Mechanisms implementing access control policy for unsuccessful logon attempts

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-7`. The library index records the exact source revision and hash.

- [SP 800-63-3](https://doi.org/10.6028/NIST.SP.800-63-3)

- [SP 800-124](https://doi.org/10.6028/NIST.SP.800-124r1)

- Catalog relationship **related**: `ac-2`.

- Catalog relationship **related**: `ac-9`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `ia-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
