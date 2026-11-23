---
title: "AC-4.14 \u2014 Security or Privacy Policy Filter Constraints"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4.14 — Security or Privacy Policy Filter Constraints

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Data structure and content restrictions reduce the range of potential malicious or unsanctioned content in cross-domain transactions. Security or privacy policy filters that restrict data structures include restricting file sizes and field lengths. Data content policy filters include encoding formats for character sets, restricting character data fields to only contain alpha-numeric characters, prohibiting special characters, and validating schema structures.

### Requirements and exact statement parts

- `ac-4.14_smt`: When transferring information between different security domains, implement [PARAM ac-4.14_prm_1] requiring fully enumerated formats that restrict data structure and content.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4.14_smt — When transferring information between different security domains, implement [PARAM ac-4.14_prm_1] requiring fully enumerated formats that restrict data structure and content.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-4.14_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.14_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.14_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-4.14_smt` — For “When transferring information between different security domains, implement [PARAM ac-4.14_prm_1] requiring fully enumerated formats that restrict data structure and content.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-4.14_prm_1` — What approved value applies to **organization-defined security or privacy policy filters**? Record the value, scope, approving authority, and decision source.

- `ac-04.14_odp.01` — What approved value applies to **security policy filters**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security policy filters to be implemented that require fully enumerated formats restricting data structure and content have been defined;

- `ac-04.14_odp.02` — What approved value applies to **privacy policy filters**? Record the value, scope, approving authority, and decision source.

  - Catalog context: privacy policy filters to be implemented that require fully enumerated formats restricting data structure and content are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4.14_obj-1` (ac-4.14_smt): when transferring information between different security domains, implemented [PARAM ac-04.14_odp.01] require fully enumerated formats that restrict data structure and content;

- `ac-4.14_obj-2` (ac-4.14_smt): when transferring information between different security domains, implemented [PARAM ac-04.14_odp.02] require fully enumerated formats that restrict data structure and content.

#### EXAMINE — `ac-4.14_asm-examine`

- Access control policy

- information flow control policies

- procedures addressing information flow enforcement

- system design documentation

- system configuration settings and associated documentation

- list of security and privacy policy filters

- list of data structure policy filters

- list of data content policy filters

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ac-4.14_asm-interview`

- System/network administrators

- organizational personnel with information security and privacy responsibilities

- system developers

#### TEST — `ac-4.14_asm-test`

- Mechanisms implementing information flow enforcement policy

- security and privacy policy filters

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4.14`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
