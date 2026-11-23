---
title: "IA-5 \u2014 Authenticator Management"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-5 — Authenticator Management

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Authenticators include passwords, cryptographic devices, biometrics, certificates, one-time password devices, and ID badges. Device authenticators include certificates and passwords. Initial authenticator content is the actual content of the authenticator (e.g., the initial password). In contrast, the requirements for authenticator content contain specific criteria or characteristics (e.g., minimum password length). Developers may deliver system components with factory default authentication credentials (i.e., passwords) to allow for initial installation and configuration. Default authentication credentials are often well known, easily discoverable, and present a significant risk. The requirement to protect individual authenticators may be implemented via control PL-4 (catalog reference: `#pl-4`) or PS-6 (catalog reference: `#ps-6`) for authenticators in the possession of individuals and by controls AC-3 (catalog reference: `#ac-3`), AC-6 (catalog reference: `#ac-6`) , and SC-28 (catalog reference: `#sc-28`) for authenticators stored in organizational systems, including passwords stored in hashed or encrypted formats or files containing encrypted or hashed passwords accessible with administrator privileges.

Systems support authenticator management by organization-defined settings and restrictions for various authenticator characteristics (e.g., minimum password length, validation time window for time synchronous one-time tokens, and number of allowed rejections during the verification stage of biometric authentication). Actions can be taken to safeguard individual authenticators, including maintaining possession of authenticators, not sharing authenticators with others, and immediately reporting lost, stolen, or compromised authenticators. Authenticator management includes issuing and revoking authenticators for temporary access when no longer needed.

### Requirements and exact statement parts

- `ia-5_smt`: Manage system authenticators by:

- `ia-5_smt.a`: Verifying, as part of the initial authenticator distribution, the identity of the individual, group, role, service, or device receiving the authenticator;

- `ia-5_smt.b`: Establishing initial authenticator content for any authenticators issued by the organization;

- `ia-5_smt.c`: Ensuring that authenticators have sufficient strength of mechanism for their intended use;

- `ia-5_smt.d`: Establishing and implementing administrative procedures for initial authenticator distribution, for lost or compromised or damaged authenticators, and for revoking authenticators;

- `ia-5_smt.e`: Changing default authenticators prior to first use;

- `ia-5_smt.f`: Changing or refreshing authenticators [PARAM ia-05_odp.01] or when [PARAM ia-05_odp.02] occur;

- `ia-5_smt.g`: Protecting authenticator content from unauthorized disclosure and modification;

- `ia-5_smt.h`: Requiring individuals to take, and having devices implement, specific controls to protect authenticators; and

- `ia-5_smt.i`: Changing authenticators for group or role accounts when membership to those accounts changes.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-5_smt — Manage system authenticators by:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5_smt.a — Verifying, as part of the initial authenticator distribution, the identity of the individual, group, role, service, or device receiving the authenticator;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5_smt.b — Establishing initial authenticator content for any authenticators issued by the organization;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5_smt.c — Ensuring that authenticators have sufficient strength of mechanism for their intended use;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5_smt.d — Establishing and implementing administrative procedures for initial authenticator distribution, for lost or compromised or damaged authenticators, and for revoking authenticators;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5_smt.e — Changing default authenticators prior to first use;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5_smt.f — Changing or refreshing authenticators [PARAM ia-05_odp.01] or when [PARAM ia-05_odp.02] occur;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5_smt.g — Protecting authenticator content from unauthorized disclosure and modification;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5_smt.h — Requiring individuals to take, and having devices implement, specific controls to protect authenticators; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5_smt.i — Changing authenticators for group or role accounts when membership to those accounts changes.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ia-05_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ia-05_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ia-5_smt` — For “Manage system authenticators by:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5_smt.a` — For “Verifying, as part of the initial authenticator distribution, the identity of the individual, group, role, service, or device receiving the authenticator;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5_smt.b` — For “Establishing initial authenticator content for any authenticators issued by the organization;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5_smt.c` — For “Ensuring that authenticators have sufficient strength of mechanism for their intended use;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5_smt.d` — For “Establishing and implementing administrative procedures for initial authenticator distribution, for lost or compromised or damaged authenticators, and for revoking authenticators;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5_smt.e` — For “Changing default authenticators prior to first use;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5_smt.f` — For “Changing or refreshing authenticators [PARAM ia-05_odp.01] or when [PARAM ia-05_odp.02] occur;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5_smt.g` — For “Protecting authenticator content from unauthorized disclosure and modification;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5_smt.h` — For “Requiring individuals to take, and having devices implement, specific controls to protect authenticators; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5_smt.i` — For “Changing authenticators for group or role accounts when membership to those accounts changes.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ia-05_odp.01` — What approved value applies to **time period by authenticator type**? Record the value, scope, approving authority, and decision source.

  - Catalog context: a time period for changing or refreshing authenticators by authenticator type is defined;

- `ia-05_odp.02` — What approved value applies to **events**? Record the value, scope, approving authority, and decision source.

  - Catalog context: events that trigger the change or refreshment of authenticators are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-5_obj.a` (ia-5_smt.a): system authenticators are managed through the verification of the identity of the individual, group, role, service, or device receiving the authenticator as part of the initial authenticator distribution;

