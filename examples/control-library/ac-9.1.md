---
title: "AC-9.1 \u2014 Unsuccessful Logons"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-9.1 — Unsuccessful Logons

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Information about the number of unsuccessful logon attempts since the last successful logon allows the user to recognize if the number of unsuccessful logon attempts is consistent with the user’s actual logon attempts.

### Requirements and exact statement parts

- `ac-9.1_smt`: Notify the user, upon successful logon, of the number of unsuccessful logon attempts since the last successful logon.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-9.1_smt — Notify the user, upon successful logon, of the number of unsuccessful logon attempts since the last successful logon.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ac-9.1_smt` — For “Notify the user, upon successful logon, of the number of unsuccessful logon attempts since the last successful logon.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-9.1_obj` (ac-9.1_smt): the user is notified, upon successful logon, of the number of unsuccessful logon attempts since the last successful logon.

#### EXAMINE — `ac-9.1_asm-examine`

- Access control policy

- procedures addressing previous logon notification

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-9.1_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developers

#### TEST — `ac-9.1_asm-test`

- Mechanisms implementing access control policy for previous logon notification

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-9.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-9`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
