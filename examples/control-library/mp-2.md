---
title: "MP-2 \u2014 Media Access"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MP-2 — Media Access

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

System media includes digital and non-digital media. Digital media includes flash drives, diskettes, magnetic tapes, external or removable hard disk drives (e.g., solid state, magnetic), compact discs, and digital versatile discs. Non-digital media includes paper and microfilm. Denying access to patient medical records in a community hospital unless the individuals seeking access to such records are authorized healthcare providers is an example of restricting access to non-digital media. Limiting access to the design specifications stored on compact discs in the media library to individuals on the system development team is an example of restricting access to digital media.

### Requirements and exact statement parts

- `mp-2_smt`: Restrict access to [PARAM mp-2_prm_1] to [PARAM mp-2_prm_2].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for mp-2_smt — Restrict access to [PARAM mp-2_prm_1] to [PARAM mp-2_prm_2].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter mp-2_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-2_prm_2: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-02_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-02_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `mp-2_smt` — For “Restrict access to [PARAM mp-2_prm_1] to [PARAM mp-2_prm_2].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `mp-2_prm_1` — What approved value applies to **organization-defined types of digital and/or non-digital media**? Record the value, scope, approving authority, and decision source.

- `mp-2_prm_2` — What approved value applies to **organization-defined personnel or roles**? Record the value, scope, approving authority, and decision source.

- `mp-02_odp.01` — What approved value applies to **types of digital media**? Record the value, scope, approving authority, and decision source.

  - Catalog context: types of digital media to which access is restricted are defined;

- `mp-02_odp.02` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles authorized to access digital media is/are defined;

- `mp-02_odp.03` — What approved value applies to **types of non-digital media**? Record the value, scope, approving authority, and decision source.

  - Catalog context: types of non-digital media to which access is restricted are defined;

- `mp-02_odp.04` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles authorized to access non-digital media is/are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `mp-2_obj-1` (mp-2_smt): access to [PARAM mp-02_odp.01] is restricted to [PARAM mp-02_odp.02];

- `mp-2_obj-2` (mp-2_smt): access to [PARAM mp-02_odp.03] is restricted to [PARAM mp-02_odp.04].

#### EXAMINE — `mp-2_asm-examine`

- System media protection policy

- procedures addressing media access restrictions

- access control policy and procedures

- physical and environmental protection policy and procedures

- media storage facilities

- access control records

- system security plan

- other relevant documents or records

#### INTERVIEW — `mp-2_asm-interview`

- Organizational personnel with system media protection responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `mp-2_asm-test`

- Organizational processes for restricting information media

- mechanisms supporting and/or implementing media access restrictions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `mp-2`. The library index records the exact source revision and hash.

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [FIPS 199](https://doi.org/10.6028/NIST.FIPS.199)

- [SP 800-111](https://doi.org/10.6028/NIST.SP.800-111)

- Catalog relationship **related**: `ac-19`.

- Catalog relationship **related**: `au-9`.

- Catalog relationship **related**: `cp-2`.

- Catalog relationship **related**: `cp-9`.

- Catalog relationship **related**: `cp-10`.

- Catalog relationship **related**: `ma-5`.

- Catalog relationship **related**: `mp-4`.

- Catalog relationship **related**: `mp-6`.

- Catalog relationship **related**: `pe-2`.

- Catalog relationship **related**: `pe-3`.

- Catalog relationship **related**: `sc-12`.

- Catalog relationship **related**: `sc-13`.

- Catalog relationship **related**: `sc-34`.

- Catalog relationship **related**: `si-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
