---
title: "CM-8.3 \u2014 Automated Unauthorized Component Detection"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-8.3 — Automated Unauthorized Component Detection

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Automated unauthorized component detection is applied in addition to the monitoring for unauthorized remote connections and mobile devices. Monitoring for unauthorized system components may be accomplished on an ongoing basis or by the periodic scanning of systems for that purpose. Automated mechanisms may also be used to prevent the connection of unauthorized components (see CM-7(9) (catalog reference: `#cm-7.9`) ). Automated mechanisms can be implemented in systems or in separate system components. When acquiring and implementing automated mechanisms, organizations consider whether such mechanisms depend on the ability of the system component to support an agent or supplicant in order to be detected since some types of components do not have or cannot support agents (e.g., IoT devices, sensors). Isolation can be achieved , for example, by placing unauthorized system components in separate domains or subnets or quarantining such components. This type of component isolation is commonly referred to as "sandboxing."

### Requirements and exact statement parts

- `cm-8.3_smt`: Statement grouping; see child parts.

- `cm-8.3_smt.a`: Detect the presence of unauthorized hardware, software, and firmware components within the system using [PARAM cm-8.3_prm_1] [PARAM cm-08.03_odp.04] ; and

- `cm-8.3_smt.b`: Take the following actions when unauthorized components are detected: [PARAM cm-08.03_odp.05].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-8.3_smt.a — Detect the presence of unauthorized hardware, software, and firmware components within the system using [PARAM cm-8.3_prm_1] [PARAM cm-08.03_odp.04] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-8.3_smt.b — Take the following actions when unauthorized components are detected: [PARAM cm-08.03_odp.05].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-8.3_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-08.03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-08.03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-08.03_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-08.03_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-08.03_odp.05: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-08.03_odp.06: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-8.3_smt.a` — For “Detect the presence of unauthorized hardware, software, and firmware components within the system using [PARAM cm-8.3_prm_1] [PARAM cm-08.03_odp.04] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-8.3_smt.b` — For “Take the following actions when unauthorized components are detected: [PARAM cm-08.03_odp.05].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-8.3_prm_1` — What approved value applies to **organization-defined automated mechanisms**? Record the value, scope, approving authority, and decision source.

- `cm-08.03_odp.01` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used to detect the presence of unauthorized hardware within the system are defined;

- `cm-08.03_odp.02` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used to detect the presence of unauthorized software within the system are defined;

- `cm-08.03_odp.03` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used to detect the presence of unauthorized firmware within the system are defined;

- `cm-08.03_odp.04` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which automated mechanisms are used to detect the presence of unauthorized system components within the system is defined;

- `cm-08.03_odp.05` — What approved value applies to **selection; choose one-or-more from: disable network access by unauthorized components; isolate unauthorized components; notify [PARAM cm-08.03_odp.06]**? Record the value, scope, approving authority, and decision source.

- `cm-08.03_odp.06` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to be notified when unauthorized components are detected is/are defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-8.3_obj.a-1` (cm-8.3_smt.a): the presence of unauthorized hardware within the system is detected using [PARAM cm-08.03_odp.01] [PARAM cm-08.03_odp.04];

- `cm-8.3_obj.a-2` (cm-8.3_smt.a): the presence of unauthorized software within the system is detected using [PARAM cm-08.03_odp.02] [PARAM cm-08.03_odp.04];

- `cm-8.3_obj.a-3` (cm-8.3_smt.a): the presence of unauthorized firmware within the system is detected using [PARAM cm-08.03_odp.03] [PARAM cm-08.03_odp.04];

- `cm-8.3_obj.b-1` (cm-8.3_smt.b): [PARAM cm-08.03_odp.05] are taken when unauthorized hardware is detected;

- `cm-8.3_obj.b-2` (cm-8.3_smt.b): [PARAM cm-08.03_odp.05] are taken when unauthorized software is detected;

- `cm-8.3_obj.b-3` (cm-8.3_smt.b): [PARAM cm-08.03_odp.05] are taken when unauthorized firmware is detected.

#### EXAMINE — `cm-8.3_asm-examine`

- Configuration management policy

- procedures addressing system component inventory

- configuration management plan

- system design documentation

- system security plan

- system component inventory

- change control records

- alerts/notifications of unauthorized components within the system

- system monitoring records

- system maintenance records

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-8.3_asm-interview`

- Organizational personnel with component inventory management responsibilities

- organizational personnel with responsibilities for managing the automated mechanisms implementing unauthorized system component detection

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `cm-8.3_asm-test`

- Organizational processes for detection of unauthorized system components

- organizational processes for taking action when unauthorized system components are detected

- automated mechanisms supporting and/or implementing the detection of unauthorized system components

- automated mechanisms supporting and/or implementing actions taken when unauthorized system components are detected

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-8.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-8`.

- Catalog relationship **related**: `ac-19`.

- Catalog relationship **related**: `ca-7`.

- Catalog relationship **related**: `ra-5`.

- Catalog relationship **related**: `sc-3`.

- Catalog relationship **related**: `sc-39`.

- Catalog relationship **related**: `sc-44`.

- Catalog relationship **related**: `si-3`.

- Catalog relationship **related**: `si-4`.

- Catalog relationship **related**: `si-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
