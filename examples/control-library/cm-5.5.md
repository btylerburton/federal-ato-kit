---
title: "CM-5.5 \u2014 Privilege Limitation for Production and Operation"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-5.5 — Privilege Limitation for Production and Operation

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

In many organizations, systems support multiple mission and business functions. Limiting privileges to change system components with respect to operational systems is necessary because changes to a system component may have far-reaching effects on mission and business processes supported by the system. The relationships between systems and mission/business processes are, in some cases, unknown to developers. System-related information includes operational procedures.

### Requirements and exact statement parts

- `cm-5.5_smt`: Statement grouping; see child parts.

- `cm-5.5_smt.a`: Limit privileges to change system components and system-related information within a production or operational environment; and

- `cm-5.5_smt.b`: Review and reevaluate privileges [PARAM cm-5.5_prm_1].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-5.5_smt.a — Limit privileges to change system components and system-related information within a production or operational environment; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-5.5_smt.b — Review and reevaluate privileges [PARAM cm-5.5_prm_1].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-5.5_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-05.05_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-05.05_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-5.5_smt.a` — For “Limit privileges to change system components and system-related information within a production or operational environment; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-5.5_smt.b` — For “Review and reevaluate privileges [PARAM cm-5.5_prm_1].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-5.5_prm_1` — What approved value applies to **organization-defined frequency**? Record the value, scope, approving authority, and decision source.

- `cm-05.05_odp.01` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to review privileges is defined;

- `cm-05.05_odp.02` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to reevaluate privileges is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-5.5_obj.a-1` (cm-5.5_smt.a): privileges to change system components within a production or operational environment are limited;

- `cm-5.5_obj.a-2` (cm-5.5_smt.a): privileges to change system-related information within a production or operational environment are limited;

- `cm-5.5_obj.b-1` (cm-5.5_smt.b): privileges are reviewed [PARAM cm-05.05_odp.01];

- `cm-5.5_obj.b-2` (cm-5.5_smt.b): privileges are reevaluated [PARAM cm-05.05_odp.02].

#### EXAMINE — `cm-5.5_asm-examine`

- Configuration management policy

- procedures addressing access restrictions for changes to the system

- configuration management plan

- system design documentation

- system architecture and configuration documentation

- system configuration settings and associated documentation

- user privilege reviews

- user privilege recertifications

- system component inventory

- change control records

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-5.5_asm-interview`

- Organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `cm-5.5_asm-test`

- Organizational processes for managing access restrictions to change

- mechanisms supporting and/or implementing access restrictions for change

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-5.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-5`.

- Catalog relationship **related**: `ac-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
