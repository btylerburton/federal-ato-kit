---
title: "CM-3.7 \u2014 Review System Changes"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-3.7 — Review System Changes

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Indications that warrant a review of changes to the system and the specific circumstances justifying such reviews may be obtained from activities carried out by organizations during the configuration change process or continuous monitoring process.

### Requirements and exact statement parts

- `cm-3.7_smt`: Review changes to the system [PARAM cm-03.07_odp.01] or when [PARAM cm-03.07_odp.02] to determine whether unauthorized changes have occurred.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-3.7_smt — Review changes to the system [PARAM cm-03.07_odp.01] or when [PARAM cm-03.07_odp.02] to determine whether unauthorized changes have occurred.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-03.07_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-03.07_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-3.7_smt` — For “Review changes to the system [PARAM cm-03.07_odp.01] or when [PARAM cm-03.07_odp.02] to determine whether unauthorized changes have occurred.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-03.07_odp.01` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which changes are to be reviewed is defined;

- `cm-03.07_odp.02` — What approved value applies to **circumstances**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the circumstances under which changes are to be reviewed are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-3.7_obj` (cm-3.7_smt): changes to the system are reviewed [PARAM cm-03.07_odp.01] or when [PARAM cm-03.07_odp.02] to determine whether unauthorized changes have occurred.

#### EXAMINE — `cm-3.7_asm-examine`

- Configuration management policy

- procedures addressing system configuration change control

- configuration management plan

- change control records

- system architecture and configuration documentation

- system configuration settings and associated documentation

- system audit records

- system component inventory

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-3.7_asm-interview`

- Organizational personnel with configuration change control responsibilities

- organizational personnel with security responsibilities

- system/network administrators

- members of change control board or similar

#### TEST — `cm-3.7_asm-test`

- Organizational processes for configuration change control

- mechanisms implementing audit records for changes

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-3.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-3`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-7`.

- Catalog relationship **related**: `cm-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
