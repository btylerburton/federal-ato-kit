---
title: "SI-3.6 \u2014 Testing and Verification"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-3.6 — Testing and Verification

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

None.

### Requirements and exact statement parts

- `si-3.6_smt`: Statement grouping; see child parts.

- `si-3.6_smt.a`: Test malicious code protection mechanisms [PARAM si-03.06_odp] by introducing known benign code into the system; and

- `si-3.6_smt.b`: Verify that the detection of the code and the associated incident reporting occur.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-3.6_smt.a — Test malicious code protection mechanisms [PARAM si-03.06_odp] by introducing known benign code into the system; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-3.6_smt.b — Verify that the detection of the code and the associated incident reporting occur.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-03.06_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-3.6_smt.a` — For “Test malicious code protection mechanisms [PARAM si-03.06_odp] by introducing known benign code into the system; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-3.6_smt.b` — For “Verify that the detection of the code and the associated incident reporting occur.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-03.06_odp` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which to test malicious code protection mechanisms is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-3.6_obj.a` (si-3.6_smt.a): malicious code protection mechanisms are tested [PARAM si-03.06_odp] by introducing known benign code into the system;

- `si-3.6_obj.b-1` (si-3.6_smt.b): the detection of (benign test) code occurs;

- `si-3.6_obj.b-2` (si-3.6_smt.b): the associated incident reporting occurs.

#### EXAMINE — `si-3.6_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing malicious code protection

- system design documentation

- system configuration settings and associated documentation

- test cases

- records providing evidence of test cases executed on malicious code protection mechanisms

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-3.6_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for malicious code protection

#### TEST — `si-3.6_asm-test`

- Mechanisms supporting and/or implementing the testing and verification of malicious code protection capabilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-3.6`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-3`.

- Catalog relationship **related**: `ca-2`.

- Catalog relationship **related**: `ca-7`.

- Catalog relationship **related**: `ra-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
