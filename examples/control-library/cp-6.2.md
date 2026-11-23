---
title: "CP-6.2 \u2014 Recovery Time and Recovery Point Objectives"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-6.2 — Recovery Time and Recovery Point Objectives

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations establish recovery time and recovery point objectives as part of contingency planning. Configuration of the alternate storage site includes physical facilities and the systems supporting recovery operations that ensure accessibility and correct execution.

### Requirements and exact statement parts

- `cp-6.2_smt`: Configure the alternate storage site to facilitate recovery operations in accordance with recovery time and recovery point objectives.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-6.2_smt — Configure the alternate storage site to facilitate recovery operations in accordance with recovery time and recovery point objectives.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `cp-6.2_smt` — For “Configure the alternate storage site to facilitate recovery operations in accordance with recovery time and recovery point objectives.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-6.2_obj-1` (cp-6.2_smt): the alternate storage site is configured to facilitate recovery operations in accordance with recovery time objectives;

- `cp-6.2_obj-2` (cp-6.2_smt): the alternate storage site is configured to facilitate recovery operations in accordance with recovery point objectives.

#### EXAMINE — `cp-6.2_asm-examine`

- Contingency planning policy

- procedures addressing alternate storage sites

- contingency plan

- alternate storage site

- alternate storage site agreements

- alternate storage site configurations

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-6.2_asm-interview`

- Organizational personnel with contingency plan testing responsibilities

- organizational personnel with responsibilities for testing related plans

- organizational personnel with information security responsibilities

#### TEST — `cp-6.2_asm-test`

- Organizational processes for contingency plan testing

- mechanisms supporting recovery time and point objectives

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-6.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cp-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
