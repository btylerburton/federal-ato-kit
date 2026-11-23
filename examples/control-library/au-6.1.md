---
title: "AU-6.1 \u2014 Automated Process Integration"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-6.1 — Automated Process Integration

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizational processes that benefit from integrated audit record review, analysis, and reporting include incident response, continuous monitoring, contingency planning, investigation and response to suspicious activities, and Inspector General audits.

### Requirements and exact statement parts

- `au-6.1_smt`: Integrate audit record review, analysis, and reporting processes using [PARAM au-06.01_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-6.1_smt — Integrate audit record review, analysis, and reporting processes using [PARAM au-06.01_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-06.01_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-6.1_smt` — For “Integrate audit record review, analysis, and reporting processes using [PARAM au-06.01_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-06.01_odp` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used for integrating audit record review, analysis, and reporting processes are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-6.1_obj` (au-6.1_smt): audit record review, analysis, and reporting processes are integrated using [PARAM au-06.01_odp].

#### EXAMINE — `au-6.1_asm-examine`

- Audit and accountability policy

- system security plan

- privacy plan

- procedures addressing audit review, analysis, and reporting

- procedures addressing investigation and response to suspicious activities

- system design documentation

- system configuration settings and associated documentation

- system audit records

- other relevant documents or records

#### INTERVIEW — `au-6.1_asm-interview`

- Organizational personnel with audit review, analysis, and reporting responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `au-6.1_asm-test`

- Automated mechanisms integrating audit review, analysis, and reporting processes

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-6.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `au-6`.

- Catalog relationship **related**: `pm-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
