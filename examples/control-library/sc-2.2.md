---
title: "SC-2.2 \u2014 Disassociability"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-2.2 — Disassociability

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

If a system is compromised, storing applications and software separately from state information about users’ interactions with an application may better protect individuals’ privacy.

### Requirements and exact statement parts

- `sc-2.2_smt`: Store state information from applications and software separately.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-2.2_smt — Store state information from applications and software separately.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sc-2.2_smt` — For “Store state information from applications and software separately.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-2.2_obj` (sc-2.2_smt): state information is stored separately from applications and software.

#### EXAMINE — `sc-2.2_asm-examine`

- System and communications protection policy

- procedures addressing application and software partitioning

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `sc-2.2_asm-interview`

- System/network administrators

- organizational personnel with information security and privacy responsibilities

- system developer

#### TEST — `sc-2.2_asm-test`

- Separation of application state information from software

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-2.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sc-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
