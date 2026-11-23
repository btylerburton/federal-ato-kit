---
title: "SA-4.5 \u2014 System, Component, and Service Configurations"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-4.5 — System, Component, and Service Configurations

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Examples of security configurations include the U.S. Government Configuration Baseline (USGCB), Security Technical Implementation Guides (STIGs), and any limitations on functions, ports, protocols, and services. Security characteristics can include requiring that default passwords have been changed.

### Requirements and exact statement parts

- `sa-4.5_smt`: Require the developer of the system, system component, or system service to:

- `sa-4.5_smt.a`: Deliver the system, component, or service with [PARAM sa-04.05_odp] implemented; and

- `sa-4.5_smt.b`: Use the configurations as the default for any subsequent system, component, or service reinstallation or upgrade.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-4.5_smt — Require the developer of the system, system component, or system service to:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sa-4.5_smt.a — Deliver the system, component, or service with [PARAM sa-04.05_odp] implemented; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sa-4.5_smt.b — Use the configurations as the default for any subsequent system, component, or service reinstallation or upgrade.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sa-04.05_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sa-4.5_smt` — For “Require the developer of the system, system component, or system service to:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sa-4.5_smt.a` — For “Deliver the system, component, or service with [PARAM sa-04.05_odp] implemented; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sa-4.5_smt.b` — For “Use the configurations as the default for any subsequent system, component, or service reinstallation or upgrade.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sa-04.05_odp` — What approved value applies to **security configurations**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security configurations for the system, component, or service are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-4.5_obj.a` (sa-4.5_smt.a): the developer of the system, system component, or system service is required to deliver the system, component, or service with [PARAM sa-04.05_odp] implemented;

- `sa-4.5_obj.b` (sa-4.5_smt.b): the configurations are used as the default for any subsequent system, component, or service reinstallation or upgrade.

#### EXAMINE — `sa-4.5_asm-examine`

- System and services acquisition policy

- procedures addressing the integration of security requirements, descriptions, and criteria into the acquisition process

- solicitation documents

- acquisition documentation

- acquisition contracts for the system, system component, or system service

- security configurations to be implemented by the developer of the system, system component, or system service

- service level agreements

- system security plan

- other relevant documents or records

#### INTERVIEW — `sa-4.5_asm-interview`

- Organizational personnel with acquisition/contracting responsibilities

- organizational personnel with the responsibility to determine system security requirements

- system developers or service provider

- organizational personnel with information security responsibilities

#### TEST — `sa-4.5_asm-test`

- Mechanisms used to verify that the configuration of the system, component, or service is delivered as specified

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-4.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
