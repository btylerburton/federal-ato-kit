---
title: "MP-6.3 \u2014 Nondestructive Techniques"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MP-6.3 — Nondestructive Techniques

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Portable storage devices include external or removable hard disk drives (e.g., solid state, magnetic), optical discs, magnetic or optical tapes, flash memory devices, flash memory cards, and other external or removable disks. Portable storage devices can be obtained from untrustworthy sources and contain malicious code that can be inserted into or transferred to organizational systems through USB ports or other entry portals. While scanning storage devices is recommended, sanitization provides additional assurance that such devices are free of malicious code. Organizations consider nondestructive sanitization of portable storage devices when the devices are purchased from manufacturers or vendors prior to initial use or when organizations cannot maintain a positive chain of custody for the devices.

### Requirements and exact statement parts

- `mp-6.3_smt`: Apply nondestructive sanitization techniques to portable storage devices prior to connecting such devices to the system under the following circumstances: [PARAM mp-06.03_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for mp-6.3_smt — Apply nondestructive sanitization techniques to portable storage devices prior to connecting such devices to the system under the following circumstances: [PARAM mp-06.03_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter mp-06.03_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `mp-6.3_smt` — For “Apply nondestructive sanitization techniques to portable storage devices prior to connecting such devices to the system under the following circumstances: [PARAM mp-06.03_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `mp-06.03_odp` — What approved value applies to **circumstances**? Record the value, scope, approving authority, and decision source.

  - Catalog context: circumstances requiring sanitization of portable storage devices are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `mp-6.3_obj` (mp-6.3_smt): non-destructive sanitization techniques are applied to portable storage devices prior to connecting such devices to the system under [PARAM mp-06.03_odp].

#### EXAMINE — `mp-6.3_asm-examine`

- System media protection policy

- procedures addressing media sanitization and disposal

- information on portable storage devices for the system

- list of circumstances requiring sanitization of portable storage devices

- media sanitization records

- audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `mp-6.3_asm-interview`

- Organizational personnel with system media sanitization responsibilities

- organizational personnel with information security responsibilities

#### TEST — `mp-6.3_asm-test`

- Organizational processes for media sanitization of portable storage devices

- mechanisms supporting and/or implementing media sanitization

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `mp-6.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `mp-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
