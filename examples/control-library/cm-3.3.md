---
title: "CM-3.3 \u2014 Automated Change Implementation"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-3.3 — Automated Change Implementation

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Automated tools can improve the accuracy, consistency, and availability of configuration baseline information. Automation can also provide data aggregation and data correlation capabilities, alerting mechanisms, and dashboards to support risk-based decision-making within the organization.

### Requirements and exact statement parts

- `cm-3.3_smt`: Implement changes to the current system baseline and deploy the updated baseline across the installed base using [PARAM cm-03.03_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-3.3_smt — Implement changes to the current system baseline and deploy the updated baseline across the installed base using [PARAM cm-03.03_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-03.03_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-3.3_smt` — For “Implement changes to the current system baseline and deploy the updated baseline across the installed base using [PARAM cm-03.03_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-03.03_odp` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: mechanisms used to automate the implementation of changes and deployment of the updated baseline across the installed base are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-3.3_obj-1` (cm-3.3_smt): changes to the current system baseline are implemented using [PARAM cm-03.03_odp];

- `cm-3.3_obj-2` (cm-3.3_smt): the updated baseline is deployed across the installed base using [PARAM cm-03.03_odp].

#### EXAMINE — `cm-3.3_asm-examine`

- Configuration management policy

- configuration management plan

- procedures addressing system configuration change control

- system design documentation

- system architecture and configuration documentation

- automated configuration control mechanisms

- change control records

- system component inventory

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-3.3_asm-interview`

- Organizational personnel with configuration change control responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

- members of change control board or similar

#### TEST — `cm-3.3_asm-test`

- Organizational processes for configuration change control

- automated mechanisms implementing changes to current system baseline

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-3.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
