---
title: "SI-7.1 \u2014 Integrity Checks"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-7.1 — Integrity Checks

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Security-relevant events include the identification of new threats to which organizational systems are susceptible and the installation of new hardware, software, or firmware. Transitional states include system startup, restart, shutdown, and abort.

### Requirements and exact statement parts

- `si-7.1_smt`: Perform an integrity check of [PARAM si-7.1_prm_1] [PARAM si-7.1_prm_2].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-7.1_smt — Perform an integrity check of [PARAM si-7.1_prm_1] [PARAM si-7.1_prm_2].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-7.1_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-7.1_prm_2: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-7.1_prm_3: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-7.1_prm_4: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07.01_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07.01_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07.01_odp.05: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07.01_odp.06: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07.01_odp.07: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07.01_odp.08: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07.01_odp.09: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07.01_odp.10: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07.01_odp.11: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07.01_odp.12: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-7.1_smt` — For “Perform an integrity check of [PARAM si-7.1_prm_1] [PARAM si-7.1_prm_2].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-7.1_prm_1` — What approved value applies to **organization-defined software, firmware, and information**? Record the value, scope, approving authority, and decision source.

- `si-7.1_prm_2` — What approved value applies to **selection; choose one-or-more from: at startup; at [PARAM si-7.1_prm_3]; [PARAM si-7.1_prm_4]**? Record the value, scope, approving authority, and decision source.

- `si-7.1_prm_3` — What approved value applies to **organization-defined transitional states or security-relevant events**? Record the value, scope, approving authority, and decision source.

- `si-7.1_prm_4` — What approved value applies to **organization-defined frequency**? Record the value, scope, approving authority, and decision source.

- `si-07.01_odp.01` — What approved value applies to **software**? Record the value, scope, approving authority, and decision source.

  - Catalog context: software on which an integrity check is to be performed is defined;

- `si-07.01_odp.02` — What approved value applies to **selection; choose one-or-more from: at startup; at [PARAM si-07.01_odp.03]; [PARAM si-07.01_odp.04]**? Record the value, scope, approving authority, and decision source.

- `si-07.01_odp.03` — What approved value applies to **transitional states or security-relevant events**? Record the value, scope, approving authority, and decision source.

  - Catalog context: transitional states or security-relevant events requiring integrity checks (on software) are defined (if selected);

- `si-07.01_odp.04` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency with which to perform an integrity check (on software) is defined (if selected);

- `si-07.01_odp.05` — What approved value applies to **firmware**? Record the value, scope, approving authority, and decision source.

  - Catalog context: firmware on which an integrity check is to be performed is defined;

- `si-07.01_odp.06` — What approved value applies to **selection; choose one-or-more from: at startup; at [PARAM si-07.01_odp.07]; [PARAM si-07.01_odp.08]**? Record the value, scope, approving authority, and decision source.

- `si-07.01_odp.07` — What approved value applies to **transitional states or security-relevant events**? Record the value, scope, approving authority, and decision source.

  - Catalog context: transitional states or security-relevant events requiring integrity checks (on firmware) are defined (if selected);

- `si-07.01_odp.08` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency with which to perform an integrity check (on firmware) is defined (if selected);

- `si-07.01_odp.09` — What approved value applies to **information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: information on which an integrity check is to be performed is defined;

- `si-07.01_odp.10` — What approved value applies to **selection; choose one-or-more from: at startup; at [PARAM si-07.01_odp.11]; [PARAM si-07.01_odp.12]**? Record the value, scope, approving authority, and decision source.

- `si-07.01_odp.11` — What approved value applies to **transitional states or security-relevant events**? Record the value, scope, approving authority, and decision source.

  - Catalog context: transitional states or security-relevant events requiring integrity checks (of information) are defined (if selected);

- `si-07.01_odp.12` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency with which to perform an integrity check (of information) is defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-7.1_obj-1` (si-7.1_smt): an integrity check of [PARAM si-07.01_odp.01] is performed [PARAM si-07.01_odp.02];

- `si-7.1_obj-2` (si-7.1_smt): an integrity check of [PARAM si-07.01_odp.05] is performed [PARAM si-07.01_odp.06];

- `si-7.1_obj-3` (si-7.1_smt): an integrity check of [PARAM si-07.01_odp.09] is performed [PARAM si-07.01_odp.10].

#### EXAMINE — `si-7.1_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing software, firmware, and information integrity testing

- system design documentation

- system configuration settings and associated documentation

- integrity verification tools and associated documentation

- records of integrity scans

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-7.1_asm-interview`

- Organizational personnel responsible for software, firmware, and/or information integrity

- organizational personnel with information security responsibilities

- system/network administrators

- system developer

#### TEST — `si-7.1_asm-test`

- Software, firmware, and information integrity verification tools

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-7.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
