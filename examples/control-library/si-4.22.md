---
title: "SI-4.22 \u2014 Unauthorized Network Services"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-4.22 — Unauthorized Network Services

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Unauthorized or unapproved network services include services in service-oriented architectures that lack organizational verification or validation and may therefore be unreliable or serve as malicious rogues for valid services.

### Requirements and exact statement parts

- `si-4.22_smt`: Statement grouping; see child parts.

- `si-4.22_smt.a`: Detect network services that have not been authorized or approved by [PARAM si-04.22_odp.01] ; and

- `si-4.22_smt.b`: [PARAM si-04.22_odp.02] when detected.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-4.22_smt.a — Detect network services that have not been authorized or approved by [PARAM si-04.22_odp.01] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-4.22_smt.b — [PARAM si-04.22_odp.02] when detected.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-04.22_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-04.22_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-04.22_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-4.22_smt.a` — For “Detect network services that have not been authorized or approved by [PARAM si-04.22_odp.01] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-4.22_smt.b` — For “[PARAM si-04.22_odp.02] when detected.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-04.22_odp.01` — What approved value applies to **authorization or approval processes**? Record the value, scope, approving authority, and decision source.

  - Catalog context: authorization or approval processes for network services are defined;

- `si-04.22_odp.02` — What approved value applies to **selection; choose one-or-more from: audit; alert [PARAM si-04.22_odp.03]**? Record the value, scope, approving authority, and decision source.

- `si-04.22_odp.03` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to be alerted upon the detection of network services that have not been authorized or approved by authorization or approval processes is/are defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-4.22_obj.a` (si-4.22_smt.a): network services that have not been authorized or approved by [PARAM si-04.22_odp.01] are detected;

- `si-4.22_obj.b` (si-4.22_smt.b): [PARAM si-04.22_odp.02] is/are initiated when network services that have not been authorized or approved by authorization or approval processes are detected.

#### EXAMINE — `si-4.22_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing system monitoring tools and techniques

- system design documentation

- system monitoring tools and techniques documentation

- system configuration settings and associated documentation

- documented authorization/approval of network services

- notifications or alerts of unauthorized network services

- system monitoring logs or records

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-4.22_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developer

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for monitoring the system

#### TEST — `si-4.22_asm-test`

- Organizational processes for system monitoring

- mechanisms supporting and/or implementing a system monitoring capability

- mechanisms for auditing network services

- mechanisms for providing alerts

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-4.22`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-4`.

- Catalog relationship **related**: `cm-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
