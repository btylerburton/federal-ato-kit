---
title: "IA-6 \u2014 Authentication Feedback"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-6 — Authentication Feedback

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Authentication feedback from systems does not provide information that would allow unauthorized individuals to compromise authentication mechanisms. For some types of systems, such as desktops or notebooks with relatively large monitors, the threat (referred to as shoulder surfing) may be significant. For other types of systems, such as mobile devices with small displays, the threat may be less significant and is balanced against the increased likelihood of typographic input errors due to small keyboards. Thus, the means for obscuring authentication feedback is selected accordingly. Obscuring authentication feedback includes displaying asterisks when users type passwords into input devices or displaying feedback for a very limited time before obscuring it.

### Requirements and exact statement parts

- `ia-6_smt`: Obscure feedback of authentication information during the authentication process to protect the information from possible exploitation and use by unauthorized individuals.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-6_smt — Obscure feedback of authentication information during the authentication process to protect the information from possible exploitation and use by unauthorized individuals.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ia-6_smt` — For “Obscure feedback of authentication information during the authentication process to protect the information from possible exploitation and use by unauthorized individuals.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-6_obj` (ia-6_smt): the feedback of authentication information is obscured during the authentication process to protect the information from possible exploitation and use by unauthorized individuals.

#### EXAMINE — `ia-6_asm-examine`

- Identification and authentication policy

- system security plan

- procedures addressing authenticator feedback

- system design documentation

- system configuration settings and associated documentation

- system audit records

- other relevant documents or records

#### INTERVIEW — `ia-6_asm-interview`

- Organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `ia-6_asm-test`

- Mechanisms supporting and/or implementing the obscuring of feedback of authentication information during authentication

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-6`. The library index records the exact source revision and hash.

- Catalog relationship **related**: `ac-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
