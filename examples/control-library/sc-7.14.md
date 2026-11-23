---
title: "SC-7.14 \u2014 Protect Against Unauthorized Physical Connections"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-7.14 — Protect Against Unauthorized Physical Connections

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Systems that operate at different security categories or classification levels may share common physical and environmental controls, since the systems may share space within the same facilities. In practice, it is possible that these separate systems may share common equipment rooms, wiring closets, and cable distribution paths. Protection against unauthorized physical connections can be achieved by using clearly identified and physically separated cable trays, connection frames, and patch panels for each side of managed interfaces with physical access controls that enforce limited authorized access to these items.

### Requirements and exact statement parts

- `sc-7.14_smt`: Protect against unauthorized physical connections at [PARAM sc-07.14_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-7.14_smt — Protect against unauthorized physical connections at [PARAM sc-07.14_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-07.14_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-7.14_smt` — For “Protect against unauthorized physical connections at [PARAM sc-07.14_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-07.14_odp` — What approved value applies to **managed interfaces**? Record the value, scope, approving authority, and decision source.

  - Catalog context: managed interfaces to be protected against unauthorized physical connections are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-7.14_obj` (sc-7.14_smt): [PARAM sc-07.14_odp] are protected against unauthorized physical connections.

#### EXAMINE — `sc-7.14_asm-examine`

- System and communications protection policy

- procedures addressing boundary protection

- system design documentation

- system hardware and software

- system architecture

- system configuration settings and associated documentation

- facility communications and wiring diagram system security plan

- other relevant documents or records

#### INTERVIEW — `sc-7.14_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel with boundary protection responsibilities

#### TEST — `sc-7.14_asm-test`

- Mechanisms supporting and/or implementing protection against unauthorized physical connections

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-7.14`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sc-7`.

- Catalog relationship **related**: `pe-4`.

- Catalog relationship **related**: `pe-19`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
