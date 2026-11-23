---
title: "CP-9.5 \u2014 Transfer to Alternate Storage Site"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-9.5 — Transfer to Alternate Storage Site

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

System backup information can be transferred to alternate storage sites either electronically or by the physical shipment of storage media.

### Requirements and exact statement parts

- `cp-9.5_smt`: Transfer system backup information to the alternate storage site [PARAM cp-9.5_prm_1].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-9.5_smt — Transfer system backup information to the alternate storage site [PARAM cp-9.5_prm_1].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cp-9.5_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-09.05_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-09.05_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cp-9.5_smt` — For “Transfer system backup information to the alternate storage site [PARAM cp-9.5_prm_1].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cp-9.5_prm_1` — What approved value applies to **organization-defined time period and transfer rate consistent with the recovery time and recovery point objectives**? Record the value, scope, approving authority, and decision source.

- `cp-09.05_odp.01` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period consistent with recovery time and recovery point objectives is defined;

- `cp-09.05_odp.02` — What approved value applies to **transfer rate**? Record the value, scope, approving authority, and decision source.

  - Catalog context: transfer rate consistent with recovery time and recovery point objectives is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-9.5_obj-1` (cp-9.5_smt): system backup information is transferred to the alternate storage site for [PARAM cp-09.05_odp.01];

- `cp-9.5_obj-2` (cp-9.5_smt): system backup information is transferred to the alternate storage site [PARAM cp-09.05_odp.02].

#### EXAMINE — `cp-9.5_asm-examine`

- Contingency planning policy

- procedures addressing system backup

- contingency plan

- system backup logs or records

- evidence of system backup information transferred to alternate storage site

- alternate storage site agreements

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-9.5_asm-interview`

- Organizational personnel with system backup responsibilities

- organizational personnel with information security responsibilities

#### TEST — `cp-9.5_asm-test`

- Organizational processes for transferring system backups to the alternate storage site

- mechanisms supporting and/or implementing system backups

- mechanisms supporting and/or implementing information transfer to the alternate storage site

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-9.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cp-9`.

- Catalog relationship **related**: `cp-7`.

- Catalog relationship **related**: `mp-3`.

- Catalog relationship **related**: `mp-4`.

- Catalog relationship **related**: `mp-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
