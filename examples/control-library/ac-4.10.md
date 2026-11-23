---
title: "AC-4.10 \u2014 Enable and Disable Security or Privacy Policy Filters"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4.10 — Enable and Disable Security or Privacy Policy Filters

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

For example, as allowed by the system authorization, administrators can enable security or privacy policy filters to accommodate approved data types. Administrators also have the capability to select the filters that are executed on a specific data flow based on the type of data that is being transferred, the source and destination security domains, and other security or privacy relevant features, as needed.

### Requirements and exact statement parts

- `ac-4.10_smt`: Provide the capability for privileged administrators to enable and disable [PARAM ac-4.10_prm_1] under the following conditions: [PARAM ac-4.10_prm_2].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4.10_smt — Provide the capability for privileged administrators to enable and disable [PARAM ac-4.10_prm_1] under the following conditions: [PARAM ac-4.10_prm_2].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-4.10_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-4.10_prm_2: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.10_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.10_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.10_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.10_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-4.10_smt` — For “Provide the capability for privileged administrators to enable and disable [PARAM ac-4.10_prm_1] under the following conditions: [PARAM ac-4.10_prm_2].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-4.10_prm_1` — What approved value applies to **organization-defined security or privacy policy filters**? Record the value, scope, approving authority, and decision source.

- `ac-4.10_prm_2` — What approved value applies to **organization-defined conditions**? Record the value, scope, approving authority, and decision source.

- `ac-04.10_odp.01` — What approved value applies to **security filters**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security policy filters that privileged administrators have the capability to enable and disable are defined;

- `ac-04.10_odp.02` — What approved value applies to **privacy filters**? Record the value, scope, approving authority, and decision source.

  - Catalog context: privacy policy filters that privileged administrators have the capability to enable and disable are defined;

- `ac-04.10_odp.03` — What approved value applies to **conditions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: conditions under which privileged administrators have the capability to enable and disable security policy filters are defined;

- `ac-04.10_odp.04` — What approved value applies to **conditions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: conditions under which privileged administrators have the capability to enable and disable privacy policy filters are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4.10_obj-1` (ac-4.10_smt): capability is provided for privileged administrators to enable and disable [PARAM ac-04.10_odp.01] under [PARAM ac-04.10_odp.03];

- `ac-4.10_obj-2` (ac-4.10_smt): capability is provided for privileged administrators to enable and disable [PARAM ac-04.10_odp.02] under [PARAM ac-04.10_odp.04].

#### EXAMINE — `ac-4.10_asm-examine`

- Access control policy

- information flow information policies

- procedures addressing information flow enforcement

- system design documentation

- system configuration settings and associated documentation

- list of security policy filters enabled/disabled by privileged administrators

- list of privacy policy filters enabled/disabled by privileged administrators

- list of approved data types for enabling/disabling by privileged administrators

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ac-4.10_asm-interview`

- Organizational personnel with responsibilities for enabling/disabling security and privacy policy filters

- system/network administrators

- organizational personnel with information security and privacy responsibilities

- system developers

#### TEST — `ac-4.10_asm-test`

- Mechanisms implementing information flow enforcement policy

- security and privacy policy filters

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4.10`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
