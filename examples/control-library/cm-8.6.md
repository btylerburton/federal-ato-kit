---
title: "CM-8.6 \u2014 Assessed Configurations and Approved Deviations"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-8.6 — Assessed Configurations and Approved Deviations

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Assessed configurations and approved deviations focus on configuration settings established by organizations for system components, the specific components that have been assessed to determine compliance with the required configuration settings, and any approved deviations from established configuration settings.

### Requirements and exact statement parts

- `cm-8.6_smt`: Include assessed component configurations and any approved deviations to current deployed configurations in the system component inventory.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-8.6_smt — Include assessed component configurations and any approved deviations to current deployed configurations in the system component inventory.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `cm-8.6_smt` — For “Include assessed component configurations and any approved deviations to current deployed configurations in the system component inventory.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-8.6_obj-1` (cm-8.6_smt): assessed component configurations are included in the system component inventory;

- `cm-8.6_obj-2` (cm-8.6_smt): any approved deviations to current deployed configurations are included in the system component inventory.

#### EXAMINE — `cm-8.6_asm-examine`

- Configuration management policy

- procedures addressing system component inventory

- configuration management plan

- system security plan

- system design documentation

- system component inventory

- system configuration settings and associated documentation

- change control records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-8.6_asm-interview`

- Organizational personnel with component inventory management responsibilities

- organizational personnel with assessment responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `cm-8.6_asm-test`

- Organizational processes for managing the system component inventory

- mechanisms supporting and/or implementing system component inventory

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-8.6`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
