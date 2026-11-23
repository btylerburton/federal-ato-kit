---
title: "SA-4.9 \u2014 Functions, Ports, Protocols, and Services in Use"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-4.9 — Functions, Ports, Protocols, and Services in Use

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The identification of functions, ports, protocols, and services early in the system development life cycle (e.g., during the initial requirements definition and design stages) allows organizations to influence the design of the system, system component, or system service. This early involvement in the system development life cycle helps organizations avoid or minimize the use of functions, ports, protocols, or services that pose unnecessarily high risks and understand the trade-offs involved in blocking specific ports, protocols, or services or requiring system service providers to do so. Early identification of functions, ports, protocols, and services avoids costly retrofitting of controls after the system, component, or system service has been implemented. SA-9 (catalog reference: `#sa-9`) describes the requirements for external system services. Organizations identify which functions, ports, protocols, and services are provided from external sources.

### Requirements and exact statement parts

- `sa-4.9_smt`: Require the developer of the system, system component, or system service to identify the functions, ports, protocols, and services intended for organizational use.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-4.9_smt — Require the developer of the system, system component, or system service to identify the functions, ports, protocols, and services intended for organizational use.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sa-4.9_smt` — For “Require the developer of the system, system component, or system service to identify the functions, ports, protocols, and services intended for organizational use.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-4.9_obj-1` (sa-4.9_smt): the developer of the system, system component, or system service is required to identify the functions intended for organizational use;

- `sa-4.9_obj-2` (sa-4.9_smt): the developer of the system, system component, or system service is required to identify the ports intended for organizational use;

- `sa-4.9_obj-3` (sa-4.9_smt): the developer of the system, system component, or system service is required to identify the protocols intended for organizational use;

- `sa-4.9_obj-4` (sa-4.9_smt): the developer of the system, system component, or system service is required to identify the services intended for organizational use.

#### EXAMINE — `sa-4.9_asm-examine`

- System and services acquisition policy

- procedures addressing the integration of security requirements, descriptions, and criteria into the acquisition process

- system design documentation

- system documentation, including functions, ports, protocols, and services intended for organizational use

- acquisition contracts for systems or services

- acquisition documentation

- solicitation documentation

- service level agreements

- organizational security requirements, descriptions, and criteria for developers of systems, system components, and system services

- system security plan

- other relevant documents or records

#### INTERVIEW — `sa-4.9_asm-interview`

- Organizational personnel with acquisition/contracting responsibilities

- organizational personnel with the responsibility for determining system security requirements

- system/network administrators

- organizational personnel operating, using, and/or maintaining the system

- system developers

- organizational personnel with information security responsibilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-4.9`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-4`.

- Catalog relationship **related**: `cm-7`.

- Catalog relationship **related**: `sa-9`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
