---
title: "PS-3.4 \u2014 Citizenship Requirements"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PS-3.4 — Citizenship Requirements

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

None.

### Requirements and exact statement parts

- `ps-3.4_smt`: Verify that individuals accessing a system processing, storing, or transmitting [PARAM ps-03.04_odp.01] meet [PARAM ps-03.04_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ps-3.4_smt — Verify that individuals accessing a system processing, storing, or transmitting [PARAM ps-03.04_odp.01] meet [PARAM ps-03.04_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ps-03.04_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ps-03.04_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ps-3.4_smt` — For “Verify that individuals accessing a system processing, storing, or transmitting [PARAM ps-03.04_odp.01] meet [PARAM ps-03.04_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ps-03.04_odp.01` — What approved value applies to **information types**? Record the value, scope, approving authority, and decision source.

  - Catalog context: information types that are processed, stored, or transmitted by a system that require individuals accessing the system to meet [PARAM ps-03.04_odp.02] are defined;

- `ps-03.04_odp.02` — What approved value applies to **citizenship requirements**? Record the value, scope, approving authority, and decision source.

  - Catalog context: citizenship requirements to be met by individuals to access a system processing, storing, or transmitting information are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ps-3.4_obj` (ps-3.4_smt): individuals accessing a system processing, storing, or transmitting [PARAM ps-03.04_odp.01] meet [PARAM ps-03.04_odp.02].

#### EXAMINE — `ps-3.4_asm-examine`

- Personnel security policy

- access control policy, procedures addressing personnel screening

- records of screened personnel

- screening criteria

- records of access authorizations

- system security plan

- other relevant documents or records

#### INTERVIEW — `ps-3.4_asm-interview`

- Organizational personnel with personnel security responsibilities

- organizational personnel with information security responsibilities

#### TEST — `ps-3.4_asm-test`

- Organizational processes for ensuring valid access authorizations for information requiring citizenship

- organizational process for additional personnel screening for information requiring citizenship

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ps-3.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ps-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
