---
title: "MA-4.7 \u2014 Disconnect Verification"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-4.7 — Disconnect Verification

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Verifying the termination of a connection once maintenance is completed ensures that connections established during nonlocal maintenance and diagnostic sessions have been terminated and are no longer available for use.

### Requirements and exact statement parts

- `ma-4.7_smt`: Verify session and network connection termination after the completion of nonlocal maintenance and diagnostic sessions.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-4.7_smt — Verify session and network connection termination after the completion of nonlocal maintenance and diagnostic sessions.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ma-4.7_smt` — For “Verify session and network connection termination after the completion of nonlocal maintenance and diagnostic sessions.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-4.7_obj-1` (ma-4.7_smt): session connection termination is verified after the completion of nonlocal maintenance and diagnostic sessions;

- `ma-4.7_obj-2` (ma-4.7_smt): network connection termination is verified after the completion of nonlocal maintenance and diagnostic sessions.

#### EXAMINE — `ma-4.7_asm-examine`

- Maintenance policy

- procedures addressing nonlocal system maintenance

- system design documentation

- system configuration settings and associated documentation

- session/network termination logs

- cryptographic mechanisms protecting nonlocal maintenance activities

- maintenance records

- diagnostic records

- audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-4.7_asm-interview`

- Organizational personnel with system maintenance responsibilities

- network engineers

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ma-4.7_asm-test`

- Mechanisms implementing remote disconnect verifications of terminated nonlocal maintenance and diagnostic sessions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-4.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ma-4`.

- Catalog relationship **related**: `ac-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
