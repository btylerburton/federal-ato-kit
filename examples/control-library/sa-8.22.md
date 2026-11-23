---
title: "SA-8.22 \u2014 Accountability and Traceability"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-8.22 — Accountability and Traceability

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The principle of accountability and traceability states that it is possible to trace security-relevant actions (i.e., subject-object interactions) to the entity on whose behalf the action is being taken. The principle of accountability and traceability requires a trustworthy infrastructure that can record details about actions that affect system security (e.g., an audit subsystem). To record the details about actions, the system is able to uniquely identify the entity on whose behalf the action is being carried out and also record the relevant sequence of actions that are carried out. The accountability policy also requires that audit trail itself be protected from unauthorized access and modification. The principle of least privilege assists in tracing the actions to particular entities, as it increases the granularity of accountability. Associating specific actions with system entities, and ultimately with users, and making the audit trail secure against unauthorized access and modifications provide non-repudiation because once an action is recorded, it is not possible to change the audit trail. Another important function that accountability and traceability serves is in the routine and forensic analysis of events associated with the violation of security policy. Analysis of audit logs may provide additional information that may be helpful in determining the path or component that allowed the violation of the security policy and the actions of individuals associated with the violation of the security policy.

### Requirements and exact statement parts

- `sa-8.22_smt`: Implement the security design principle of accountability and traceability in [PARAM sa-8.22_prm_1].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-8.22_smt — Implement the security design principle of accountability and traceability in [PARAM sa-8.22_prm_1].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sa-8.22_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sa-08.22_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sa-08.22_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sa-8.22_smt` — For “Implement the security design principle of accountability and traceability in [PARAM sa-8.22_prm_1].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sa-8.22_prm_1` — What approved value applies to **organization-defined systems or system components**? Record the value, scope, approving authority, and decision source.

- `sa-08.22_odp.01` — What approved value applies to **systems or system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems or system components that implement the security design principle of accountability are defined;

- `sa-08.22_odp.02` — What approved value applies to **systems or system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems or system components that implement the security design principle of traceability are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-8.22_obj-1` (sa-8.22_smt): [PARAM sa-08.22_odp.01] implement the security design principle of accountability;

- `sa-8.22_obj-2` (sa-8.22_smt): [PARAM sa-08.22_odp.02] implement the security design principle of traceability.

#### EXAMINE — `sa-8.22_asm-examine`

- System and services acquisition policy

- audit and accountability policy

- access control policy

- procedures addressing least privilege

- procedures addressing auditable events

- identification and authentication policy

- procedures addressing user identification and authentication

- procedures addressing the security design principle of accountability and traceability used in the specification, design, development, implementation, and modification of the system

- system design documentation

- system audit records

- system auditable events

- system configuration settings and associated documentation

- security and privacy requirements and specifications for the system

- system security and privacy architecture

- system security plan

- other relevant documents or records

#### INTERVIEW — `sa-8.22_asm-interview`

- Organizational personnel with the responsibility for determining system security and privacy requirements

- organizational personnel with audit and accountability responsibilities

- organizational personnel with system specification, design, development, implementation, and modification responsibilities

- system developers

- organizational personnel with information security responsibilities

#### TEST — `sa-8.22_asm-test`

- Organizational processes for applying the security design principle of accountability and traceability in system specification, design, development, implementation, and modification

- mechanisms supporting the application of the security design principle of accountability and traceability in system specification, design, development, implementation, and modification

- mechanisms implementing information system auditing

- mechanisms implementing least privilege functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-8.22`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-8`.

- Catalog relationship **related**: `ac-6`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-3`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-9`.

- Catalog relationship **related**: `au-10`.

- Catalog relationship **related**: `au-12`.

- Catalog relationship **related**: `ia-2`.

- Catalog relationship **related**: `ir-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
