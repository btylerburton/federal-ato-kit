---
title: "AU-9.3 \u2014 Cryptographic Protection"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-9.3 — Cryptographic Protection

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Cryptographic mechanisms used for protecting the integrity of audit information include signed hash functions using asymmetric cryptography. This enables the distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.

### Requirements and exact statement parts

- `au-9.3_smt`: Implement cryptographic mechanisms to protect the integrity of audit information and audit tools.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-9.3_smt — Implement cryptographic mechanisms to protect the integrity of audit information and audit tools.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `au-9.3_smt` — For “Implement cryptographic mechanisms to protect the integrity of audit information and audit tools.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-9.3_obj` (au-9.3_smt): cryptographic mechanisms to protect the integrity of audit information and audit tools are implemented.

#### EXAMINE — `au-9.3_asm-examine`

- Audit and accountability policy

- system security plan

- privacy plan

- access control policy and procedures

- procedures addressing protection of audit information

- system design documentation

- system hardware settings

- system configuration settings and associated documentation

- system audit records

- other relevant documents or records

#### INTERVIEW — `au-9.3_asm-interview`

- Organizational personnel with audit and accountability responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

- system developers

#### TEST — `au-9.3_asm-test`

- Cryptographic mechanisms protecting the integrity of audit information and tools

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-9.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `au-9`.

- Catalog relationship **related**: `au-10`.

- Catalog relationship **related**: `sc-12`.

- Catalog relationship **related**: `sc-13`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
