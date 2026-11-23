---
title: "PS-3 \u2014 Personnel Screening"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PS-3 — Personnel Screening

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Personnel screening and rescreening activities reflect applicable laws, executive orders, directives, regulations, policies, standards, guidelines, and specific criteria established for the risk designations of assigned positions. Examples of personnel screening include background investigations and agency checks. Organizations may define different rescreening conditions and frequencies for personnel accessing systems based on types of information processed, stored, or transmitted by the systems.

### Requirements and exact statement parts

- `ps-3_smt`: Statement grouping; see child parts.

- `ps-3_smt.a`: Screen individuals prior to authorizing access to the system; and

- `ps-3_smt.b`: Rescreen individuals in accordance with [PARAM ps-3_prm_1].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ps-3_smt.a — Screen individuals prior to authorizing access to the system; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ps-3_smt.b — Rescreen individuals in accordance with [PARAM ps-3_prm_1].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ps-3_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ps-03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ps-03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ps-3_smt.a` — For “Screen individuals prior to authorizing access to the system; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ps-3_smt.b` — For “Rescreen individuals in accordance with [PARAM ps-3_prm_1].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ps-3_prm_1` — What approved value applies to **organization-defined conditions requiring rescreening and, where rescreening is so indicated, the frequency of rescreening**? Record the value, scope, approving authority, and decision source.

- `ps-03_odp.01` — What approved value applies to **conditions requiring rescreening**? Record the value, scope, approving authority, and decision source.

  - Catalog context: conditions requiring rescreening of individuals are defined;

- `ps-03_odp.02` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency of rescreening individuals where it is so indicated is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ps-3_obj.a` (ps-3_smt.a): individuals are screened prior to authorizing access to the system;

- `ps-3_obj.b-1` (ps-3_smt.b): individuals are rescreened in accordance with [PARAM ps-03_odp.01];

- `ps-3_obj.b-2` (ps-3_smt.b): where rescreening is so indicated, individuals are rescreened [PARAM ps-03_odp.02].

#### EXAMINE — `ps-3_asm-examine`

- Personnel security policy

- procedures addressing personnel screening

- records of screened personnel

- system security plan

- other relevant documents or records

#### INTERVIEW — `ps-3_asm-interview`

- Organizational personnel with personnel security responsibilities

- organizational personnel with information security responsibilities

#### TEST — `ps-3_asm-test`

- Organizational processes for personnel screening

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ps-3`. The library index records the exact source revision and hash.

- [EO 13526](https://www.archives.gov/isoo/policy-documents/cnsi-eo.html)

- [EO 13587](https://obamawhitehouse.archives.gov/the-press-office/2011/10/07/executive-order-13587-structural-reforms-improve-security-classified-net)

- [FIPS 199](https://doi.org/10.6028/NIST.FIPS.199)

- [FIPS 201-2](https://doi.org/10.6028/NIST.FIPS.201-2)

- [SP 800-60-1](https://doi.org/10.6028/NIST.SP.800-60v1r1)

- [SP 800-60-2](https://doi.org/10.6028/NIST.SP.800-60v2r1)

- [SP 800-73-4](https://doi.org/10.6028/NIST.SP.800-73-4)

- [SP 800-76-2](https://doi.org/10.6028/NIST.SP.800-76-2)

- [SP 800-78-4](https://doi.org/10.6028/NIST.SP.800-78-4)

- Catalog relationship **related**: `ac-2`.

- Catalog relationship **related**: `ia-4`.

- Catalog relationship **related**: `ma-5`.

- Catalog relationship **related**: `pe-2`.

- Catalog relationship **related**: `pm-12`.

- Catalog relationship **related**: `ps-2`.

- Catalog relationship **related**: `ps-6`.

- Catalog relationship **related**: `ps-7`.

- Catalog relationship **related**: `sa-21`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
