---
title: "IA-2.10 \u2014 Single Sign-on"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-2.10 — Single Sign-on

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Single sign-on enables users to log in once and gain access to multiple system resources. Organizations consider the operational efficiencies provided by single sign-on capabilities with the risk introduced by allowing access to multiple systems via a single authentication event. Single sign-on can present opportunities to improve system security, for example by providing the ability to add multi-factor authentication for applications and systems (existing and new) that may not be able to natively support multi-factor authentication.

### Requirements and exact statement parts

- `ia-2.10_smt`: Provide a single sign-on capability for [PARAM ia-02.10_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-2.10_smt — Provide a single sign-on capability for [PARAM ia-02.10_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ia-02.10_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ia-2.10_smt` — For “Provide a single sign-on capability for [PARAM ia-02.10_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ia-02.10_odp` — What approved value applies to **system accounts and services**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system accounts and services for which a single sign-on capability must be provided are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-2.10_obj` (ia-2.10_smt): a single sign-on capability is provided for [PARAM ia-02.10_odp].

#### EXAMINE — `ia-2.10_asm-examine`

- Identification and authentication policy

- system security plan

- procedures addressing single sign-on capability for system accounts and services

- procedures addressing identification and authentication

- system design documentation

- system configuration settings and associated documentation

- system audit records

- list of system accounts and services requiring single sign-on capability

- other relevant documents or records

#### INTERVIEW — `ia-2.10_asm-interview`

- Organizational personnel with system operations responsibilities

- organizational personnel with account management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `ia-2.10_asm-test`

- Mechanisms supporting and/or implementing identification and authentication capabilities

- mechanisms supporting and/or implementing single sign-on capability for system accounts and services

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-2.10`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
