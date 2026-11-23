---
title: "CM-5.4 \u2014 Dual Authorization"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-5.4 — Dual Authorization

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations employ dual authorization to help ensure that any changes to selected system components and information cannot occur unless two qualified individuals approve and implement such changes. The two individuals possess the skills and expertise to determine if the proposed changes are correct implementations of approved changes. The individuals are also accountable for the changes. Dual authorization may also be known as two-person control. To reduce the risk of collusion, organizations consider rotating dual authorization duties to other individuals. System-level information includes operational procedures.

### Requirements and exact statement parts

- `cm-5.4_smt`: Enforce dual authorization for implementing changes to [PARAM cm-5.4_prm_1].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-5.4_smt — Enforce dual authorization for implementing changes to [PARAM cm-5.4_prm_1].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-5.4_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-05.04_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-05.04_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-5.4_smt` — For “Enforce dual authorization for implementing changes to [PARAM cm-5.4_prm_1].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-5.4_prm_1` — What approved value applies to **organization-defined system components and system-level information**? Record the value, scope, approving authority, and decision source.

- `cm-05.04_odp.01` — What approved value applies to **system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system components requiring dual authorization for changes are defined;

- `cm-05.04_odp.02` — What approved value applies to **system-level information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system-level information requiring dual authorization for changes is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-5.4_obj-1` (cm-5.4_smt): dual authorization for implementing changes to [PARAM cm-05.04_odp.01] is enforced;

- `cm-5.4_obj-2` (cm-5.4_smt): dual authorization for implementing changes to [PARAM cm-05.04_odp.02] is enforced.

#### EXAMINE — `cm-5.4_asm-examine`

- Configuration management policy

- procedures addressing access restrictions for changes to the system

- configuration management plan

- system design documentation

- system architecture and configuration documentation

- system configuration settings and associated documentation

- change control records

- system audit records

- system component inventory

- system information types information

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-5.4_asm-interview`

- Organizational personnel with dual authorization enforcement responsibilities for implementing system changes

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `cm-5.4_asm-test`

- Organizational processes for managing access restrictions to change

- mechanisms implementing dual authorization enforcement

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-5.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-5`.

- Catalog relationship **related**: `ac-2`.

- Catalog relationship **related**: `ac-5`.

- Catalog relationship **related**: `cm-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
