---
title: "AC-7.3 \u2014 Biometric Attempt Limiting"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-7.3 — Biometric Attempt Limiting

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Biometrics are probabilistic in nature. The ability to successfully authenticate can be impacted by many factors, including matching performance and presentation attack detection mechanisms. Organizations select the appropriate number of attempts for users based on organizationally-defined factors.

### Requirements and exact statement parts

- `ac-7.3_smt`: Limit the number of unsuccessful biometric logon attempts to [PARAM ac-07.03_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-7.3_smt — Limit the number of unsuccessful biometric logon attempts to [PARAM ac-07.03_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-07.03_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-7.3_smt` — For “Limit the number of unsuccessful biometric logon attempts to [PARAM ac-07.03_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-07.03_odp` — What approved value applies to **number**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the number of unsuccessful biometric logon attempts is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-7.3_obj` (ac-7.3_smt): unsuccessful biometric logon attempts are limited to [PARAM ac-07.03_odp].

#### EXAMINE — `ac-7.3_asm-examine`

- Access control policy

- procedures addressing unsuccessful logon attempts on biometric devices

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-7.3_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

#### TEST — `ac-7.3_asm-test`

- Mechanisms implementing access control policy for unsuccessful logon attempts

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-7.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-7`.

- Catalog relationship **related**: `ia-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
