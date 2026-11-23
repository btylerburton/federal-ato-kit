---
title: "CP-9 \u2014 System Backup"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-9 — System Backup

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

System-level information includes system state information, operating system software, middleware, application software, and licenses. User-level information includes information other than system-level information. Mechanisms employed to protect the integrity of system backups include digital signatures and cryptographic hashes. Protection of system backup information while in transit is addressed by MP-5 (catalog reference: `#mp-5`) and SC-8 (catalog reference: `#sc-8`) . System backups reflect the requirements in contingency plans as well as other organizational requirements for backing up information. Organizations may be subject to laws, executive orders, directives, regulations, or policies with requirements regarding specific categories of information (e.g., personal health information). Organizational personnel consult with the senior agency official for privacy and legal counsel regarding such requirements.

### Requirements and exact statement parts

- `cp-9_smt`: Statement grouping; see child parts.

- `cp-9_smt.a`: Conduct backups of user-level information contained in [PARAM cp-09_odp.01] [PARAM cp-09_odp.02];

- `cp-9_smt.b`: Conduct backups of system-level information contained in the system [PARAM cp-09_odp.03];

- `cp-9_smt.c`: Conduct backups of system documentation, including security- and privacy-related documentation [PARAM cp-09_odp.04] ; and

- `cp-9_smt.d`: Protect the confidentiality, integrity, and availability of backup information.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-9_smt.a — Conduct backups of user-level information contained in [PARAM cp-09_odp.01] [PARAM cp-09_odp.02];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-9_smt.b — Conduct backups of system-level information contained in the system [PARAM cp-09_odp.03];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-9_smt.c — Conduct backups of system documentation, including security- and privacy-related documentation [PARAM cp-09_odp.04] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cp-9_smt.d — Protect the confidentiality, integrity, and availability of backup information.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cp-09_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-09_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-09_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-09_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cp-9_smt.a` — For “Conduct backups of user-level information contained in [PARAM cp-09_odp.01] [PARAM cp-09_odp.02];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-9_smt.b` — For “Conduct backups of system-level information contained in the system [PARAM cp-09_odp.03];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-9_smt.c` — For “Conduct backups of system documentation, including security- and privacy-related documentation [PARAM cp-09_odp.04] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cp-9_smt.d` — For “Protect the confidentiality, integrity, and availability of backup information.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cp-09_odp.01` — What approved value applies to **system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system components for which to conduct backups of user-level information is defined;

- `cp-09_odp.02` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to conduct backups of user-level information consistent with recovery time and recovery point objectives is defined;

- `cp-09_odp.03` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to conduct backups of system-level information consistent with recovery time and recovery point objectives is defined;

- `cp-09_odp.04` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to conduct backups of system documentation consistent with recovery time and recovery point objectives is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-9_obj.a` (cp-9_smt.a): backups of user-level information contained in [PARAM cp-09_odp.01] are conducted [PARAM cp-09_odp.02];

- `cp-9_obj.b` (cp-9_smt.b): backups of system-level information contained in the system are conducted [PARAM cp-09_odp.03];

- `cp-9_obj.c` (cp-9_smt.c): backups of system documentation, including security- and privacy-related documentation are conducted [PARAM cp-09_odp.04];

- `cp-9_obj.d-1` (cp-9_smt.d): the confidentiality of backup information is protected;

- `cp-9_obj.d-2` (cp-9_smt.d): the integrity of backup information is protected;

- `cp-9_obj.d-3` (cp-9_smt.d): the availability of backup information is protected.

#### EXAMINE — `cp-9_asm-examine`

- Contingency planning policy

- procedures addressing system backup

- contingency plan

- backup storage location(s)

- system backup logs or records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `cp-9_asm-interview`

- Organizational personnel with system backup responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `cp-9_asm-test`

- Organizational processes for conducting system backups

- mechanisms supporting and/or implementing system backups

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-9`. The library index records the exact source revision and hash.

- [FIPS 140-3](https://doi.org/10.6028/NIST.FIPS.140-3)

- [FIPS 186-4](https://doi.org/10.6028/NIST.FIPS.186-4)

- [SP 800-34](https://doi.org/10.6028/NIST.SP.800-34r1)

- [SP 800-130](https://doi.org/10.6028/NIST.SP.800-130)

- [SP 800-152](https://doi.org/10.6028/NIST.SP.800-152)

- Catalog relationship **related**: `cp-2`.

- Catalog relationship **related**: `cp-6`.

- Catalog relationship **related**: `cp-10`.

- Catalog relationship **related**: `mp-4`.

- Catalog relationship **related**: `mp-5`.

- Catalog relationship **related**: `sc-8`.

- Catalog relationship **related**: `sc-12`.

- Catalog relationship **related**: `sc-13`.

- Catalog relationship **related**: `si-4`.

- Catalog relationship **related**: `si-13`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
