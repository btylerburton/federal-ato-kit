---
title: "AC-4.1 \u2014 Object Security and Privacy Attributes"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4.1 — Object Security and Privacy Attributes

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Information flow enforcement mechanisms compare security and privacy attributes associated with information (i.e., data content and structure) and source and destination objects and respond appropriately when the enforcement mechanisms encounter information flows not explicitly allowed by information flow policies. For example, an information object labeled Secret would be allowed to flow to a destination object labeled Secret, but an information object labeled Top Secret would not be allowed to flow to a destination object labeled Secret. A dataset of personally identifiable information may be tagged with restrictions against combining with other types of datasets and, thus, would not be allowed to flow to the restricted dataset. Security and privacy attributes can also include source and destination addresses employed in traffic filter firewalls. Flow enforcement using explicit security or privacy attributes can be used, for example, to control the release of certain types of information.

### Requirements and exact statement parts

- `ac-4.1_smt`: Use [PARAM ac-4.1_prm_1] associated with [PARAM ac-4.1_prm_2] to enforce [PARAM ac-04.01_odp.09] as a basis for flow control decisions.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4.1_smt — Use [PARAM ac-4.1_prm_1] associated with [PARAM ac-4.1_prm_2] to enforce [PARAM ac-04.01_odp.09] as a basis for flow control decisions.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-4.1_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-4.1_prm_2: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.01_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.01_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.01_odp.05: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.01_odp.06: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.01_odp.07: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.01_odp.08: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.01_odp.09: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-4.1_smt` — For “Use [PARAM ac-4.1_prm_1] associated with [PARAM ac-4.1_prm_2] to enforce [PARAM ac-04.01_odp.09] as a basis for flow control decisions.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-4.1_prm_1` — What approved value applies to **organization-defined security and privacy attributes**? Record the value, scope, approving authority, and decision source.

- `ac-4.1_prm_2` — What approved value applies to **organization-defined information, source, and destination objects**? Record the value, scope, approving authority, and decision source.

- `ac-04.01_odp.01` — What approved value applies to **security attributes**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security attributes to be associated with information, source, and destination objects are defined;

- `ac-04.01_odp.02` — What approved value applies to **privacy attributes**? Record the value, scope, approving authority, and decision source.

  - Catalog context: privacy attributes to be associated with information, source, and destination objects are defined;

- `ac-04.01_odp.03` — What approved value applies to **information objects**? Record the value, scope, approving authority, and decision source.

  - Catalog context: information objects to be associated with information security attributes are defined;

- `ac-04.01_odp.04` — What approved value applies to **information objects**? Record the value, scope, approving authority, and decision source.

  - Catalog context: information objects to be associated with privacy attributes are defined;

- `ac-04.01_odp.05` — What approved value applies to **source objects**? Record the value, scope, approving authority, and decision source.

  - Catalog context: source objects to be associated with information security attributes are defined;

- `ac-04.01_odp.06` — What approved value applies to **source objects**? Record the value, scope, approving authority, and decision source.

  - Catalog context: source objects to be associated with privacy attributes are defined;

- `ac-04.01_odp.07` — What approved value applies to **destination objects**? Record the value, scope, approving authority, and decision source.

  - Catalog context: destination objects to be associated with information security attributes are defined;

- `ac-04.01_odp.08` — What approved value applies to **destination objects**? Record the value, scope, approving authority, and decision source.

  - Catalog context: destination objects to be associated with privacy attributes are defined;

- `ac-04.01_odp.09` — What approved value applies to **information flow control policies**? Record the value, scope, approving authority, and decision source.

  - Catalog context: information flow control policies as a basis for enforcement of flow control decisions are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4.1_obj-1` (ac-4.1_smt): [PARAM ac-04.01_odp.01] associated with [PARAM ac-04.01_odp.03], [PARAM ac-04.01_odp.05] , and [PARAM ac-04.01_odp.07] are used to enforce [PARAM ac-04.01_odp.09] as a basis for flow control decisions;

- `ac-4.1_obj-2` (ac-4.1_smt): [PARAM ac-04.01_odp.02] associated with [PARAM ac-04.01_odp.04], [PARAM ac-04.01_odp.06] , and [PARAM ac-04.01_odp.08] are used to enforce [PARAM ac-04.01_odp.09] as a basis for flow control decisions.

#### EXAMINE — `ac-4.1_asm-examine`

- Access control policy

- information flow control policies

- procedures addressing information flow enforcement

- system design documentation

- system configuration settings and associated documentation

- list of security and privacy attributes and associated source and destination objects

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ac-4.1_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel with privacy responsibilities

- system developers

#### TEST — `ac-4.1_asm-test`

- Mechanisms implementing information flow enforcement policy

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
