---
title: "PM-5.1 \u2014 Inventory of Personally Identifiable Information"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PM-5.1 — Inventory of Personally Identifiable Information

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

An inventory of systems, applications, and projects that process personally identifiable information supports the mapping of data actions, providing individuals with privacy notices, maintaining accurate personally identifiable information, and limiting the processing of personally identifiable information when such information is not needed for operational purposes. Organizations may use this inventory to ensure that systems only process the personally identifiable information for authorized purposes and that this processing is still relevant and necessary for the purpose specified therein.

### Requirements and exact statement parts

- `pm-5.1_smt`: Establish, maintain, and update [PARAM pm-05.01_odp] an inventory of all systems, applications, and projects that process personally identifiable information.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pm-5.1_smt — Establish, maintain, and update [PARAM pm-05.01_odp] an inventory of all systems, applications, and projects that process personally identifiable information.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pm-05.01_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pm-5.1_smt` — For “Establish, maintain, and update [PARAM pm-05.01_odp] an inventory of all systems, applications, and projects that process personally identifiable information.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pm-05.01_odp` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which to update the inventory of systems, applications, and projects that process personally identifiable information is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pm-5.1_obj-1` (pm-5.1_smt): an inventory of all systems, applications, and projects that process personally identifiable information is established;

- `pm-5.1_obj-2` (pm-5.1_smt): an inventory of all systems, applications, and projects that process personally identifiable information is maintained;

- `pm-5.1_obj-3` (pm-5.1_smt): an inventory of all systems, applications, and projects that process personally identifiable information is updated [PARAM pm-05.01_odp].

#### EXAMINE — `pm-5.1_asm-examine`

- Procedures addressing system inventory development, maintenance, and updates

- OMB FISMA reporting guidance

- privacy program plan

- information security program plan

- personally identifiable information processing policy

- system inventory

- personally identifiable information inventory

- data mapping documentation

- other relevant documents or records

#### INTERVIEW — `pm-5.1_asm-interview`

- Organizational personnel with privacy program planning and plan implementation responsibilities

- organizational personnel responsible for developing and maintaining the system inventory

- organizational personnel with information security and privacy responsibilities

#### TEST — `pm-5.1_asm-test`

- Organizational processes for system inventory development, maintenance, and updates

- mechanisms supporting the system inventory

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pm-5.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pm-5`.

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `cm-8`.

- Catalog relationship **related**: `cm-12`.

- Catalog relationship **related**: `cm-13`.

- Catalog relationship **related**: `pl-8`.

- Catalog relationship **related**: `pm-22`.

- Catalog relationship **related**: `pt-3`.

- Catalog relationship **related**: `pt-5`.

- Catalog relationship **related**: `si-12`.

- Catalog relationship **related**: `si-18`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
