---
title: "MP-7.2 \u2014 Prohibit Use of Sanitization-resistant Media"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MP-7.2 — Prohibit Use of Sanitization-resistant Media

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Sanitization resistance refers to how resistant media are to non-destructive sanitization techniques with respect to the capability to purge information from media. Certain types of media do not support sanitization commands, or if supported, the interfaces are not supported in a standardized way across these devices. Sanitization-resistant media includes compact flash, embedded flash on boards and devices, solid state drives, and USB removable media.

### Requirements and exact statement parts

- `mp-7.2_smt`: Prohibit the use of sanitization-resistant media in organizational systems.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for mp-7.2_smt — Prohibit the use of sanitization-resistant media in organizational systems.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `mp-7.2_smt` — For “Prohibit the use of sanitization-resistant media in organizational systems.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `mp-7.2_obj-1` (mp-7.2_smt): sanitization-resistant media is identified;

- `mp-7.2_obj-2` (mp-7.2_smt): the use of sanitization-resistant media in organizational systems is prohibited.

#### EXAMINE — `mp-7.2_asm-examine`

- System media protection policy

- system use policy

- procedures addressing media usage restrictions

- rules of behavior

- system configuration settings and associated documentation

- system security plan

- other relevant documents or records

#### INTERVIEW — `mp-7.2_asm-interview`

- Organizational personnel with system media use responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `mp-7.2_asm-test`

- Organizational processes for media use

- mechanisms prohibiting use of media on systems or system components

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `mp-7.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `mp-7`.

- Catalog relationship **related**: `mp-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
