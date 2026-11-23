---
title: "AC-4.9 \u2014 Human Reviews"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4.9 — Human Reviews

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations define security or privacy policy filters for all situations where automated flow control decisions are possible. When a fully automated flow control decision is not possible, then a human review may be employed in lieu of or as a complement to automated security or privacy policy filtering. Human reviews may also be employed as deemed necessary by organizations.

### Requirements and exact statement parts

- `ac-4.9_smt`: Enforce the use of human reviews for [PARAM ac-04.09_odp.01] under the following conditions: [PARAM ac-04.09_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4.9_smt — Enforce the use of human reviews for [PARAM ac-04.09_odp.01] under the following conditions: [PARAM ac-04.09_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-04.09_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.09_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-4.9_smt` — For “Enforce the use of human reviews for [PARAM ac-04.09_odp.01] under the following conditions: [PARAM ac-04.09_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-04.09_odp.01` — What approved value applies to **information flows**? Record the value, scope, approving authority, and decision source.

  - Catalog context: information flows requiring the use of human reviews are defined;

- `ac-04.09_odp.02` — What approved value applies to **conditions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: conditions under which the use of human reviews for information flows are to be enforced are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4.9_obj` (ac-4.9_smt): human reviews are used for [PARAM ac-04.09_odp.01] under [PARAM ac-04.09_odp.02].

#### EXAMINE — `ac-4.9_asm-examine`

- Access control policy

- information flow control policies

- procedures addressing information flow enforcement

- system design documentation

- system configuration settings and associated documentation

- records of human reviews regarding information flows

- list of information flows requiring the use of human reviews

- list of conditions requiring human reviews for information flows

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ac-4.9_asm-interview`

- System/network administrators

- organizational personnel with information security and privacy responsibilities

- organizational personnel with information flow enforcement responsibilities

- system developers

#### TEST — `ac-4.9_asm-test`

- Mechanisms enforcing the use of human reviews

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4.9`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
