---
title: "IA-3 \u2014 Device Identification and Authentication"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-3 — Device Identification and Authentication

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Devices that require unique device-to-device identification and authentication are defined by type, device, or a combination of type and device. Organization-defined device types include devices that are not owned by the organization. Systems use shared known information (e.g., Media Access Control [MAC], Transmission Control Protocol/Internet Protocol [TCP/IP] addresses) for device identification or organizational authentication solutions (e.g., Institute of Electrical and Electronics Engineers (IEEE) 802.1x and Extensible Authentication Protocol [EAP], RADIUS server with EAP-Transport Layer Security [TLS] authentication, Kerberos) to identify and authenticate devices on local and wide area networks. Organizations determine the required strength of authentication mechanisms based on the security categories of systems and mission or business requirements. Because of the challenges of implementing device authentication on a large scale, organizations can restrict the application of the control to a limited number/type of devices based on mission or business needs.

### Requirements and exact statement parts

- `ia-3_smt`: Uniquely identify and authenticate [PARAM ia-03_odp.01] before establishing a [PARAM ia-03_odp.02] connection.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-3_smt — Uniquely identify and authenticate [PARAM ia-03_odp.01] before establishing a [PARAM ia-03_odp.02] connection.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ia-03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ia-03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ia-3_smt` — For “Uniquely identify and authenticate [PARAM ia-03_odp.01] before establishing a [PARAM ia-03_odp.02] connection.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ia-03_odp.01` — What approved value applies to **devices and/or types of devices**? Record the value, scope, approving authority, and decision source.

  - Catalog context: devices and/or types of devices to be uniquely identified and authenticated before establishing a connection are defined;

- `ia-03_odp.02` — What approved value applies to **selection; choose one-or-more from: local; remote; network**? Record the value, scope, approving authority, and decision source.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-3_obj` (ia-3_smt): [PARAM ia-03_odp.01] are uniquely identified and authenticated before establishing a [PARAM ia-03_odp.02] connection.

#### EXAMINE — `ia-3_asm-examine`

- Identification and authentication policy

- system security plan

- procedures addressing device identification and authentication

- system design documentation

- list of devices requiring unique identification and authentication

- device connection reports

- system configuration settings and associated documentation

- other relevant documents or records

#### INTERVIEW — `ia-3_asm-interview`

- Organizational personnel with operational responsibilities for device identification and authentication

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `ia-3_asm-test`

- Mechanisms supporting and/or implementing device identification and authentication capabilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-3`. The library index records the exact source revision and hash.

- Catalog relationship **related**: `ac-17`.

- Catalog relationship **related**: `ac-18`.

- Catalog relationship **related**: `ac-19`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `ca-3`.

- Catalog relationship **related**: `ca-9`.

- Catalog relationship **related**: `ia-4`.

- Catalog relationship **related**: `ia-5`.

- Catalog relationship **related**: `ia-9`.

- Catalog relationship **related**: `ia-11`.

- Catalog relationship **related**: `ia-13`.

- Catalog relationship **related**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
