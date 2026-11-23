---
title: "CM-7 \u2014 Least Functionality"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-7 — Least Functionality

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Systems provide a wide variety of functions and services. Some of the functions and services routinely provided by default may not be necessary to support essential organizational missions, functions, or operations. Additionally, it is sometimes convenient to provide multiple services from a single system component, but doing so increases risk over limiting the services provided by that single component. Where feasible, organizations limit component functionality to a single function per component. Organizations consider removing unused or unnecessary software and disabling unused or unnecessary physical and logical ports and protocols to prevent unauthorized connection of components, transfer of information, and tunneling. Organizations employ network scanning tools, intrusion detection and prevention systems, and end-point protection technologies, such as firewalls and host-based intrusion detection systems, to identify and prevent the use of prohibited functions, protocols, ports, and services. Least functionality can also be achieved as part of the fundamental design and development of the system (see SA-8 (catalog reference: `#sa-8`), SC-2 (catalog reference: `#sc-2`) , and SC-3 (catalog reference: `#sc-3`)).

### Requirements and exact statement parts

- `cm-7_smt`: Statement grouping; see child parts.

- `cm-7_smt.a`: Configure the system to provide only [PARAM cm-07_odp.01] ; and

- `cm-7_smt.b`: Prohibit or restrict the use of the following functions, ports, protocols, software, and/or services: [PARAM cm-7_prm_2].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-7_smt.a — Configure the system to provide only [PARAM cm-07_odp.01] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-7_smt.b — Prohibit or restrict the use of the following functions, ports, protocols, software, and/or services: [PARAM cm-7_prm_2].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-7_prm_2: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-07_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-07_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-07_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-07_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-07_odp.05: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-07_odp.06: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-7_smt.a` — For “Configure the system to provide only [PARAM cm-07_odp.01] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-7_smt.b` — For “Prohibit or restrict the use of the following functions, ports, protocols, software, and/or services: [PARAM cm-7_prm_2].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-7_prm_2` — What approved value applies to **organization-defined prohibited or restricted functions, system ports, protocols, software, and/or services**? Record the value, scope, approving authority, and decision source.

- `cm-07_odp.01` — What approved value applies to **mission-essential capabilities**? Record the value, scope, approving authority, and decision source.

  - Catalog context: mission-essential capabilities for the system are defined;

- `cm-07_odp.02` — What approved value applies to **functions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: functions to be prohibited or restricted are defined;

- `cm-07_odp.03` — What approved value applies to **ports**? Record the value, scope, approving authority, and decision source.

  - Catalog context: ports to be prohibited or restricted are defined;

- `cm-07_odp.04` — What approved value applies to **protocols**? Record the value, scope, approving authority, and decision source.

  - Catalog context: protocols to be prohibited or restricted are defined;

- `cm-07_odp.05` — What approved value applies to **software**? Record the value, scope, approving authority, and decision source.

  - Catalog context: software to be prohibited or restricted is defined;

- `cm-07_odp.06` — What approved value applies to **services**? Record the value, scope, approving authority, and decision source.

  - Catalog context: services to be prohibited or restricted are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-7_obj.a` (cm-7_smt.a): the system is configured to provide only [PARAM cm-07_odp.01];

- `cm-7_obj.b-1` (cm-7_smt.b): the use of [PARAM cm-07_odp.02] is prohibited or restricted;

- `cm-7_obj.b-2` (cm-7_smt.b): the use of [PARAM cm-07_odp.03] is prohibited or restricted;

- `cm-7_obj.b-3` (cm-7_smt.b): the use of [PARAM cm-07_odp.04] is prohibited or restricted;

- `cm-7_obj.b-4` (cm-7_smt.b): the use of [PARAM cm-07_odp.05] is prohibited or restricted;

- `cm-7_obj.b-5` (cm-7_smt.b): the use of [PARAM cm-07_odp.06] is prohibited or restricted.

#### EXAMINE — `cm-7_asm-examine`

- Configuration management policy

- procedures addressing least functionality in the system

- configuration management plan

- system design documentation

- system configuration settings and associated documentation

- system component inventory

- common secure configuration checklists

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-7_asm-interview`

- Organizational personnel with security configuration management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `cm-7_asm-test`

- Organizational processes prohibiting or restricting functions, ports, protocols, software, and/or services

- mechanisms implementing restrictions or prohibition of functions, ports, protocols, software, and/or services

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-7`. The library index records the exact source revision and hash.

- [FIPS 140-3](https://doi.org/10.6028/NIST.FIPS.140-3)

- [FIPS 180-4](https://doi.org/10.6028/NIST.FIPS.180-4)

- [FIPS 186-4](https://doi.org/10.6028/NIST.FIPS.186-4)

- [FIPS 202](https://doi.org/10.6028/NIST.FIPS.202)

- [SP 800-167](https://doi.org/10.6028/NIST.SP.800-167)

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-4`.

- Catalog relationship **related**: `cm-2`.

- Catalog relationship **related**: `cm-5`.

- Catalog relationship **related**: `cm-6`.

- Catalog relationship **related**: `cm-11`.

- Catalog relationship **related**: `ra-5`.

- Catalog relationship **related**: `sa-4`.

- Catalog relationship **related**: `sa-5`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sa-9`.

- Catalog relationship **related**: `sa-15`.

- Catalog relationship **related**: `sc-2`.

- Catalog relationship **related**: `sc-3`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `sc-37`.

- Catalog relationship **related**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
