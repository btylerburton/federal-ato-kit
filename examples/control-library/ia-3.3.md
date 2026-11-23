---
title: "IA-3.3 \u2014 Dynamic Address Allocation"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-3.3 — Dynamic Address Allocation

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The Dynamic Host Configuration Protocol (DHCP) is an example of a means by which clients can dynamically receive network address assignments.

### Requirements and exact statement parts

- `ia-3.3_smt`: Statement grouping; see child parts.

- `ia-3.3_smt.a`: Where addresses are allocated dynamically, standardize dynamic address allocation lease information and the lease duration assigned to devices in accordance with [PARAM ia-3.3_prm_1] ; and

- `ia-3.3_smt.b`: Audit lease information when assigned to a device.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-3.3_smt.a — Where addresses are allocated dynamically, standardize dynamic address allocation lease information and the lease duration assigned to devices in accordance with [PARAM ia-3.3_prm_1] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-3.3_smt.b — Audit lease information when assigned to a device.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ia-3.3_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ia-03.03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ia-03.03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ia-3.3_smt.a` — For “Where addresses are allocated dynamically, standardize dynamic address allocation lease information and the lease duration assigned to devices in accordance with [PARAM ia-3.3_prm_1] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-3.3_smt.b` — For “Audit lease information when assigned to a device.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ia-3.3_prm_1` — What approved value applies to **organization-defined lease information and lease duration**? Record the value, scope, approving authority, and decision source.

- `ia-03.03_odp.01` — What approved value applies to **lease information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: lease information to be employed to standardize dynamic address allocation for devices is defined;

- `ia-03.03_odp.02` — What approved value applies to **lease duration**? Record the value, scope, approving authority, and decision source.

  - Catalog context: lease duration to be employed to standardize dynamic address allocation for devices is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-3.3_obj.a-1` (ia-3.3_smt.a): dynamic address allocation lease information assigned to devices where addresses are allocated dynamically are standardized in accordance with [PARAM ia-03.03_odp.01];

- `ia-3.3_obj.a-2` (ia-3.3_smt.a): dynamic address allocation lease duration assigned to devices where addresses are allocated dynamically are standardized in accordance with [PARAM ia-03.03_odp.02];

- `ia-3.3_obj.b` (ia-3.3_smt.b): lease information is audited when assigned to a device.

#### EXAMINE — `ia-3.3_asm-examine`

- Identification and authentication policy

- system security plan

- procedures addressing device identification and authentication

- system design documentation

- system configuration settings and associated documentation

- evidence of lease information and lease duration assigned to devices

- device connection reports

- system audit records

- other relevant documents or records

#### INTERVIEW — `ia-3.3_asm-interview`

- Organizational personnel with operational responsibilities for device identification and authentication

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `ia-3.3_asm-test`

- Mechanisms supporting and/or implementing device identification and authentication capabilities

- mechanisms supporting and/or implementing dynamic address allocation

- mechanisms supporting and/or implanting auditing of lease information

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-3.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-3`.

- Catalog relationship **related**: `au-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
