---
title: "CP-4.3 \u2014 Automated Testing"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-4.3 — Automated Testing

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Automated mechanisms facilitate thorough and effective testing of contingency plans by providing more complete coverage of contingency issues, selecting more realistic test scenarios and environments, and effectively stressing the system and supported mission and business functions.

### Requirements and exact statement parts

- `cp-4.3_smt`: Test the contingency plan using [PARAM cp-04.03_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-4.3_smt — Test the contingency plan using [PARAM cp-04.03_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cp-04.03_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cp-4.3_smt` — For “Test the contingency plan using [PARAM cp-04.03_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cp-04.03_odp` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms for contingency plan testing are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-4.3_obj` (cp-4.3_smt): the contingency plan is tested using [PARAM cp-04.03_odp].

#### EXAMINE — `cp-4.3_asm-examine`

- Contingency planning policy

- procedures addressing contingency plan testing

- contingency plan

- automated mechanisms supporting contingency plan testing

- contingency plan test documentation

- contingency plan test results

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-4.3_asm-interview`

- Organizational personnel with contingency plan testing responsibilities

- organizational personnel with information security responsibilities

#### TEST — `cp-4.3_asm-test`

- Organizational processes for contingency plan testing

- automated mechanisms supporting contingency plan testing

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-4.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cp-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
