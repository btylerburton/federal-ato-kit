---
title: "MA-6.2 \u2014 Predictive Maintenance"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-6.2 — Predictive Maintenance

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Predictive maintenance evaluates the condition of equipment by performing periodic or continuous (online) equipment condition monitoring. The goal of predictive maintenance is to perform maintenance at a scheduled time when the maintenance activity is most cost-effective and before the equipment loses performance within a threshold. The predictive component of predictive maintenance stems from the objective of predicting the future trend of the equipment's condition. The predictive maintenance approach employs principles of statistical process control to determine at what point in the future maintenance activities will be appropriate. Most predictive maintenance inspections are performed while equipment is in service, thus minimizing disruption of normal system operations. Predictive maintenance can result in substantial cost savings and higher system reliability.

### Requirements and exact statement parts

- `ma-6.2_smt`: Perform predictive maintenance on [PARAM ma-06.02_odp.01] at [PARAM ma-06.02_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-6.2_smt — Perform predictive maintenance on [PARAM ma-06.02_odp.01] at [PARAM ma-06.02_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ma-06.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ma-06.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ma-6.2_smt` — For “Perform predictive maintenance on [PARAM ma-06.02_odp.01] at [PARAM ma-06.02_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ma-06.02_odp.01` — What approved value applies to **system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system components on which predictive maintenance is to be performed are defined;

- `ma-06.02_odp.02` — What approved value applies to **time intervals**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time intervals within which predictive maintenance is to be performed are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-6.2_obj` (ma-6.2_smt): predictive maintenance is performed on [PARAM ma-06.02_odp.01] at [PARAM ma-06.02_odp.02].

#### EXAMINE — `ma-6.2_asm-examine`

- Maintenance policy

- procedures addressing system maintenance

- service provider contracts

- service-level agreements

- maintenance records

- list of system components requiring predictive maintenance

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-6.2_asm-interview`

- Organizational personnel with system maintenance responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ma-6.2_asm-test`

- Organizational processes for predictive maintenance

- mechanisms supporting and/or implementing predictive maintenance

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-6.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ma-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
