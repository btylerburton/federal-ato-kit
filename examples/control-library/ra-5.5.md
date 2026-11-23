---
title: "RA-5.5 \u2014 Privileged Access"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# RA-5.5 — Privileged Access

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

In certain situations, the nature of the vulnerability scanning may be more intrusive, or the system component that is the subject of the scanning may contain classified or controlled unclassified information, such as personally identifiable information. Privileged access authorization to selected system components facilitates more thorough vulnerability scanning and protects the sensitive nature of such scanning.

### Requirements and exact statement parts

- `ra-5.5_smt`: Implement privileged access authorization to [PARAM ra-05.05_odp.01] for [PARAM ra-05.05_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ra-5.5_smt — Implement privileged access authorization to [PARAM ra-05.05_odp.01] for [PARAM ra-05.05_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ra-05.05_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ra-05.05_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ra-5.5_smt` — For “Implement privileged access authorization to [PARAM ra-05.05_odp.01] for [PARAM ra-05.05_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ra-05.05_odp.01` — What approved value applies to **system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system components to which privileged access is authorized for selected vulnerability scanning activities are defined;

- `ra-05.05_odp.02` — What approved value applies to **vulnerability scanning activities**? Record the value, scope, approving authority, and decision source.

  - Catalog context: vulnerability scanning activities selected for privileged access authorization to system components are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ra-5.5_obj` (ra-5.5_smt): privileged access authorization is implemented to [PARAM ra-05.05_odp.01] for [PARAM ra-05.05_odp.02].

#### EXAMINE — `ra-5.5_asm-examine`

- Risk assessment policy

- procedures addressing vulnerability scanning

- system design documentation

- system configuration settings and associated documentation

- list of system components for vulnerability scanning

- personnel access authorization list

- authorization credentials

- access authorization records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ra-5.5_asm-interview`

- Organizational personnel with vulnerability scanning responsibilities

- system/network administrators

- organizational personnel responsible for access control to the system

- organizational personnel responsible for configuration management of the system

- system developers

- organizational personnel with security responsibilities

#### TEST — `ra-5.5_asm-test`

- Organizational processes for vulnerability scanning

- organizational processes for access control

- mechanisms supporting and/or implementing access control

- mechanisms/tools supporting and/or implementing vulnerability scanning

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ra-5.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ra-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
