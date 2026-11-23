---
title: "SR-8 \u2014 Notification Agreements"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SR-8 — Notification Agreements

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The establishment of agreements and procedures facilitates communications among supply chain entities. Early notification of compromises and potential compromises in the supply chain that can potentially adversely affect or have adversely affected organizational systems or system components is essential for organizations to effectively respond to such incidents. The results of assessments or audits may include open-source information that contributed to a decision or result and could be used to help the supply chain entity resolve a concern or improve its processes.

### Requirements and exact statement parts

- `sr-8_smt`: Establish agreements and procedures with entities involved in the supply chain for the system, system component, or system service for the [PARAM sr-08_odp.01].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sr-8_smt — Establish agreements and procedures with entities involved in the supply chain for the system, system component, or system service for the [PARAM sr-08_odp.01].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sr-08_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sr-08_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sr-8_smt` — For “Establish agreements and procedures with entities involved in the supply chain for the system, system component, or system service for the [PARAM sr-08_odp.01].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sr-08_odp.01` — What approved value applies to **selection; choose one-or-more from: notification of supply chain compromises; [PARAM sr-08_odp.02]**? Record the value, scope, approving authority, and decision source.

- `sr-08_odp.02` — What approved value applies to **results of assessments or audits**? Record the value, scope, approving authority, and decision source.

  - Catalog context: information for which agreements and procedures are to be established are defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sr-8_obj` (sr-8_smt): agreements and procedures are established with entities involved in the supply chain for the system, system components, or system service for [PARAM sr-08_odp.01].

#### EXAMINE — `sr-8_asm-examine`

- Supply chain risk management policy and procedures

- supply chain risk management plan

- system and services acquisition policy

- procedures addressing supply chain protection

- acquisition documentation

- service level agreements

- acquisition contracts for the system, system component, or system service

- inter-organizational agreements and procedures

- system security plan

- other relevant documents or records

#### INTERVIEW — `sr-8_asm-interview`

- Organizational personnel with system and service acquisition responsibilities

- organizational personnel with information security responsibilities

- organizational personnel with supply chain risk management responsibilities

#### TEST — `sr-8_asm-test`

- Organizational processes for establishing inter-organizational agreements and procedures with supply chain entities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sr-8`. The library index records the exact source revision and hash.

- [FASC18](https://www.congress.gov/bill/115th-congress/senate-bill/3085)

- [41 CFR 201](https://www.federalregister.gov/d/2020-18939)

- [EO 13873](https://www.whitehouse.gov/presidential-actions/executive-order-securing-information-communications-technology-services-supply-chain)

- [ISO 27036](https://www.iso.org/standard/59648.html)

- [SP 800-30](https://doi.org/10.6028/NIST.SP.800-30r1)

- [SP 800-161](https://doi.org/10.6028/NIST.SP.800-161)

- [IR 7622](https://doi.org/10.6028/NIST.IR.7622)

- Catalog relationship **related**: `ir-4`.

- Catalog relationship **related**: `ir-6`.

- Catalog relationship **related**: `ir-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
