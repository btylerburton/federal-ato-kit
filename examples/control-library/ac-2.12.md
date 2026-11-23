---
title: "AC-2.12 \u2014 Account Monitoring for Atypical Usage"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-2.12 — Account Monitoring for Atypical Usage

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Atypical usage includes accessing systems at certain times of the day or from locations that are not consistent with the normal usage patterns of individuals. Monitoring for atypical usage may reveal rogue behavior by individuals or an attack in progress. Account monitoring may inadvertently create privacy risks since data collected to identify atypical usage may reveal previously unknown information about the behavior of individuals. Organizations assess and document privacy risks from monitoring accounts for atypical usage in their privacy impact assessment and make determinations that are in alignment with their privacy program plan.

### Requirements and exact statement parts

- `ac-2.12_smt`: Statement grouping; see child parts.

- `ac-2.12_smt.a`: Monitor system accounts for [PARAM ac-02.12_odp.01] ; and

- `ac-2.12_smt.b`: Report atypical usage of system accounts to [PARAM ac-02.12_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-2.12_smt.a — Monitor system accounts for [PARAM ac-02.12_odp.01] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-2.12_smt.b — Report atypical usage of system accounts to [PARAM ac-02.12_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-02.12_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-02.12_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-2.12_smt.a` — For “Monitor system accounts for [PARAM ac-02.12_odp.01] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-2.12_smt.b` — For “Report atypical usage of system accounts to [PARAM ac-02.12_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-02.12_odp.01` — What approved value applies to **atypical usage**? Record the value, scope, approving authority, and decision source.

  - Catalog context: atypical usage for which to monitor system accounts is defined;

- `ac-02.12_odp.02` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to report atypical usage is/are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-2.12_obj.a` (ac-2.12_smt.a): system accounts are monitored for [PARAM ac-02.12_odp.01];

- `ac-2.12_obj.b` (ac-2.12_smt.b): atypical usage of system accounts is reported to [PARAM ac-02.12_odp.02].

#### EXAMINE — `ac-2.12_asm-examine`

- Access control policy

- procedures addressing account management

- system design documentation

- system configuration settings and associated documentation

- system monitoring records

- system audit records

- audit tracking and monitoring reports

- privacy impact assessment

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ac-2.12_asm-interview`

- Organizational personnel with account management responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

#### TEST — `ac-2.12_asm-test`

- Mechanisms implementing account management functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-2.12`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-2`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-7`.

- Catalog relationship **related**: `ca-7`.

- Catalog relationship **related**: `ir-8`.

- Catalog relationship **related**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
