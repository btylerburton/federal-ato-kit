---
title: "CM-6.1 \u2014 Automated Management, Application, and Verification"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-6.1 — Automated Management, Application, and Verification

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Automated tools (e.g., hardening tools, baseline configuration tools) can improve the accuracy, consistency, and availability of configuration settings information. Automation can also provide data aggregation and data correlation capabilities, alerting mechanisms, and dashboards to support risk-based decision-making within the organization.

### Requirements and exact statement parts

- `cm-6.1_smt`: Manage, apply, and verify configuration settings for [PARAM cm-06.01_odp.01] using [PARAM cm-6.1_prm_2].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-6.1_smt — Manage, apply, and verify configuration settings for [PARAM cm-06.01_odp.01] using [PARAM cm-6.1_prm_2].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-6.1_prm_2: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-06.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-06.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-06.01_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-06.01_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-6.1_smt` — For “Manage, apply, and verify configuration settings for [PARAM cm-06.01_odp.01] using [PARAM cm-6.1_prm_2].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-6.1_prm_2` — What approved value applies to **organization-defined automated mechanisms**? Record the value, scope, approving authority, and decision source.

- `cm-06.01_odp.01` — What approved value applies to **system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system components for which to manage, apply, and verify configuration settings are defined;

- `cm-06.01_odp.02` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms to manage configuration settings are defined;

- `cm-06.01_odp.03` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms to apply configuration settings are defined;

- `cm-06.01_odp.04` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms to verify configuration settings are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-6.1_obj-1` (cm-6.1_smt): configuration settings for [PARAM cm-06.01_odp.01] are managed using [PARAM cm-06.01_odp.02];

- `cm-6.1_obj-2` (cm-6.1_smt): configuration settings for [PARAM cm-06.01_odp.01] are applied using [PARAM cm-06.01_odp.03];

- `cm-6.1_obj-3` (cm-6.1_smt): configuration settings for [PARAM cm-06.01_odp.01] are verified using [PARAM cm-06.01_odp.04].

#### EXAMINE — `cm-6.1_asm-examine`

- Configuration management policy

- procedures addressing configuration settings for the system

- configuration management plan

- system design documentation

- system configuration settings and associated documentation

- system component inventory

- common secure configuration checklists

- change control records

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `cm-6.1_asm-interview`

- Organizational personnel with security configuration management responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

- system developers

#### TEST — `cm-6.1_asm-test`

- Organizational processes for managing configuration settings

- automated mechanisms implemented to manage, apply, and verify system configuration settings

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-6.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-6`.

- Catalog relationship **related**: `ca-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
