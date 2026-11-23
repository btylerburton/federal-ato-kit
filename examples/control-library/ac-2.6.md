---
title: "AC-2.6 \u2014 Dynamic Privilege Management"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-2.6 — Dynamic Privilege Management

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

In contrast to access control approaches that employ static accounts and predefined user privileges, dynamic access control approaches rely on runtime access control decisions facilitated by dynamic privilege management, such as attribute-based access control. While user identities remain relatively constant over time, user privileges typically change more frequently based on ongoing mission or business requirements and the operational needs of organizations. An example of dynamic privilege management is the immediate revocation of privileges from users as opposed to requiring that users terminate and restart their sessions to reflect changes in privileges. Dynamic privilege management can also include mechanisms that change user privileges based on dynamic rules as opposed to editing specific user profiles. Examples include automatic adjustments of user privileges if they are operating out of their normal work times, if their job function or assignment changes, or if systems are under duress or in emergency situations. Dynamic privilege management includes the effects of privilege changes, for example, when there are changes to encryption keys used for communications.

### Requirements and exact statement parts

- `ac-2.6_smt`: Implement [PARAM ac-02.06_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-2.6_smt — Implement [PARAM ac-02.06_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-02.06_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-2.6_smt` — For “Implement [PARAM ac-02.06_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-02.06_odp` — What approved value applies to **dynamic privilege management capabilities**? Record the value, scope, approving authority, and decision source.

  - Catalog context: dynamic privilege management capabilities are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-2.6_obj` (ac-2.6_smt): [PARAM ac-02.06_odp] are implemented.

#### EXAMINE — `ac-2.6_asm-examine`

- Access control policy

- procedures addressing account management

- system design documentation

- system configuration settings and associated documentation

- system-generated list of dynamic privilege management capabilities

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-2.6_asm-interview`

- Organizational personnel with account management responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

- system developers

#### TEST — `ac-2.6_asm-test`

- system or mechanisms implementing dynamic privilege management capabilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-2.6`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-2`.

- Catalog relationship **related**: `ac-16`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
