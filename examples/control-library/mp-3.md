---
title: "MP-3 \u2014 Media Marking"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MP-3 — Media Marking

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Security marking refers to the application or use of human-readable security attributes. Digital media includes diskettes, magnetic tapes, external or removable hard disk drives (e.g., solid state, magnetic), flash drives, compact discs, and digital versatile discs. Non-digital media includes paper and microfilm. Controlled unclassified information is defined by the National Archives and Records Administration along with the appropriate safeguarding and dissemination requirements for such information and is codified in 32 CFR 2002 (catalog reference: `#91f992fb-f668-4c91-a50f-0f05b95ccee3`) . Security markings are generally not required for media that contains information determined by organizations to be in the public domain or to be publicly releasable. Some organizations may require markings for public information indicating that the information is publicly releasable. System media marking reflects applicable laws, executive orders, directives, policies, regulations, standards, and guidelines.

### Requirements and exact statement parts

- `mp-3_smt`: Statement grouping; see child parts.

- `mp-3_smt.a`: Mark system media indicating the distribution limitations, handling caveats, and applicable security markings (if any) of the information; and

- `mp-3_smt.b`: Exempt [PARAM mp-03_odp.01] from marking if the media remain within [PARAM mp-03_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for mp-3_smt.a — Mark system media indicating the distribution limitations, handling caveats, and applicable security markings (if any) of the information; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for mp-3_smt.b — Exempt [PARAM mp-03_odp.01] from marking if the media remain within [PARAM mp-03_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter mp-03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `mp-3_smt.a` — For “Mark system media indicating the distribution limitations, handling caveats, and applicable security markings (if any) of the information; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `mp-3_smt.b` — For “Exempt [PARAM mp-03_odp.01] from marking if the media remain within [PARAM mp-03_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `mp-03_odp.01` — What approved value applies to **types of media exempted from marking**? Record the value, scope, approving authority, and decision source.

  - Catalog context: types of system media exempt from marking when remaining in controlled areas are defined;

- `mp-03_odp.02` — What approved value applies to **controlled areas**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controlled areas where media is exempt from marking are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `mp-3_obj.a` (mp-3_smt.a): system media is marked to indicate distribution limitations, handling caveats, and applicable security markings (if any) of the information;

- `mp-3_obj.b` (mp-3_smt.b): [PARAM mp-03_odp.01] remain within [PARAM mp-03_odp.02].

#### EXAMINE — `mp-3_asm-examine`

- System media protection policy

- procedures addressing media marking

- physical and environmental protection policy and procedures

- list of system media marking security attributes

- designated controlled areas

- system security plan

- other relevant documents or records

#### INTERVIEW — `mp-3_asm-interview`

- Organizational personnel with system media protection and marking responsibilities

- organizational personnel with information security responsibilities

#### TEST — `mp-3_asm-test`

- Organizational processes for marking information media

- mechanisms supporting and/or implementing media marking

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `mp-3`. The library index records the exact source revision and hash.

- [EO 13556](https://obamawhitehouse.archives.gov/the-press-office/2010/11/04/executive-order-13556-controlled-unclassified-information)

- [32 CFR 2002](https://www.federalregister.gov/documents/2016/09/14/2016-21665/controlled-unclassified-information)

- [FIPS 199](https://doi.org/10.6028/NIST.FIPS.199)

- Catalog relationship **related**: `ac-16`.

- Catalog relationship **related**: `cp-9`.

- Catalog relationship **related**: `mp-5`.

- Catalog relationship **related**: `pe-22`.

- Catalog relationship **related**: `si-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
