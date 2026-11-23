---
title: "SR-3.2 \u2014 Limitation of Harm"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SR-3.2 — Limitation of Harm

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Controls that can be implemented to reduce the probability of adversaries successfully identifying and targeting the supply chain include avoiding the purchase of custom or non-standardized configurations, employing approved vendor lists with standing reputations in industry, following pre-agreed maintenance schedules and update and patch delivery mechanisms, maintaining a contingency plan in case of a supply chain event, using procurement carve-outs that provide exclusions to commitments or obligations, using diverse delivery routes, and minimizing the time between purchase decisions and delivery.

### Requirements and exact statement parts

- `sr-3.2_smt`: Employ the following controls to limit harm from potential adversaries identifying and targeting the organizational supply chain: [PARAM sr-03.02_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sr-3.2_smt — Employ the following controls to limit harm from potential adversaries identifying and targeting the organizational supply chain: [PARAM sr-03.02_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sr-03.02_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sr-3.2_smt` — For “Employ the following controls to limit harm from potential adversaries identifying and targeting the organizational supply chain: [PARAM sr-03.02_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sr-03.02_odp` — What approved value applies to **controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controls to limit harm from potential supply chain adversaries are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sr-3.2_obj` (sr-3.2_smt): [PARAM sr-03.02_odp] are employed to limit harm from potential adversaries identifying and targeting the organizational supply chain.

#### EXAMINE — `sr-3.2_asm-examine`

- Supply chain risk management policy and procedures

- supply chain risk management plan

- system and services acquisition policy

- configuration management policy

- procedures addressing supply chain protection

- procedures addressing the integration of information security requirements into the acquisition process

- procedures addressing the baseline configuration of the system

- configuration management plan

- system design documentation

- system architecture and associated configuration documentation

- solicitation documentation

- acquisition documentation

- acquisition contracts for the system, system component, or system service

- threat assessments

- vulnerability assessments

- list of security safeguards to be taken to protect the organizational supply chain against potential supply chain threats

- system security plan

- other relevant documents or records

#### INTERVIEW — `sr-3.2_asm-interview`

- Organizational personnel with system and services acquisition responsibilities

- organizational personnel with information security responsibilities

- organizational personnel with supply chain risk management responsibilities

#### TEST — `sr-3.2_asm-test`

- Organizational processes for defining and employing safeguards to limit harm from adversaries of the organizational supply chain

- mechanisms supporting and/or implementing the definition and employment of safeguards to protect the organizational supply chain

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sr-3.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sr-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
