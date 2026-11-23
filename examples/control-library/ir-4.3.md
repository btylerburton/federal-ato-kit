---
title: "IR-4.3 \u2014 Continuity of Operations"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-4.3 — Continuity of Operations

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Classes of incidents include malfunctions due to design or implementation errors and omissions, targeted malicious attacks, and untargeted malicious attacks. Incident response actions include orderly system degradation, system shutdown, fall back to manual mode or activation of alternative technology whereby the system operates differently, employing deceptive measures, alternate information flows, or operating in a mode that is reserved for when systems are under attack. Organizations consider whether continuity of operations requirements during an incident conflict with the capability to automatically disable the system as specified as part of IR-4(5) (catalog reference: `#ir-4.5`).

### Requirements and exact statement parts

- `ir-4.3_smt`: Identify [PARAM ir-04.03_odp.01] and take the following actions in response to those incidents to ensure continuation of organizational mission and business functions: [PARAM ir-04.03_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-4.3_smt — Identify [PARAM ir-04.03_odp.01] and take the following actions in response to those incidents to ensure continuation of organizational mission and business functions: [PARAM ir-04.03_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ir-04.03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ir-04.03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ir-4.3_smt` — For “Identify [PARAM ir-04.03_odp.01] and take the following actions in response to those incidents to ensure continuation of organizational mission and business functions: [PARAM ir-04.03_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ir-04.03_odp.01` — What approved value applies to **classes of incidents**? Record the value, scope, approving authority, and decision source.

  - Catalog context: classes of incidents requiring an organization-defined action (defined in IR-04(03)_ODP[02]) to be taken are defined;

- `ir-04.03_odp.02` — What approved value applies to **actions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: actions to be taken in response to organization-defined classes of incidents are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-4.3_obj-1` (ir-4.3_smt): [PARAM ir-04.03_odp.01] are identified;

- `ir-4.3_obj-2` (ir-4.3_smt): [PARAM ir-04.03_odp.02] are taken in response to those incidents (defined in IR-04(03)_ODP[01]) to ensure the continuation of organizational mission and business functions.

#### EXAMINE — `ir-4.3_asm-examine`

- Incident response policy

- procedures addressing incident handling

- incident response plan

- privacy plan

- list of classes of incidents

- list of appropriate incident response actions

- system security plan

- other relevant documents or records

#### INTERVIEW — `ir-4.3_asm-interview`

- Organizational personnel with incident handling responsibilities

- organizational personnel with information security responsibilities

#### TEST — `ir-4.3_asm-test`

- Mechanisms that support and/or implement continuity of operations

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-4.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ir-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
