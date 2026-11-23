---
title: "AU-6.7 \u2014 Permitted Actions"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-6.7 — Permitted Actions

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations specify permitted actions for system processes, roles, and users associated with the review, analysis, and reporting of audit records through system account management activities. Specifying permitted actions on audit record information is a way to enforce the principle of least privilege. Permitted actions are enforced by the system and include read, write, execute, append, and delete.

### Requirements and exact statement parts

- `au-6.7_smt`: Specify the permitted actions for each [PARAM au-06.07_odp] associated with the review, analysis, and reporting of audit record information.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-6.7_smt — Specify the permitted actions for each [PARAM au-06.07_odp] associated with the review, analysis, and reporting of audit record information.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-06.07_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-6.7_smt` — For “Specify the permitted actions for each [PARAM au-06.07_odp] associated with the review, analysis, and reporting of audit record information.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-06.07_odp` — What approved value applies to **selection; choose one-or-more from: system process; role; user**? Record the value, scope, approving authority, and decision source.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-6.7_obj` (au-6.7_smt): the permitted actions for each [PARAM au-06.07_odp] associated with the review, analysis, and reporting of audit record information are specified.

#### EXAMINE — `au-6.7_asm-examine`

- Audit and accountability policy

- procedures addressing process, role and/or user permitted actions from audit review, analysis, and reporting

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `au-6.7_asm-interview`

- Organizational personnel with audit review, analysis, and reporting responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `au-6.7_asm-test`

- Mechanisms supporting permitted actions for the review, analysis, and reporting of audit information

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-6.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `au-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
