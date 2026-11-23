---
title: "MA-6 \u2014 Timely Maintenance"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-6 — Timely Maintenance

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations specify the system components that result in increased risk to organizational operations and assets, individuals, other organizations, or the Nation when the functionality provided by those components is not operational. Organizational actions to obtain maintenance support include having appropriate contracts in place.

### Requirements and exact statement parts

- `ma-6_smt`: Obtain maintenance support and/or spare parts for [PARAM ma-06_odp.01] within [PARAM ma-06_odp.02] of failure.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-6_smt — Obtain maintenance support and/or spare parts for [PARAM ma-06_odp.01] within [PARAM ma-06_odp.02] of failure.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ma-06_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ma-06_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ma-6_smt` — For “Obtain maintenance support and/or spare parts for [PARAM ma-06_odp.01] within [PARAM ma-06_odp.02] of failure.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ma-06_odp.01` — What approved value applies to **system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system components for which maintenance support and/or spare parts are obtained are defined;

- `ma-06_odp.02` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period within which maintenance support and/or spare parts are to be obtained after a failure are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-6_obj` (ma-6_smt): maintenance support and/or spare parts are obtained for [PARAM ma-06_odp.01] within [PARAM ma-06_odp.02] of failure.

#### EXAMINE — `ma-6_asm-examine`

- Maintenance policy

- procedures addressing system maintenance

- service provider contracts

- service-level agreements

- inventory and availability of spare parts

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-6_asm-interview`

- Organizational personnel with system maintenance responsibilities

- organizational personnel with acquisition responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ma-6_asm-test`

- Organizational processes for ensuring timely maintenance

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-6`. The library index records the exact source revision and hash.

- Catalog relationship **related**: `cm-8`.

- Catalog relationship **related**: `cp-2`.

- Catalog relationship **related**: `cp-7`.

- Catalog relationship **related**: `ra-7`.

- Catalog relationship **related**: `sa-15`.

- Catalog relationship **related**: `si-13`.

- Catalog relationship **related**: `sr-2`.

- Catalog relationship **related**: `sr-3`.

- Catalog relationship **related**: `sr-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
