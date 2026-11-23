---
title: "AU-9.4 \u2014 Access by Subset of Privileged Users"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-9.4 — Access by Subset of Privileged Users

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Individuals or roles with privileged access to a system and who are also the subject of an audit by that system may affect the reliability of the audit information by inhibiting audit activities or modifying audit records. Requiring privileged access to be further defined between audit-related privileges and other privileges limits the number of users or roles with audit-related privileges.

### Requirements and exact statement parts

- `au-9.4_smt`: Authorize access to management of audit logging functionality to only [PARAM au-09.04_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-9.4_smt — Authorize access to management of audit logging functionality to only [PARAM au-09.04_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-09.04_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-9.4_smt` — For “Authorize access to management of audit logging functionality to only [PARAM au-09.04_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-09.04_odp` — What approved value applies to **subset of privileged users or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: a subset of privileged users or roles authorized to access management of audit logging functionality is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-9.4_obj` (au-9.4_smt): access to management of audit logging functionality is authorized only to [PARAM au-09.04_odp].

#### EXAMINE — `au-9.4_asm-examine`

- Audit and accountability policy

- system security plan

- privacy plan

- access control policy and procedures

- procedures addressing protection of audit information

- system design documentation

- system configuration settings and associated documentation

- system-generated list of privileged users with access to management of audit functionality

- access authorizations

- access control list

- system audit records

- other relevant documents or records

#### INTERVIEW — `au-9.4_asm-interview`

- Organizational personnel with audit and accountability responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

#### TEST — `au-9.4_asm-test`

- Mechanisms managing access to audit functionality

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-9.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `au-9`.

- Catalog relationship **related**: `ac-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
