---
title: "SI-3.8 \u2014 Detect Unauthorized Commands"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-3.8 — Detect Unauthorized Commands

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Detecting unauthorized commands can be applied to critical interfaces other than kernel-based interfaces, including interfaces with virtual machines and privileged applications. Unauthorized operating system commands include commands for kernel functions from system processes that are not trusted to initiate such commands as well as commands for kernel functions that are suspicious even though commands of that type are reasonable for processes to initiate. Organizations can define the malicious commands to be detected by a combination of command types, command classes, or specific instances of commands. Organizations can also define hardware components by component type, component, component location in the network, or a combination thereof. Organizations may select different actions for different types, classes, or instances of malicious commands.

### Requirements and exact statement parts

- `si-3.8_smt`: Statement grouping; see child parts.

- `si-3.8_smt.a`: Detect the following unauthorized operating system commands through the kernel application programming interface on [PARAM si-03.08_odp.02]: [PARAM si-03.08_odp.01] ; and

- `si-3.8_smt.b`: [PARAM si-03.08_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-3.8_smt.a — Detect the following unauthorized operating system commands through the kernel application programming interface on [PARAM si-03.08_odp.02]: [PARAM si-03.08_odp.01] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-3.8_smt.b — [PARAM si-03.08_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-03.08_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-03.08_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-03.08_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-3.8_smt.a` — For “Detect the following unauthorized operating system commands through the kernel application programming interface on [PARAM si-03.08_odp.02]: [PARAM si-03.08_odp.01] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-3.8_smt.b` — For “[PARAM si-03.08_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-03.08_odp.01` — What approved value applies to **unauthorized operating system commands**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system hardware components for which unauthorized operating system commands are to be detected through the kernel application programming interface are defined;

- `si-03.08_odp.02` — What approved value applies to **system hardware components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: unauthorized operating system commands to be detected are defined;

- `si-03.08_odp.03` — What approved value applies to **selection; choose one-or-more from: issue a warning; audit the command execution; prevent the execution of the command**? Record the value, scope, approving authority, and decision source.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-3.8_obj.a` (si-3.8_smt.a): [PARAM si-03.08_odp.01] are detected through the kernel application programming interface on [PARAM si-03.08_odp.02];

- `si-3.8_obj.b` (si-3.8_smt.b): [PARAM si-03.08_odp.03] is/are performed.

#### EXAMINE — `si-3.8_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing malicious code protection

- system design documentation

- malicious code protection mechanisms

- warning messages sent upon the detection of unauthorized operating system command execution

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-3.8_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developers

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for malicious code protection

#### TEST — `si-3.8_asm-test`

- Mechanisms supporting and/or implementing malicious code protection capabilities

- mechanisms supporting and/or implementing the detection of unauthorized operating system commands through the kernel application programming interface

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-3.8`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-3`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
