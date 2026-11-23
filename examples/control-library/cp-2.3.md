---
title: "CP-2.3 \u2014 Resume Mission and Business Functions"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-2.3 — Resume Mission and Business Functions

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations may choose to conduct contingency planning activities to resume mission and business functions as part of business continuity planning or as part of business impact analyses. Organizations prioritize the resumption of mission and business functions. The time period for resuming mission and business functions may be dependent on the severity and extent of the disruptions to the system and its supporting infrastructure.

### Requirements and exact statement parts

- `cp-2.3_smt`: Plan for the resumption of [PARAM cp-02.03_odp.01] mission and business functions within [PARAM cp-02.03_odp.02] of contingency plan activation.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-2.3_smt — Plan for the resumption of [PARAM cp-02.03_odp.01] mission and business functions within [PARAM cp-02.03_odp.02] of contingency plan activation.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cp-02.03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-02.03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cp-2.3_smt` — For “Plan for the resumption of [PARAM cp-02.03_odp.01] mission and business functions within [PARAM cp-02.03_odp.02] of contingency plan activation.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cp-02.03_odp.01` — What approved value applies to **selection; choose one from: all; essential**? Record the value, scope, approving authority, and decision source.

- `cp-02.03_odp.02` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the contingency plan activation time period within which to resume mission and business functions is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-2.3_obj` (cp-2.3_smt): the resumption of [PARAM cp-02.03_odp.01] mission and business functions are planned for within [PARAM cp-02.03_odp.02] of contingency plan activation.

#### EXAMINE — `cp-2.3_asm-examine`

- Contingency planning policy

- procedures addressing contingency operations for the system

- contingency plan

- business impact assessment

- system security plan

- privacy plan

- other related plans

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-2.3_asm-interview`

- Organizational personnel with contingency planning and plan implementation responsibilities

- organizational personnel with information security and privacy responsibilities

- organizational personnel with knowledge of requirements for mission and business functions

#### TEST — `cp-2.3_asm-test`

- Organizational processes for resumption of missions and business functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-2.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cp-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
