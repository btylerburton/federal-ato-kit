---
title: "SA-9.7 \u2014 Organization-controlled Integrity Checking"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-9.7 — Organization-controlled Integrity Checking

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Storage of organizational information in an external system could limit visibility into the security status of its data. The ability of the organization to verify and validate the integrity of its stored data without transferring it out of the external system provides such visibility.

### Requirements and exact statement parts

- `sa-9.7_smt`: Provide the capability to check the integrity of information while it resides in the external system.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-9.7_smt — Provide the capability to check the integrity of information while it resides in the external system.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sa-9.7_smt` — For “Provide the capability to check the integrity of information while it resides in the external system.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-9.7_obj` (sa-9.7_smt): the capability is provided to check the integrity of information while it resides in the external system.

#### EXAMINE — `sa-9.7_asm-examine`

- System and services acquisition policy

- procedures addressing external system services

- acquisition contracts for the system, system component, or system service

- solicitation documentation

- acquisition documentation

- service level agreements

- procedures addressing organization-controlled integrity checking

- information/data and/or system services

- organizational security requirements or conditions for external providers

- system security plan

- supply chain risk management plan

- other relevant documents or records

#### INTERVIEW — `sa-9.7_asm-interview`

- Organizational personnel with system and service acquisition responsibilities

- organizational personnel with information security responsibilities

- organization personnel with integrity checking responsibilities

- external providers of system services

- organizational personnel with supply chain risk management responsibilities

#### TEST — `sa-9.7_asm-test`

- Organizational processes for integrity checking

- mechanisms for supporting and implementing integrity checking of information in external systems

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-9.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-9`.

- Catalog relationship **related**: `si-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
