---
title: "MA-5 \u2014 Maintenance Personnel"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-5 — Maintenance Personnel

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Maintenance personnel refers to individuals who perform hardware or software maintenance on organizational systems, while PE-2 (catalog reference: `#pe-2`) addresses physical access for individuals whose maintenance duties place them within the physical protection perimeter of the systems. Technical competence of supervising individuals relates to the maintenance performed on the systems, while having required access authorizations refers to maintenance on and near the systems. Individuals not previously identified as authorized maintenance personnel—such as information technology manufacturers, vendors, systems integrators, and consultants—may require privileged access to organizational systems, such as when they are required to conduct maintenance activities with little or no notice. Based on organizational assessments of risk, organizations may issue temporary credentials to these individuals. Temporary credentials may be for one-time use or for very limited time periods.

### Requirements and exact statement parts

- `ma-5_smt`: Statement grouping; see child parts.

- `ma-5_smt.a`: Establish a process for maintenance personnel authorization and maintain a list of authorized maintenance organizations or personnel;

- `ma-5_smt.b`: Verify that non-escorted personnel performing maintenance on the system possess the required access authorizations; and

- `ma-5_smt.c`: Designate organizational personnel with required access authorizations and technical competence to supervise the maintenance activities of personnel who do not possess the required access authorizations.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-5_smt.a — Establish a process for maintenance personnel authorization and maintain a list of authorized maintenance organizations or personnel;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-5_smt.b — Verify that non-escorted personnel performing maintenance on the system possess the required access authorizations; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-5_smt.c — Designate organizational personnel with required access authorizations and technical competence to supervise the maintenance activities of personnel who do not possess the required access authorizations.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ma-5_smt.a` — For “Establish a process for maintenance personnel authorization and maintain a list of authorized maintenance organizations or personnel;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-5_smt.b` — For “Verify that non-escorted personnel performing maintenance on the system possess the required access authorizations; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-5_smt.c` — For “Designate organizational personnel with required access authorizations and technical competence to supervise the maintenance activities of personnel who do not possess the required access authorizations.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-5_obj.a-1` (ma-5_smt.a): a process for maintenance personnel authorization is established;

- `ma-5_obj.a-2` (ma-5_smt.a): a list of authorized maintenance organizations or personnel is maintained;

- `ma-5_obj.b` (ma-5_smt.b): non-escorted personnel performing maintenance on the system possess the required access authorizations;

- `ma-5_obj.c` (ma-5_smt.c): organizational personnel with required access authorizations and technical competence is/are designated to supervise the maintenance activities of personnel who do not possess the required access authorizations.

#### EXAMINE — `ma-5_asm-examine`

- Maintenance policy

- procedures addressing maintenance personnel

- service provider contracts

- service-level agreements

- list of authorized personnel

- maintenance records

- access control records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-5_asm-interview`

- Organizational personnel with system maintenance responsibilities

- organizational personnel with information security responsibilities

#### TEST — `ma-5_asm-test`

- Organizational processes for authorizing and managing maintenance personnel

- mechanisms supporting and/or implementing authorization of maintenance personnel

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-5`. The library index records the exact source revision and hash.

- Catalog relationship **related**: `ac-2`.

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-5`.

- Catalog relationship **related**: `ac-6`.

- Catalog relationship **related**: `ia-2`.

- Catalog relationship **related**: `ia-8`.

- Catalog relationship **related**: `ma-4`.

- Catalog relationship **related**: `mp-2`.

- Catalog relationship **related**: `pe-2`.

- Catalog relationship **related**: `pe-3`.

- Catalog relationship **related**: `ps-7`.

- Catalog relationship **related**: `ra-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
