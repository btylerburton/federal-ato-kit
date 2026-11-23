---
title: "PM-7.1 \u2014 Offloading"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PM-7.1 — Offloading

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Not every function or service that a system provides is essential to organizational mission or business functions. Printing or copying is an example of a non-essential but supporting service for an organization. Whenever feasible, such supportive but non-essential functions or services are not co-located with the functions or services that support essential mission or business functions. Maintaining such functions on the same system or system component increases the attack surface of the organization’s mission-essential functions or services. Moving supportive but non-essential functions to a non-critical system, system component, or external provider can also increase efficiency by putting those functions or services under the control of individuals or providers who are subject matter experts in the functions or services.

### Requirements and exact statement parts

- `pm-7.1_smt`: Offload [PARAM pm-07.01_odp] to other systems, system components, or an external provider.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pm-7.1_smt — Offload [PARAM pm-07.01_odp] to other systems, system components, or an external provider.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pm-07.01_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pm-7.1_smt` — For “Offload [PARAM pm-07.01_odp] to other systems, system components, or an external provider.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pm-07.01_odp` — What approved value applies to **non-essential functions or services**? Record the value, scope, approving authority, and decision source.

  - Catalog context: non-essential functions or services to be offloaded are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pm-7.1_obj` (pm-7.1_smt): [PARAM pm-07.01_odp] are offloaded to other systems, system components, or an external provider.

#### EXAMINE — `pm-7.1_asm-examine`

- Information security program plan

- privacy program plan

- enterprise architecture documentation

- procedures addressing enterprise architecture development

- procedures for identifying and offloading functions or services

- results of risk assessments of enterprise architecture

- other relevant documents or records

#### INTERVIEW — `pm-7.1_asm-interview`

- Organizational personnel with information security and privacy program planning and plan implementation responsibilities

- organizational personnel responsible for developing enterprise architecture

- organizational personnel responsible for risk assessments of enterprise architecture

- organizational personnel with information security and privacy responsibilities

#### TEST — `pm-7.1_asm-test`

- Organizational processes for enterprise architecture development

- mechanisms supporting the enterprise architecture and its development

- mechanisms for offloading functions and services

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pm-7.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pm-7`.

- Catalog relationship **related**: `sa-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
