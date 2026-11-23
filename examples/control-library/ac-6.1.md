---
title: "AC-6.1 \u2014 Authorize Access to Security Functions"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-6.1 — Authorize Access to Security Functions

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Security functions include establishing system accounts, configuring access authorizations (i.e., permissions, privileges), configuring settings for events to be audited, and establishing intrusion detection parameters. Security-relevant information includes filtering rules for routers or firewalls, configuration parameters for security services, cryptographic key management information, and access control lists. Authorized personnel include security administrators, system administrators, system security officers, system programmers, and other privileged users.

### Requirements and exact statement parts

- `ac-6.1_smt`: Authorize access for [PARAM ac-06.01_odp.01] to:

- `ac-6.1_smt.a`: [PARAM ac-6.1_prm_2] ; and

- `ac-6.1_smt.b`: [PARAM ac-06.01_odp.05].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-6.1_smt — Authorize access for [PARAM ac-06.01_odp.01] to:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-6.1_smt.a — [PARAM ac-6.1_prm_2] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-6.1_smt.b — [PARAM ac-06.01_odp.05].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-6.1_prm_2: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-06.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-06.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-06.01_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-06.01_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-06.01_odp.05: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-6.1_smt` — For “Authorize access for [PARAM ac-06.01_odp.01] to:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-6.1_smt.a` — For “[PARAM ac-6.1_prm_2] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-6.1_smt.b` — For “[PARAM ac-06.01_odp.05].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-6.1_prm_2` — What approved value applies to **organization-defined security functions (deployed in hardware, software, and firmware)**? Record the value, scope, approving authority, and decision source.

- `ac-06.01_odp.01` — What approved value applies to **individuals and roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: individuals and roles with authorized access to security functions and security-relevant information are defined;

- `ac-06.01_odp.02` — What approved value applies to **security functions (deployed in hardware)**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security functions (deployed in hardware) for authorized access are defined;

- `ac-06.01_odp.03` — What approved value applies to **security functions (deployed in software)**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security functions (deployed in software) for authorized access are defined;

- `ac-06.01_odp.04` — What approved value applies to **security functions (deployed in firmware)**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security functions (deployed in firmware) for authorized access are defined;

- `ac-06.01_odp.05` — What approved value applies to **security-relevant information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security-relevant information for authorized access is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-6.1_obj.a-1` (ac-6.1_smt.a): access is authorized for [PARAM ac-06.01_odp.01] to [PARAM ac-06.01_odp.02];

- `ac-6.1_obj.a-2` (ac-6.1_smt.a): access is authorized for [PARAM ac-06.01_odp.01] to [PARAM ac-06.01_odp.03];

- `ac-6.1_obj.a-3` (ac-6.1_smt.a): access is authorized for [PARAM ac-06.01_odp.01] to [PARAM ac-06.01_odp.04];

- `ac-6.1_obj.b` (ac-6.1_smt.b): access is authorized for [PARAM ac-06.01_odp.01] to [PARAM ac-06.01_odp.05].

#### EXAMINE — `ac-6.1_asm-examine`

- Access control policy

- procedures addressing least privilege

- list of security functions (deployed in hardware, software, and firmware) and security-relevant information for which access must be explicitly authorized

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-6.1_asm-interview`

- Organizational personnel with responsibilities for defining least privileges necessary to accomplish specified tasks

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ac-6.1_asm-test`

- Mechanisms implementing least privilege functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-6.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-6`.

- Catalog relationship **related**: `ac-17`.

- Catalog relationship **related**: `ac-18`.

- Catalog relationship **related**: `ac-19`.

- Catalog relationship **related**: `au-9`.

- Catalog relationship **related**: `pe-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
