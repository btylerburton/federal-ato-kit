---
title: "AU-5.1 \u2014 Storage Capacity Warning"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-5.1 — Storage Capacity Warning

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations may have multiple audit log storage repositories distributed across multiple system components with each repository having different storage volume capacities.

### Requirements and exact statement parts

- `au-5.1_smt`: Provide a warning to [PARAM au-05.01_odp.01] within [PARAM au-05.01_odp.02] when allocated audit log storage volume reaches [PARAM au-05.01_odp.03] of repository maximum audit log storage capacity.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-5.1_smt — Provide a warning to [PARAM au-05.01_odp.01] within [PARAM au-05.01_odp.02] when allocated audit log storage volume reaches [PARAM au-05.01_odp.03] of repository maximum audit log storage capacity.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-05.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter au-05.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter au-05.01_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-5.1_smt` — For “Provide a warning to [PARAM au-05.01_odp.01] within [PARAM au-05.01_odp.02] when allocated audit log storage volume reaches [PARAM au-05.01_odp.03] of repository maximum audit log storage capacity.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-05.01_odp.01` — What approved value applies to **personnel, roles, and/or locations**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel, roles, and/or locations to be warned when allocated audit log storage volume reaches a percentage of repository maximum audit log storage capacity.

- `au-05.01_odp.02` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period for defined personnel, roles, and/or locations to be warned when allocated audit log storage volume reaches a percentage of repository maximum audit log storage capacity is defined;

- `au-05.01_odp.03` — What approved value applies to **percentage**? Record the value, scope, approving authority, and decision source.

  - Catalog context: percentage of repository maximum audit log storage capacity is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-5.1_obj` (au-5.1_smt): a warning is provided to [PARAM au-05.01_odp.01] within [PARAM au-05.01_odp.02] when allocated audit log storage volume reaches [PARAM au-05.01_odp.03] of repository maximum audit log storage capacity.

#### EXAMINE — `au-5.1_asm-examine`

- Audit and accountability policy

- procedures addressing response to audit processing failures

- system design documentation

- system security plan

- privacy system configuration settings and associated documentation

- system audit records

- other relevant documents or records

#### INTERVIEW — `au-5.1_asm-interview`

- Organizational personnel with audit and accountability responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

- system developers

#### TEST — `au-5.1_asm-test`

- Mechanisms implementing audit storage limit warnings

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-5.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `au-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
