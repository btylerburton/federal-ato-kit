---
title: "CM-5 \u2014 Access Restrictions for Change"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-5 — Access Restrictions for Change

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Changes to the hardware, software, or firmware components of systems or the operational procedures related to the system can potentially have significant effects on the security of the systems or individuals’ privacy. Therefore, organizations permit only qualified and authorized individuals to access systems for purposes of initiating changes. Access restrictions include physical and logical access controls (see AC-3 (catalog reference: `#ac-3`) and PE-3 (catalog reference: `#pe-3`) ), software libraries, workflow automation, media libraries, abstract layers (i.e., changes implemented into external interfaces rather than directly into systems), and change windows (i.e., changes occur only during specified times).

### Requirements and exact statement parts

- `cm-5_smt`: Define, document, approve, and enforce physical and logical access restrictions associated with changes to the system.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-5_smt — Define, document, approve, and enforce physical and logical access restrictions associated with changes to the system.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `cm-5_smt` — For “Define, document, approve, and enforce physical and logical access restrictions associated with changes to the system.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-5_obj-1` (cm-5_smt): physical access restrictions associated with changes to the system are defined and documented;

- `cm-5_obj-2` (cm-5_smt): physical access restrictions associated with changes to the system are approved;

- `cm-5_obj-3` (cm-5_smt): physical access restrictions associated with changes to the system are enforced;

- `cm-5_obj-4` (cm-5_smt): logical access restrictions associated with changes to the system are defined and documented;

- `cm-5_obj-5` (cm-5_smt): logical access restrictions associated with changes to the system are approved;

- `cm-5_obj-6` (cm-5_smt): logical access restrictions associated with changes to the system are enforced.

#### EXAMINE — `cm-5_asm-examine`

- Configuration management policy

- procedures addressing access restrictions for changes to the system

- configuration management plan

- system design documentation

- system architecture and configuration documentation

- system configuration settings and associated documentation

- logical access approvals

- physical access approvals

- access credentials

- change control records

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-5_asm-interview`

- Organizational personnel with logical access control responsibilities

- organizational personnel with physical access control responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `cm-5_asm-test`

- Organizational processes for managing access restrictions to change

- mechanisms supporting, implementing, or enforcing access restrictions associated with changes to the system

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-5`. The library index records the exact source revision and hash.

- [FIPS 140-3](https://doi.org/10.6028/NIST.FIPS.140-3)

- [FIPS 186-4](https://doi.org/10.6028/NIST.FIPS.186-4)

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-5`.

- Catalog relationship **related**: `ac-6`.

- Catalog relationship **related**: `cm-9`.

- Catalog relationship **related**: `pe-3`.

- Catalog relationship **related**: `sc-28`.

- Catalog relationship **related**: `sc-34`.

- Catalog relationship **related**: `sc-37`.

- Catalog relationship **related**: `si-2`.

- Catalog relationship **related**: `si-10`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
