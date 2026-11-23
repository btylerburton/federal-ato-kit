---
title: "IA-3.1 \u2014 Cryptographic Bidirectional Authentication"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-3.1 — Cryptographic Bidirectional Authentication

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

A local connection is a connection with a device that communicates without the use of a network. A network connection is a connection with a device that communicates through a network. A remote connection is a connection with a device that communicates through an external network. Bidirectional authentication provides stronger protection to validate the identity of other devices for connections that are of greater risk.

### Requirements and exact statement parts

- `ia-3.1_smt`: Authenticate [PARAM ia-03.01_odp.01] before establishing [PARAM ia-03.01_odp.02] connection using bidirectional authentication that is cryptographically based.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-3.1_smt — Authenticate [PARAM ia-03.01_odp.01] before establishing [PARAM ia-03.01_odp.02] connection using bidirectional authentication that is cryptographically based.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ia-03.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ia-03.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ia-3.1_smt` — For “Authenticate [PARAM ia-03.01_odp.01] before establishing [PARAM ia-03.01_odp.02] connection using bidirectional authentication that is cryptographically based.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ia-03.01_odp.01` — What approved value applies to **devices and/or types of devices**? Record the value, scope, approving authority, and decision source.

  - Catalog context: devices and/or types of devices requiring use of cryptographically based, bidirectional authentication to authenticate before establishing one or more connections are defined;

- `ia-03.01_odp.02` — What approved value applies to **selection; choose one-or-more from: local; remote; network**? Record the value, scope, approving authority, and decision source.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-3.1_obj` (ia-3.1_smt): [PARAM ia-03.01_odp.01] are authenticated before establishing [PARAM ia-03.01_odp.02] connection using bidirectional authentication that is cryptographically based.

#### EXAMINE — `ia-3.1_asm-examine`

- Identification and authentication policy

- system security plan

- procedures addressing device identification and authentication

- system design documentation

- list of devices requiring unique identification and authentication

- device connection reports

- system configuration settings and associated documentation

- other relevant documents or records

#### INTERVIEW — `ia-3.1_asm-interview`

- Organizational personnel with operational responsibilities for device identification and authentication

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `ia-3.1_asm-test`

- Mechanisms supporting and/or implementing device authentication capability

- cryptographically based bidirectional authentication mechanisms

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-3.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-3`.

- Catalog relationship **related**: `sc-8`.

- Catalog relationship **related**: `sc-12`.

- Catalog relationship **related**: `sc-13`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
