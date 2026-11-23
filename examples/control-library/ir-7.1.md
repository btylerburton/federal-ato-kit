---
title: "IR-7.1 \u2014 Automation Support for Availability of Information and Support"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-7.1 — Automation Support for Availability of Information and Support

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Automated mechanisms can provide a push or pull capability for users to obtain incident response assistance. For example, individuals may have access to a website to query the assistance capability, or the assistance capability can proactively send incident response information to users (general distribution or targeted) as part of increasing understanding of current response capabilities and support.

### Requirements and exact statement parts

- `ir-7.1_smt`: Increase the availability of incident response information and support using [PARAM ir-07.01_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-7.1_smt — Increase the availability of incident response information and support using [PARAM ir-07.01_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ir-07.01_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ir-7.1_smt` — For “Increase the availability of incident response information and support using [PARAM ir-07.01_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ir-07.01_odp` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used to increase the availability of incident response information and support are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-7.1_obj` (ir-7.1_smt): the availability of incident response information and support is increased using [PARAM ir-07.01_odp].

#### EXAMINE — `ir-7.1_asm-examine`

- Incident response policy

- procedures addressing incident response assistance

- automated mechanisms supporting incident response support and assistance

- system design documentation

- system configuration settings and associated documentation

- incident response plan

- system security plan

- other relevant documents or records

#### INTERVIEW — `ir-7.1_asm-interview`

- Organizational personnel with incident response support and assistance responsibilities

- organizational personnel with access to incident response support and assistance capability

- organizational personnel with information security responsibilities

#### TEST — `ir-7.1_asm-test`

- Organizational processes for incident response assistance

- automated mechanisms supporting and/or implementing an increase in the availability of incident response information and support

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-7.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ir-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
