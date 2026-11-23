---
title: "AC-3.14 \u2014 Individual Access"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-3.14 — Individual Access

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Individual access affords individuals the ability to review personally identifiable information about them held within organizational records, regardless of format. Access helps individuals to develop an understanding about how their personally identifiable information is being processed. It can also help individuals ensure that their data is accurate. Access mechanisms can include request forms and application interfaces. For federal agencies, PRIVACT (catalog reference: `#18e71fec-c6fd-475a-925a-5d8495cf8455`) processes can be located in systems of record notices and on agency websites. Access to certain types of records may not be appropriate (e.g., for federal agencies, law enforcement records within a system of records may be exempt from disclosure under the PRIVACT (catalog reference: `#18e71fec-c6fd-475a-925a-5d8495cf8455`) ) or may require certain levels of authentication assurance. Organizational personnel consult with the senior agency official for privacy and legal counsel to determine appropriate mechanisms and access rights or limitations.

### Requirements and exact statement parts

- `ac-3.14_smt`: Provide [PARAM ac-03.14_odp.01] to enable individuals to have access to the following elements of their personally identifiable information: [PARAM ac-03.14_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-3.14_smt — Provide [PARAM ac-03.14_odp.01] to enable individuals to have access to the following elements of their personally identifiable information: [PARAM ac-03.14_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-03.14_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-03.14_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-3.14_smt` — For “Provide [PARAM ac-03.14_odp.01] to enable individuals to have access to the following elements of their personally identifiable information: [PARAM ac-03.14_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-03.14_odp.01` — What approved value applies to **mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: mechanisms enabling individuals to have access to elements of their personally identifiable information are defined;

- `ac-03.14_odp.02` — What approved value applies to **elements**? Record the value, scope, approving authority, and decision source.

  - Catalog context: elements of personally identifiable information to which individuals have access are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-3.14_obj` (ac-3.14_smt): [PARAM ac-03.14_odp.01] are provided to enable individuals to have access to [PARAM ac-03.14_odp.02] of their personally identifiable information.

#### EXAMINE — `ac-3.14_asm-examine`

- Access mechanisms (e.g., request forms and application interfaces)

- access control policy

- procedures addressing access enforcement

- system design documentation

- system configuration settings and associated documentation

- documentation regarding access to an individual’s personally identifiable information

- system audit records

- system security plan

- privacy plan

- privacy impact assessment

- privacy assessment findings and/or reports

- other relevant documents or records

#### INTERVIEW — `ac-3.14_asm-interview`

- Organizational personnel with access enforcement responsibilities

- system/network administrators

- organizational personnel with information security and privacy responsibilities

- legal counsel

#### TEST — `ac-3.14_asm-test`

- Mechanisms implementing access enforcement functions

- mechanisms enabling individual access to personally identifiable information

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-3.14`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-3`.

- Catalog relationship **related**: `ia-8`.

- Catalog relationship **related**: `pm-22`.

- Catalog relationship **related**: `pm-20`.

- Catalog relationship **related**: `pm-21`.

- Catalog relationship **related**: `pt-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
