---
title: "SR-5.1 \u2014 Adequate Supply"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SR-5.1 — Adequate Supply

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Adversaries can attempt to impede organizational operations by disrupting the supply of critical system components or corrupting supplier operations. Organizations may track systems and component mean time to failure to mitigate the loss of temporary or permanent system function. Controls to ensure that adequate supplies of critical system components include the use of multiple suppliers throughout the supply chain for the identified critical components, stockpiling spare components to ensure operation during mission-critical times, and the identification of functionally identical or similar components that may be used, if necessary.

### Requirements and exact statement parts

- `sr-5.1_smt`: Employ the following controls to ensure an adequate supply of [PARAM sr-05.01_odp.02]: [PARAM sr-05.01_odp.01].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sr-5.1_smt — Employ the following controls to ensure an adequate supply of [PARAM sr-05.01_odp.02]: [PARAM sr-05.01_odp.01].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sr-05.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sr-05.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sr-5.1_smt` — For “Employ the following controls to ensure an adequate supply of [PARAM sr-05.01_odp.02]: [PARAM sr-05.01_odp.01].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sr-05.01_odp.01` — What approved value applies to **controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controls to ensure an adequate supply of critical system components are defined;

- `sr-05.01_odp.02` — What approved value applies to **critical system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: critical system components of which an adequate supply is required are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sr-5.1_obj` (sr-5.1_smt): [PARAM sr-05.01_odp.01] are employed to ensure an adequate supply of [PARAM sr-05.01_odp.02].

#### EXAMINE — `sr-5.1_asm-examine`

- Supply chain risk management policy and procedures

- supply chain risk management strategy

- supply chain risk management plan

- contingency planning documents

- inventory of critical systems and system components

- determination of adequate supply

- system and services acquisition policy

- procedures addressing supply chain protection

- procedures addressing the integration of information security requirements into the acquisition process

- procedures addressing the integration of acquisition strategies, contract tools, and procurement methods into the acquisition process

- solicitation documentation

- acquisition documentation

- service level agreements

- acquisition contracts for systems or services

- purchase orders/requisitions for the system, system component, or system service from suppliers

- system security plan

- other relevant documents or records

#### INTERVIEW — `sr-5.1_asm-interview`

- Organizational personnel with system and services acquisition responsibilities

- organizational personnel with information security responsibilities

- organizational personnel with supply chain risk management responsibilities

#### TEST — `sr-5.1_asm-test`

- Organizational processes for defining and employing tailored acquisition strategies, contract tools, and procurement methods

- mechanisms supporting and/or implementing the definition and employment of tailored acquisition strategies, contract tools, and procurement methods

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sr-5.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sr-5`.

- Catalog relationship **related**: `ra-9`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
