---
title: "MA-3.3 \u2014 Prevent Unauthorized Removal"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-3.3 — Prevent Unauthorized Removal

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizational information includes all information owned by organizations and any information provided to organizations for which the organizations serve as information stewards.

### Requirements and exact statement parts

- `ma-3.3_smt`: Prevent the removal of maintenance equipment containing organizational information by:

- `ma-3.3_smt.a`: Verifying that there is no organizational information contained on the equipment;

- `ma-3.3_smt.b`: Sanitizing or destroying the equipment;

- `ma-3.3_smt.c`: Retaining the equipment within the facility; or

- `ma-3.3_smt.d`: Obtaining an exemption from [PARAM ma-03.03_odp] explicitly authorizing removal of the equipment from the facility.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-3.3_smt — Prevent the removal of maintenance equipment containing organizational information by:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-3.3_smt.a — Verifying that there is no organizational information contained on the equipment;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-3.3_smt.b — Sanitizing or destroying the equipment;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-3.3_smt.c — Retaining the equipment within the facility; or
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-3.3_smt.d — Obtaining an exemption from [PARAM ma-03.03_odp] explicitly authorizing removal of the equipment from the facility.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ma-03.03_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ma-3.3_smt` — For “Prevent the removal of maintenance equipment containing organizational information by:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-3.3_smt.a` — For “Verifying that there is no organizational information contained on the equipment;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-3.3_smt.b` — For “Sanitizing or destroying the equipment;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-3.3_smt.c` — For “Retaining the equipment within the facility; or”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-3.3_smt.d` — For “Obtaining an exemption from [PARAM ma-03.03_odp] explicitly authorizing removal of the equipment from the facility.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ma-03.03_odp` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles who can authorize removal of equipment from the facility is/are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-3.3_obj.a` (ma-3.3_smt.a): the removal of maintenance equipment containing organizational information is prevented by verifying that there is no organizational information contained on the equipment; or

- `ma-3.3_obj.b` (ma-3.3_smt.b): the removal of maintenance equipment containing organizational information is prevented by sanitizing or destroying the equipment; or

- `ma-3.3_obj.c` (ma-3.3_smt.c): the removal of maintenance equipment containing organizational information is prevented by retaining the equipment within the facility; or

- `ma-3.3_obj.d` (ma-3.3_smt.d): the removal of maintenance equipment containing organizational information is prevented by obtaining an exemption from [PARAM ma-03.03_odp] explicitly authorizing removal of the equipment from the facility.

#### EXAMINE — `ma-3.3_asm-examine`

- Maintenance policy

- procedures addressing system maintenance tools

- system maintenance tools and associated documentation

- maintenance records

- equipment sanitization records

- media sanitization records

- exemptions for equipment removal

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-3.3_asm-interview`

- Organizational personnel with system maintenance responsibilities

- organizational personnel with information security responsibilities

- organizational personnel responsible for media sanitization

#### TEST — `ma-3.3_asm-test`

- Organizational process for preventing unauthorized removal of information

- mechanisms supporting media sanitization or destruction of equipment

- mechanisms supporting verification of media sanitization

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-3.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ma-3`.

- Catalog relationship **related**: `mp-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
