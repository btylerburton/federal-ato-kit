---
title: "SI-2.2 \u2014 Automated Flaw Remediation Status"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-2.2 — Automated Flaw Remediation Status

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Automated mechanisms can track and determine the status of known flaws for system components.

### Requirements and exact statement parts

- `si-2.2_smt`: Determine if system components have applicable security-relevant software and firmware updates installed using [PARAM si-02.02_odp.01] [PARAM si-02.02_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-2.2_smt — Determine if system components have applicable security-relevant software and firmware updates installed using [PARAM si-02.02_odp.01] [PARAM si-02.02_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-02.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-02.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-2.2_smt` — For “Determine if system components have applicable security-relevant software and firmware updates installed using [PARAM si-02.02_odp.01] [PARAM si-02.02_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-02.02_odp.01` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms to determine if applicable security-relevant software and firmware updates are installed on system components are defined;

- `si-02.02_odp.02` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which to determine if applicable security-relevant software and firmware updates are installed on system components is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-2.2_obj` (si-2.2_smt): system components have applicable security-relevant software and firmware updates installed [PARAM si-02.02_odp.02] using [PARAM si-02.02_odp.01].

#### EXAMINE — `si-2.2_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing flaw remediation

- automated mechanisms supporting centralized management of flaw remediation

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-2.2_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for flaw remediation

#### TEST — `si-2.2_asm-test`

- Automated mechanisms used to determine the state of system components with regard to flaw remediation

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-2.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-2`.

- Catalog relationship **related**: `ca-7`.

- Catalog relationship **related**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
