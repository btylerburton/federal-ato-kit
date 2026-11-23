---
title: "CM-8.1 \u2014 Updates During Installation and Removal"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-8.1 — Updates During Installation and Removal

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations can improve the accuracy, completeness, and consistency of system component inventories if the inventories are updated as part of component installations or removals or during general system updates. If inventories are not updated at these key times, there is a greater likelihood that the information will not be appropriately captured and documented. System updates include hardware, software, and firmware components.

### Requirements and exact statement parts

- `cm-8.1_smt`: Update the inventory of system components as part of component installations, removals, and system updates.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-8.1_smt — Update the inventory of system components as part of component installations, removals, and system updates.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `cm-8.1_smt` — For “Update the inventory of system components as part of component installations, removals, and system updates.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-8.1_obj-1` (cm-8.1_smt): the inventory of system components is updated as part of component installations;

- `cm-8.1_obj-2` (cm-8.1_smt): the inventory of system components is updated as part of component removals;

- `cm-8.1_obj-3` (cm-8.1_smt): the inventory of system components is updated as part of system updates.

#### EXAMINE — `cm-8.1_asm-examine`

- Configuration management policy

- procedures addressing system component inventory

- configuration management plan

- system security plan

- system component inventory

- inventory reviews and update records

- change control records

- component installation records

- component removal records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-8.1_asm-interview`

- Organizational personnel with component inventory updating responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `cm-8.1_asm-test`

- Organizational processes for updating the system component inventory

- mechanisms supporting and/or implementing system component inventory updates

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-8.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-8`.

- Catalog relationship **related**: `pm-16`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
