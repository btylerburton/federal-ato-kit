---
title: "AU-4 \u2014 Audit Log Storage Capacity"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-4 — Audit Log Storage Capacity

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations consider the types of audit logging to be performed and the audit log processing requirements when allocating audit log storage capacity. Allocating sufficient audit log storage capacity reduces the likelihood of such capacity being exceeded and resulting in the potential loss or reduction of audit logging capability.

### Requirements and exact statement parts

- `au-4_smt`: Allocate audit log storage capacity to accommodate [PARAM au-04_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-4_smt — Allocate audit log storage capacity to accommodate [PARAM au-04_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-04_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-4_smt` — For “Allocate audit log storage capacity to accommodate [PARAM au-04_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-04_odp` — What approved value applies to **audit log retention requirements**? Record the value, scope, approving authority, and decision source.

  - Catalog context: audit log retention requirements are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-4_obj` (au-4_smt): audit log storage capacity is allocated to accommodate [PARAM au-04_odp].

#### EXAMINE — `au-4_asm-examine`

- Audit and accountability policy

- procedures addressing audit storage capacity

- system security plan

- privacy plan

- system design documentation

- system configuration settings and associated documentation

- audit record storage requirements

- audit record storage capability for system components

- system audit records

- other relevant documents or records

#### INTERVIEW — `au-4_asm-interview`

- Organizational personnel with audit and accountability responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

- system developers

#### TEST — `au-4_asm-test`

- Audit record storage capacity and related configuration settings

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-4`. The library index records the exact source revision and hash.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-5`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-7`.

- Catalog relationship **related**: `au-9`.

- Catalog relationship **related**: `au-11`.

- Catalog relationship **related**: `au-12`.

- Catalog relationship **related**: `au-14`.

- Catalog relationship **related**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
