---
title: "AC-3.10 \u2014 Audited Override of Access Control Mechanisms"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-3.10 — Audited Override of Access Control Mechanisms

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

In certain situations, such as when there is a threat to human life or an event that threatens the organization’s ability to carry out critical missions or business functions, an override capability for access control mechanisms may be needed. Override conditions are defined by organizations and used only in those limited circumstances. Audit events are defined in AU-2 (catalog reference: `#au-2`) . Audit records are generated in AU-12 (catalog reference: `#au-12`).

### Requirements and exact statement parts

- `ac-3.10_smt`: Employ an audited override of automated access control mechanisms under [PARAM ac-03.10_odp.01] by [PARAM ac-03.10_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-3.10_smt — Employ an audited override of automated access control mechanisms under [PARAM ac-03.10_odp.01] by [PARAM ac-03.10_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-03.10_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-03.10_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-3.10_smt` — For “Employ an audited override of automated access control mechanisms under [PARAM ac-03.10_odp.01] by [PARAM ac-03.10_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-03.10_odp.01` — What approved value applies to **conditions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: conditions under which to employ an audited override of automated access control mechanisms are defined;

- `ac-03.10_odp.02` — What approved value applies to **roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: roles allowed to employ an audited override of automated access control mechanisms are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-3.10_obj` (ac-3.10_smt): an audited override of automated access control mechanisms is employed under [PARAM ac-03.10_odp.01] by [PARAM ac-03.10_odp.02].

#### EXAMINE — `ac-3.10_asm-examine`

- Access control policy

- procedures addressing access enforcement

- system design documentation

- system configuration settings and associated documentation

- conditions for employing audited override of automated access control mechanisms

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-3.10_asm-interview`

- Organizational personnel with access enforcement responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

#### TEST — `ac-3.10_asm-test`

- Mechanisms implementing access enforcement functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-3.10`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-3`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-10`.

- Catalog relationship **related**: `au-12`.

- Catalog relationship **related**: `au-14`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
