---
title: "AU-9.1 \u2014 Hardware Write-once Media"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-9.1 — Hardware Write-once Media

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Writing audit trails to hardware-enforced, write-once media applies to the initial generation of audit trails (i.e., the collection of audit records that represents the information to be used for detection, analysis, and reporting purposes) and to the backup of those audit trails. Writing audit trails to hardware-enforced, write-once media does not apply to the initial generation of audit records prior to being written to an audit trail. Write-once, read-many (WORM) media includes Compact Disc-Recordable (CD-R), Blu-Ray Disc Recordable (BD-R), and Digital Versatile Disc-Recordable (DVD-R). In contrast, the use of switchable write-protection media, such as tape cartridges, Universal Serial Bus (USB) drives, Compact Disc Re-Writeable (CD-RW), and Digital Versatile Disc-Read Write (DVD-RW) results in write-protected but not write-once media.

### Requirements and exact statement parts

- `au-9.1_smt`: Write audit trails to hardware-enforced, write-once media.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-9.1_smt — Write audit trails to hardware-enforced, write-once media.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `au-9.1_smt` — For “Write audit trails to hardware-enforced, write-once media.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-9.1_obj` (au-9.1_smt): audit trails are written to hardware-enforced, write-once media.

#### EXAMINE — `au-9.1_asm-examine`

- Audit and accountability policy

- system security plan

- privacy plan

- access control policy and procedures

- procedures addressing protection of audit information

- system design documentation

- system hardware settings

- system configuration settings and associated documentation

- system storage media

- system audit records

- other relevant documents or records

#### INTERVIEW — `au-9.1_asm-interview`

- Organizational personnel with audit and accountability responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

- system developers

#### TEST — `au-9.1_asm-test`

- System media storing audit trails

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-9.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `au-9`.

- Catalog relationship **related**: `au-4`.

- Catalog relationship **related**: `au-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
