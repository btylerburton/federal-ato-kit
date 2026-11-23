---
title: "AU-3.3 \u2014 Limit Personally Identifiable Information Elements"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-3.3 — Limit Personally Identifiable Information Elements

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Limiting personally identifiable information in audit records when such information is not needed for operational purposes helps reduce the level of privacy risk created by a system.

### Requirements and exact statement parts

- `au-3.3_smt`: Limit personally identifiable information contained in audit records to the following elements identified in the privacy risk assessment: [PARAM au-03.03_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-3.3_smt — Limit personally identifiable information contained in audit records to the following elements identified in the privacy risk assessment: [PARAM au-03.03_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-03.03_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-3.3_smt` — For “Limit personally identifiable information contained in audit records to the following elements identified in the privacy risk assessment: [PARAM au-03.03_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-03.03_odp` — What approved value applies to **elements**? Record the value, scope, approving authority, and decision source.

  - Catalog context: elements identified in the privacy risk assessment are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-3.3_obj` (au-3.3_smt): personally identifiable information contained in audit records is limited to [PARAM au-03.03_odp] identified in the privacy risk assessment.

#### EXAMINE — `au-3.3_asm-examine`

- Audit and accountability policy

- system security plan

- privacy plan

- privacy risk assessment

- privacy risk assessment results

- procedures addressing content of audit records

- system design documentation

- system configuration settings and associated documentation

- list of organization-defined auditable events

- system audit records

- third party contracts

- other relevant documents or records

#### INTERVIEW — `au-3.3_asm-interview`

- Organizational personnel with audit and accountability responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

- system developers

#### TEST — `au-3.3_asm-test`

- system audit capability

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-3.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `au-3`.

- Catalog relationship **related**: `ra-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
