---
title: "CM-5.6 \u2014 Limit Library Privileges"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-5.6 — Limit Library Privileges

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Software libraries include privileged programs.

### Requirements and exact statement parts

- `cm-5.6_smt`: Limit privileges to change software resident within software libraries.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-5.6_smt — Limit privileges to change software resident within software libraries.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `cm-5.6_smt` — For “Limit privileges to change software resident within software libraries.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-5.6_obj` (cm-5.6_smt): privileges to change software resident within software libraries are limited.

#### EXAMINE — `cm-5.6_asm-examine`

- Configuration management policy

- procedures addressing access restrictions for changes to the system

- configuration management plan

- system design documentation

- system architecture and configuration documentation

- system configuration settings and associated documentation

- system component inventory

- change control records

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-5.6_asm-interview`

- Organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `cm-5.6_asm-test`

- Organizational processes for managing access restrictions to change

- mechanisms supporting and/or implementing access restrictions for change

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-5.6`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-5`.

- Catalog relationship **related**: `ac-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
