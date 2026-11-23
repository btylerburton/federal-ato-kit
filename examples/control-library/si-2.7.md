---
title: "SI-2.7 \u2014 Root Cause Analysis"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-2.7 — Root Cause Analysis

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Root cause analysis includes a wide range of approaches, tools, and techniques to systematically identify the underlying cause of issues or failures to systems and systems components (hardware, software, and firmware). Organizations consider the severity of the incident to determine what root cause analysis method is used and how quickly implementation of the remediation actions. The root cause analysis includes a timeline, missed warning signs, key decisions, gaps, mitigations, and verification of effectiveness. The actions identified to address the source of the issue are implemented and integrated into applicable organizational policy, procedures, and control implementation.

### Requirements and exact statement parts

- `si-2.7_smt`: Statement grouping; see child parts.

- `si-2.7_smt.a`: Conduct root cause analysis to identify underlying causes of issues or failures.

- `si-2.7_smt.b`: Develop actions to address the root cause of the issue or failure.

- `si-2.7_smt.c`: Implement the actions and monitor the implementation for effectiveness.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-2.7_smt.a — Conduct root cause analysis to identify underlying causes of issues or failures.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-2.7_smt.b — Develop actions to address the root cause of the issue or failure.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-2.7_smt.c — Implement the actions and monitor the implementation for effectiveness.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `si-2.7_smt.a` — For “Conduct root cause analysis to identify underlying causes of issues or failures.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-2.7_smt.b` — For “Develop actions to address the root cause of the issue or failure.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-2.7_smt.c` — For “Implement the actions and monitor the implementation for effectiveness.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-2.7_obj` (si-2.7_smt): Determine if:

- `si-2.7_obj.a` (si-2.7_smt.a): Root cause analysis is conducted to identify underlying causes of issues or failures

- `si-2.7_obj.b` (si-2.7_smt.b): Actions to address the root cause of the issue of failure are developed

- `si-2.7_obj.c-1` (si-2.7_smt.c): The actions (defined in SI-02(07)b. (catalog reference: `#si-2.7_smt.b`)) are implemented

- `si-2.7_obj.c-2` (si-2.7_smt.c): The implementation of actions is monitored for effectiveness.

#### EXAMINE — `si-2.7_asm-examine`

- System and information integrity policy;

- system and information integrity procedures;

- procedures addressing flaw remediation;

- procedures addressing root cause analysis/process improvement;

- system design documentation;

- system configuration settings and associated documentation;

- system audit records;

- system security and privacy plan;

- other relevant documents or records

#### INTERVIEW — `si-2.7_asm-interview`

- System/network administrators;

- organizational personnel with information security and privacy responsibilities;

- organizational personnel responsible for installing, configuring, and/or maintaining the system;

- organizational personnel responsible for flaw remediation;

- organizational personnel with configuration management responsibilities

#### TEST — `si-2.7_asm-test`

- Organizational processes for identifying, reporting, and correcting system flaws;

- organizational process for installing software and firmware updates;

- mechanisms supporting and/or implementing the reporting and correcting of system flaws;

- mechanisms supporting and/or implementing testing software and firmware updates

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-2.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-2`.

- Catalog relationship **related**: `ac-1`.

- Catalog relationship **related**: `at-1`.

- Catalog relationship **related**: `au-1`.

- Catalog relationship **related**: `ca-1`.

- Catalog relationship **related**: `cm-1`.

- Catalog relationship **related**: `cp-1`.

- Catalog relationship **related**: `ia-1`.

- Catalog relationship **related**: `ir-1`.

- Catalog relationship **related**: `ma-1`.

- Catalog relationship **related**: `mp-1`.

- Catalog relationship **related**: `pe-1`.

- Catalog relationship **related**: `pl-1`.

- Catalog relationship **related**: `pm-1`.

- Catalog relationship **related**: `ps-1`.

- Catalog relationship **related**: `pt-1`.

- Catalog relationship **related**: `ra-1`.

- Catalog relationship **related**: `sa-1`.

- Catalog relationship **related**: `sc-1`.

- Catalog relationship **related**: `si-1`.

- Catalog relationship **related**: `sr-1`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `ca-7`.

- Catalog relationship **related**: `ir-6`.

- Catalog relationship **related**: `ir-8`.

- Catalog relationship **related**: `ma-3`.

- Catalog relationship **related**: `ra-5`.

- Catalog relationship **related**: `sa-11`.

- Catalog relationship **related**: `sa-15`.

- Catalog relationship **related**: `sr-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
