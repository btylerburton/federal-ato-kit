---
title: "PT-4.3 \u2014 Revocation"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PT-4.3 — Revocation

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Revocation of consent enables individuals to exercise control over their initial consent decision when circumstances change. Organizations consider usability factors in enabling easy-to-use revocation capabilities.

### Requirements and exact statement parts

- `pt-4.3_smt`: Implement [PARAM pt-04.03_odp] for individuals to revoke consent to the processing of their personally identifiable information.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pt-4.3_smt — Implement [PARAM pt-04.03_odp] for individuals to revoke consent to the processing of their personally identifiable information.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pt-04.03_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pt-4.3_smt` — For “Implement [PARAM pt-04.03_odp] for individuals to revoke consent to the processing of their personally identifiable information.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pt-04.03_odp` — What approved value applies to **tools or mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the tools or mechanisms to be implemented for revoking consent to the processing of personally identifiable information are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pt-4.3_obj` (pt-4.3_smt): the [PARAM pt-04.03_odp] are implemented for individuals to revoke consent to the processing of their personally identifiable information.

#### EXAMINE — `pt-4.3_asm-examine`

- Personally identifiable information processing and transparency policy and procedures

- consent revocation policies and procedures

- consent revocation user interface or user experience

- privacy plan

- other relevant documents or records

#### INTERVIEW — `pt-4.3_asm-interview`

- Organizational personnel with personally identifiable information processing and transparency responsibilities

- organizational personnel with user interface or user experience responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `pt-4.3_asm-test`

- Organizational processes for consenting to the processing of personally identifiable information

- tools or mechanisms for implementing consent revocation

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pt-4.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pt-4`.

- Catalog relationship **related**: `pt-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
