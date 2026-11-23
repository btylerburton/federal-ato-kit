---
title: "AC-6.8 \u2014 Privilege Levels for Code Execution"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-6.8 — Privilege Levels for Code Execution

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

In certain situations, software applications or programs need to execute with elevated privileges to perform required functions. However, depending on the software functionality and configuration, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking such applications or programs, those users may indirectly be provided with greater privileges than assigned.

### Requirements and exact statement parts

- `ac-6.8_smt`: Prevent the following software from executing at higher privilege levels than users executing the software: [PARAM ac-06.08_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-6.8_smt — Prevent the following software from executing at higher privilege levels than users executing the software: [PARAM ac-06.08_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-06.08_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-6.8_smt` — For “Prevent the following software from executing at higher privilege levels than users executing the software: [PARAM ac-06.08_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-06.08_odp` — What approved value applies to **software**? Record the value, scope, approving authority, and decision source.

  - Catalog context: software to be prevented from executing at higher privilege levels than users executing the software is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-6.8_obj` (ac-6.8_smt): [PARAM ac-06.08_odp] is prevented from executing at higher privilege levels than users executing the software.

#### EXAMINE — `ac-6.8_asm-examine`

- Access control policy

- procedures addressing least privilege

- list of software that should not execute at higher privilege levels than users executing software

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-6.8_asm-interview`

- Organizational personnel with responsibilities for defining least privileges necessary to accomplish specified tasks

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `ac-6.8_asm-test`

- Mechanisms implementing least privilege functions for software execution

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-6.8`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
