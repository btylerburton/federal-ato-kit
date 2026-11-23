---
title: "PE-8.3 \u2014 Limit Personally Identifiable Information Elements"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PE-8.3 — Limit Personally Identifiable Information Elements

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations may have requirements that specify the contents of visitor access records. Limiting personally identifiable information in visitor access records when such information is not needed for operational purposes helps reduce the level of privacy risk created by a system.

### Requirements and exact statement parts

- `pe-8.3_smt`: Limit personally identifiable information contained in visitor access records to the following elements identified in the privacy risk assessment: [PARAM pe-08.03_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pe-8.3_smt — Limit personally identifiable information contained in visitor access records to the following elements identified in the privacy risk assessment: [PARAM pe-08.03_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pe-08.03_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pe-8.3_smt` — For “Limit personally identifiable information contained in visitor access records to the following elements identified in the privacy risk assessment: [PARAM pe-08.03_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pe-08.03_odp` — What approved value applies to **elements**? Record the value, scope, approving authority, and decision source.

  - Catalog context: elements identified in the privacy risk assessment to limit personally identifiable information contained in visitor access logs are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pe-8.3_obj` (pe-8.3_smt): personally identifiable information contained in visitor access records is limited to [PARAM pe-08.03_odp] identified in the privacy risk assessment.

#### EXAMINE — `pe-8.3_asm-examine`

- Physical and environmental protection policy

- personally identifiable information processing policy

- privacy risk assessment documentation

- privacy impact assessment

- visitor access records

- personally identifiable information inventory

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `pe-8.3_asm-interview`

- Organizational personnel with visitor access records responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `pe-8.3_asm-test`

- Organizational processes for maintaining and reviewing visitor access records

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pe-8.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pe-8`.

- Catalog relationship **related**: `ra-3`.

- Catalog relationship **related**: `sa-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
