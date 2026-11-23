---
title: "MA-3.5 \u2014 Execution with Privilege"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-3.5 — Execution with Privilege

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Maintenance tools that execute with increased system privilege can result in unauthorized access to organizational information and assets that would otherwise be inaccessible.

### Requirements and exact statement parts

- `ma-3.5_smt`: Monitor the use of maintenance tools that execute with increased privilege.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-3.5_smt — Monitor the use of maintenance tools that execute with increased privilege.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ma-3.5_smt` — For “Monitor the use of maintenance tools that execute with increased privilege.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-3.5_obj` (ma-3.5_smt): the use of maintenance tools that execute with increased privilege is monitored.

#### EXAMINE — `ma-3.5_asm-examine`

- Maintenance policy

- procedures addressing system maintenance tools

- system maintenance tools and associated documentation

- list of personnel authorized to use maintenance tools

- maintenance tool usage records

- maintenance records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-3.5_asm-interview`

- Organizational personnel with system maintenance responsibilities

- organizational personnel with information security responsibilities

#### TEST — `ma-3.5_asm-test`

- Organizational processes for restricting the use of maintenance tools

- organizational process for monitoring maintenance tools and maintenance tool usage

- mechanisms monitoring the use of maintenance tools

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-3.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ma-3`.

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
