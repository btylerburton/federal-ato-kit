---
title: "IA-5.13 \u2014 Expiration of Cached Authenticators"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-5.13 — Expiration of Cached Authenticators

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Cached authenticators are used to authenticate to the local machine when the network is not available. If cached authentication information is out of date, the validity of the authentication information may be questionable.

### Requirements and exact statement parts

- `ia-5.13_smt`: Prohibit the use of cached authenticators after [PARAM ia-05.13_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-5.13_smt — Prohibit the use of cached authenticators after [PARAM ia-05.13_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ia-05.13_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ia-5.13_smt` — For “Prohibit the use of cached authenticators after [PARAM ia-05.13_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ia-05.13_odp` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the time period after which the use of cached authenticators is prohibited is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-5.13_obj` (ia-5.13_smt): the use of cached authenticators is prohibited after [PARAM ia-05.13_odp].

#### EXAMINE — `ia-5.13_asm-examine`

- Identification and authentication policy

- procedures addressing authenticator management

- system security plan

- system design documentation

- system configuration settings and associated documentation

- system audit records

- other relevant documents or records

#### INTERVIEW — `ia-5.13_asm-interview`

- Organizational personnel with authenticator management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `ia-5.13_asm-test`

- Mechanisms supporting and/or implementing authenticator management capability

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-5.13`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
