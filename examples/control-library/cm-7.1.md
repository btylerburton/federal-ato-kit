---
title: "CM-7.1 \u2014 Periodic Review"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-7.1 — Periodic Review

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations review functions, ports, protocols, and services provided by systems or system components to determine the functions and services that are candidates for elimination. Such reviews are especially important during transition periods from older technologies to newer technologies (e.g., transition from IPv4 to IPv6). These technology transitions may require implementing the older and newer technologies simultaneously during the transition period and returning to minimum essential functions, ports, protocols, and services at the earliest opportunity. Organizations can either decide the relative security of the function, port, protocol, and/or service or base the security decision on the assessment of other entities. Unsecure protocols include Bluetooth, FTP, and peer-to-peer networking.

### Requirements and exact statement parts

- `cm-7.1_smt`: Statement grouping; see child parts.

- `cm-7.1_smt.a`: Review the system [PARAM cm-07.01_odp.01] to identify unnecessary and/or nonsecure functions, ports, protocols, software, and services; and

- `cm-7.1_smt.b`: Disable or remove [PARAM cm-7.1_prm_2].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-7.1_smt.a — Review the system [PARAM cm-07.01_odp.01] to identify unnecessary and/or nonsecure functions, ports, protocols, software, and services; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-7.1_smt.b — Disable or remove [PARAM cm-7.1_prm_2].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-7.1_prm_2: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-07.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-07.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-07.01_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-07.01_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-07.01_odp.05: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-07.01_odp.06: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-7.1_smt.a` — For “Review the system [PARAM cm-07.01_odp.01] to identify unnecessary and/or nonsecure functions, ports, protocols, software, and services; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-7.1_smt.b` — For “Disable or remove [PARAM cm-7.1_prm_2].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-7.1_prm_2` — What approved value applies to **organization-defined functions, ports, protocols, software, and services within the system deemed to be unnecessary and/or nonsecure**? Record the value, scope, approving authority, and decision source.

- `cm-07.01_odp.01` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which to review the system to identify unnecessary and/or non-secure functions, ports, protocols, software, and/or services is defined;

- `cm-07.01_odp.02` — What approved value applies to **functions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: functions to be disabled or removed when deemed unnecessary or non-secure are defined;

- `cm-07.01_odp.03` — What approved value applies to **ports**? Record the value, scope, approving authority, and decision source.

  - Catalog context: ports to be disabled or removed when deemed unnecessary or non-secure are defined;

- `cm-07.01_odp.04` — What approved value applies to **protocols**? Record the value, scope, approving authority, and decision source.

  - Catalog context: protocols to be disabled or removed when deemed unnecessary or non-secure are defined;

- `cm-07.01_odp.05` — What approved value applies to **software**? Record the value, scope, approving authority, and decision source.

  - Catalog context: software to be disabled or removed when deemed unnecessary or non-secure is defined;

- `cm-07.01_odp.06` — What approved value applies to **services**? Record the value, scope, approving authority, and decision source.

  - Catalog context: services to be disabled or removed when deemed unnecessary or non-secure are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-7.1_obj.a` (cm-7.1_smt.a): the system is reviewed [PARAM cm-07.01_odp.01] to identify unnecessary and/or non-secure functions, ports, protocols, software, and services:

- `cm-7.1_obj.b-1` (cm-7.1_smt.b): [PARAM cm-07.01_odp.02] deemed to be unnecessary and/or non-secure are disabled or removed;

- `cm-7.1_obj.b-2` (cm-7.1_smt.b): [PARAM cm-07.01_odp.03] deemed to be unnecessary and/or non-secure are disabled or removed;

- `cm-7.1_obj.b-3` (cm-7.1_smt.b): [PARAM cm-07.01_odp.04] deemed to be unnecessary and/or non-secure are disabled or removed;

- `cm-7.1_obj.b-4` (cm-7.1_smt.b): [PARAM cm-07.01_odp.05] deemed to be unnecessary and/or non-secure is disabled or removed;

- `cm-7.1_obj.b-5` (cm-7.1_smt.b): [PARAM cm-07.01_odp.06] deemed to be unnecessary and/or non-secure are disabled or removed.

#### EXAMINE — `cm-7.1_asm-examine`

- Configuration management policy

- procedures addressing least functionality in the system

- configuration management plan

- system design documentation

- system configuration settings and associated documentation

- common secure configuration checklists

- documented reviews of functions, ports, protocols, and/or services

- change control records

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-7.1_asm-interview`

- Organizational personnel with responsibilities for reviewing functions, ports, protocols, and services on the system

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `cm-7.1_asm-test`

- Organizational processes for reviewing or disabling functions, ports, protocols, and services on the system

- mechanisms implementing review and disabling of functions, ports, protocols, and/or services

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-7.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-7`.

- Catalog relationship **related**: `ac-18`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
