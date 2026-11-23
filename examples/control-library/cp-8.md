---
title: "CP-8 \u2014 Telecommunications Services"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-8 — Telecommunications Services

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Telecommunications services (for data and voice) for primary and alternate processing and storage sites are in scope for CP-8 (catalog reference: `#cp-8`) . Alternate telecommunications services reflect the continuity requirements in contingency plans to maintain essential mission and business functions despite the loss of primary telecommunications services. Organizations may specify different time periods for primary or alternate sites. Alternate telecommunications services include additional organizational or commercial ground-based circuits or lines, network-based approaches to telecommunications, or the use of satellites. Organizations consider factors such as availability, quality of service, and access when entering into alternate telecommunications agreements.

### Requirements and exact statement parts

- `cp-8_smt`: Establish alternate telecommunications services, including necessary agreements to permit the resumption of [PARAM cp-08_odp.01] for essential mission and business functions within [PARAM cp-08_odp.02] when the primary telecommunications capabilities are unavailable at either the primary or alternate processing or storage sites.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-8_smt — Establish alternate telecommunications services, including necessary agreements to permit the resumption of [PARAM cp-08_odp.01] for essential mission and business functions within [PARAM cp-08_odp.02] when the primary telecommunications capabilities are unavailable at either the primary or alternate processing or storage sites.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cp-08_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-08_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cp-8_smt` — For “Establish alternate telecommunications services, including necessary agreements to permit the resumption of [PARAM cp-08_odp.01] for essential mission and business functions within [PARAM cp-08_odp.02] when the primary telecommunications capabilities are unavailable at either the primary or alternate processing or storage sites.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cp-08_odp.01` — What approved value applies to **system operations**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system operations to be resumed for essential mission and business functions are defined;

- `cp-08_odp.02` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period within which to resume essential mission and business functions when the primary telecommunications capabilities are unavailable is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-8_obj` (cp-8_smt): alternate telecommunications services, including necessary agreements to permit the resumption of [PARAM cp-08_odp.01] , are established for essential mission and business functions within [PARAM cp-08_odp.02] when the primary telecommunications capabilities are unavailable at either the primary or alternate processing or storage sites.

#### EXAMINE — `cp-8_asm-examine`

- Contingency planning policy

- procedures addressing alternate telecommunications services

- contingency plan

- primary and alternate telecommunications service agreements

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-8_asm-interview`

- Organizational personnel with contingency plan telecommunications responsibilities

- organizational personnel with system recovery responsibilities

- organizational personnel with knowledge of requirements for mission and business functions

- organizational personnel with information security responsibilities

- organizational personnel with responsibility for acquisitions/contractual agreements

#### TEST — `cp-8_asm-test`

- Mechanisms supporting telecommunications

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-8`. The library index records the exact source revision and hash.

- [SP 800-34](https://doi.org/10.6028/NIST.SP.800-34r1)

- Catalog relationship **related**: `cp-2`.

- Catalog relationship **related**: `cp-6`.

- Catalog relationship **related**: `cp-7`.

- Catalog relationship **related**: `cp-11`.

- Catalog relationship **related**: `sc-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
