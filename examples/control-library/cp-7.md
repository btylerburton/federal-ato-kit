---
title: "CP-7 \u2014 Alternate Processing Site"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-7 — Alternate Processing Site

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Alternate processing sites are geographically distinct from primary processing sites and provide processing capability if the primary processing site is not available. The alternate processing capability may be addressed using a physical processing site or other alternatives, such as failover to a cloud-based service provider or other internally or externally provided processing service. Geographically distributed architectures that support contingency requirements may also be considered alternate processing sites. Controls that are covered by alternate processing site agreements include the environmental conditions at alternate sites, access rules, physical and environmental protection requirements, and the coordination for the transfer and assignment of personnel. Requirements are allocated to alternate processing sites that reflect the requirements in contingency plans to maintain essential mission and business functions despite disruption, compromise, or failure in organizational systems.

### Requirements and exact statement parts

- `cp-7_smt`: Statement grouping; see child parts.

- `cp-7_smt.a`: Establish an alternate processing site, including necessary agreements to permit the transfer and resumption of [PARAM cp-07_odp.01] for essential mission and business functions within [PARAM cp-07_odp.02] when the primary processing capabilities are unavailable;

- `cp-7_smt.b`: Make available at the alternate processing site, the equipment and supplies required to transfer and resume operations or put contracts in place to support delivery to the site within the organization-defined time period for transfer and resumption; and

- `cp-7_smt.c`: Provide controls at the alternate processing site that are equivalent to those at the primary site.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-7_smt.a — Establish an alternate processing site, including necessary agreements to permit the transfer and resumption of [PARAM cp-07_odp.01] for essential mission and business functions within [PARAM cp-07_odp.02] when the primary processing capabilities are unavailable;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-7_smt.b — Make available at the alternate processing site, the equipment and supplies required to transfer and resume operations or put contracts in place to support delivery to the site within the organization-defined time period for transfer and resumption; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-7_smt.c — Provide controls at the alternate processing site that are equivalent to those at the primary site.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cp-07_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-07_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cp-7_smt.a` — For “Establish an alternate processing site, including necessary agreements to permit the transfer and resumption of [PARAM cp-07_odp.01] for essential mission and business functions within [PARAM cp-07_odp.02] when the primary processing capabilities are unavailable;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-7_smt.b` — For “Make available at the alternate processing site, the equipment and supplies required to transfer and resume operations or put contracts in place to support delivery to the site within the organization-defined time period for transfer and resumption; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-7_smt.c` — For “Provide controls at the alternate processing site that are equivalent to those at the primary site.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cp-07_odp.01` — What approved value applies to **system operations**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system operations for essential mission and business functions are defined;

- `cp-07_odp.02` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period consistent with recovery time and recovery point objectives is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-7_obj.a` (cp-7_smt.a): an alternate processing site, including necessary agreements to permit the transfer and resumption of [PARAM cp-07_odp.01] for essential mission and business functions, is established within [PARAM cp-07_odp.02] when the primary processing capabilities are unavailable;

- `cp-7_obj.b-1` (cp-7_smt.b): the equipment and supplies required to transfer operations are made available at the alternate processing site or if contracts are in place to support delivery to the site within [PARAM cp-07_odp.02] for transfer;

- `cp-7_obj.b-2` (cp-7_smt.b): the equipment and supplies required to resume operations are made available at the alternate processing site or if contracts are in place to support delivery to the site within [PARAM cp-07_odp.02] for resumption;

- `cp-7_obj.c` (cp-7_smt.c): controls provided at the alternate processing site are equivalent to those at the primary site.

#### EXAMINE — `cp-7_asm-examine`

- Contingency planning policy

- procedures addressing alternate processing sites

- contingency plan

- alternate processing site agreements

- primary processing site agreements

- spare equipment and supplies inventory at alternate processing site

- equipment and supply contracts

- service-level agreements

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-7_asm-interview`

- Organizational personnel with responsibilities for contingency planning and/or alternate site arrangements

- organizational personnel with information security responsibilities

#### TEST — `cp-7_asm-test`

- Organizational processes for recovery at the alternate site

- mechanisms supporting and/or implementing recovery at the alternate processing site

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-7`. The library index records the exact source revision and hash.

- [SP 800-34](https://doi.org/10.6028/NIST.SP.800-34r1)

- Catalog relationship **related**: `cp-2`.

- Catalog relationship **related**: `cp-6`.

- Catalog relationship **related**: `cp-8`.

- Catalog relationship **related**: `cp-9`.

- Catalog relationship **related**: `cp-10`.

- Catalog relationship **related**: `ma-6`.

- Catalog relationship **related**: `pe-3`.

- Catalog relationship **related**: `pe-11`.

- Catalog relationship **related**: `pe-12`.

- Catalog relationship **related**: `pe-17`.

- Catalog relationship **related**: `sc-36`.

- Catalog relationship **related**: `si-13`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
