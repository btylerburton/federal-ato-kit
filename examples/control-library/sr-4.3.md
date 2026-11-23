---
title: "SR-4.3 \u2014 Validate as Genuine and Not Altered"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SR-4.3 — Validate as Genuine and Not Altered

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

For many systems and system components, especially hardware, there are technical means to determine if the items are genuine or have been altered, including optical and nanotechnology tagging, physically unclonable functions, side-channel analysis, cryptographic hash verifications or digital signatures, and visible anti-tamper labels or stickers. Controls can also include monitoring for out of specification performance, which can be an indicator of tampering or counterfeits. Organizations may leverage supplier and contractor processes for validating that a system or component is genuine and has not been altered and for replacing a suspect system or component. Some indications of tampering may be visible and addressable before accepting delivery, such as inconsistent packaging, broken seals, and incorrect labels. When a system or system component is suspected of being altered or counterfeit, the supplier, contractor, or original equipment manufacturer may be able to replace the item or provide a forensic capability to determine the origin of the counterfeit or altered item. Organizations can provide training to personnel on how to identify suspicious system or component deliveries.

### Requirements and exact statement parts

- `sr-4.3_smt`: Employ the following controls to validate that the system or system component received is genuine and has not been altered: [PARAM sr-4.3_prm_1].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sr-4.3_smt — Employ the following controls to validate that the system or system component received is genuine and has not been altered: [PARAM sr-4.3_prm_1].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sr-4.3_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sr-04.03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sr-04.03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sr-4.3_smt` — For “Employ the following controls to validate that the system or system component received is genuine and has not been altered: [PARAM sr-4.3_prm_1].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sr-4.3_prm_1` — What approved value applies to **organization-defined controls**? Record the value, scope, approving authority, and decision source.

- `sr-04.03_odp.01` — What approved value applies to **controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controls to validate that the system or system component received is genuine are defined;

- `sr-04.03_odp.02` — What approved value applies to **controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controls to validate that the system or system component received has not been altered are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sr-4.3_obj-1` (sr-4.3_smt): [PARAM sr-04.03_odp.01] are employed to validate that the system or system component received is genuine;

- `sr-4.3_obj-2` (sr-4.3_smt): [PARAM sr-04.03_odp.02] are employed to validate that the system or system component received has not been altered.

#### EXAMINE — `sr-4.3_asm-examine`

- Supply chain risk management policy and procedures

- supply chain risk management plan

- system and services acquisition policy

- procedures addressing supply chain protection

- procedures addressing the security design principle of trusted components used in the specification, design, development, implementation, and modification of the system

- system design documentation

- procedures addressing the integration of information security requirements into the acquisition process

- solicitation documentation

- acquisition documentation

- service level agreements

- acquisition contracts for the system, system component, or system service

- evidentiary documentation (including applicable configurations) indicating that the system or system component is genuine and has not been altered

- system security plan

- other relevant documents or records

#### INTERVIEW — `sr-4.3_asm-interview`

- Organizational personnel with system and services acquisition responsibilities

- organizational personnel with information security responsibilities

- organizational personnel with supply chain risk management responsibilities

#### TEST — `sr-4.3_asm-test`

- Organizational processes for defining and employing validation safeguards

- mechanisms supporting and/or implementing the definition and employment of validation safeguards

- mechanisms supporting the application of the security design principle of trusted components in system specification, design, development, implementation, and modification

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sr-4.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sr-4`.

- Catalog relationship **related**: `at-3`.

- Catalog relationship **related**: `sr-9`.

- Catalog relationship **related**: `sr-10`.

- Catalog relationship **related**: `sr-11`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
