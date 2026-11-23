---
title: "RA-3.1 \u2014 Supply Chain Risk Assessment"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# RA-3.1 — Supply Chain Risk Assessment

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Supply chain-related events include disruption, use of defective components, insertion of counterfeits, theft, malicious development practices, improper delivery practices, and insertion of malicious code. These events can have a significant impact on the confidentiality, integrity, or availability of a system and its information and, therefore, can also adversely impact organizational operations (including mission, functions, image, or reputation), organizational assets, individuals, other organizations, and the Nation. The supply chain-related events may be unintentional or malicious and can occur at any point during the system life cycle. An analysis of supply chain risk can help an organization identify systems or components for which additional supply chain risk mitigations are required.

### Requirements and exact statement parts

- `ra-3.1_smt`: Statement grouping; see child parts.

- `ra-3.1_smt.a`: Assess supply chain risks associated with [PARAM ra-03.01_odp.01] ; and

- `ra-3.1_smt.b`: Update the supply chain risk assessment [PARAM ra-03.01_odp.02] , when there are significant changes to the relevant supply chain, or when changes to the system, environments of operation, or other conditions may necessitate a change in the supply chain.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ra-3.1_smt.a — Assess supply chain risks associated with [PARAM ra-03.01_odp.01] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ra-3.1_smt.b — Update the supply chain risk assessment [PARAM ra-03.01_odp.02] , when there are significant changes to the relevant supply chain, or when changes to the system, environments of operation, or other conditions may necessitate a change in the supply chain.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ra-03.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ra-03.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ra-3.1_smt.a` — For “Assess supply chain risks associated with [PARAM ra-03.01_odp.01] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ra-3.1_smt.b` — For “Update the supply chain risk assessment [PARAM ra-03.01_odp.02] , when there are significant changes to the relevant supply chain, or when changes to the system, environments of operation, or other conditions may necessitate a change in the supply chain.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ra-03.01_odp.01` — What approved value applies to **systems, system components, and system services**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems, system components, and system services to assess supply chain risks are defined;

- `ra-03.01_odp.02` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which to update the supply chain risk assessment is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ra-3.1_obj.a` (ra-3.1_smt.a): supply chain risks associated with [PARAM ra-03.01_odp.01] are assessed;

- `ra-3.1_obj.b` (ra-3.1_smt.b): the supply chain risk assessment is updated [PARAM ra-03.01_odp.02] , when there are significant changes to the relevant supply chain, or when changes to the system, environments of operation, or other conditions may necessitate a change in the supply chain.

#### EXAMINE — `ra-3.1_asm-examine`

- Supply chain risk management policy

- inventory of critical systems, system components, and system services

- risk assessment policy

- security planning policy and procedures

- procedures addressing organizational assessments of supply chain risk

- risk assessment

- risk assessment results

- risk assessment reviews

- risk assessment updates

- acquisition policy

- system security plan

- supply chain risk management plan

- other relevant documents or records

#### INTERVIEW — `ra-3.1_asm-interview`

- Organizational personnel with risk assessment responsibilities

- organizational personnel with security responsibilities

- organizational personnel with supply chain risk management responsibilities

#### TEST — `ra-3.1_asm-test`

- Organizational processes for risk assessment

- mechanisms supporting and/or conducting, documenting, reviewing, disseminating, and updating the supply chain risk assessment

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ra-3.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ra-3`.

- Catalog relationship **related**: `ra-2`.

- Catalog relationship **related**: `ra-9`.

- Catalog relationship **related**: `pm-17`.

- Catalog relationship **related**: `pm-30`.

- Catalog relationship **related**: `sr-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
