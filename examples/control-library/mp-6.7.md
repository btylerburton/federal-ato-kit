---
title: "MP-6.7 \u2014 Dual Authorization"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MP-6.7 — Dual Authorization

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations employ dual authorization to help ensure that system media sanitization cannot occur unless two technically qualified individuals conduct the designated task. Individuals who sanitize system media possess sufficient skills and expertise to determine if the proposed sanitization reflects applicable federal and organizational standards, policies, and procedures. Dual authorization also helps to ensure that sanitization occurs as intended, protecting against errors and false claims of having performed the sanitization actions. Dual authorization may also be known as two-person control. To reduce the risk of collusion, organizations consider rotating dual authorization duties to other individuals.

### Requirements and exact statement parts

- `mp-6.7_smt`: Enforce dual authorization for the sanitization of [PARAM mp-06.07_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for mp-6.7_smt — Enforce dual authorization for the sanitization of [PARAM mp-06.07_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter mp-06.07_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `mp-6.7_smt` — For “Enforce dual authorization for the sanitization of [PARAM mp-06.07_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `mp-06.07_odp` — What approved value applies to **system media**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system media to be sanitized using dual authorization is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `mp-6.7_obj` (mp-6.7_smt): dual authorization for sanitization of [PARAM mp-06.07_odp] is enforced.

#### EXAMINE — `mp-6.7_asm-examine`

- System media protection policy

- procedures addressing media sanitization and disposal

- dual authorization policy and procedures

- list of system media requiring dual authorization for sanitization

- authorization records

- media sanitization records

- audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `mp-6.7_asm-interview`

- Organizational personnel with system media sanitization responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `mp-6.7_asm-test`

- Organizational processes requiring dual authorization for media sanitization

- mechanisms supporting and/or implementing media sanitization

- mechanisms supporting and/or implementing dual authorization

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `mp-6.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `mp-6`.

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `mp-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
