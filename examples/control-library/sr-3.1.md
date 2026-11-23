---
title: "SR-3.1 \u2014 Diverse Supply Base"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SR-3.1 — Diverse Supply Base

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Diversifying the supply of systems, system components, and services can reduce the probability that adversaries will successfully identify and target the supply chain and can reduce the impact of a supply chain event or compromise. Identifying multiple suppliers for replacement components can reduce the probability that the replacement component will become unavailable. Employing a diverse set of developers or logistics service providers can reduce the impact of a natural disaster or other supply chain event. Organizations consider designing the system to include diverse materials and components.

### Requirements and exact statement parts

- `sr-3.1_smt`: Employ a diverse set of sources for the following system components and services: [PARAM sr-3.1_prm_1].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sr-3.1_smt — Employ a diverse set of sources for the following system components and services: [PARAM sr-3.1_prm_1].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sr-3.1_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sr-03.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sr-03.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sr-3.1_smt` — For “Employ a diverse set of sources for the following system components and services: [PARAM sr-3.1_prm_1].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sr-3.1_prm_1` — What approved value applies to **organization-defined system components and services**? Record the value, scope, approving authority, and decision source.

- `sr-03.01_odp.01` — What approved value applies to **system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system components with a diverse set of sources are defined;

- `sr-03.01_odp.02` — What approved value applies to **services**? Record the value, scope, approving authority, and decision source.

  - Catalog context: services with a diverse set of sources are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sr-3.1_obj-1` (sr-3.1_smt): a diverse set of sources is employed for [PARAM sr-03.01_odp.01];

- `sr-3.1_obj-2` (sr-3.1_smt): a diverse set of sources is employed for [PARAM sr-03.01_odp.02].

#### EXAMINE — `sr-3.1_asm-examine`

- Supply chain risk management policy and procedures

- system and services acquisition policy

- planning policy

- procedures addressing supply chain protection

- physical inventory of critical systems and system components

- inventory of critical suppliers, service providers, developers, and contracts

- inventory records of critical system components

- list of security safeguards ensuring an adequate supply of critical system components

- system security plan

- other relevant documents or records

#### INTERVIEW — `sr-3.1_asm-interview`

- Organizational personnel with system and services acquisition responsibilities

- organizational personnel with information security responsibilities

- organizational personnel with supply chain protection responsibilities

#### TEST — `sr-3.1_asm-test`

- Organizational processes for defining and employing security safeguards to ensure an adequate supply of critical system components

- processes to identify critical suppliers

- mechanisms supporting and/or implementing the security safeguards that ensure an adequate supply of critical system components

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sr-3.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sr-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
