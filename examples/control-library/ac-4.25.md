---
title: "AC-4.25 \u2014 Data Sanitization"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4.25 — Data Sanitization

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Data sanitization is the process of irreversibly removing or destroying data stored on a memory device (e.g., hard drives, flash memory/solid state drives, mobile devices, CDs, and DVDs) or in hard copy form.

### Requirements and exact statement parts

- `ac-4.25_smt`: When transferring information between different security domains, sanitize data to minimize [PARAM ac-04.25_odp.01] in accordance with [PARAM ac-04.25_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4.25_smt — When transferring information between different security domains, sanitize data to minimize [PARAM ac-04.25_odp.01] in accordance with [PARAM ac-04.25_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-04.25_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.25_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-4.25_smt` — For “When transferring information between different security domains, sanitize data to minimize [PARAM ac-04.25_odp.01] in accordance with [PARAM ac-04.25_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-04.25_odp.01` — What approved value applies to **selection; choose one-or-more from: delivery of malicious content, command and control of malicious code, malicious code augmentation, and steganography-encoded data; spillage of sensitive information**? Record the value, scope, approving authority, and decision source.

- `ac-04.25_odp.02` — What approved value applies to **policy**? Record the value, scope, approving authority, and decision source.

  - Catalog context: policy for sanitizing data is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4.25_obj` (ac-4.25_smt): when transferring information between different security domains, data is sanitized to minimize [PARAM ac-04.25_odp.01] in accordance with [PARAM ac-04.25_odp.02].

#### EXAMINE — `ac-4.25_asm-examine`

- Information flow enforcement policy

- procedures addressing information flow enforcement

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-4.25_asm-interview`

- Organizational personnel with information flow enforcement responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

#### TEST — `ac-4.25_asm-test`

- Mechanisms implementing information flow enforcement functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4.25`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-4`.

- Catalog relationship **related**: `mp-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
