---
title: "IA-2 \u2014 Identification and Authentication (Organizational Users)"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-2 — Identification and Authentication (Organizational Users)

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations can satisfy the identification and authentication requirements by complying with the requirements in HSPD 12 (catalog reference: `#f16e438e-7114-4144-bfe2-2dfcad8cb2d0`) . Organizational users include employees or individuals who organizations consider to have an equivalent status to employees (e.g., contractors and guest researchers). Unique identification and authentication of users applies to all accesses other than those that are explicitly identified in AC-14 (catalog reference: `#ac-14`) and that occur through the authorized use of group authenticators without individual authentication. Since processes execute on behalf of groups and roles, organizations may require unique identification of individuals in group accounts or for detailed accountability of individual activity.

Organizations employ passwords, physical authenticators, or biometrics to authenticate user identities or, in the case of multi-factor authentication, some combination thereof. Access to organizational systems is defined as either local access or network access. Local access is any access to organizational systems by users or processes acting on behalf of users, where access is obtained through direct connections without the use of networks. Network access is access to organizational systems by users (or processes acting on behalf of users) where access is obtained through network connections (i.e., nonlocal accesses). Remote access is a type of network access that involves communication through external networks. Internal networks include local area networks and wide area networks.

The use of encrypted virtual private networks for network connections between organization-controlled endpoints and non-organization-controlled endpoints may be treated as internal networks with respect to protecting the confidentiality and integrity of information traversing the network. Identification and authentication requirements for non-organizational users are described in IA-8 (catalog reference: `#ia-8`).

### Requirements and exact statement parts

- `ia-2_smt`: Uniquely identify and authenticate organizational users and associate that unique identification with processes acting on behalf of those users.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-2_smt — Uniquely identify and authenticate organizational users and associate that unique identification with processes acting on behalf of those users.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ia-2_smt` — For “Uniquely identify and authenticate organizational users and associate that unique identification with processes acting on behalf of those users.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-2_obj-1` (ia-2_smt): organizational users are uniquely identified and authenticated;

- `ia-2_obj-2` (ia-2_smt): the unique identification of authenticated organizational users is associated with processes acting on behalf of those users.

#### EXAMINE — `ia-2_asm-examine`

- Identification and authentication policy

- procedures addressing user identification and authentication

- system security plan, system design documentation

- system configuration settings and associated documentation

- system audit records

- list of system accounts

- other relevant documents or records

#### INTERVIEW — `ia-2_asm-interview`

- Organizational personnel with system operations responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- organizational personnel with account management responsibilities

- system developers

#### TEST — `ia-2_asm-test`

- Organizational processes for uniquely identifying and authenticating users

- mechanisms supporting and/or implementing identification and authentication capabilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-2`. The library index records the exact source revision and hash.

- [FIPS 140-3](https://doi.org/10.6028/NIST.FIPS.140-3)

- [FIPS 201-2](https://doi.org/10.6028/NIST.FIPS.201-2)

- [FIPS 202](https://doi.org/10.6028/NIST.FIPS.202)

- [SP 800-63-3](https://doi.org/10.6028/NIST.SP.800-63-3)

- [SP 800-73-4](https://doi.org/10.6028/NIST.SP.800-73-4)

- [SP 800-76-2](https://doi.org/10.6028/NIST.SP.800-76-2)

- [SP 800-78-4](https://doi.org/10.6028/NIST.SP.800-78-4)

- [SP 800-79-2](https://doi.org/10.6028/NIST.SP.800-79-2)

- [SP 800-156](https://doi.org/10.6028/NIST.SP.800-156)

- [SP 800-166](https://doi.org/10.6028/NIST.SP.800-166)

- [IR 7539](https://doi.org/10.6028/NIST.IR.7539)

- [IR 7676](https://doi.org/10.6028/NIST.IR.7676)

- [IR 7817](https://doi.org/10.6028/NIST.IR.7817)

- [IR 7849](https://doi.org/10.6028/NIST.IR.7849)

- [IR 7870](https://doi.org/10.6028/NIST.IR.7870)

- [IR 7874](https://doi.org/10.6028/NIST.IR.7874)

- [IR 7966](https://doi.org/10.6028/NIST.IR.7966)

- Catalog relationship **related**: `ac-2`.

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-4`.

- Catalog relationship **related**: `ac-14`.

- Catalog relationship **related**: `ac-17`.

- Catalog relationship **related**: `ac-18`.

- Catalog relationship **related**: `au-1`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `ia-4`.

- Catalog relationship **related**: `ia-5`.

- Catalog relationship **related**: `ia-8`.

- Catalog relationship **related**: `ia-13`.

- Catalog relationship **related**: `ma-4`.

- Catalog relationship **related**: `ma-5`.

- Catalog relationship **related**: `pe-2`.

- Catalog relationship **related**: `pl-4`.

- Catalog relationship **related**: `sa-4`.

- Catalog relationship **related**: `sa-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
