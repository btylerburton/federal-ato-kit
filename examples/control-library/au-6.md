---
title: "AU-6 \u2014 Audit Record Review, Analysis, and Reporting"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-6 — Audit Record Review, Analysis, and Reporting

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Audit record review, analysis, and reporting covers information security- and privacy-related logging performed by organizations, including logging that results from the monitoring of account usage, remote access, wireless connectivity, mobile device connection, configuration settings, system component inventory, use of maintenance tools and non-local maintenance, physical access, temperature and humidity, equipment delivery and removal, communications at system interfaces, and use of mobile code or Voice over Internet Protocol (VoIP). Findings can be reported to organizational entities that include the incident response team, help desk, and security or privacy offices. If organizations are prohibited from reviewing and analyzing audit records or unable to conduct such activities, the review or analysis may be carried out by other organizations granted such authority. The frequency, scope, and/or depth of the audit record review, analysis, and reporting may be adjusted to meet organizational needs based on new information received.

### Requirements and exact statement parts

- `au-6_smt`: Statement grouping; see child parts.

- `au-6_smt.a`: Review and analyze system audit records [PARAM au-06_odp.01] for indications of [PARAM au-06_odp.02] and the potential impact of the inappropriate or unusual activity;

- `au-6_smt.b`: Report findings to [PARAM au-06_odp.03] ; and

- `au-6_smt.c`: Adjust the level of audit record review, analysis, and reporting within the system when there is a change in risk based on law enforcement information, intelligence information, or other credible sources of information.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-6_smt.a — Review and analyze system audit records [PARAM au-06_odp.01] for indications of [PARAM au-06_odp.02] and the potential impact of the inappropriate or unusual activity;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for au-6_smt.b — Report findings to [PARAM au-06_odp.03] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for au-6_smt.c — Adjust the level of audit record review, analysis, and reporting within the system when there is a change in risk based on law enforcement information, intelligence information, or other credible sources of information.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-06_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter au-06_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter au-06_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-6_smt.a` — For “Review and analyze system audit records [PARAM au-06_odp.01] for indications of [PARAM au-06_odp.02] and the potential impact of the inappropriate or unusual activity;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `au-6_smt.b` — For “Report findings to [PARAM au-06_odp.03] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `au-6_smt.c` — For “Adjust the level of audit record review, analysis, and reporting within the system when there is a change in risk based on law enforcement information, intelligence information, or other credible sources of information.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-06_odp.01` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which system audit records are reviewed and analyzed is defined;

- `au-06_odp.02` — What approved value applies to **inappropriate or unusual activity**? Record the value, scope, approving authority, and decision source.

  - Catalog context: inappropriate or unusual activity is defined;

- `au-06_odp.03` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to receive findings from reviews and analyses of system records is/are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-6_obj.a` (au-6_smt.a): system audit records are reviewed and analyzed [PARAM au-06_odp.01] for indications of [PARAM au-06_odp.02] and the potential impact of the inappropriate or unusual activity;

- `au-6_obj.b` (au-6_smt.b): findings are reported to [PARAM au-06_odp.03];

- `au-6_obj.c` (au-6_smt.c): the level of audit record review, analysis, and reporting within the system is adjusted when there is a change in risk based on law enforcement information, intelligence information, or other credible sources of information.

#### EXAMINE — `au-6_asm-examine`

- Audit and accountability policy

- system security plan

- privacy plan

- procedures addressing audit review, analysis, and reporting

- reports of audit findings

- records of actions taken in response to reviews/analyses of audit records

- other relevant documents or records

#### INTERVIEW — `au-6_asm-interview`

- Organizational personnel with audit review, analysis, and reporting responsibilities

- organizational personnel with information security and privacy responsibilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-6`. The library index records the exact source revision and hash.

- [SP 800-86](https://doi.org/10.6028/NIST.SP.800-86)

- [SP 800-101](https://doi.org/10.6028/NIST.SP.800-101r1)

- Catalog relationship **related**: `ac-2`.

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-5`.

- Catalog relationship **related**: `ac-6`.

- Catalog relationship **related**: `ac-7`.

- Catalog relationship **related**: `ac-17`.

- Catalog relationship **related**: `au-7`.

- Catalog relationship **related**: `au-16`.

- Catalog relationship **related**: `ca-2`.

- Catalog relationship **related**: `ca-7`.

- Catalog relationship **related**: `cm-2`.

- Catalog relationship **related**: `cm-5`.

- Catalog relationship **related**: `cm-6`.

- Catalog relationship **related**: `cm-10`.

- Catalog relationship **related**: `cm-11`.

- Catalog relationship **related**: `ia-2`.

- Catalog relationship **related**: `ia-3`.

- Catalog relationship **related**: `ia-5`.

- Catalog relationship **related**: `ia-8`.

- Catalog relationship **related**: `ir-5`.

- Catalog relationship **related**: `ma-4`.

- Catalog relationship **related**: `mp-4`.

- Catalog relationship **related**: `pe-3`.

- Catalog relationship **related**: `pe-6`.

- Catalog relationship **related**: `ra-5`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `si-3`.

- Catalog relationship **related**: `si-4`.

- Catalog relationship **related**: `si-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
