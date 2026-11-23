---
title: "AC-3.8 \u2014 Revocation of Access Authorizations"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-3.8 — Revocation of Access Authorizations

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Revocation of access rules may differ based on the types of access revoked. For example, if a subject (i.e., user or process acting on behalf of a user) is removed from a group, access may not be revoked until the next time the object is opened or the next time the subject attempts to access the object. Revocation based on changes to security labels may take effect immediately. Organizations provide alternative approaches on how to make revocations immediate if systems cannot provide such capability and immediate revocation is necessary.

### Requirements and exact statement parts

- `ac-3.8_smt`: Enforce the revocation of access authorizations resulting from changes to the security attributes of subjects and objects based on [PARAM ac-03.08_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-3.8_smt — Enforce the revocation of access authorizations resulting from changes to the security attributes of subjects and objects based on [PARAM ac-03.08_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-03.08_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-3.8_smt` — For “Enforce the revocation of access authorizations resulting from changes to the security attributes of subjects and objects based on [PARAM ac-03.08_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-03.08_odp` — What approved value applies to **rules**? Record the value, scope, approving authority, and decision source.

  - Catalog context: rules governing the timing of revocations of access authorizations are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-3.8_obj-1` (ac-3.8_smt): revocation of access authorizations is enforced, resulting from changes to the security attributes of subjects based on [PARAM ac-03.08_odp];

- `ac-3.8_obj-2` (ac-3.8_smt): revocation of access authorizations is enforced resulting from changes to the security attributes of objects based on [PARAM ac-03.08_odp].

#### EXAMINE — `ac-3.8_asm-examine`

- Access control policy

- procedures addressing access enforcement

- system design documentation

- system configuration settings and associated documentation

- rules governing revocation of access authorizations, system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-3.8_asm-interview`

- Organizational personnel with access enforcement responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

- system developers

#### TEST — `ac-3.8_asm-test`

- Mechanisms implementing access enforcement functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-3.8`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
