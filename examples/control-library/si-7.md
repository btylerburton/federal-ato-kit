---
title: "SI-7 \u2014 Software, Firmware, and Information Integrity"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-7 — Software, Firmware, and Information Integrity

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Unauthorized changes to software, firmware, and information can occur due to errors or malicious activity. Software includes operating systems (with key internal components, such as kernels or drivers), middleware, and applications. Firmware interfaces include Unified Extensible Firmware Interface (UEFI) and Basic Input/Output System (BIOS). Information includes personally identifiable information and metadata that contains security and privacy attributes associated with information. Integrity-checking mechanisms—including parity checks, cyclical redundancy checks, cryptographic hashes, and associated tools—can automatically monitor the integrity of systems and hosted applications.

### Requirements and exact statement parts

- `si-7_smt`: Statement grouping; see child parts.

- `si-7_smt.a`: Employ integrity verification tools to detect unauthorized changes to the following software, firmware, and information: [PARAM si-7_prm_1] ; and

- `si-7_smt.b`: Take the following actions when unauthorized changes to the software, firmware, and information are detected: [PARAM si-7_prm_2].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-7_smt.a — Employ integrity verification tools to detect unauthorized changes to the following software, firmware, and information: [PARAM si-7_prm_1] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-7_smt.b — Take the following actions when unauthorized changes to the software, firmware, and information are detected: [PARAM si-7_prm_2].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-7_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-7_prm_2: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07_odp.05: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07_odp.06: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-7_smt.a` — For “Employ integrity verification tools to detect unauthorized changes to the following software, firmware, and information: [PARAM si-7_prm_1] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-7_smt.b` — For “Take the following actions when unauthorized changes to the software, firmware, and information are detected: [PARAM si-7_prm_2].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-7_prm_1` — What approved value applies to **organization-defined software, firmware, and information**? Record the value, scope, approving authority, and decision source.

- `si-7_prm_2` — What approved value applies to **organization-defined actions**? Record the value, scope, approving authority, and decision source.

- `si-07_odp.01` — What approved value applies to **software**? Record the value, scope, approving authority, and decision source.

  - Catalog context: software requiring integrity verification tools to be employed to detect unauthorized changes is defined;

- `si-07_odp.02` — What approved value applies to **firmware**? Record the value, scope, approving authority, and decision source.

  - Catalog context: firmware requiring integrity verification tools to be employed to detect unauthorized changes is defined;

- `si-07_odp.03` — What approved value applies to **information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: information requiring integrity verification tools to be employed to detect unauthorized changes is defined;

- `si-07_odp.04` — What approved value applies to **actions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: actions to be taken when unauthorized changes to software are detected are defined;

- `si-07_odp.05` — What approved value applies to **actions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: actions to be taken when unauthorized changes to firmware are detected are defined;

- `si-07_odp.06` — What approved value applies to **actions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: actions to be taken when unauthorized changes to information are detected are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-7_obj.a-1` (si-7_smt.a): integrity verification tools are employed to detect unauthorized changes to [PARAM si-07_odp.01];

- `si-7_obj.a-2` (si-7_smt.a): integrity verification tools are employed to detect unauthorized changes to [PARAM si-07_odp.02];

- `si-7_obj.a-3` (si-7_smt.a): integrity verification tools are employed to detect unauthorized changes to [PARAM si-07_odp.03];

- `si-7_obj.b-1` (si-7_smt.b): [PARAM si-07_odp.04] are taken when unauthorized changes to the software, are detected;

- `si-7_obj.b-2` (si-7_smt.b): [PARAM si-07_odp.05] are taken when unauthorized changes to the firmware are detected;

- `si-7_obj.b-3` (si-7_smt.b): [PARAM si-07_odp.06] are taken when unauthorized changes to the information are detected.

#### EXAMINE — `si-7_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing software, firmware, and information integrity

- personally identifiable information processing policy

- system design documentation

- system configuration settings and associated documentation

- integrity verification tools and associated documentation

- records generated or triggered by integrity verification tools regarding unauthorized software, firmware, and information changes

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `si-7_asm-interview`

- Organizational personnel responsible for software, firmware, and/or information integrity

- organizational personnel with information security and privacy responsibilities

- system/network administrators

#### TEST — `si-7_asm-test`

- Software, firmware, and information integrity verification tools

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-7`. The library index records the exact source revision and hash.

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [FIPS 140-3](https://doi.org/10.6028/NIST.FIPS.140-3)

- [FIPS 180-4](https://doi.org/10.6028/NIST.FIPS.180-4)

- [FIPS 186-4](https://doi.org/10.6028/NIST.FIPS.186-4)

- [FIPS 202](https://doi.org/10.6028/NIST.FIPS.202)

- [SP 800-70](https://doi.org/10.6028/NIST.SP.800-70r4)

- [SP 800-147](https://doi.org/10.6028/NIST.SP.800-147)

- Catalog relationship **related**: `ac-4`.

- Catalog relationship **related**: `cm-3`.

- Catalog relationship **related**: `cm-7`.

- Catalog relationship **related**: `cm-8`.

- Catalog relationship **related**: `ma-3`.

- Catalog relationship **related**: `ma-4`.

- Catalog relationship **related**: `ra-5`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sa-9`.

- Catalog relationship **related**: `sa-10`.

- Catalog relationship **related**: `sc-8`.

- Catalog relationship **related**: `sc-12`.

- Catalog relationship **related**: `sc-13`.

- Catalog relationship **related**: `sc-28`.

- Catalog relationship **related**: `sc-37`.

- Catalog relationship **related**: `si-3`.

- Catalog relationship **related**: `sr-3`.

- Catalog relationship **related**: `sr-4`.

- Catalog relationship **related**: `sr-5`.

- Catalog relationship **related**: `sr-6`.

- Catalog relationship **related**: `sr-9`.

- Catalog relationship **related**: `sr-10`.

- Catalog relationship **related**: `sr-11`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
