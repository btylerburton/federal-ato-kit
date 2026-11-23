---
title: "SI-7.2 \u2014 Automated Notifications of Integrity Violations"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-7.2 — Automated Notifications of Integrity Violations

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The employment of automated tools to report system and information integrity violations and to notify organizational personnel in a timely matter is essential to effective risk response. Personnel with an interest in system and information integrity violations include mission and business owners, system owners, senior agency information security official, senior agency official for privacy, system administrators, software developers, systems integrators, information security officers, and privacy officers.

### Requirements and exact statement parts

- `si-7.2_smt`: Employ automated tools that provide notification to [PARAM si-07.02_odp] upon discovering discrepancies during integrity verification.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-7.2_smt — Employ automated tools that provide notification to [PARAM si-07.02_odp] upon discovering discrepancies during integrity verification.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-07.02_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-7.2_smt` — For “Employ automated tools that provide notification to [PARAM si-07.02_odp] upon discovering discrepancies during integrity verification.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-07.02_odp` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to whom notification is to be provided upon discovering discrepancies during integrity verification is/are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-7.2_obj` (si-7.2_smt): automated tools that provide notification to [PARAM si-07.02_odp] upon discovering discrepancies during integrity verification are employed.

#### EXAMINE — `si-7.2_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing software, firmware, and information integrity

- personally identifiable information processing policy

- system design documentation

- system configuration settings and associated documentation

- integrity verification tools and associated documentation

- records of integrity scans

- automated tools supporting alerts and notifications for integrity discrepancies

- notifications provided upon discovering discrepancies during integrity verifications

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `si-7.2_asm-interview`

- Organizational personnel responsible for software, firmware, and/or information integrity

- organizational personnel with information security and privacy responsibilities

- system administrators

- software developers

#### TEST — `si-7.2_asm-test`

- Software, firmware, and information integrity verification tools

- mechanisms providing integrity discrepancy notifications

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-7.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
