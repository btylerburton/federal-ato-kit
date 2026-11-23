---
title: "CP-4.5 \u2014 Self-challenge"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-4.5 — Self-challenge

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Often, the best method of assessing system resilience is to disrupt the system in some manner. The mechanisms used by the organization could disrupt system functions or system services in many ways, including terminating or disabling critical system components, changing the configuration of system components, degrading critical functionality (e.g., restricting network bandwidth), or altering privileges. Automated, on-going, and simulated cyber-attacks and service disruptions can reveal unexpected functional dependencies and help the organization determine its ability to ensure resilience in the face of an actual cyber-attack.

### Requirements and exact statement parts

- `cp-4.5_smt`: Employ [PARAM cp-04.05_odp.01] to [PARAM cp-04.05_odp.02] to disrupt and adversely affect the system or system component.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-4.5_smt — Employ [PARAM cp-04.05_odp.01] to [PARAM cp-04.05_odp.02] to disrupt and adversely affect the system or system component.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cp-04.05_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-04.05_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cp-4.5_smt` — For “Employ [PARAM cp-04.05_odp.01] to [PARAM cp-04.05_odp.02] to disrupt and adversely affect the system or system component.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cp-04.05_odp.01` — What approved value applies to **mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: mechanisms employed to disrupt and adversely affect the system or system component are defined;

- `cp-04.05_odp.02` — What approved value applies to **system or system component**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system or system component on which to apply disruption mechanisms are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-4.5_obj` (cp-4.5_smt): [PARAM cp-04.05_odp.01] are employed to disrupt and adversely affect the [PARAM cp-04.05_odp.02].

#### EXAMINE — `cp-4.5_asm-examine`

- Contingency planning policy

- procedures addressing system recovery and reconstitution

- contingency plan

- contingency plan test documentation

- contingency plan test results

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-4.5_asm-interview`

- Organizational personnel with contingency plan testing responsibilities

- organizational personnel with system recovery and reconstitution responsibilities

- organizational personnel with information security responsibilities

#### TEST — `cp-4.5_asm-test`

- Organizational processes for contingency plan testing

- mechanisms supporting contingency plan testing

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-4.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cp-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
