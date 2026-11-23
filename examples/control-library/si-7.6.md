---
title: "SI-7.6 \u2014 Cryptographic Protection"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-7.6 — Cryptographic Protection

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Cryptographic mechanisms used to protect integrity include digital signatures and the computation and application of signed hashes using asymmetric cryptography, protecting the confidentiality of the key used to generate the hash, and using the public key to verify the hash information. Organizations that employ cryptographic mechanisms also consider cryptographic key management solutions.

### Requirements and exact statement parts

- `si-7.6_smt`: Implement cryptographic mechanisms to detect unauthorized changes to software, firmware, and information.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-7.6_smt — Implement cryptographic mechanisms to detect unauthorized changes to software, firmware, and information.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `si-7.6_smt` — For “Implement cryptographic mechanisms to detect unauthorized changes to software, firmware, and information.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-7.6_obj-1` (si-7.6_smt): cryptographic mechanisms are implemented to detect unauthorized changes to software;

- `si-7.6_obj-2` (si-7.6_smt): cryptographic mechanisms are implemented to detect unauthorized changes to firmware;

- `si-7.6_obj-3` (si-7.6_smt): cryptographic mechanisms are implemented to detect unauthorized changes to information.

#### EXAMINE — `si-7.6_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing software, firmware, and information integrity

- system design documentation

- system configuration settings and associated documentation

- cryptographic mechanisms and associated documentation

- records of detected unauthorized changes to software, firmware, and information

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-7.6_asm-interview`

- Organizational personnel responsible for software, firmware, and/or information integrity

- organizational personnel with information security responsibilities

- system/network administrators

- system developer

#### TEST — `si-7.6_asm-test`

- Software, firmware, and information integrity verification tools

- cryptographic mechanisms implementing software, firmware, and information integrity

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-7.6`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-7`.

- Catalog relationship **related**: `sc-12`.

- Catalog relationship **related**: `sc-13`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
