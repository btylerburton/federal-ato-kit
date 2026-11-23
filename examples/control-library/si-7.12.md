---
title: "SI-7.12 \u2014 Integrity Verification"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-7.12 — Integrity Verification

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations verify the integrity of user-installed software prior to execution to reduce the likelihood of executing malicious code or programs that contains errors from unauthorized modifications. Organizations consider the source of the software, ensuring the software and updates come from authorized sources and/or sites, and the practicality of approaches to verifying software integrity, including the availability of trustworthy checksums from software developers and vendors.

### Requirements and exact statement parts

- `si-7.12_smt`: Require that the integrity of the following user-installed software be verified prior to execution: [PARAM si-07.12_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-7.12_smt — Require that the integrity of the following user-installed software be verified prior to execution: [PARAM si-07.12_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-07.12_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-7.12_smt` — For “Require that the integrity of the following user-installed software be verified prior to execution: [PARAM si-07.12_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-07.12_odp` — What approved value applies to **user-installed software**? Record the value, scope, approving authority, and decision source.

  - Catalog context: user-installed software requiring integrity verification prior to execution is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-7.12_obj` (si-7.12_smt): the integrity of [PARAM si-07.12_odp] is verified prior to execution.

#### EXAMINE — `si-7.12_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing software, firmware, and information integrity

- system design documentation

- system configuration settings and associated documentation

- integrity verification records

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-7.12_asm-interview`

- Organizational personnel responsible for software, firmware, and/or information integrity

- organizational personnel with information security responsibilities

#### TEST — `si-7.12_asm-test`

- Software, firmware, and information integrity verification tools

- mechanisms supporting and/or implementing verification of the integrity of user-installed software prior to execution

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-7.12`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-7`.

- Catalog relationship **related**: `si-2`.

- Catalog relationship **related**: `cm-11`.

- [SP 800-81-2](https://doi.org/10.6028/NIST.SP.800-81-2)

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
