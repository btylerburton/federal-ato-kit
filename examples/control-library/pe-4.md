---
title: "PE-4 \u2014 Access Control for Transmission"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PE-4 — Access Control for Transmission

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Security controls applied to system distribution and transmission lines prevent accidental damage, disruption, and physical tampering. Such controls may also be necessary to prevent eavesdropping or modification of unencrypted transmissions. Security controls used to control physical access to system distribution and transmission lines include disconnected or locked spare jacks, locked wiring closets, protection of cabling by conduit or cable trays, and wiretapping sensors.

### Requirements and exact statement parts

- `pe-4_smt`: Control physical access to [PARAM pe-04_odp.01] within organizational facilities using [PARAM pe-04_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pe-4_smt — Control physical access to [PARAM pe-04_odp.01] within organizational facilities using [PARAM pe-04_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pe-04_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pe-04_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pe-4_smt` — For “Control physical access to [PARAM pe-04_odp.01] within organizational facilities using [PARAM pe-04_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pe-04_odp.01` — What approved value applies to **system distribution and transmission lines**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system distribution and transmission lines requiring physical access controls are defined;

- `pe-04_odp.02` — What approved value applies to **security controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security controls to be implemented to control physical access to system distribution and transmission lines within the organizational facility are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pe-4_obj` (pe-4_smt): physical access to [PARAM pe-04_odp.01] within organizational facilities is controlled using [PARAM pe-04_odp.02].

#### EXAMINE — `pe-4_asm-examine`

- Physical and environmental protection policy

- procedures addressing access control for transmission mediums

- system design documentation

- facility communications and wiring diagrams

- list of physical security safeguards applied to system distribution and transmission lines

- system security plan

- other relevant documents or records

#### INTERVIEW — `pe-4_asm-interview`

- Organizational personnel with physical access control responsibilities

- organizational personnel with information security responsibilities

#### TEST — `pe-4_asm-test`

- Organizational processes for access control to distribution and transmission lines

- mechanisms/security safeguards supporting and/or implementing access control to distribution and transmission lines

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pe-4`. The library index records the exact source revision and hash.

- Catalog relationship **related**: `at-3`.

- Catalog relationship **related**: `ia-4`.

- Catalog relationship **related**: `mp-2`.

- Catalog relationship **related**: `mp-4`.

- Catalog relationship **related**: `pe-2`.

- Catalog relationship **related**: `pe-3`.

- Catalog relationship **related**: `pe-5`.

- Catalog relationship **related**: `pe-9`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `sc-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
