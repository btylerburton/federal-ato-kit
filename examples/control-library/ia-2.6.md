---
title: "IA-2.6 \u2014 Access to Accounts \u2014separate Device"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-2.6 — Access to Accounts —separate Device

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The purpose of requiring a device that is separate from the system to which the user is attempting to gain access for one of the factors during multi-factor authentication is to reduce the likelihood of compromising authenticators or credentials stored on the system. Adversaries may be able to compromise such authenticators or credentials and subsequently impersonate authorized users. Implementing one of the factors on a separate device (e.g., a hardware token), provides a greater strength of mechanism and an increased level of assurance in the authentication process.

### Requirements and exact statement parts

- `ia-2.6_smt`: Implement multi-factor authentication for [PARAM ia-02.06_odp.01] access to [PARAM ia-02.06_odp.02] such that:

- `ia-2.6_smt.a`: One of the factors is provided by a device separate from the system gaining access; and

- `ia-2.6_smt.b`: The device meets [PARAM ia-02.06_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-2.6_smt — Implement multi-factor authentication for [PARAM ia-02.06_odp.01] access to [PARAM ia-02.06_odp.02] such that:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-2.6_smt.a — One of the factors is provided by a device separate from the system gaining access; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-2.6_smt.b — The device meets [PARAM ia-02.06_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ia-02.06_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ia-02.06_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ia-02.06_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ia-2.6_smt` — For “Implement multi-factor authentication for [PARAM ia-02.06_odp.01] access to [PARAM ia-02.06_odp.02] such that:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-2.6_smt.a` — For “One of the factors is provided by a device separate from the system gaining access; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-2.6_smt.b` — For “The device meets [PARAM ia-02.06_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ia-02.06_odp.01` — What approved value applies to **selection; choose one-or-more from: local; network; remote**? Record the value, scope, approving authority, and decision source.

- `ia-02.06_odp.02` — What approved value applies to **selection; choose one-or-more from: privileged accounts; non-privileged accounts**? Record the value, scope, approving authority, and decision source.

- `ia-02.06_odp.03` — What approved value applies to **strength of mechanism requirements**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the strength of mechanism requirements to be enforced by a device separate from the system gaining access to accounts is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-2.6_obj.a` (ia-2.6_smt.a): multi-factor authentication is implemented for [PARAM ia-02.06_odp.01] access to [PARAM ia-02.06_odp.02] such that one of the factors is provided by a device separate from the system gaining access;

- `ia-2.6_obj.b` (ia-2.6_smt.b): multi-factor authentication is implemented for [PARAM ia-02.06_odp.01] access to [PARAM ia-02.06_odp.02] such that the device meets [PARAM ia-02.06_odp.03].

#### EXAMINE — `ia-2.6_asm-examine`

- Identification and authentication policy

- system security plan

- procedures addressing user identification and authentication

- system design documentation

- system configuration settings and associated documentation

- system audit records

- list of system accounts

- other relevant documents or records

#### INTERVIEW — `ia-2.6_asm-interview`

- Organizational personnel with system operations responsibilities

- organizational personnel with account management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `ia-2.6_asm-test`

- Mechanisms supporting and/or implementing multi-factor authentication capability

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-2.6`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-2`.

- Catalog relationship **related**: `ac-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
