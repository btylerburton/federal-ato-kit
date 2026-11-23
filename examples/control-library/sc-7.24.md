---
title: "SC-7.24 \u2014 Personally Identifiable Information"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-7.24 — Personally Identifiable Information

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Managing the processing of personally identifiable information is an important aspect of protecting an individual’s privacy. Applying, monitoring for, and documenting exceptions to processing rules ensure that personally identifiable information is processed only in accordance with established privacy requirements.

### Requirements and exact statement parts

- `sc-7.24_smt`: For systems that process personally identifiable information:

- `sc-7.24_smt.a`: Apply the following processing rules to data elements of personally identifiable information: [PARAM sc-07.24_odp];

- `sc-7.24_smt.b`: Monitor for permitted processing at the external interfaces to the system and at key internal boundaries within the system;

- `sc-7.24_smt.c`: Document each processing exception; and

- `sc-7.24_smt.d`: Review and remove exceptions that are no longer supported.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-7.24_smt — For systems that process personally identifiable information:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sc-7.24_smt.a — Apply the following processing rules to data elements of personally identifiable information: [PARAM sc-07.24_odp];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sc-7.24_smt.b — Monitor for permitted processing at the external interfaces to the system and at key internal boundaries within the system;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sc-7.24_smt.c — Document each processing exception; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sc-7.24_smt.d — Review and remove exceptions that are no longer supported.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-07.24_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-7.24_smt` — For “For systems that process personally identifiable information:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sc-7.24_smt.a` — For “Apply the following processing rules to data elements of personally identifiable information: [PARAM sc-07.24_odp];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sc-7.24_smt.b` — For “Monitor for permitted processing at the external interfaces to the system and at key internal boundaries within the system;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sc-7.24_smt.c` — For “Document each processing exception; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sc-7.24_smt.d` — For “Review and remove exceptions that are no longer supported.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-07.24_odp` — What approved value applies to **processing rules**? Record the value, scope, approving authority, and decision source.

  - Catalog context: processing rules for systems that process personally identifiable information are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-7.24_obj.a` (sc-7.24_smt.a): [PARAM sc-07.24_odp] are applied to data elements of personally identifiable information on systems that process personally identifiable information;

- `sc-7.24_obj.b-1` (sc-7.24_smt.b): permitted processing is monitored at the external interfaces to the systems that process personally identifiable information;

- `sc-7.24_obj.b-2` (sc-7.24_smt.b): permitted processing is monitored at key internal boundaries within the systems that process personally identifiable information;

- `sc-7.24_obj.c` (sc-7.24_smt.c): each processing exception is documented for systems that process personally identifiable information;

- `sc-7.24_obj.d-1` (sc-7.24_smt.d): exceptions for systems that process personally identifiable information are reviewed;

- `sc-7.24_obj.d-2` (sc-7.24_smt.d): exceptions for systems that process personally identifiable information that are no longer supported are removed.

#### EXAMINE — `sc-7.24_asm-examine`

- System and communications protection policy

- procedures addressing boundary protection

- personally identifiable information processing policies

- list of key internal boundaries of the system

- system design documentation

- system configuration settings and associated documentation

- enterprise security and privacy architecture documentation

- system audit records

- system security plan

- privacy plan

- personally identifiable information inventory documentation

- data mapping documentation

- other relevant documents or records

#### INTERVIEW — `sc-7.24_asm-interview`

- System/network administrators

- organizational personnel with information security and privacy responsibilities

- system developer

- organizational personnel with boundary protection responsibilities

#### TEST — `sc-7.24_asm-test`

- Mechanisms implementing boundary protection capabilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-7.24`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sc-7`.

- Catalog relationship **related**: `pt-2`.

- Catalog relationship **related**: `si-15`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
