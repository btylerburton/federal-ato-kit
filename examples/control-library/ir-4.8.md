---
title: "IR-4.8 \u2014 Correlation with External Organizations"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-4.8 — Correlation with External Organizations

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The coordination of incident information with external organizations—including mission or business partners, military or coalition partners, customers, and developers—can provide significant benefits. Cross-organizational coordination can serve as an important risk management capability. This capability allows organizations to leverage information from a variety of sources to effectively respond to incidents and breaches that could potentially affect the organization’s operations, assets, and individuals.

### Requirements and exact statement parts

- `ir-4.8_smt`: Coordinate with [PARAM ir-04.08_odp.01] to correlate and share [PARAM ir-04.08_odp.02] to achieve a cross-organization perspective on incident awareness and more effective incident responses.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-4.8_smt — Coordinate with [PARAM ir-04.08_odp.01] to correlate and share [PARAM ir-04.08_odp.02] to achieve a cross-organization perspective on incident awareness and more effective incident responses.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ir-04.08_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ir-04.08_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ir-4.8_smt` — For “Coordinate with [PARAM ir-04.08_odp.01] to correlate and share [PARAM ir-04.08_odp.02] to achieve a cross-organization perspective on incident awareness and more effective incident responses.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ir-04.08_odp.01` — What approved value applies to **external organizations**? Record the value, scope, approving authority, and decision source.

  - Catalog context: external organizations with whom organizational incident information is to be coordinated and shared are defined;

- `ir-04.08_odp.02` — What approved value applies to **incident information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: incident information to be correlated and shared with organization-defined external organizations are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-4.8_obj` (ir-4.8_smt): there is coordination with [PARAM ir-04.08_odp.01] to correlate and share [PARAM ir-04.08_odp.02] to achieve a cross-organization perspective on incident awareness and more effective incident responses.

#### EXAMINE — `ir-4.8_asm-examine`

- Incident response policy

- procedures addressing incident handling

- list of external organizations

- records of incident handling coordination with external organizations

- incident response plan

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ir-4.8_asm-interview`

- Organizational personnel with incident handling responsibilities

- organizational personnel with information security and privacy responsibilities

- personnel from external organizations with whom incident response information is to be coordinated, shared, and correlated

#### TEST — `ir-4.8_asm-test`

- Organizational processes for coordinating incident handling information with external organizations

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-4.8`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ir-4`.

- Catalog relationship **related**: `au-16`.

- Catalog relationship **related**: `pm-16`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
