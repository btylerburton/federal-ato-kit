---
title: "IA-4.1 \u2014 Prohibit Account Identifiers as Public Identifiers"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-4.1 — Prohibit Account Identifiers as Public Identifiers

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Prohibiting account identifiers as public identifiers applies to any publicly disclosed account identifier used for communication such as, electronic mail and instant messaging. Prohibiting the use of systems account identifiers that are the same as some public identifier, such as the individual identifier section of an electronic mail address, makes it more difficult for adversaries to guess user identifiers. Prohibiting account identifiers as public identifiers without the implementation of other supporting controls only complicates guessing of identifiers. Additional protections are required for authenticators and credentials to protect the account.

### Requirements and exact statement parts

- `ia-4.1_smt`: Prohibit the use of system account identifiers that are the same as public identifiers for individual accounts.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-4.1_smt — Prohibit the use of system account identifiers that are the same as public identifiers for individual accounts.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ia-4.1_smt` — For “Prohibit the use of system account identifiers that are the same as public identifiers for individual accounts.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-4.1_obj` (ia-4.1_smt): the use of system account identifiers that are the same as public identifiers is prohibited for individual accounts.

#### EXAMINE — `ia-4.1_asm-examine`

- Identification and authentication policy

- system security plan

- procedures addressing identifier management

- procedures addressing account management

- system design documentation

- system configuration settings and associated documentation

- system audit records

- other relevant documents or records

#### INTERVIEW — `ia-4.1_asm-interview`

- Organizational personnel with identifier management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ia-4.1_asm-test`

- Mechanisms supporting and/or implementing identifier management

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-4.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-4`.

- Catalog relationship **related**: `at-2`.

- Catalog relationship **related**: `pt-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
