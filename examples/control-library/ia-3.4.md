---
title: "IA-3.4 \u2014 Device Attestation"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-3.4 — Device Attestation

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Device attestation refers to the identification and authentication of a device based on its configuration and known operating state. Device attestation can be determined via a cryptographic hash of the device. If device attestation is the means of identification and authentication, then it is important that patches and updates to the device are handled via a configuration management process such that the patches and updates are done securely and do not disrupt identification and authentication to other devices.

### Requirements and exact statement parts

- `ia-3.4_smt`: Handle device identification and authentication based on attestation by [PARAM ia-03.04_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-3.4_smt — Handle device identification and authentication based on attestation by [PARAM ia-03.04_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ia-03.04_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ia-3.4_smt` — For “Handle device identification and authentication based on attestation by [PARAM ia-03.04_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ia-03.04_odp` — What approved value applies to **configuration management process**? Record the value, scope, approving authority, and decision source.

  - Catalog context: configuration management process to be employed to handle device identification and authentication based on attestation is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-3.4_obj` (ia-3.4_smt): device identification and authentication are handled based on attestation by [PARAM ia-03.04_odp].

#### EXAMINE — `ia-3.4_asm-examine`

- Identification and authentication policy

- system security plan

- procedures addressing device identification and authentication

- procedures addressing device configuration management

- system design documentation

- system configuration settings and associated documentation

- configuration management records

- change control records

- system audit records

- other relevant documents or records

#### INTERVIEW — `ia-3.4_asm-interview`

- Organizational personnel with operational responsibilities for device identification and authentication

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ia-3.4_asm-test`

- Mechanisms supporting and/or implementing device identification and authentication capabilities

- mechanisms supporting and/or implementing configuration management

- cryptographic mechanisms supporting device attestation

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-3.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-3`.

- Catalog relationship **related**: `cm-2`.

- Catalog relationship **related**: `cm-3`.

- Catalog relationship **related**: `cm-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
