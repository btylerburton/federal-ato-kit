---
title: "CP-6 \u2014 Alternate Storage Site"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-6 — Alternate Storage Site

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Alternate storage sites are geographically distinct from primary storage sites and maintain duplicate copies of information and data if the primary storage site is not available. Similarly, alternate processing sites provide processing capability if the primary processing site is not available. Geographically distributed architectures that support contingency requirements may be considered alternate storage sites. Items covered by alternate storage site agreements include environmental conditions at the alternate sites, access rules for systems and facilities, physical and environmental protection requirements, and coordination of delivery and retrieval of backup media. Alternate storage sites reflect the requirements in contingency plans so that organizations can maintain essential mission and business functions despite compromise, failure, or disruption in organizational systems.

### Requirements and exact statement parts

- `cp-6_smt`: Statement grouping; see child parts.

- `cp-6_smt.a`: Establish an alternate storage site, including necessary agreements to permit the storage and retrieval of system backup information; and

- `cp-6_smt.b`: Ensure that the alternate storage site provides controls equivalent to that of the primary site.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-6_smt.a — Establish an alternate storage site, including necessary agreements to permit the storage and retrieval of system backup information; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-6_smt.b — Ensure that the alternate storage site provides controls equivalent to that of the primary site.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `cp-6_smt.a` — For “Establish an alternate storage site, including necessary agreements to permit the storage and retrieval of system backup information; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-6_smt.b` — For “Ensure that the alternate storage site provides controls equivalent to that of the primary site.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-6_obj.a-1` (cp-6_smt.a): an alternate storage site is established;

- `cp-6_obj.a-2` (cp-6_smt.a): establishment of the alternate storage site includes necessary agreements to permit the storage and retrieval of system backup information;

- `cp-6_obj.b` (cp-6_smt.b): the alternate storage site provides controls equivalent to that of the primary site.

#### EXAMINE — `cp-6_asm-examine`

- Contingency planning policy

- procedures addressing alternate storage sites

- contingency plan

- alternate storage site agreements

- primary storage site agreements

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-6_asm-interview`

- Organizational personnel with contingency plan alternate storage site responsibilities

- organizational personnel with system recovery responsibilities

- organizational personnel with information security responsibilities

#### TEST — `cp-6_asm-test`

- Organizational processes for storing and retrieving system backup information at the alternate storage site

- mechanisms supporting and/or implementing the storage and retrieval of system backup information at the alternate storage site

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-6`. The library index records the exact source revision and hash.

- [SP 800-34](https://doi.org/10.6028/NIST.SP.800-34r1)

- Catalog relationship **related**: `cp-2`.

- Catalog relationship **related**: `cp-7`.

- Catalog relationship **related**: `cp-8`.

- Catalog relationship **related**: `cp-9`.

- Catalog relationship **related**: `cp-10`.

- Catalog relationship **related**: `mp-4`.

- Catalog relationship **related**: `mp-5`.

- Catalog relationship **related**: `pe-3`.

- Catalog relationship **related**: `sc-36`.

- Catalog relationship **related**: `si-13`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