- `ia-5_obj.b` (ia-5_smt.b): system authenticators are managed through the establishment of initial authenticator content for any authenticators issued by the organization;

- `ia-5_obj.c` (ia-5_smt.c): system authenticators are managed to ensure that authenticators have sufficient strength of mechanism for their intended use;

- `ia-5_obj.d` (ia-5_smt.d): system authenticators are managed through the establishment and implementation of administrative procedures for initial authenticator distribution; lost, compromised, or damaged authenticators; and the revocation of authenticators;

- `ia-5_obj.e` (ia-5_smt.e): system authenticators are managed through the change of default authenticators prior to first use;

- `ia-5_obj.f` (ia-5_smt.f): system authenticators are managed through the change or refreshment of authenticators [PARAM ia-05_odp.01] or when [PARAM ia-05_odp.02] occur;

- `ia-5_obj.g` (ia-5_smt.g): system authenticators are managed through the protection of authenticator content from unauthorized disclosure and modification;

- `ia-5_obj.h-1` (ia-5_smt.h): system authenticators are managed through the requirement for individuals to take specific controls to protect authenticators;

- `ia-5_obj.h-2` (ia-5_smt.h): system authenticators are managed through the requirement for devices to implement specific controls to protect authenticators;

- `ia-5_obj.i` (ia-5_smt.i): system authenticators are managed through the change of authenticators for group or role accounts when membership to those accounts changes.

#### EXAMINE — `ia-5_asm-examine`

- Identification and authentication policy

- system security plan

- addressing authenticator management

- system design documentation

- system configuration settings and associated documentation

- list of system authenticator types

- change control records associated with managing system authenticators

- system audit records

- other relevant documents or records

#### INTERVIEW — `ia-5_asm-interview`

- Organizational personnel with authenticator management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ia-5_asm-test`

- Mechanisms supporting and/or implementing authenticator management capability

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-5`. The library index records the exact source revision and hash.

- [FIPS 140-3](https://doi.org/10.6028/NIST.FIPS.140-3)

- [FIPS 180-4](https://doi.org/10.6028/NIST.FIPS.180-4)

- [FIPS 201-2](https://doi.org/10.6028/NIST.FIPS.201-2)

- [FIPS 202](https://doi.org/10.6028/NIST.FIPS.202)

- [SP 800-63-3](https://doi.org/10.6028/NIST.SP.800-63-3)

- [SP 800-73-4](https://doi.org/10.6028/NIST.SP.800-73-4)

- [SP 800-76-2](https://doi.org/10.6028/NIST.SP.800-76-2)

- [SP 800-78-4](https://doi.org/10.6028/NIST.SP.800-78-4)

- [IR 7539](https://doi.org/10.6028/NIST.IR.7539)

- [IR 7817](https://doi.org/10.6028/NIST.IR.7817)

- [IR 7849](https://doi.org/10.6028/NIST.IR.7849)

- [IR 7870](https://doi.org/10.6028/NIST.IR.7870)

- [IR 8040](https://doi.org/10.6028/NIST.IR.8040)

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-6`.

- Catalog relationship **related**: `cm-6`.

- Catalog relationship **related**: `ia-2`.

- Catalog relationship **related**: `ia-4`.

- Catalog relationship **related**: `ia-7`.

- Catalog relationship **related**: `ia-8`.

- Catalog relationship **related**: `ia-9`.

- Catalog relationship **related**: `ma-4`.

- Catalog relationship **related**: `pe-2`.

- Catalog relationship **related**: `pl-4`.

- Catalog relationship **related**: `sc-12`.

- Catalog relationship **related**: `sc-13`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
