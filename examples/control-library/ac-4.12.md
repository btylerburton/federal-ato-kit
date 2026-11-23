---
title: "AC-4.12 \u2014 Data Type Identifiers"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4.12 — Data Type Identifiers

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Data type identifiers include filenames, file types, file signatures or tokens, and multiple internal file signatures or tokens. Systems only allow transfer of data that is compliant with data type format specifications. Identification and validation of data types is based on defined specifications associated with each allowed data format. The filename and number alone are not used for data type identification. Content is validated syntactically and semantically against its specification to ensure that it is the proper data type.

### Requirements and exact statement parts

- `ac-4.12_smt`: When transferring information between different security domains, use [PARAM ac-04.12_odp] to validate data essential for information flow decisions.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4.12_smt — When transferring information between different security domains, use [PARAM ac-04.12_odp] to validate data essential for information flow decisions.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-04.12_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-4.12_smt` — For “When transferring information between different security domains, use [PARAM ac-04.12_odp] to validate data essential for information flow decisions.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-04.12_odp` — What approved value applies to **data type identifiers**? Record the value, scope, approving authority, and decision source.

  - Catalog context: data type identifiers to be used to validate data essential for information flow decisions are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4.12_obj` (ac-4.12_smt): when transferring information between different security domains, [PARAM ac-04.12_odp] are used to validate data essential for information flow decisions.

#### EXAMINE — `ac-4.12_asm-examine`

- Access control policy

- information flow control policies

- procedures addressing information flow enforcement

- system design documentation

- system configuration settings and associated documentation

- list of data type identifiers

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-4.12_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developers

#### TEST — `ac-4.12_asm-test`

- Mechanisms implementing information flow enforcement policy

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4.12`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
