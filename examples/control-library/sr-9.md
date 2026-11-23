---
title: "SR-9 \u2014 Tamper Resistance and Detection"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SR-9 — Tamper Resistance and Detection

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Anti-tamper technologies, tools, and techniques provide a level of protection for systems, system components, and services against many threats, including reverse engineering, modification, and substitution. Strong identification combined with tamper resistance and/or tamper detection is essential to protecting systems and components during distribution and when in use.

### Requirements and exact statement parts

- `sr-9_smt`: Implement a tamper protection program for the system, system component, or system service.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sr-9_smt — Implement a tamper protection program for the system, system component, or system service.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sr-9_smt` — For “Implement a tamper protection program for the system, system component, or system service.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sr-9_obj` (sr-9_smt): a tamper protection program is implemented for the system, system component, or system service.

#### EXAMINE — `sr-9_asm-examine`

- Supply chain risk management policy and procedures

- supply chain risk management plan

- system and services acquisition policy

- procedures addressing supply chain protection

- procedures addressing tamper resistance and detection

- tamper protection program documentation

- tamper protection tools and techniques documentation

- tamper resistance and detection tools and techniques documentation

- acquisition documentation

- service level agreements

- acquisition contracts for the system, system component, or system service

- system security plan

- other relevant documents or records

#### INTERVIEW — `sr-9_asm-interview`

- Organizational personnel with tamper protection program responsibilities

- organizational personnel with information security responsibilities

- organizational personnel with supply chain risk management responsibilities

#### TEST — `sr-9_asm-test`

- Organizational processes for the implementation of the tamper protection program

- mechanisms supporting and/or implementing the tamper protection program

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sr-9`. The library index records the exact source revision and hash.

- [ISO 20243](https://www.iso.org/standard/74399.html)

- Catalog relationship **related**: `pe-3`.

- Catalog relationship **related**: `pm-30`.

- Catalog relationship **related**: `sa-15`.

- Catalog relationship **related**: `si-4`.

- Catalog relationship **related**: `si-7`.

- Catalog relationship **related**: `sr-3`.

- Catalog relationship **related**: `sr-4`.

- Catalog relationship **related**: `sr-5`.

- Catalog relationship **related**: `sr-10`.

- Catalog relationship **related**: `sr-11`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
