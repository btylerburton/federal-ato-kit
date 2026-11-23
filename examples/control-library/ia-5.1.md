---
title: "IA-5.1 \u2014 Password-based Authentication"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-5.1 — Password-based Authentication

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Password-based authentication applies to passwords regardless of whether they are used in single-factor or multi-factor authentication. Long passwords or passphrases are preferable over shorter passwords. Enforced composition rules provide marginal security benefits while decreasing usability. However, organizations may choose to establish certain rules for password generation (e.g., minimum character length for long passwords) under certain circumstances and can enforce this requirement in IA-5(1)(h). Account recovery can occur, for example, in situations when a password is forgotten. Cryptographically protected passwords include salted one-way cryptographic hashes of passwords. The list of commonly used, compromised, or expected passwords includes passwords obtained from previous breach corpuses, dictionary words, and repetitive or sequential characters. The list includes context-specific words, such as the name of the service, username, and derivatives thereof.

### Requirements and exact statement parts

- `ia-5.1_smt`: For password-based authentication:

- `ia-5.1_smt.a`: Maintain a list of commonly-used, expected, or compromised passwords and update the list [PARAM ia-05.01_odp.01] and when organizational passwords are suspected to have been compromised directly or indirectly;

- `ia-5.1_smt.b`: Verify, when users create or update passwords, that the passwords are not found on the list of commonly-used, expected, or compromised passwords in IA-5(1)(a);

- `ia-5.1_smt.c`: Transmit passwords only over cryptographically-protected channels;

- `ia-5.1_smt.d`: Store passwords using an approved salted key derivation function, preferably using a keyed hash;

- `ia-5.1_smt.e`: Require immediate selection of a new password upon account recovery;

- `ia-5.1_smt.f`: Allow user selection of long passwords and passphrases, including spaces and all printable characters;

- `ia-5.1_smt.g`: Employ automated tools to assist the user in selecting strong password authenticators; and

- `ia-5.1_smt.h`: Enforce the following composition and complexity rules: [PARAM ia-05.01_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-5.1_smt — For password-based authentication:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5.1_smt.a — Maintain a list of commonly-used, expected, or compromised passwords and update the list [PARAM ia-05.01_odp.01] and when organizational passwords are suspected to have been compromised directly or indirectly;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5.1_smt.b — Verify, when users create or update passwords, that the passwords are not found on the list of commonly-used, expected, or compromised passwords in IA-5(1)(a);
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5.1_smt.c — Transmit passwords only over cryptographically-protected channels;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5.1_smt.d — Store passwords using an approved salted key derivation function, preferably using a keyed hash;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5.1_smt.e — Require immediate selection of a new password upon account recovery;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5.1_smt.f — Allow user selection of long passwords and passphrases, including spaces and all printable characters;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5.1_smt.g — Employ automated tools to assist the user in selecting strong password authenticators; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5.1_smt.h — Enforce the following composition and complexity rules: [PARAM ia-05.01_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ia-05.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ia-05.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ia-5.1_smt` — For “For password-based authentication:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5.1_smt.a` — For “Maintain a list of commonly-used, expected, or compromised passwords and update the list [PARAM ia-05.01_odp.01] and when organizational passwords are suspected to have been compromised directly or indirectly;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5.1_smt.b` — For “Verify, when users create or update passwords, that the passwords are not found on the list of commonly-used, expected, or compromised passwords in IA-5(1)(a);”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5.1_smt.c` — For “Transmit passwords only over cryptographically-protected channels;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5.1_smt.d` — For “Store passwords using an approved salted key derivation function, preferably using a keyed hash;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5.1_smt.e` — For “Require immediate selection of a new password upon account recovery;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5.1_smt.f` — For “Allow user selection of long passwords and passphrases, including spaces and all printable characters;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5.1_smt.g` — For “Employ automated tools to assist the user in selecting strong password authenticators; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5.1_smt.h` — For “Enforce the following composition and complexity rules: [PARAM ia-05.01_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ia-05.01_odp.01` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which to update the list of commonly used, expected, or compromised passwords is defined;

- `ia-05.01_odp.02` — What approved value applies to **composition and complexity rules**? Record the value, scope, approving authority, and decision source.

  - Catalog context: authenticator composition and complexity rules are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-5.1_obj.a` (ia-5.1_smt.a): for password-based authentication, a list of commonly used, expected, or compromised passwords is maintained and updated [PARAM ia-05.01_odp.01] and when organizational passwords are suspected to have been compromised directly or indirectly;

- `ia-5.1_obj.b` (ia-5.1_smt.b): for password-based authentication when passwords are created or updated by users, the passwords are verified not to be found on the list of commonly used, expected, or compromised passwords in IA-05(01)(a);

- `ia-5.1_obj.c` (ia-5.1_smt.c): for password-based authentication, passwords are only transmitted over cryptographically protected channels;

- `ia-5.1_obj.d` (ia-5.1_smt.d): for password-based authentication, passwords are stored using an approved salted key derivation function, preferably using a keyed hash;

- `ia-5.1_obj.e` (ia-5.1_smt.e): for password-based authentication, immediate selection of a new password is required upon account recovery;

- `ia-5.1_obj.f` (ia-5.1_smt.f): for password-based authentication, user selection of long passwords and passphrases is allowed, including spaces and all printable characters;

- `ia-5.1_obj.g` (ia-5.1_smt.g): for password-based authentication, automated tools are employed to assist the user in selecting strong password authenticators;

- `ia-5.1_obj.h` (ia-5.1_smt.h): for password-based authentication, [PARAM ia-05.01_odp.02] are enforced.

#### EXAMINE — `ia-5.1_asm-examine`

- Identification and authentication policy

- password policy

- procedures addressing authenticator management

- system security plan

- system design documentation

- system configuration settings and associated documentation

- password configurations and associated documentation

- other relevant documents or records

#### INTERVIEW — `ia-5.1_asm-interview`

- Organizational personnel with authenticator management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `ia-5.1_asm-test`

- Mechanisms supporting and/or implementing password-based authenticator management capability

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-5.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-5`.

- Catalog relationship **related**: `ia-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
