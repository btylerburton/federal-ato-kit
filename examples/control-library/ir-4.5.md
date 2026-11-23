---
title: "IR-4.5 \u2014 Automatic Disabling of System"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-4.5 — Automatic Disabling of System

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations consider whether the capability to automatically disable the system conflicts with continuity of operations requirements specified as part of CP-2 (catalog reference: `#cp-2`) or IR-4(3) (catalog reference: `#ir-4.3`) . Security violations include cyber-attacks that have compromised the integrity of the system or exfiltrated organizational information and serious errors in software programs that could adversely impact organizational missions or functions or jeopardize the safety of individuals.

### Requirements and exact statement parts

- `ir-4.5_smt`: Implement a configurable capability to automatically disable the system if [PARAM ir-04.05_odp] are detected.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-4.5_smt — Implement a configurable capability to automatically disable the system if [PARAM ir-04.05_odp] are detected.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ir-04.05_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ir-4.5_smt` — For “Implement a configurable capability to automatically disable the system if [PARAM ir-04.05_odp] are detected.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ir-04.05_odp` — What approved value applies to **security violations**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security violations that automatically disable a system are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-4.5_obj` (ir-4.5_smt): a configurable capability is implemented to automatically disable the system if [PARAM ir-04.05_odp] are detected.

#### EXAMINE — `ir-4.5_asm-examine`

- Incident response policy

- procedures addressing incident handling

- automated mechanisms supporting incident handling

- system design documentation

- system configuration settings and associated documentation

- system security plan

- incident response plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ir-4.5_asm-interview`

- Organizational personnel with incident handling responsibilities

- organizational personnel with information security responsibilities

- system developers

#### TEST — `ir-4.5_asm-test`

- Incident handling capability for the organization

- automated mechanisms supporting and/or implementing automatic disabling of the system

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-4.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ir-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
