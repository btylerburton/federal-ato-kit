---
title: "MP-6 \u2014 Media Sanitization"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MP-6 — Media Sanitization

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Media sanitization applies to all digital and non-digital system media subject to disposal or reuse, whether or not the media is considered removable. Examples include digital media in scanners, copiers, printers, notebook computers, workstations, network components, mobile devices, and non-digital media (e.g., paper and microfilm). The sanitization process removes information from system media such that the information cannot be retrieved or reconstructed. Sanitization techniques—including clearing, purging, cryptographic erase, de-identification of personally identifiable information, and destruction—prevent the disclosure of information to unauthorized individuals when such media is reused or released for disposal. Organizations determine the appropriate sanitization methods, recognizing that destruction is sometimes necessary when other methods cannot be applied to media requiring sanitization. Organizations use discretion on the employment of approved sanitization techniques and procedures for media that contains information deemed to be in the public domain or publicly releasable or information deemed to have no adverse impact on organizations or individuals if released for reuse or disposal. Sanitization of non-digital media includes destruction, removing a classified appendix from an otherwise unclassified document, or redacting selected sections or words from a document by obscuring the redacted sections or words in a manner equivalent in effectiveness to removing them from the document. NSA standards and policies control the sanitization process for media that contains classified information. NARA policies control the sanitization process for controlled unclassified information.

### Requirements and exact statement parts

- `mp-6_smt`: Statement grouping; see child parts.

- `mp-6_smt.a`: Sanitize [PARAM mp-6_prm_1] prior to disposal, release out of organizational control, or release for reuse using [PARAM mp-6_prm_2] ; and

- `mp-6_smt.b`: Employ sanitization mechanisms with the strength and integrity commensurate with the security category or classification of the information.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for mp-6_smt.a — Sanitize [PARAM mp-6_prm_1] prior to disposal, release out of organizational control, or release for reuse using [PARAM mp-6_prm_2] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for mp-6_smt.b — Employ sanitization mechanisms with the strength and integrity commensurate with the security category or classification of the information.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter mp-6_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-6_prm_2: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-06_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-06_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-06_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-06_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-06_odp.05: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-06_odp.06: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `mp-6_smt.a` — For “Sanitize [PARAM mp-6_prm_1] prior to disposal, release out of organizational control, or release for reuse using [PARAM mp-6_prm_2] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `mp-6_smt.b` — For “Employ sanitization mechanisms with the strength and integrity commensurate with the security category or classification of the information.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `mp-6_prm_1` — What approved value applies to **organization-defined system media**? Record the value, scope, approving authority, and decision source.

- `mp-6_prm_2` — What approved value applies to **organization-defined sanitization techniques and procedures**? Record the value, scope, approving authority, and decision source.

- `mp-06_odp.01` — What approved value applies to **system media**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system media to be sanitized prior to disposal is defined;

- `mp-06_odp.02` — What approved value applies to **system media**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system media to be sanitized prior to release from organizational control is defined;

- `mp-06_odp.03` — What approved value applies to **system media**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system media to be sanitized prior to release for reuse is defined;

- `mp-06_odp.04` — What approved value applies to **sanitization techniques and procedures**? Record the value, scope, approving authority, and decision source.

  - Catalog context: sanitization techniques and procedures to be used for sanitization prior to disposal are defined;

- `mp-06_odp.05` — What approved value applies to **sanitization techniques and procedures**? Record the value, scope, approving authority, and decision source.

  - Catalog context: sanitization techniques and procedures to be used for sanitization prior to release from organizational control are defined;

- `mp-06_odp.06` — What approved value applies to **sanitization techniques and procedures**? Record the value, scope, approving authority, and decision source.

  - Catalog context: sanitization techniques and procedures to be used for sanitization prior to release for reuse are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `mp-6_obj.a-1` (mp-6_smt.a): [PARAM mp-06_odp.01] is sanitized using [PARAM mp-06_odp.04] prior to disposal;

- `mp-6_obj.a-2` (mp-6_smt.a): [PARAM mp-06_odp.02] is sanitized using [PARAM mp-06_odp.05] prior to release from organizational control;

- `mp-6_obj.a-3` (mp-6_smt.a): [PARAM mp-06_odp.03] is sanitized using [PARAM mp-06_odp.06] prior to release for reuse;

- `mp-6_obj.b` (mp-6_smt.b): sanitization mechanisms with strength and integrity commensurate with the security category or classification of the information are employed.

#### EXAMINE — `mp-6_asm-examine`

- System media protection policy

- procedures addressing media sanitization and disposal

- applicable federal standards and policies addressing media sanitization policy

- media sanitization records

- system audit records

- system design documentation

- records retention and disposition policy

- records retention and disposition procedures

- system configuration settings and associated documentation

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `mp-6_asm-interview`

- Organizational personnel with media sanitization responsibilities

- organizational personnel with records retention and disposition responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

#### TEST — `mp-6_asm-test`

- Organizational processes for media sanitization

- mechanisms supporting and/or implementing media sanitization

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `mp-6`. The library index records the exact source revision and hash.

- [32 CFR 2002](https://www.federalregister.gov/documents/2016/09/14/2016-21665/controlled-unclassified-information)

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [NARA CUI](https://www.archives.gov/cui)

- [FIPS 199](https://doi.org/10.6028/NIST.FIPS.199)

- [SP 800-60-1](https://doi.org/10.6028/NIST.SP.800-60v1r1)

- [SP 800-60-2](https://doi.org/10.6028/NIST.SP.800-60v2r1)

- [SP 800-88](https://doi.org/10.6028/NIST.SP.800-88r1)

- [SP 800-124](https://doi.org/10.6028/NIST.SP.800-124r1)

- [IR 8023](https://doi.org/10.6028/NIST.IR.8023)

- [NSA MEDIA](https://www.nsa.gov/resources/everyone/media-destruction)

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-7`.

- Catalog relationship **related**: `au-11`.

- Catalog relationship **related**: `ma-2`.

- Catalog relationship **related**: `ma-3`.

- Catalog relationship **related**: `ma-4`.

- Catalog relationship **related**: `ma-5`.

- Catalog relationship **related**: `pm-22`.

- Catalog relationship **related**: `si-12`.

- Catalog relationship **related**: `si-18`.

- Catalog relationship **related**: `si-19`.

- Catalog relationship **related**: `sr-11`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
