---
title: "AC-7.2 \u2014 Purge or Wipe Mobile Device"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-7.2 — Purge or Wipe Mobile Device

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

A mobile device is a computing device that has a small form factor such that it can be carried by a single individual; is designed to operate without a physical connection; possesses local, non-removable or removable data storage; and includes a self-contained power source. Purging or wiping the device applies only to mobile devices for which the organization-defined number of unsuccessful logons occurs. The logon is to the mobile device, not to any one account on the device. Successful logons to accounts on mobile devices reset the unsuccessful logon count to zero. Purging or wiping may be unnecessary if the information on the device is protected with sufficiently strong encryption mechanisms.

### Requirements and exact statement parts

- `ac-7.2_smt`: Purge or wipe information from [PARAM ac-07.02_odp.01] based on [PARAM ac-07.02_odp.02] after [PARAM ac-07.02_odp.03] consecutive, unsuccessful device logon attempts.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-7.2_smt — Purge or wipe information from [PARAM ac-07.02_odp.01] based on [PARAM ac-07.02_odp.02] after [PARAM ac-07.02_odp.03] consecutive, unsuccessful device logon attempts.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-07.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-07.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-07.02_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-7.2_smt` — For “Purge or wipe information from [PARAM ac-07.02_odp.01] based on [PARAM ac-07.02_odp.02] after [PARAM ac-07.02_odp.03] consecutive, unsuccessful device logon attempts.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-07.02_odp.01` — What approved value applies to **mobile devices**? Record the value, scope, approving authority, and decision source.

  - Catalog context: mobile devices to be purged or wiped of information are defined;

- `ac-07.02_odp.02` — What approved value applies to **purging or wiping requirements and techniques**? Record the value, scope, approving authority, and decision source.

  - Catalog context: purging and wiping requirements and techniques to be used when mobile devices are purged or wiped of information are defined;

- `ac-07.02_odp.03` — What approved value applies to **number**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the number of consecutive, unsuccessful logon attempts before the information is purged or wiped from mobile devices is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-7.2_obj` (ac-7.2_smt): information is purged or wiped from [PARAM ac-07.02_odp.01] based on [PARAM ac-07.02_odp.02] after [PARAM ac-07.02_odp.03] consecutive, unsuccessful device logon attempts.

#### EXAMINE — `ac-7.2_asm-examine`

- Access control policy

- procedures addressing unsuccessful logon attempts on mobile devices

- system design documentation

- system configuration settings and associated documentation

- list of mobile devices to be purged/wiped after organization-defined consecutive, unsuccessful device logon attempts

- list of purging/wiping requirements or techniques for mobile devices

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-7.2_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

#### TEST — `ac-7.2_asm-test`

- Mechanisms implementing access control policy for unsuccessful device logon attempts

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-7.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-7`.

- Catalog relationship **related**: `ac-19`.

- Catalog relationship **related**: `mp-5`.

- Catalog relationship **related**: `mp-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
