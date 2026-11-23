---
title: "IA-5.8 \u2014 Multiple System Accounts"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-5.8 — Multiple System Accounts

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

When individuals have accounts on multiple systems and use the same authenticators such as passwords, there is the risk that a compromise of one account may lead to the compromise of other accounts. Alternative approaches include having different authenticators (passwords) on all systems, employing a single sign-on or federation mechanism, or using some form of one-time passwords on all systems. Organizations can also use rules of behavior (see PL-4 (catalog reference: `#pl-4`) ) and access agreements (see PS-6 (catalog reference: `#ps-6`) ) to mitigate the risk of multiple system accounts.

### Requirements and exact statement parts

- `ia-5.8_smt`: Implement [PARAM ia-05.08_odp] to manage the risk of compromise due to individuals having accounts on multiple systems.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-5.8_smt — Implement [PARAM ia-05.08_odp] to manage the risk of compromise due to individuals having accounts on multiple systems.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ia-05.08_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ia-5.8_smt` — For “Implement [PARAM ia-05.08_odp] to manage the risk of compromise due to individuals having accounts on multiple systems.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ia-05.08_odp` — What approved value applies to **security controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security controls implemented to manage the risk of compromise due to individuals having accounts on multiple systems are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-5.8_obj` (ia-5.8_smt): [PARAM ia-05.08_odp] are implemented to manage the risk of compromise due to individuals having accounts on multiple systems.

#### EXAMINE — `ia-5.8_asm-examine`

- Identification and authentication policy

- procedures addressing authenticator management

- system security plan

- list of individuals having accounts on multiple systems

- list of security safeguards intended to manage risk of compromise due to individuals having accounts on multiple systems

- other relevant documents or records

#### INTERVIEW — `ia-5.8_asm-interview`

- Organizational personnel with authenticator management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ia-5.8_asm-test`

- Mechanisms supporting and/or implementing safeguards for authenticator management

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-5.8`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-5`.

- Catalog relationship **related**: `ps-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
