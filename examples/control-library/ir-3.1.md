---
title: "IR-3.1 \u2014 Automated Testing"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-3.1 — Automated Testing

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations use automated mechanisms to more thoroughly and effectively test incident response capabilities. This can be accomplished by providing more complete coverage of incident response issues, selecting realistic test scenarios and environments, and stressing the response capability.

### Requirements and exact statement parts

- `ir-3.1_smt`: Test the incident response capability using [PARAM ir-03.01_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-3.1_smt — Test the incident response capability using [PARAM ir-03.01_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ir-03.01_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ir-3.1_smt` — For “Test the incident response capability using [PARAM ir-03.01_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ir-03.01_odp` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used to test the incident response capability are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-3.1_obj` (ir-3.1_smt): the incident response capability is tested using [PARAM ir-03.01_odp].

#### EXAMINE — `ir-3.1_asm-examine`

- Incident response policy

- contingency planning policy

- procedures addressing incident response testing

- procedures addressing contingency plan testing

- incident response testing documentation

- incident response test results

- incident response test plan

- incident response plan

- contingency plan

- system security plan

- automated mechanisms supporting incident response tests

- other relevant documents or records

#### INTERVIEW — `ir-3.1_asm-interview`

- Organizational personnel with incident response testing responsibilities

- organizational personnel with information security responsibilities

#### TEST — `ir-3.1_asm-test`

- Automated mechanisms that more thoroughly and effectively test the incident response capability

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-3.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ir-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
