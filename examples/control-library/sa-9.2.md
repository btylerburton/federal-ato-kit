---
title: "SA-9.2 \u2014 Identification of Functions, Ports, Protocols, and Services"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-9.2 — Identification of Functions, Ports, Protocols, and Services

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Information from external service providers regarding the specific functions, ports, protocols, and services used in the provision of such services can be useful when the need arises to understand the trade-offs involved in restricting certain functions and services or blocking certain ports and protocols.

### Requirements and exact statement parts

- `sa-9.2_smt`: Require providers of the following external system services to identify the functions, ports, protocols, and other services required for the use of such services: [PARAM sa-09.02_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-9.2_smt — Require providers of the following external system services to identify the functions, ports, protocols, and other services required for the use of such services: [PARAM sa-09.02_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sa-09.02_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sa-9.2_smt` — For “Require providers of the following external system services to identify the functions, ports, protocols, and other services required for the use of such services: [PARAM sa-09.02_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sa-09.02_odp` — What approved value applies to **external system services**? Record the value, scope, approving authority, and decision source.

  - Catalog context: external system services that require the identification of functions, ports, protocols, and other services are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-9.2_obj` (sa-9.2_smt): providers of [PARAM sa-09.02_odp] are required to identify the functions, ports, protocols, and other services required for the use of such services.

#### EXAMINE — `sa-9.2_asm-examine`

- System and services acquisition policy

- supply chain risk management policy and procedures

- procedures addressing external system services

- acquisition contracts for the system, system component, or system service

- acquisition documentation

- solicitation documentation

- service level agreements

- organizational security requirements and security specifications for external service providers

- list of required functions, ports, protocols, and other services

- system security plan

- other relevant documents or records

#### INTERVIEW — `sa-9.2_asm-interview`

- Organizational personnel with system and service acquisition responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- external providers of system services

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-9.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-9`.

- Catalog relationship **related**: `cm-6`.

- Catalog relationship **related**: `cm-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
