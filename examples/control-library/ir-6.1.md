---
title: "IR-6.1 \u2014 Automated Reporting"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-6.1 — Automated Reporting

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The recipients of incident reports are specified in IR-6b (catalog reference: `#ir-6_smt.b`) . Automated reporting mechanisms include email, posting on websites (with automatic updates), and automated incident response tools and programs.

### Requirements and exact statement parts

- `ir-6.1_smt`: Report incidents using [PARAM ir-06.01_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-6.1_smt — Report incidents using [PARAM ir-06.01_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ir-06.01_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ir-6.1_smt` — For “Report incidents using [PARAM ir-06.01_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ir-06.01_odp` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used for reporting incidents are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-6.1_obj` (ir-6.1_smt): incidents are reported using [PARAM ir-06.01_odp].

#### EXAMINE — `ir-6.1_asm-examine`

- Incident response policy

- procedures addressing incident reporting

- automated mechanisms supporting incident reporting

- system design documentation

- system configuration settings and associated documentation

- incident response plan

- system security plan

- other relevant documents or records

#### INTERVIEW — `ir-6.1_asm-interview`

- Organizational personnel with incident reporting responsibilities

- organizational personnel with information security responsibilities

#### TEST — `ir-6.1_asm-test`

- Organizational processes for incident reporting

- automated mechanisms supporting and/or implementing the reporting of security incidents

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-6.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ir-6`.

- Catalog relationship **related**: `ir-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
