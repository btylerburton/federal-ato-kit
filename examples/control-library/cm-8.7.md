---
title: "CM-8.7 \u2014 Centralized Repository"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-8.7 — Centralized Repository

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations may implement centralized system component inventories that include components from all organizational systems. Centralized repositories of component inventories provide opportunities for efficiencies in accounting for organizational hardware, software, and firmware assets. Such repositories may also help organizations rapidly identify the location and responsible individuals of components that have been compromised, breached, or are otherwise in need of mitigation actions. Organizations ensure that the resulting centralized inventories include system-specific information required for proper component accountability.

### Requirements and exact statement parts

- `cm-8.7_smt`: Provide a centralized repository for the inventory of system components.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-8.7_smt — Provide a centralized repository for the inventory of system components.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `cm-8.7_smt` — For “Provide a centralized repository for the inventory of system components.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-8.7_obj` (cm-8.7_smt): a centralized repository for the system component inventory is provided.

#### EXAMINE — `cm-8.7_asm-examine`

- Configuration management policy

- procedures addressing system component inventory

- configuration management plan

- system design documentation

- system security plan

- system component inventory

- system configuration settings and associated documentation

- change control records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-8.7_asm-interview`

- Organizational personnel with component inventory management responsibilities

- organizational personnel with security responsibilities

#### TEST — `cm-8.7_asm-test`

- Organizational processes for managing the system component inventory

- mechanisms supporting and/or implementing system component inventory

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-8.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
