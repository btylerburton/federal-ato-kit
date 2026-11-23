---
title: "AU-7 \u2014 Audit Record Reduction and Report Generation"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-7 — Audit Record Reduction and Report Generation

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Audit record reduction is a process that manipulates collected audit log information and organizes it into a summary format that is more meaningful to analysts. Audit record reduction and report generation capabilities do not always emanate from the same system or from the same organizational entities that conduct audit logging activities. The audit record reduction capability includes modern data mining techniques with advanced data filters to identify anomalous behavior in audit records. The report generation capability provided by the system can generate customizable reports. Time ordering of audit records can be an issue if the granularity of the timestamp in the record is insufficient.

### Requirements and exact statement parts

- `au-7_smt`: Provide and implement an audit record reduction and report generation capability that:

- `au-7_smt.a`: Supports on-demand audit record review, analysis, and reporting requirements and after-the-fact investigations of incidents; and

- `au-7_smt.b`: Does not alter the original content or time ordering of audit records.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-7_smt — Provide and implement an audit record reduction and report generation capability that:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for au-7_smt.a — Supports on-demand audit record review, analysis, and reporting requirements and after-the-fact investigations of incidents; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for au-7_smt.b — Does not alter the original content or time ordering of audit records.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `au-7_smt` — For “Provide and implement an audit record reduction and report generation capability that:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `au-7_smt.a` — For “Supports on-demand audit record review, analysis, and reporting requirements and after-the-fact investigations of incidents; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `au-7_smt.b` — For “Does not alter the original content or time ordering of audit records.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-7_obj.a-1` (au-7_smt.a): an audit record reduction and report generation capability is provided that supports on-demand audit record review, analysis, and reporting requirements and after-the-fact investigations of incidents;

- `au-7_obj.a-2` (au-7_smt.a): an audit record reduction and report generation capability is implemented that supports on-demand audit record review, analysis, and reporting requirements and after-the-fact investigations of incidents;

- `au-7_obj.b-1` (au-7_smt.b): an audit record reduction and report generation capability is provided that does not alter the original content or time ordering of audit records;

- `au-7_obj.b-2` (au-7_smt.b): an audit record reduction and report generation capability is implemented that does not alter the original content or time ordering of audit records.

#### EXAMINE — `au-7_asm-examine`

- Audit and accountability policy

- system security plan

- privacy plan

- procedures addressing audit reduction and report generation

- system design documentation

- system configuration settings and associated documentation

- audit reduction, review, analysis, and reporting tools

- system audit records

- other relevant documents or records

#### INTERVIEW — `au-7_asm-interview`

- Organizational personnel with audit reduction and report generation responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `au-7_asm-test`

- Audit reduction and report generation capability

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-7`. The library index records the exact source revision and hash.

- Catalog relationship **related**: `ac-2`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-3`.

- Catalog relationship **related**: `au-4`.

- Catalog relationship **related**: `au-5`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-12`.

- Catalog relationship **related**: `au-16`.

- Catalog relationship **related**: `cm-5`.

- Catalog relationship **related**: `ia-5`.

- Catalog relationship **related**: `ir-4`.

- Catalog relationship **related**: `pm-12`.

- Catalog relationship **related**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
