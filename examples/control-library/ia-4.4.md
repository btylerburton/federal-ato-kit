---
title: "IA-4.4 \u2014 Identify User Status"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-4.4 — Identify User Status

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Characteristics that identify the status of individuals include contractors, foreign nationals, and non-organizational users. Identifying the status of individuals by these characteristics provides additional information about the people with whom organizational personnel are communicating. For example, it might be useful for a government employee to know that one of the individuals on an email message is a contractor.

### Requirements and exact statement parts

- `ia-4.4_smt`: Manage individual identifiers by uniquely identifying each individual as [PARAM ia-04.04_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-4.4_smt — Manage individual identifiers by uniquely identifying each individual as [PARAM ia-04.04_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ia-04.04_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ia-4.4_smt` — For “Manage individual identifiers by uniquely identifying each individual as [PARAM ia-04.04_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ia-04.04_odp` — What approved value applies to **characteristics**? Record the value, scope, approving authority, and decision source.

  - Catalog context: characteristics used to identify individual status is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-4.4_obj` (ia-4.4_smt): individual identifiers are managed by uniquely identifying each individual as [PARAM ia-04.04_odp].

#### EXAMINE — `ia-4.4_asm-examine`

- Identification and authentication policy

- system security plan

- procedures addressing identifier management

- procedures addressing account management

- list of characteristics identifying individual status

- other relevant documents or records

#### INTERVIEW — `ia-4.4_asm-interview`

- Organizational personnel with identifier management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ia-4.4_asm-test`

- Mechanisms supporting and/or implementing identifier management

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-4.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
