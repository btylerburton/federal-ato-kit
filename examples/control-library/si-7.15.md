---
title: "SI-7.15 \u2014 Code Authentication"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-7.15 — Code Authentication

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Cryptographic authentication includes verifying that software or firmware components have been digitally signed using certificates recognized and approved by organizations. Code signing is an effective method to protect against malicious code. Organizations that employ cryptographic mechanisms also consider cryptographic key management solutions.

### Requirements and exact statement parts

- `si-7.15_smt`: Implement cryptographic mechanisms to authenticate the following software or firmware components prior to installation: [PARAM si-07.15_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-7.15_smt — Implement cryptographic mechanisms to authenticate the following software or firmware components prior to installation: [PARAM si-07.15_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-07.15_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-7.15_smt` — For “Implement cryptographic mechanisms to authenticate the following software or firmware components prior to installation: [PARAM si-07.15_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-07.15_odp` — What approved value applies to **software or firmware components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: software or firmware components to be authenticated by cryptographic mechanisms prior to installation are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-7.15_obj` (si-7.15_smt): cryptographic mechanisms are implemented to authenticate [PARAM si-07.15_odp] prior to installation.

#### EXAMINE — `si-7.15_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing software, firmware, and information integrity

- system design documentation

- system configuration settings and associated documentation

- cryptographic mechanisms and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-7.15_asm-interview`

- Organizational personnel responsible for software, firmware, and/or information integrity

- organizational personnel with information security responsibilities

- system/network administrators

- system developer

#### TEST — `si-7.15_asm-test`

- Cryptographic mechanisms authenticating software and firmware prior to installation

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-7.15`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-7`.

- Catalog relationship **related**: `cm-5`.

- Catalog relationship **related**: `sc-12`.

- Catalog relationship **related**: `sc-13`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
