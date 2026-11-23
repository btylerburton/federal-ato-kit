---
title: "MA-7 \u2014 Field Maintenance"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-7 — Field Maintenance

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Field maintenance is the type of maintenance conducted on a system or system component after the system or component has been deployed to a specific site (i.e., operational environment). In certain instances, field maintenance (i.e., local maintenance at the site) may not be executed with the same degree of rigor or with the same quality control checks as depot maintenance. For critical systems designated as such by the organization, it may be necessary to restrict or prohibit field maintenance at the local site and require that such maintenance be conducted in trusted facilities with additional controls.

### Requirements and exact statement parts

- `ma-7_smt`: Restrict or prohibit field maintenance on [PARAM ma-07_odp.01] to [PARAM ma-07_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-7_smt — Restrict or prohibit field maintenance on [PARAM ma-07_odp.01] to [PARAM ma-07_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ma-07_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ma-07_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ma-7_smt` — For “Restrict or prohibit field maintenance on [PARAM ma-07_odp.01] to [PARAM ma-07_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ma-07_odp.01` — What approved value applies to **systems or system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems or system components on which field maintenance is restricted or prohibited to trusted maintenance facilities are defined;

- `ma-07_odp.02` — What approved value applies to **trusted maintenance facilities**? Record the value, scope, approving authority, and decision source.

  - Catalog context: trusted maintenance facilities that are not restricted or prohibited from conducting field maintenance are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-7_obj` (ma-7_smt): field maintenance on [PARAM ma-07_odp.01] are restricted or prohibited to [PARAM ma-07_odp.02].

#### EXAMINE — `ma-7_asm-examine`

- Maintenance policy

- procedures addressing field maintenance

- system design documentation

- system configuration settings and associated documentation

- maintenance records

- diagnostic records

- system security plan

- other relevant documents or records.

#### INTERVIEW — `ma-7_asm-interview`

- Organizational personnel with system maintenance responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ma-7_asm-test`

- Organizational processes for managing field maintenance

- mechanisms implementing, supporting, and/or managing field maintenance

- mechanisms for strong authentication of field maintenance diagnostic sessions

- mechanisms for terminating field maintenance sessions and network connections

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-7`. The library index records the exact source revision and hash.

- Catalog relationship **related**: `ma-2`.

- Catalog relationship **related**: `ma-4`.

- Catalog relationship **related**: `ma-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
