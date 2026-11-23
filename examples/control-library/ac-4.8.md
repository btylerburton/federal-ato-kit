---
title: "AC-4.8 \u2014 Security and Privacy Policy Filters"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4.8 — Security and Privacy Policy Filters

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organization-defined security or privacy policy filters can address data structures and content. For example, security or privacy policy filters for data structures can check for maximum file lengths, maximum field sizes, and data/file types (for structured and unstructured data). Security or privacy policy filters for data content can check for specific words, enumerated values or data value ranges, and hidden content. Structured data permits the interpretation of data content by applications. Unstructured data refers to digital information without a data structure or with a data structure that does not facilitate the development of rule sets to address the impact or classification level of the information conveyed by the data or the flow enforcement decisions. Unstructured data consists of bitmap objects that are inherently non-language-based (i.e., image, video, or audio files) and textual objects that are based on written or printed languages. Organizations can implement more than one security or privacy policy filter to meet information flow control objectives.

### Requirements and exact statement parts

- `ac-4.8_smt`: Statement grouping; see child parts.

- `ac-4.8_smt.a`: Enforce information flow control using [PARAM ac-4.8_prm_1] as a basis for flow control decisions for [PARAM ac-4.8_prm_2] ; and

- `ac-4.8_smt.b`: [PARAM ac-04.08_odp.05] data after a filter processing failure in accordance with [PARAM ac-4.8_prm_4].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4.8_smt.a — Enforce information flow control using [PARAM ac-4.8_prm_1] as a basis for flow control decisions for [PARAM ac-4.8_prm_2] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-4.8_smt.b — [PARAM ac-04.08_odp.05] data after a filter processing failure in accordance with [PARAM ac-4.8_prm_4].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-4.8_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-4.8_prm_2: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-4.8_prm_4: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.08_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.08_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.08_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.08_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.08_odp.05: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.08_odp.06: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.08_odp.07: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-4.8_smt.a` — For “Enforce information flow control using [PARAM ac-4.8_prm_1] as a basis for flow control decisions for [PARAM ac-4.8_prm_2] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-4.8_smt.b` — For “[PARAM ac-04.08_odp.05] data after a filter processing failure in accordance with [PARAM ac-4.8_prm_4].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-4.8_prm_1` — What approved value applies to **organization-defined security or privacy policy filters**? Record the value, scope, approving authority, and decision source.

- `ac-4.8_prm_2` — What approved value applies to **organization-defined information flows**? Record the value, scope, approving authority, and decision source.

- `ac-4.8_prm_4` — What approved value applies to **organization-defined security or privacy policy**? Record the value, scope, approving authority, and decision source.

- `ac-04.08_odp.01` — What approved value applies to **security policy filter**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security policy filters to be used as a basis for enforcing information flow control are defined;

- `ac-04.08_odp.02` — What approved value applies to **privacy policy filter**? Record the value, scope, approving authority, and decision source.

  - Catalog context: privacy policy filters to be used as a basis for enforcing information flow control are defined;

- `ac-04.08_odp.03` — What approved value applies to **information flows**? Record the value, scope, approving authority, and decision source.

  - Catalog context: information flows for which information flow control is enforced by security filters are defined;

- `ac-04.08_odp.04` — What approved value applies to **information flows**? Record the value, scope, approving authority, and decision source.

  - Catalog context: information flows for which information flow control is enforced by privacy filters are defined;

- `ac-04.08_odp.05` — What approved value applies to **selection; choose one-or-more from: block; strip; modify; quarantine**? Record the value, scope, approving authority, and decision source.

- `ac-04.08_odp.06` — What approved value applies to **security policy**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security policy identifying actions to be taken after a filter processing failure are defined;

- `ac-04.08_odp.07` — What approved value applies to **privacy policy**? Record the value, scope, approving authority, and decision source.

  - Catalog context: privacy policy identifying actions to be taken after a filter processing failure are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4.8_obj.a-1` (ac-4.8_smt.a): information flow control is enforced using [PARAM ac-04.08_odp.01] as a basis for flow control decisions for [PARAM ac-04.08_odp.03];

- `ac-4.8_obj.a-2` (ac-4.8_smt.a): information flow control is enforced using [PARAM ac-04.08_odp.02] as a basis for flow control decisions for [PARAM ac-04.08_odp.04];

- `ac-4.8_obj.b` (ac-4.8_smt.b): [PARAM ac-04.08_odp.05] data after a filter processing failure in accordance with [PARAM ac-04.08_odp.06];

[PARAM ac-04.08_odp.05] data after a filter processing failure in accordance with [PARAM ac-04.08_odp.07].

#### EXAMINE — `ac-4.8_asm-examine`

- Access control policy

- information flow control policies

- procedures addressing information flow enforcement

- system design documentation

- system configuration settings and associated documentation

- list of security policy filters regulating flow control decisions

- list of privacy policy filters regulating flow control decisions

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ac-4.8_asm-interview`

- System/network administrators

- organizational personnel with information security and privacy responsibilities

- system developers

#### TEST — `ac-4.8_asm-test`

- Mechanisms implementing information flow enforcement policy

- security and privacy policy filters

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4.8`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
