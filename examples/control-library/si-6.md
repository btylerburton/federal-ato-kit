---
title: "SI-6 \u2014 Security and Privacy Function Verification"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-6 — Security and Privacy Function Verification

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Transitional states for systems include system startup, restart, shutdown, and abort. System notifications include hardware indicator lights, electronic alerts to system administrators, and messages to local computer consoles. In contrast to security function verification, privacy function verification ensures that privacy functions operate as expected and are approved by the senior agency official for privacy or that privacy attributes are applied or used as expected.

### Requirements and exact statement parts

- `si-6_smt`: Statement grouping; see child parts.

- `si-6_smt.a`: Verify the correct operation of [PARAM si-6_prm_1];

- `si-6_smt.b`: Perform the verification of the functions specified in SI-6a [PARAM si-06_odp.03];

- `si-6_smt.c`: Alert [PARAM si-06_odp.06] to failed security and privacy verification tests; and

- `si-6_smt.d`: [PARAM si-06_odp.07] when anomalies are discovered.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-6_smt.a — Verify the correct operation of [PARAM si-6_prm_1];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-6_smt.b — Perform the verification of the functions specified in SI-6a [PARAM si-06_odp.03];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-6_smt.c — Alert [PARAM si-06_odp.06] to failed security and privacy verification tests; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-6_smt.d — [PARAM si-06_odp.07] when anomalies are discovered.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-6_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-06_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-06_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-06_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-06_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-06_odp.05: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-06_odp.06: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-06_odp.07: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-06_odp.08: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-6_smt.a` — For “Verify the correct operation of [PARAM si-6_prm_1];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-6_smt.b` — For “Perform the verification of the functions specified in SI-6a [PARAM si-06_odp.03];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-6_smt.c` — For “Alert [PARAM si-06_odp.06] to failed security and privacy verification tests; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-6_smt.d` — For “[PARAM si-06_odp.07] when anomalies are discovered.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-6_prm_1` — What approved value applies to **organization-defined security and privacy functions**? Record the value, scope, approving authority, and decision source.

- `si-06_odp.01` — What approved value applies to **security functions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security functions to be verified for correct operation are defined;

- `si-06_odp.02` — What approved value applies to **privacy functions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: privacy functions to be verified for correct operation are defined;

- `si-06_odp.03` — What approved value applies to **selection; choose one-or-more from: [PARAM si-06_odp.04]; upon command by user with appropriate privilege; [PARAM si-06_odp.05]**? Record the value, scope, approving authority, and decision source.

- `si-06_odp.04` — What approved value applies to **system transitional states**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system transitional states requiring the verification of security and privacy functions are defined; (if selected)

- `si-06_odp.05` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to verify the correct operation of security and privacy functions is defined; (if selected)

- `si-06_odp.06` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to be alerted of failed security and privacy verification tests is/are defined;

- `si-06_odp.07` — What approved value applies to **selection; choose one-or-more from: shut the system down; restart the system; [PARAM si-06_odp.08]**? Record the value, scope, approving authority, and decision source.

- `si-06_odp.08` — What approved value applies to **alternative action(s)**? Record the value, scope, approving authority, and decision source.

  - Catalog context: alternative action(s) to be performed when anomalies are discovered are defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-6_obj.a-1` (si-6_smt.a): [PARAM si-06_odp.01] are verified to be operating correctly;

- `si-6_obj.a-2` (si-6_smt.a): [PARAM si-06_odp.02] are verified to be operating correctly;

- `si-6_obj.b-1` (si-6_smt.b): [PARAM si-06_odp.01] are verified [PARAM si-06_odp.03];

- `si-6_obj.b-2` (si-6_smt.b): [PARAM si-06_odp.02] are verified [PARAM si-06_odp.03];

- `si-6_obj.c-1` (si-6_smt.c): [PARAM si-06_odp.06] is/are alerted to failed security verification tests;

- `si-6_obj.c-2` (si-6_smt.c): [PARAM si-06_odp.06] is/are alerted to failed privacy verification tests;

- `si-6_obj.d` (si-6_smt.d): [PARAM si-06_odp.07] is/are initiated when anomalies are discovered.

#### EXAMINE — `si-6_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing security and privacy function verification

- system design documentation

- system configuration settings and associated documentation

- alerts/notifications of failed security verification tests

- list of system transition states requiring security functionality verification

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `si-6_asm-interview`

- Organizational personnel with security and privacy function verification responsibilities

- organizational personnel implementing, operating, and maintaining the system

- system/network administrators

- organizational personnel with information security and privacy responsibilities

- system developer

#### TEST — `si-6_asm-test`

- Organizational processes for security and privacy function verification

- mechanisms supporting and/or implementing the security and privacy function verification capability

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-6`. The library index records the exact source revision and hash.

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- Catalog relationship **related**: `ca-7`.

- Catalog relationship **related**: `cm-4`.

- Catalog relationship **related**: `cm-6`.

- Catalog relationship **related**: `si-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
