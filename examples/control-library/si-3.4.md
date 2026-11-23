---
title: "SI-3.4 \u2014 Updates Only by Privileged Users"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-3.4 — Updates Only by Privileged Users

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Protection mechanisms for malicious code are typically categorized as security-related software and, as such, are only updated by organizational personnel with appropriate access privileges.

### Requirements and exact statement parts

- `si-3.4_smt`: Update malicious code protection mechanisms only when directed by a privileged user.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-3.4_smt — Update malicious code protection mechanisms only when directed by a privileged user.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `si-3.4_smt` — For “Update malicious code protection mechanisms only when directed by a privileged user.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-3.4_obj` (si-3.4_smt): malicious code protection mechanisms are updated only when directed by a privileged user.

#### EXAMINE — `si-3.4_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing malicious code protection

- list of privileged users on system

- system design documentation

- malicious code protection mechanisms

- records of malicious code protection updates

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-3.4_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developers

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for malicious code protection

#### TEST — `si-3.4_asm-test`

- Mechanisms supporting and/or implementing malicious code protection capabilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-3.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-3`.

- Catalog relationship **related**: `cm-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
