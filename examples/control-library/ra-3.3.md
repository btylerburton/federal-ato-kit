---
title: "RA-3.3 \u2014 Dynamic Threat Awareness"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# RA-3.3 — Dynamic Threat Awareness

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The threat awareness information that is gathered feeds into the organization’s information security operations to ensure that procedures are updated in response to the changing threat environment. For example, at higher threat levels, organizations may change the privilege or authentication thresholds required to perform certain operations.

### Requirements and exact statement parts

- `ra-3.3_smt`: Determine the current cyber threat environment on an ongoing basis using [PARAM ra-03.03_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ra-3.3_smt — Determine the current cyber threat environment on an ongoing basis using [PARAM ra-03.03_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ra-03.03_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ra-3.3_smt` — For “Determine the current cyber threat environment on an ongoing basis using [PARAM ra-03.03_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ra-03.03_odp` — What approved value applies to **means**? Record the value, scope, approving authority, and decision source.

  - Catalog context: means to determine the current cyber threat environment on an ongoing basis;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ra-3.3_obj` (ra-3.3_smt): the current cyber threat environment is determined on an ongoing basis using [PARAM ra-03.03_odp].

#### EXAMINE — `ra-3.3_asm-examine`

- Risk assessment policy

- security planning policy and procedures

- procedures addressing organizational assessments of risk

- risk assessment

- risk assessment results

- risk assessment reviews

- risk assessment updates

- risk reports

- system security plan

- other relevant documents or records

#### INTERVIEW — `ra-3.3_asm-interview`

- Organizational personnel with risk assessment responsibilities

- organizational personnel with security responsibilities

#### TEST — `ra-3.3_asm-test`

- Organizational processes for risk assessment

- mechanisms supporting and/or conducting, documenting, reviewing, disseminating, and updating the risk assessment

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ra-3.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ra-3`.

- Catalog relationship **related**: `at-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
