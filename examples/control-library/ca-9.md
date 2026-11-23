---
title: "CA-9 \u2014 Internal System Connections"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CA-9 — Internal System Connections

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Internal system connections are connections between organizational systems and separate constituent system components (i.e., connections between components that are part of the same system) including components used for system development. Intra-system connections include connections with mobile devices, notebook and desktop computers, tablets, printers, copiers, facsimile machines, scanners, sensors, and servers. Instead of authorizing each internal system connection individually, organizations can authorize internal connections for a class of system components with common characteristics and/or configurations, including printers, scanners, and copiers with a specified processing, transmission, and storage capability or smart phones and tablets with a specific baseline configuration. The continued need for an internal system connection is reviewed from the perspective of whether it provides support for organizational missions or business functions.

### Requirements and exact statement parts

- `ca-9_smt`: Statement grouping; see child parts.

- `ca-9_smt.a`: Authorize internal connections of [PARAM ca-09_odp.01] to the system;

- `ca-9_smt.b`: Document, for each internal connection, the interface characteristics, security and privacy requirements, and the nature of the information communicated;

- `ca-9_smt.c`: Terminate internal system connections after [PARAM ca-09_odp.02] ; and

- `ca-9_smt.d`: Review [PARAM ca-09_odp.03] the continued need for each internal connection.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ca-9_smt.a — Authorize internal connections of [PARAM ca-09_odp.01] to the system;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ca-9_smt.b — Document, for each internal connection, the interface characteristics, security and privacy requirements, and the nature of the information communicated;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ca-9_smt.c — Terminate internal system connections after [PARAM ca-09_odp.02] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ca-9_smt.d — Review [PARAM ca-09_odp.03] the continued need for each internal connection.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ca-09_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ca-09_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ca-09_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ca-9_smt.a` — For “Authorize internal connections of [PARAM ca-09_odp.01] to the system;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ca-9_smt.b` — For “Document, for each internal connection, the interface characteristics, security and privacy requirements, and the nature of the information communicated;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ca-9_smt.c` — For “Terminate internal system connections after [PARAM ca-09_odp.02] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ca-9_smt.d` — For “Review [PARAM ca-09_odp.03] the continued need for each internal connection.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ca-09_odp.01` — What approved value applies to **system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system components or classes of components requiring internal connections to the system are defined;

- `ca-09_odp.02` — What approved value applies to **conditions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: conditions requiring termination of internal connections are defined;

- `ca-09_odp.03` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to review the continued need for each internal connection is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ca-9_obj.a` (ca-9_smt.a): internal connections of [PARAM ca-09_odp.01] to the system are authorized;

- `ca-9_obj.b-1` (ca-9_smt.b): for each internal connection, the interface characteristics are documented;

- `ca-9_obj.b-2` (ca-9_smt.b): for each internal connection, the security requirements are documented;

- `ca-9_obj.b-3` (ca-9_smt.b): for each internal connection, the privacy requirements are documented;

- `ca-9_obj.b-4` (ca-9_smt.b): for each internal connection, the nature of the information communicated is documented;

- `ca-9_obj.c` (ca-9_smt.c): internal system connections are terminated after [PARAM ca-09_odp.02];

- `ca-9_obj.d` (ca-9_smt.d): the continued need for each internal connection is reviewed [PARAM ca-09_odp.03].

#### EXAMINE — `ca-9_asm-examine`

- Assessment, authorization, and monitoring policy

- access control policy

- procedures addressing system connections

- system and communications protection policy

- system design documentation

- system configuration settings and associated documentation

- list of components or classes of components authorized as internal system connections

- assessment report

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ca-9_asm-interview`

- Organizational personnel with responsibilities for developing, implementing, or authorizing internal system connections

- organizational personnel with information security and privacy responsibilities

#### TEST — `ca-9_asm-test`

- Mechanisms supporting internal system connections

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ca-9`. The library index records the exact source revision and hash.

- [SP 800-124](https://doi.org/10.6028/NIST.SP.800-124r1)

- [IR 8023](https://doi.org/10.6028/NIST.IR.8023)

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-4`.

- Catalog relationship **related**: `ac-18`.

- Catalog relationship **related**: `ac-19`.

- Catalog relationship **related**: `cm-2`.

- Catalog relationship **related**: `ia-3`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `si-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
