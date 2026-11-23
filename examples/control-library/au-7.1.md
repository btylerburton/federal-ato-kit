---
title: "AU-7.1 \u2014 Automatic Processing"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-7.1 — Automatic Processing

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Events of interest can be identified by the content of audit records, including system resources involved, information objects accessed, identities of individuals, event types, event locations, event dates and times, Internet Protocol addresses involved, or event success or failure. Organizations may define event criteria to any degree of granularity required, such as locations selectable by a general networking location or by specific system component.

### Requirements and exact statement parts

- `au-7.1_smt`: Provide and implement the capability to process, sort, and search audit records for events of interest based on the following content: [PARAM au-07.01_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-7.1_smt — Provide and implement the capability to process, sort, and search audit records for events of interest based on the following content: [PARAM au-07.01_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-07.01_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-7.1_smt` — For “Provide and implement the capability to process, sort, and search audit records for events of interest based on the following content: [PARAM au-07.01_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-07.01_odp` — What approved value applies to **fields within audit records**? Record the value, scope, approving authority, and decision source.

  - Catalog context: fields within audit records that can be processed, sorted, or searched are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-7.1_obj-1` (au-7.1_smt): the capability to process, sort, and search audit records for events of interest based on [PARAM au-07.01_odp] are provided;

- `au-7.1_obj-2` (au-7.1_smt): the capability to process, sort, and search audit records for events of interest based on [PARAM au-07.01_odp] are implemented.

#### EXAMINE — `au-7.1_asm-examine`

- Audit and accountability policy

- system security plan

- privacy plan

- procedures addressing audit reduction and report generation

- system design documentation

- system configuration settings and associated documentation

- audit reduction, review, analysis, and reporting tools

- audit record criteria (fields) establishing events of interest

- system audit records

- other relevant documents or records

#### INTERVIEW — `au-7.1_asm-interview`

- Organizational personnel with audit reduction and report generation responsibilities

- organizational personnel with information security and privacy responsibilities

- system developers

#### TEST — `au-7.1_asm-test`

- Audit reduction and report generation capability

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-7.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `au-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
