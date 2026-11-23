---
title: "SI-7.17 \u2014 Runtime Application Self-protection"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-7.17 — Runtime Application Self-protection

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Runtime application self-protection employs runtime instrumentation to detect and block the exploitation of software vulnerabilities by taking advantage of information from the software in execution. Runtime exploit prevention differs from traditional perimeter-based protections such as guards and firewalls which can only detect and block attacks by using network information without contextual awareness. Runtime application self-protection technology can reduce the susceptibility of software to attacks by monitoring its inputs and blocking those inputs that could allow attacks. It can also help protect the runtime environment from unwanted changes and tampering. When a threat is detected, runtime application self-protection technology can prevent exploitation and take other actions (e.g., sending a warning message to the user, terminating the user's session, terminating the application, or sending an alert to organizational personnel). Runtime application self-protection solutions can be deployed in either a monitor or protection mode.

### Requirements and exact statement parts

- `si-7.17_smt`: Implement [PARAM si-07.17_odp] for application self-protection at runtime.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-7.17_smt — Implement [PARAM si-07.17_odp] for application self-protection at runtime.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-07.17_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-7.17_smt` — For “Implement [PARAM si-07.17_odp] for application self-protection at runtime.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-07.17_odp` — What approved value applies to **controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controls to be implemented for application self-protection at runtime are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-7.17_obj` (si-7.17_smt): [PARAM si-07.17_odp] are implemented for application self-protection at runtime.

#### EXAMINE — `si-7.17_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing software and information integrity

- system design documentation

- system configuration settings and associated documentation

- list of known vulnerabilities addressed by runtime instrumentation

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-7.17_asm-interview`

- Organizational personnel responsible for software, firmware, and/or information integrity

- organizational personnel with information security responsibilities

- system/network administrators

- system developer

#### TEST — `si-7.17_asm-test`

- Software, firmware, and information integrity verification tools

- mechanisms supporting and/or implementing runtime application self-protection

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-7.17`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-7`.

- Catalog relationship **related**: `si-16`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
