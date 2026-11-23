---
title: "CM-8.2 \u2014 Automated Maintenance"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-8.2 — Automated Maintenance

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations maintain system inventories to the extent feasible. For example, virtual machines can be difficult to monitor because such machines are not visible to the network when not in use. In such cases, organizations maintain as up-to-date, complete, and accurate an inventory as is deemed reasonable. Automated maintenance can be achieved by the implementation of CM-2(2) (catalog reference: `#cm-2.2`) for organizations that combine system component inventory and baseline configuration activities.

### Requirements and exact statement parts

- `cm-8.2_smt`: Maintain the currency, completeness, accuracy, and availability of the inventory of system components using [PARAM cm-8.2_prm_1].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-8.2_smt — Maintain the currency, completeness, accuracy, and availability of the inventory of system components using [PARAM cm-8.2_prm_1].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-8.2_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-08.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-08.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-08.02_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-08.02_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-8.2_smt` — For “Maintain the currency, completeness, accuracy, and availability of the inventory of system components using [PARAM cm-8.2_prm_1].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-8.2_prm_1` — What approved value applies to **organization-defined automated mechanisms**? Record the value, scope, approving authority, and decision source.

- `cm-08.02_odp.01` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used to maintain the currency of the system component inventory are defined;

- `cm-08.02_odp.02` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used to maintain the completeness of the system component inventory are defined;

- `cm-08.02_odp.03` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used to maintain the accuracy of the system component inventory are defined;

- `cm-08.02_odp.04` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used to maintain the availability of the system component inventory are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-8.2_obj-1` (cm-8.2_smt): [PARAM cm-08.02_odp.01] are used to maintain the currency of the system component inventory;

- `cm-8.2_obj-2` (cm-8.2_smt): [PARAM cm-08.02_odp.02] are used to maintain the completeness of the system component inventory;

- `cm-8.2_obj-3` (cm-8.2_smt): [PARAM cm-08.02_odp.03] are used to maintain the accuracy of the system component inventory;

- `cm-8.2_obj-4` (cm-8.2_smt): [PARAM cm-08.02_odp.04] are used to maintain the availability of the system component inventory.

#### EXAMINE — `cm-8.2_asm-examine`

- Configuration management policy

- procedures addressing system component inventory

- configuration management plan

- system design documentation

- system security plan

- system component inventory

- change control records

- system maintenance records

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-8.2_asm-interview`

- Organizational personnel with component inventory management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `cm-8.2_asm-test`

- Organizational processes for maintaining the system component inventory

- automated mechanisms supporting and/or implementing the system component inventory

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-8.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
