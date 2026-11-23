---
title: "AC-4.21 \u2014 Physical or Logical Separation of Information Flows"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4.21 — Physical or Logical Separation of Information Flows

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Enforcing the separation of information flows associated with defined types of data can enhance protection by ensuring that information is not commingled while in transit and by enabling flow control by transmission paths that are not otherwise achievable. Types of separable information include inbound and outbound communications traffic, service requests and responses, and information of differing security impact or classification levels.

### Requirements and exact statement parts

- `ac-4.21_smt`: Separate information flows logically or physically using [PARAM ac-4.21_prm_1] to accomplish [PARAM ac-04.21_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4.21_smt — Separate information flows logically or physically using [PARAM ac-4.21_prm_1] to accomplish [PARAM ac-04.21_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-4.21_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.21_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.21_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.21_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-4.21_smt` — For “Separate information flows logically or physically using [PARAM ac-4.21_prm_1] to accomplish [PARAM ac-04.21_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-4.21_prm_1` — What approved value applies to **organization-defined mechanisms and/or techniques**? Record the value, scope, approving authority, and decision source.

- `ac-04.21_odp.01` — What approved value applies to **mechanisms and/or techniques**? Record the value, scope, approving authority, and decision source.

  - Catalog context: mechanisms and/or techniques used to logically separate information flows are defined (if selected);

- `ac-04.21_odp.02` — What approved value applies to **mechanisms and/or techniques**? Record the value, scope, approving authority, and decision source.

  - Catalog context: mechanisms and/or techniques used to physically separate information flows are defined (if selected);

- `ac-04.21_odp.03` — What approved value applies to **required separations**? Record the value, scope, approving authority, and decision source.

  - Catalog context: required separations by types of information are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4.21_obj-1` (ac-4.21_smt): information flows are separated logically using [PARAM ac-04.21_odp.01] to accomplish [PARAM ac-04.21_odp.03];

- `ac-4.21_obj-2` (ac-4.21_smt): information flows are separated physically using [PARAM ac-04.21_odp.02] to accomplish [PARAM ac-04.21_odp.03].

#### EXAMINE — `ac-4.21_asm-examine`

- Information flow enforcement policy

- information flow control policies

- procedures addressing information flow enforcement

- system design documentation

- system configuration settings and associated documentation

- list of required separation of information flows by information types

- list of mechanisms and/or techniques used to logically or physically separate information flows

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-4.21_asm-interview`

- Organizational personnel with information flow enforcement responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

- system developers

#### TEST — `ac-4.21_asm-test`

- Mechanisms implementing information flow enforcement functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4.21`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-4`.

- Catalog relationship **related**: `sc-32`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
