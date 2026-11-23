---
title: "SR-6 \u2014 Supplier Assessments and Reviews"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SR-6 — Supplier Assessments and Reviews

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

An assessment and review of supplier risk includes security and supply chain risk management processes, foreign ownership, control or influence (FOCI), and the ability of the supplier to effectively assess subordinate second-tier and third-tier suppliers and contractors. The reviews may be conducted by the organization or by an independent third party. The reviews consider documented processes, documented controls, all-source intelligence, and publicly available information related to the supplier or contractor. Organizations can use open-source information to monitor for indications of stolen information, poor development and quality control practices, information spillage, or counterfeits. In some cases, it may be appropriate or required to share assessment and review results with other organizations in accordance with any applicable rules, policies, or inter-organizational agreements or contracts.

### Requirements and exact statement parts

- `sr-6_smt`: Assess and review the supply chain-related risks associated with suppliers or contractors and the system, system component, or system service they provide [PARAM sr-06_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sr-6_smt — Assess and review the supply chain-related risks associated with suppliers or contractors and the system, system component, or system service they provide [PARAM sr-06_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sr-06_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sr-6_smt` — For “Assess and review the supply chain-related risks associated with suppliers or contractors and the system, system component, or system service they provide [PARAM sr-06_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sr-06_odp` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which to assess and review the supply chain-related risks associated with suppliers or contractors and the systems, system components, or system services they provide is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sr-6_obj` (sr-6_smt): the supply chain-related risks associated with suppliers or contractors and the systems, system components, or system services they provide are assessed and reviewed [PARAM sr-06_odp].

#### EXAMINE — `sr-6_asm-examine`

- Supply chain risk management policy and procedures

- supply chain risk management strategy

- supply chain risk management plan

- system and services acquisition policy

- procedures addressing supply chain protection

- procedures addressing the integration of information security requirements into the acquisition process

- records of supplier due diligence reviews

- system security plan

- other relevant documents or records

#### INTERVIEW — `sr-6_asm-interview`

- Organizational personnel with system and services acquisition responsibilities

- organizational personnel with information security responsibilities

- organizational personnel with supply chain protection responsibilities

#### TEST — `sr-6_asm-test`

- Organizational processes for conducting supplier reviews

- mechanisms supporting and/or implementing supplier reviews

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sr-6`. The library index records the exact source revision and hash.

- [FASC18](https://www.congress.gov/bill/115th-congress/senate-bill/3085)

- [41 CFR 201](https://www.federalregister.gov/d/2020-18939)

- [EO 13873](https://www.whitehouse.gov/presidential-actions/executive-order-securing-information-communications-technology-services-supply-chain)

- [ISO 27036](https://www.iso.org/standard/59648.html)

- [ISO 20243](https://www.iso.org/standard/74399.html)

- [FIPS 140-3](https://doi.org/10.6028/NIST.FIPS.140-3)

- [FIPS 180-4](https://doi.org/10.6028/NIST.FIPS.180-4)

- [FIPS 186-4](https://doi.org/10.6028/NIST.FIPS.186-4)

- [FIPS 202](https://doi.org/10.6028/NIST.FIPS.202)

- [SP 800-30](https://doi.org/10.6028/NIST.SP.800-30r1)

- [SP 800-161](https://doi.org/10.6028/NIST.SP.800-161)

- [IR 7622](https://doi.org/10.6028/NIST.IR.7622)

- [IR 8272](https://doi.org/10.6028/NIST.IR.8272)

- Catalog relationship **related**: `sr-3`.

- Catalog relationship **related**: `sr-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
