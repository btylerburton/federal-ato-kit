---
title: "MA-4.1 \u2014 Logging and Review"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-4.1 — Logging and Review

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Audit logging for nonlocal maintenance is enforced by AU-2 (catalog reference: `#au-2`) . Audit events are defined in AU-2a (catalog reference: `#au-2_smt.a`).

### Requirements and exact statement parts

- `ma-4.1_smt`: Statement grouping; see child parts.

- `ma-4.1_smt.a`: Log [PARAM ma-4.1_prm_1] for nonlocal maintenance and diagnostic sessions; and

- `ma-4.1_smt.b`: Review the audit records of the maintenance and diagnostic sessions to detect anomalous behavior.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-4.1_smt.a — Log [PARAM ma-4.1_prm_1] for nonlocal maintenance and diagnostic sessions; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-4.1_smt.b — Review the audit records of the maintenance and diagnostic sessions to detect anomalous behavior.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ma-4.1_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ma-04.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ma-04.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ma-4.1_smt.a` — For “Log [PARAM ma-4.1_prm_1] for nonlocal maintenance and diagnostic sessions; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-4.1_smt.b` — For “Review the audit records of the maintenance and diagnostic sessions to detect anomalous behavior.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ma-4.1_prm_1` — What approved value applies to **organization-defined audit events**? Record the value, scope, approving authority, and decision source.

- `ma-04.01_odp.01` — What approved value applies to **audit events**? Record the value, scope, approving authority, and decision source.

  - Catalog context: audit events to be logged for nonlocal maintenance are defined;

- `ma-04.01_odp.02` — What approved value applies to **audit events**? Record the value, scope, approving authority, and decision source.

  - Catalog context: audit events to be logged for diagnostic sessions are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-4.1_obj.a-1` (ma-4.1_smt.a): [PARAM ma-04.01_odp.01] are logged for nonlocal maintenance sessions;

- `ma-4.1_obj.a-2` (ma-4.1_smt.a): [PARAM ma-04.01_odp.02] are logged for nonlocal diagnostic sessions;

- `ma-4.1_obj.b-1` (ma-4.1_smt.b): the audit records of the maintenance sessions are reviewed to detect anomalous behavior;

- `ma-4.1_obj.b-2` (ma-4.1_smt.b): the audit records of the diagnostic sessions are reviewed to detect anomalous behavior.

#### EXAMINE — `ma-4.1_asm-examine`

- Maintenance policy

- procedures addressing nonlocal system maintenance

- list of audit events

- system configuration settings and associated documentation

- maintenance records

- diagnostic records

- audit records

- reviews of maintenance and diagnostic session records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-4.1_asm-interview`

- Organizational personnel with system maintenance responsibilities

- organizational personnel with information security responsibilities

- organizational personnel with audit and review responsibilities

- system/network administrators

#### TEST — `ma-4.1_asm-test`

- Organizational processes for audit and review of nonlocal maintenance

- mechanisms supporting and/or implementing audit and review of nonlocal maintenance

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-4.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ma-4`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
