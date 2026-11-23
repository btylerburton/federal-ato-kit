---
title: "SR-7 \u2014 Supply Chain Operations Security"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SR-7 — Supply Chain Operations Security

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Supply chain OPSEC expands the scope of OPSEC to include suppliers and potential suppliers. OPSEC is a process that includes identifying critical information, analyzing friendly actions related to operations and other activities to identify actions that can be observed by potential adversaries, determining indicators that potential adversaries might obtain that could be interpreted or pieced together to derive information in sufficient time to cause harm to organizations, implementing safeguards or countermeasures to eliminate or reduce exploitable vulnerabilities and risk to an acceptable level, and considering how aggregated information may expose users or specific uses of the supply chain. Supply chain information includes user identities; uses for systems, system components, and system services; supplier identities; security and privacy requirements; system and component configurations; supplier processes; design specifications; and testing and evaluation results. Supply chain OPSEC may require organizations to withhold mission or business information from suppliers and may include the use of intermediaries to hide the end use or users of systems, system components, or system services.

### Requirements and exact statement parts

- `sr-7_smt`: Employ the following Operations Security (OPSEC) controls to protect supply chain-related information for the system, system component, or system service: [PARAM sr-07_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sr-7_smt — Employ the following Operations Security (OPSEC) controls to protect supply chain-related information for the system, system component, or system service: [PARAM sr-07_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sr-07_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sr-7_smt` — For “Employ the following Operations Security (OPSEC) controls to protect supply chain-related information for the system, system component, or system service: [PARAM sr-07_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sr-07_odp` — What approved value applies to **OPSEC controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: Operations Security (OPSEC) controls to protect supply chain-related information for the system, system component, or system service are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sr-7_obj` (sr-7_smt): [PARAM sr-07_odp] are employed to protect supply chain-related information for the system, system component, or system service.

#### EXAMINE — `sr-7_asm-examine`

- Supply chain risk management plan

- supply chain risk management procedures

- system and services acquisition policy

- system and services acquisition procedures

- procedures addressing supply chain protection

- list of OPSEC controls to be employed

- solicitation documentation

- acquisition documentation

- acquisition contracts for the system, system component, or system service

- records of all-source intelligence analyses

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `sr-7_asm-interview`

- Organizational personnel with acquisition responsibilities

- organizational personnel with information security and privacy responsibilities

- organizational personnel with OPSEC responsibilities

- organizational personnel with supply chain risk management responsibilities

#### TEST — `sr-7_asm-test`

- Organizational processes for defining and employing OPSEC safeguards

- mechanisms supporting and/or implementing the definition and employment of OPSEC safeguards

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sr-7`. The library index records the exact source revision and hash.

- [EO 13873](https://www.whitehouse.gov/presidential-actions/executive-order-securing-information-communications-technology-services-supply-chain)

- [SP 800-30](https://doi.org/10.6028/NIST.SP.800-30r1)

- [ISO 27036](https://www.iso.org/standard/59648.html)

- [SP 800-161](https://doi.org/10.6028/NIST.SP.800-161)

- [IR 7622](https://doi.org/10.6028/NIST.IR.7622)

- Catalog relationship **related**: `sc-38`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
