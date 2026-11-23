---
title: "MP-7 \u2014 Media Use"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MP-7 — Media Use

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

System media includes both digital and non-digital media. Digital media includes diskettes, magnetic tapes, flash drives, compact discs, digital versatile discs, and removable hard disk drives. Non-digital media includes paper and microfilm. Media use protections also apply to mobile devices with information storage capabilities. In contrast to MP-2 (catalog reference: `#mp-2`) , which restricts user access to media, MP-7 restricts the use of certain types of media on systems, for example, restricting or prohibiting the use of flash drives or external hard disk drives. Organizations use technical and nontechnical controls to restrict the use of system media. Organizations may restrict the use of portable storage devices, for example, by using physical cages on workstations to prohibit access to certain external ports or disabling or removing the ability to insert, read, or write to such devices. Organizations may also limit the use of portable storage devices to only approved devices, including devices provided by the organization, devices provided by other approved organizations, and devices that are not personally owned. Finally, organizations may restrict the use of portable storage devices based on the type of device, such as by prohibiting the use of writeable, portable storage devices and implementing this restriction by disabling or removing the capability to write to such devices. Requiring identifiable owners for storage devices reduces the risk of using such devices by allowing organizations to assign responsibility for addressing known vulnerabilities in the devices.

### Requirements and exact statement parts

- `mp-7_smt`: Statement grouping; see child parts.

- `mp-7_smt.a`: [PARAM mp-07_odp.02] the use of [PARAM mp-07_odp.01] on [PARAM mp-07_odp.03] using [PARAM mp-07_odp.04] ; and

- `mp-7_smt.b`: Prohibit the use of portable storage devices in organizational systems when such devices have no identifiable owner.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for mp-7_smt.a — [PARAM mp-07_odp.02] the use of [PARAM mp-07_odp.01] on [PARAM mp-07_odp.03] using [PARAM mp-07_odp.04] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for mp-7_smt.b — Prohibit the use of portable storage devices in organizational systems when such devices have no identifiable owner.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter mp-07_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-07_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-07_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-07_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `mp-7_smt.a` — For “[PARAM mp-07_odp.02] the use of [PARAM mp-07_odp.01] on [PARAM mp-07_odp.03] using [PARAM mp-07_odp.04] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `mp-7_smt.b` — For “Prohibit the use of portable storage devices in organizational systems when such devices have no identifiable owner.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `mp-07_odp.01` — What approved value applies to **types of system media**? Record the value, scope, approving authority, and decision source.

  - Catalog context: types of system media to be restricted or prohibited from use on systems or system components are defined;

- `mp-07_odp.02` — What approved value applies to **selection; choose one from: restrict; prohibit**? Record the value, scope, approving authority, and decision source.

- `mp-07_odp.03` — What approved value applies to **systems or system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems or system components on which the use of specific types of system media to be restricted or prohibited are defined;

- `mp-07_odp.04` — What approved value applies to **controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controls to restrict or prohibit the use of specific types of system media on systems or system components are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `mp-7_obj.a` (mp-7_smt.a): the use of [PARAM mp-07_odp.01] is [PARAM mp-07_odp.02] on [PARAM mp-07_odp.03] using [PARAM mp-07_odp.04];

- `mp-7_obj.b` (mp-7_smt.b): the use of portable storage devices in organizational systems is prohibited when such devices have no identifiable owner.

#### EXAMINE — `mp-7_asm-examine`

- System media protection policy

- system use policy

- procedures addressing media usage restrictions

- rules of behavior

- system design documentation

- system configuration settings and associated documentation

- audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `mp-7_asm-interview`

- Organizational personnel with system media use responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `mp-7_asm-test`

- Organizational processes for media use

- mechanisms restricting or prohibiting the use of system media on systems or system components

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `mp-7`. The library index records the exact source revision and hash.

- [FIPS 199](https://doi.org/10.6028/NIST.FIPS.199)

- [SP 800-111](https://doi.org/10.6028/NIST.SP.800-111)

- Catalog relationship **related**: `ac-19`.

- Catalog relationship **related**: `ac-20`.

- Catalog relationship **related**: `pl-4`.

- Catalog relationship **related**: `pm-12`.

- Catalog relationship **related**: `sc-34`.

- Catalog relationship **related**: `sc-41`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
