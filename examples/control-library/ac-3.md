---
title: "AC-3 \u2014 Access Enforcement"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-3 — Access Enforcement

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Access control policies control access between active entities or subjects (i.e., users or processes acting on behalf of users) and passive entities or objects (i.e., devices, files, records, domains) in organizational systems. In addition to enforcing authorized access at the system level and recognizing that systems can host many applications and services in support of mission and business functions, access enforcement mechanisms can also be employed at the application and service level to provide increased information security and privacy. In contrast to logical access controls that are implemented within the system, physical access controls are addressed by the controls in the Physical and Environmental Protection ( PE (catalog reference: `#pe`) ) family.

### Requirements and exact statement parts

- `ac-3_smt`: Enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-3_smt — Enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ac-3_smt` — For “Enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-3_obj` (ac-3_smt): approved authorizations for logical access to information and system resources are enforced in accordance with applicable access control policies.

#### EXAMINE — `ac-3_asm-examine`

- Access control policy

- procedures addressing access enforcement

- system design documentation

- system configuration settings and associated documentation

- list of approved authorizations (user privileges)

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ac-3_asm-interview`

- Organizational personnel with access enforcement responsibilities

- system/network administrators

- organizational personnel with information security and privacy responsibilities

- system developers

#### TEST — `ac-3_asm-test`

- Mechanisms implementing access control policy

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-3`. The library index records the exact source revision and hash.

- [PRIVACT](https://www.govinfo.gov/content/pkg/STATUTE-88/pdf/STATUTE-88-Pg1896.pdf)

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [SP 800-57-1](https://doi.org/10.6028/NIST.SP.800-57pt1r5)

- [SP 800-57-2](https://doi.org/10.6028/NIST.SP.800-57pt2r1)

- [SP 800-57-3](https://doi.org/10.6028/NIST.SP.800-57pt3r1)

- [SP 800-162](https://doi.org/10.6028/NIST.SP.800-162)

- [SP 800-178](https://doi.org/10.6028/NIST.SP.800-178)

- [IR 7874](https://doi.org/10.6028/NIST.IR.7874)

- Catalog relationship **related**: `ac-2`.

- Catalog relationship **related**: `ac-4`.

- Catalog relationship **related**: `ac-5`.

- Catalog relationship **related**: `ac-6`.

- Catalog relationship **related**: `ac-16`.

- Catalog relationship **related**: `ac-17`.

- Catalog relationship **related**: `ac-18`.

- Catalog relationship **related**: `ac-19`.

- Catalog relationship **related**: `ac-20`.

- Catalog relationship **related**: `ac-21`.

- Catalog relationship **related**: `ac-22`.

- Catalog relationship **related**: `ac-24`.

- Catalog relationship **related**: `ac-25`.

- Catalog relationship **related**: `at-2`.

- Catalog relationship **related**: `at-3`.

- Catalog relationship **related**: `au-9`.

- Catalog relationship **related**: `ca-9`.

- Catalog relationship **related**: `cm-5`.

- Catalog relationship **related**: `cm-11`.

- Catalog relationship **related**: `ia-2`.

- Catalog relationship **related**: `ia-5`.

- Catalog relationship **related**: `ia-6`.

- Catalog relationship **related**: `ia-7`.

- Catalog relationship **related**: `ia-11`.

- Catalog relationship **related**: `ia-13`.

- Catalog relationship **related**: `ma-3`.

- Catalog relationship **related**: `ma-4`.

- Catalog relationship **related**: `ma-5`.

- Catalog relationship **related**: `mp-4`.

- Catalog relationship **related**: `pm-2`.

- Catalog relationship **related**: `ps-3`.

- Catalog relationship **related**: `pt-2`.

- Catalog relationship **related**: `pt-3`.

- Catalog relationship **related**: `sa-17`.

- Catalog relationship **related**: `sc-2`.

- Catalog relationship **related**: `sc-3`.

- Catalog relationship **related**: `sc-4`.

- Catalog relationship **related**: `sc-12`.

- Catalog relationship **related**: `sc-13`.

- Catalog relationship **related**: `sc-28`.

- Catalog relationship **related**: `sc-31`.

- Catalog relationship **related**: `sc-34`.

- Catalog relationship **related**: `si-4`.

- Catalog relationship **related**: `si-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
