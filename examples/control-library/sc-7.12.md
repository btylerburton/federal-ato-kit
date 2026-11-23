---
title: "SC-7.12 \u2014 Host-based Protection"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-7.12 — Host-based Protection

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Host-based boundary protection mechanisms include host-based firewalls. System components that employ host-based boundary protection mechanisms include servers, workstations, notebook computers, and mobile devices.

### Requirements and exact statement parts

- `sc-7.12_smt`: Implement [PARAM sc-07.12_odp.01] at [PARAM sc-07.12_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-7.12_smt — Implement [PARAM sc-07.12_odp.01] at [PARAM sc-07.12_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-07.12_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sc-07.12_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-7.12_smt` — For “Implement [PARAM sc-07.12_odp.01] at [PARAM sc-07.12_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-07.12_odp.01` — What approved value applies to **host-based boundary protection mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: host-based boundary protection mechanisms to be implemented are defined;

- `sc-07.12_odp.02` — What approved value applies to **system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system components where host-based boundary protection mechanisms are to be implemented are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-7.12_obj` (sc-7.12_smt): [PARAM sc-07.12_odp.01] are implemented at [PARAM sc-07.12_odp.02].

#### EXAMINE — `sc-7.12_asm-examine`

- System and communications protection policy

- procedures addressing boundary protection

- system design documentation

- boundary protection hardware and software

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-7.12_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel with boundary protection responsibilities

- system users

#### TEST — `sc-7.12_asm-test`

- Mechanisms implementing host-based boundary protection capabilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-7.12`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sc-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
