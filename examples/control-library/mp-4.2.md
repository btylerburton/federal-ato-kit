---
title: "MP-4.2 \u2014 Automated Restricted Access"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MP-4.2 — Automated Restricted Access

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Automated mechanisms include keypads, biometric readers, or card readers on the external entries to media storage areas.

### Requirements and exact statement parts

- `mp-4.2_smt`: Restrict access to media storage areas and log access attempts and access granted using [PARAM mp-4.2_prm_1].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for mp-4.2_smt — Restrict access to media storage areas and log access attempts and access granted using [PARAM mp-4.2_prm_1].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter mp-4.2_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-04.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-04.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-04.02_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `mp-4.2_smt` — For “Restrict access to media storage areas and log access attempts and access granted using [PARAM mp-4.2_prm_1].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `mp-4.2_prm_1` — What approved value applies to **organization-defined automated mechanisms**? Record the value, scope, approving authority, and decision source.

- `mp-04.02_odp.01` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms to restrict access to media storage areas are defined;

- `mp-04.02_odp.02` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms to log access attempts to media storage areas are defined;

- `mp-04.02_odp.03` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms to log access granted to media storage areas are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `mp-4.2_obj-1` (mp-4.2_smt): access to media storage areas is restricted using [PARAM mp-04.02_odp.01];

- `mp-4.2_obj-2` (mp-4.2_smt): access attempts to media storage areas are logged using [PARAM mp-04.02_odp.02];

- `mp-4.2_obj-3` (mp-4.2_smt): access granted to media storage areas is logged using [PARAM mp-04.02_odp.03].

#### EXAMINE — `mp-4.2_asm-examine`

- System media protection policy

- procedures addressing media storage

- access control policy and procedures

- physical and environmental protection policy and procedures

- system design documentation

- system configuration settings and associated documentation

- media storage facilities

- access control devices

- access control records

- audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `mp-4.2_asm-interview`

- Organizational personnel with system media protection and storage responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `mp-4.2_asm-test`

- Automated mechanisms restricting access to media storage areas

- automated mechanisms auditing access attempts and access granted to media storage areas

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `mp-4.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `mp-4`.

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-9`.

- Catalog relationship **related**: `au-12`.

- Catalog relationship **related**: `pe-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
