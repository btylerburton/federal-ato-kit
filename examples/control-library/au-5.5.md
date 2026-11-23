---
title: "AU-5.5 \u2014 Alternate Audit Logging Capability"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-5.5 — Alternate Audit Logging Capability

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Since an alternate audit logging capability may be a short-term protection solution employed until the failure in the primary audit logging capability is corrected, organizations may determine that the alternate audit logging capability need only provide a subset of the primary audit logging functionality that is impacted by the failure.

### Requirements and exact statement parts

- `au-5.5_smt`: Provide an alternate audit logging capability in the event of a failure in primary audit logging capability that implements [PARAM au-05.05_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-5.5_smt — Provide an alternate audit logging capability in the event of a failure in primary audit logging capability that implements [PARAM au-05.05_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-05.05_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-5.5_smt` — For “Provide an alternate audit logging capability in the event of a failure in primary audit logging capability that implements [PARAM au-05.05_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-05.05_odp` — What approved value applies to **alternate audit logging functionality**? Record the value, scope, approving authority, and decision source.

  - Catalog context: an alternate audit logging functionality in the event of a failure in primary audit logging capability is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-5.5_obj` (au-5.5_smt): an alternate audit logging capability is provided in the event of a failure in primary audit logging capability that implements [PARAM au-05.05_odp].

#### EXAMINE — `au-5.5_asm-examine`

- Audit and accountability policy

- procedures addressing response to audit processing failures

- system design documentation

- system security plan

- privacy plan

- system configuration settings and associated documentation

- system audit records

- other relevant documents or records

#### INTERVIEW — `au-5.5_asm-interview`

- Organizational personnel with audit and accountability responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

- system developers

#### TEST — `au-5.5_asm-test`

- Alternate audit logging capability

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-5.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `au-5`.

- Catalog relationship **related**: `au-9`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
