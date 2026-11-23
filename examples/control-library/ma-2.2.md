---
title: "MA-2.2 \u2014 Automated Maintenance Activities"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-2.2 — Automated Maintenance Activities

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The use of automated mechanisms to manage and control system maintenance programs and activities helps to ensure the generation of timely, accurate, complete, and consistent maintenance records.

### Requirements and exact statement parts

- `ma-2.2_smt`: Statement grouping; see child parts.

- `ma-2.2_smt.a`: Schedule, conduct, and document maintenance, repair, and replacement actions for the system using [PARAM ma-2.2_prm_1] ; and

- `ma-2.2_smt.b`: Produce up-to date, accurate, and complete records of all maintenance, repair, and replacement actions requested, scheduled, in process, and completed.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-2.2_smt.a — Schedule, conduct, and document maintenance, repair, and replacement actions for the system using [PARAM ma-2.2_prm_1] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-2.2_smt.b — Produce up-to date, accurate, and complete records of all maintenance, repair, and replacement actions requested, scheduled, in process, and completed.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ma-2.2_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ma-02.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ma-02.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ma-02.02_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ma-2.2_smt.a` — For “Schedule, conduct, and document maintenance, repair, and replacement actions for the system using [PARAM ma-2.2_prm_1] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-2.2_smt.b` — For “Produce up-to date, accurate, and complete records of all maintenance, repair, and replacement actions requested, scheduled, in process, and completed.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ma-2.2_prm_1` — What approved value applies to **organization-defined automated mechanisms**? Record the value, scope, approving authority, and decision source.

- `ma-02.02_odp.01` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used to schedule maintenance, repair, and replacement actions for the system are defined;

- `ma-02.02_odp.02` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used to conduct maintenance, repair, and replacement actions for the system are defined;

- `ma-02.02_odp.03` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used to document maintenance, repair, and replacement actions for the system are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-2.2_obj.a-1` (ma-2.2_smt.a): [PARAM ma-02.02_odp.01] are used to schedule maintenance, repair, and replacement actions for the system;

- `ma-2.2_obj.a-2` (ma-2.2_smt.a): [PARAM ma-02.02_odp.02] are used to conduct maintenance, repair, and replacement actions for the system;

- `ma-2.2_obj.a-3` (ma-2.2_smt.a): [PARAM ma-02.02_odp.03] are used to document maintenance, repair, and replacement actions for the system;

- `ma-2.2_obj.b-1` (ma-2.2_smt.b): up-to date, accurate, and complete records of all maintenance actions requested, scheduled, in process, and completed are produced.

- `ma-2.2_obj.b-2` (ma-2.2_smt.b): up-to date, accurate, and complete records of all repair actions requested, scheduled, in process, and completed are produced.

- `ma-2.2_obj.b-3` (ma-2.2_smt.b): up-to date, accurate, and complete records of all replacement actions requested, scheduled, in process, and completed are produced.

#### EXAMINE — `ma-2.2_asm-examine`

- Maintenance policy

- procedures addressing controlled system maintenance

- automated mechanisms supporting system maintenance activities

- system configuration settings and associated documentation

- maintenance records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-2.2_asm-interview`

- Organizational personnel with system maintenance responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ma-2.2_asm-test`

- Automated mechanisms supporting and/or implementing controlled maintenance

- automated mechanisms supporting and/or implementing the production of records of maintenance and repair actions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-2.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ma-2`.

- Catalog relationship **related**: `ma-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
