---
title: "PE-9.1 \u2014 Redundant Cabling"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PE-9.1 — Redundant Cabling

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Physically separate and redundant power cables ensure that power continues to flow in the event that one of the cables is cut or otherwise damaged.

### Requirements and exact statement parts

- `pe-9.1_smt`: Employ redundant power cabling paths that are physically separated by [PARAM pe-09.01_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pe-9.1_smt — Employ redundant power cabling paths that are physically separated by [PARAM pe-09.01_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pe-09.01_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pe-9.1_smt` — For “Employ redundant power cabling paths that are physically separated by [PARAM pe-09.01_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pe-09.01_odp` — What approved value applies to **distance**? Record the value, scope, approving authority, and decision source.

  - Catalog context: distance by which redundant power cabling paths are to be physically separated is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pe-9.1_obj` (pe-9.1_smt): redundant power cabling paths that are physically separated by [PARAM pe-09.01_odp] are employed.

#### EXAMINE — `pe-9.1_asm-examine`

- Physical and environmental protection policy

- procedures addressing power equipment/cabling protection

- facilities housing power equipment/cabling

- system security plan

- other relevant documents or records

#### INTERVIEW — `pe-9.1_asm-interview`

- Organizational personnel with the responsibility to protect power equipment/cabling

- organizational personnel with information security responsibilities

#### TEST — `pe-9.1_asm-test`

- Mechanisms supporting and/or implementing the protection of power equipment/cabling

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pe-9.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pe-9`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
