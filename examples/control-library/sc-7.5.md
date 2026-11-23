---
title: "SC-7.5 \u2014 Deny by Default \u2014 Allow by Exception"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-7.5 — Deny by Default — Allow by Exception

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Denying by default and allowing by exception applies to inbound and outbound network communications traffic. A deny-all, permit-by-exception network communications traffic policy ensures that only those system connections that are essential and approved are allowed. Deny by default, allow by exception also applies to a system that is connected to an external system.

### Requirements and exact statement parts

- `sc-7.5_smt`: Deny network communications traffic by default and allow network communications traffic by exception [PARAM sc-07.05_odp.01].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-7.5_smt — Deny network communications traffic by default and allow network communications traffic by exception [PARAM sc-07.05_odp.01].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-07.05_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sc-07.05_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-7.5_smt` — For “Deny network communications traffic by default and allow network communications traffic by exception [PARAM sc-07.05_odp.01].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-07.05_odp.01` — What approved value applies to **selection; choose one-or-more from: at managed interfaces; for [PARAM sc-07.05_odp.02]**? Record the value, scope, approving authority, and decision source.

- `sc-07.05_odp.02` — What approved value applies to **systems**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems for which network communications traffic is denied by default and network communications traffic is allowed by exception are defined (if selected).

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-7.5_obj-1` (sc-7.5_smt): network communications traffic is denied by default [PARAM sc-07.05_odp.01];

- `sc-7.5_obj-2` (sc-7.5_smt): network communications traffic is allowed by exception [PARAM sc-07.05_odp.01].

#### EXAMINE — `sc-7.5_asm-examine`

- System and communications protection policy

- procedures addressing boundary protection

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-7.5_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developer

- organizational personnel with boundary protection responsibilities

#### TEST — `sc-7.5_asm-test`

- Mechanisms implementing traffic management at managed interfaces

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-7.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sc-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
