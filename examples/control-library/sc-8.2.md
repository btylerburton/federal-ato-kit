---
title: "SC-8.2 \u2014 Pre- and Post-transmission Handling"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-8.2 — Pre- and Post-transmission Handling

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Information can be unintentionally or maliciously disclosed or modified during preparation for transmission or during reception, including during aggregation, at protocol transformation points, and during packing and unpacking. Such unauthorized disclosures or modifications compromise the confidentiality or integrity of the information.

### Requirements and exact statement parts

- `sc-8.2_smt`: Maintain the [PARAM sc-08.02_odp] of information during preparation for transmission and during reception.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-8.2_smt — Maintain the [PARAM sc-08.02_odp] of information during preparation for transmission and during reception.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-08.02_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-8.2_smt` — For “Maintain the [PARAM sc-08.02_odp] of information during preparation for transmission and during reception.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-08.02_odp` — What approved value applies to **selection; choose one-or-more from: confidentiality; integrity**? Record the value, scope, approving authority, and decision source.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-8.2_obj-1` (sc-8.2_smt): information [PARAM sc-08.02_odp] is/are maintained during preparation for transmission;

- `sc-8.2_obj-2` (sc-8.2_smt): information [PARAM sc-08.02_odp] is/are maintained during reception.

#### EXAMINE — `sc-8.2_asm-examine`

- System and communications protection policy

- procedures addressing transmission confidentiality and integrity

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-8.2_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developer

#### TEST — `sc-8.2_asm-test`

- Mechanisms supporting and/or implementing transmission confidentiality and/or integrity

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-8.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sc-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
