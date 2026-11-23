---
title: "AC-4.19 \u2014 Validation of Metadata"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4.19 — Validation of Metadata

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

All information (including metadata and the data to which the metadata applies) is subject to filtering and inspection. Some organizations distinguish between metadata and data payloads (i.e., only the data to which the metadata is bound). Other organizations do not make such distinctions and consider metadata and the data to which the metadata applies to be part of the payload.

### Requirements and exact statement parts

- `ac-4.19_smt`: When transferring information between different security domains, implement [PARAM ac-4.19_prm_1] on metadata.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4.19_smt — When transferring information between different security domains, implement [PARAM ac-4.19_prm_1] on metadata.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-4.19_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.19_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.19_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-4.19_smt` — For “When transferring information between different security domains, implement [PARAM ac-4.19_prm_1] on metadata.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-4.19_prm_1` — What approved value applies to **organization-defined security or privacy policy filters**? Record the value, scope, approving authority, and decision source.

- `ac-04.19_odp.01` — What approved value applies to **security policy filters**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security policy filters to be implemented on metadata are defined (if selected);

- `ac-04.19_odp.02` — What approved value applies to **privacy policy filters**? Record the value, scope, approving authority, and decision source.

  - Catalog context: privacy policy filters to be implemented on metadata are defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4.19_obj-1` (ac-4.19_smt): when transferring information between different security domains, [PARAM ac-04.19_odp.01] are implemented on metadata;

- `ac-4.19_obj-2` (ac-4.19_smt): when transferring information between different security domains, [PARAM ac-04.19_odp.02] are implemented on metadata.

#### EXAMINE — `ac-4.19_asm-examine`

- Information flow enforcement policy

- information flow control policies

- procedures addressing information flow enforcement

- system design documentation

- system configuration settings and associated documentation

- list of security policy filtering criteria applied to metadata and data payloads

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ac-4.19_asm-interview`

- Organizational personnel with information flow enforcement responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

- organizational personnel with privacy responsibilities

- system developers

#### TEST — `ac-4.19_asm-test`

- Mechanisms implementing information flow enforcement functions

- security and policy filters

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4.19`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
