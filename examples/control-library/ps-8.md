---
title: "PS-8 \u2014 Personnel Sanctions"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PS-8 — Personnel Sanctions

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizational sanctions reflect applicable laws, executive orders, directives, regulations, policies, standards, and guidelines. Sanctions processes are described in access agreements and can be included as part of general personnel policies for organizations and/or specified in security and privacy policies. Organizations consult with the Office of the General Counsel regarding matters of employee sanctions.

### Requirements and exact statement parts

- `ps-8_smt`: Statement grouping; see child parts.

- `ps-8_smt.a`: Employ a formal sanctions process for individuals failing to comply with established information security and privacy policies and procedures; and

- `ps-8_smt.b`: Notify [PARAM ps-08_odp.01] within [PARAM ps-08_odp.02] when a formal employee sanctions process is initiated, identifying the individual sanctioned and the reason for the sanction.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ps-8_smt.a — Employ a formal sanctions process for individuals failing to comply with established information security and privacy policies and procedures; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ps-8_smt.b — Notify [PARAM ps-08_odp.01] within [PARAM ps-08_odp.02] when a formal employee sanctions process is initiated, identifying the individual sanctioned and the reason for the sanction.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ps-08_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ps-08_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ps-8_smt.a` — For “Employ a formal sanctions process for individuals failing to comply with established information security and privacy policies and procedures; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ps-8_smt.b` — For “Notify [PARAM ps-08_odp.01] within [PARAM ps-08_odp.02] when a formal employee sanctions process is initiated, identifying the individual sanctioned and the reason for the sanction.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ps-08_odp.01` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to be notified when a formal employee sanctions process is initiated is/are defined;

- `ps-08_odp.02` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the time period within which organization-defined personnel or roles must be notified when a formal employee sanctions process is initiated is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ps-8_obj.a` (ps-8_smt.a): a formal sanctions process is employed for individuals failing to comply with established information security and privacy policies and procedures;

- `ps-8_obj.b` (ps-8_smt.b): [PARAM ps-08_odp.01] is/are notified within [PARAM ps-08_odp.02] when a formal employee sanctions process is initiated, identifying the individual sanctioned and the reason for the sanction.

#### EXAMINE — `ps-8_asm-examine`

- Personnel security policy

- personnel security procedures

- procedures addressing personnel sanctions

- access agreements (including non-disclosure agreements, acceptable use agreements, rules of behavior, and conflict-of-interest agreements)

- list of personnel or roles to be notified of formal employee sanctions

- records or notifications of formal employee sanctions

- system security plan

- privacy plan

- personally identifiable information processing policy

- other relevant documents or records

#### INTERVIEW — `ps-8_asm-interview`

- Organizational personnel with personnel security responsibilities

- legal counsel

- organizational personnel with information security and privacy responsibilities

#### TEST — `ps-8_asm-test`

- Organizational processes for managing formal employee sanctions

- mechanisms supporting and/or implementing formal employee sanctions notifications

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ps-8`. The library index records the exact source revision and hash.

- Catalog relationship **related**: `pl-4`.

- Catalog relationship **related**: `pm-12`.

- Catalog relationship **related**: `ps-6`.

- Catalog relationship **related**: `pt-1`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
