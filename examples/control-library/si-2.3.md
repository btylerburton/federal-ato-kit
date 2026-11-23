---
title: "SI-2.3 \u2014 Time to Remediate Flaws and Benchmarks for Corrective Actions"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-2.3 — Time to Remediate Flaws and Benchmarks for Corrective Actions

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations determine the time it takes on average to correct system flaws after such flaws have been identified and subsequently establish organizational benchmarks (i.e., time frames) for taking corrective actions. Benchmarks can be established by the type of flaw or the severity of the potential vulnerability if the flaw can be exploited.

### Requirements and exact statement parts

- `si-2.3_smt`: Statement grouping; see child parts.

- `si-2.3_smt.a`: Measure the time between flaw identification and flaw remediation; and

- `si-2.3_smt.b`: Establish the following benchmarks for taking corrective actions: [PARAM si-02.03_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-2.3_smt.a — Measure the time between flaw identification and flaw remediation; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-2.3_smt.b — Establish the following benchmarks for taking corrective actions: [PARAM si-02.03_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-02.03_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-2.3_smt.a` — For “Measure the time between flaw identification and flaw remediation; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-2.3_smt.b` — For “Establish the following benchmarks for taking corrective actions: [PARAM si-02.03_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-02.03_odp` — What approved value applies to **benchmarks**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the benchmarks for taking corrective actions are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-2.3_obj.a` (si-2.3_smt.a): the time between flaw identification and flaw remediation is measured;

- `si-2.3_obj.b` (si-2.3_smt.b): [PARAM si-02.03_odp] for taking corrective actions have been established.

#### EXAMINE — `si-2.3_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing flaw remediation

- system design documentation

- system configuration settings and associated documentation

- list of benchmarks for taking corrective action on identified flaws

- records that provide timestamps of flaw identification and subsequent flaw remediation activities

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-2.3_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for flaw remediation

#### TEST — `si-2.3_asm-test`

- Organizational processes for identifying, reporting, and correcting system flaws

- mechanisms used to measure the time between flaw identification and flaw remediation

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-2.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
