---
title: "MA-4.4 \u2014 Authentication and Separation of Maintenance Sessions"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-4.4 — Authentication and Separation of Maintenance Sessions

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Communications paths can be logically separated using encryption.

### Requirements and exact statement parts

- `ma-4.4_smt`: Protect nonlocal maintenance sessions by:

- `ma-4.4_smt.a`: Employing [PARAM ma-04.04_odp] ; and

- `ma-4.4_smt.b`: Separating the maintenance sessions from other network sessions with the system by either:

- `ma-4.4_smt.b.1`: Physically separated communications paths; or

- `ma-4.4_smt.b.2`: Logically separated communications paths.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-4.4_smt — Protect nonlocal maintenance sessions by:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-4.4_smt.a — Employing [PARAM ma-04.04_odp] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-4.4_smt.b — Separating the maintenance sessions from other network sessions with the system by either:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-4.4_smt.b.1 — Physically separated communications paths; or
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-4.4_smt.b.2 — Logically separated communications paths.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ma-04.04_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ma-4.4_smt` — For “Protect nonlocal maintenance sessions by:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-4.4_smt.a` — For “Employing [PARAM ma-04.04_odp] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-4.4_smt.b` — For “Separating the maintenance sessions from other network sessions with the system by either:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-4.4_smt.b.1` — For “Physically separated communications paths; or”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-4.4_smt.b.2` — For “Logically separated communications paths.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ma-04.04_odp` — What approved value applies to **authenticators that are replay resistant**? Record the value, scope, approving authority, and decision source.

  - Catalog context: authenticators that are replay resistant are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-4.4_obj.a` (ma-4.4_smt.a): nonlocal maintenance sessions are protected by employing [PARAM ma-04.04_odp];

- `ma-4.4_obj.b.1` (ma-4.4_smt.b.1): nonlocal maintenance sessions are protected by separating maintenance sessions from other network sessions with the system by physically separated communication paths; or

- `ma-4.4_obj.b.2` (ma-4.4_smt.b.2): nonlocal maintenance sessions are protected by logically separated communication paths.

#### EXAMINE — `ma-4.4_asm-examine`

- Maintenance policy

- procedures addressing nonlocal system maintenance

- system design documentation

- system configuration settings and associated documentation

- maintenance records

- audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-4.4_asm-interview`

- Organizational personnel with system maintenance responsibilities

- network engineers

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ma-4.4_asm-test`

- Organizational processes for protecting nonlocal maintenance sessions

- mechanisms implementing replay-resistant authenticators

- mechanisms implementing logically separated/encrypted communication paths

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-4.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ma-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
