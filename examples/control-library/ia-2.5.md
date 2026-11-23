---
title: "IA-2.5 \u2014 Individual Authentication with Group Authentication"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-2.5 — Individual Authentication with Group Authentication

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Individual authentication prior to shared group authentication mitigates the risk of using group accounts or authenticators.

### Requirements and exact statement parts

- `ia-2.5_smt`: When shared accounts or authenticators are employed, require users to be individually authenticated before granting access to the shared accounts or resources.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-2.5_smt — When shared accounts or authenticators are employed, require users to be individually authenticated before granting access to the shared accounts or resources.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ia-2.5_smt` — For “When shared accounts or authenticators are employed, require users to be individually authenticated before granting access to the shared accounts or resources.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-2.5_obj` (ia-2.5_smt): users are required to be individually authenticated before granting access to the shared accounts or resources when shared accounts or authenticators are employed.

#### EXAMINE — `ia-2.5_asm-examine`

- Identification and authentication policy

- system security plan

- procedures addressing user identification and authentication

- system design documentation

- system configuration settings and associated documentation

- system audit records

- list of system accounts

- other relevant documents or records

#### INTERVIEW — `ia-2.5_asm-interview`

- Organizational personnel with system operations responsibilities

- organizational personnel with account management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `ia-2.5_asm-test`

- Mechanisms supporting and/or implementing an authentication capability for group accounts

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-2.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
