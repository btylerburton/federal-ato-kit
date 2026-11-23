---
title: "SA-9.6 \u2014 Organization-controlled Cryptographic Keys"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-9.6 — Organization-controlled Cryptographic Keys

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Maintaining exclusive control of cryptographic keys in an external system prevents decryption of organizational data by external system staff. Organizational control of cryptographic keys can be implemented by encrypting and decrypting data inside the organization as data is sent to and received from the external system or by employing a component that permits encryption and decryption functions to be local to the external system but allows exclusive organizational access to the encryption keys.

### Requirements and exact statement parts

- `sa-9.6_smt`: Maintain exclusive control of cryptographic keys for encrypted material stored or transmitted through an external system.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-9.6_smt — Maintain exclusive control of cryptographic keys for encrypted material stored or transmitted through an external system.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sa-9.6_smt` — For “Maintain exclusive control of cryptographic keys for encrypted material stored or transmitted through an external system.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-9.6_obj` (sa-9.6_smt): exclusive control of cryptographic keys is maintained for encrypted material stored or transmitted through an external system.

#### EXAMINE — `sa-9.6_asm-examine`

- System and services acquisition policy

- procedures addressing external system services

- acquisition contracts for the system, system component, or system service

- solicitation documentation

- acquisition documentation

- service level agreements

- procedures addressing organization-controlled cryptographic key management

- organizational security requirements or conditions for external providers

- system security plan

- supply chain risk management plan

- other relevant documents or records

#### INTERVIEW — `sa-9.6_asm-interview`

- Organizational personnel with system and service acquisition responsibilities

- organizational personnel with information security responsibilities

- organization personnel with cryptographic key management responsibilities

- external providers of system services

- organizational personnel with supply chain risk management responsibilities

#### TEST — `sa-9.6_asm-test`

- Organizational processes for cryptographic key management

- mechanisms for supporting and implementing the management of organization-controlled cryptographic keys

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-9.6`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-9`.

- Catalog relationship **related**: `sc-12`.

- Catalog relationship **related**: `sc-13`.

- Catalog relationship **related**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
