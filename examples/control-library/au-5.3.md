---
title: "AU-5.3 \u2014 Configurable Traffic Volume Thresholds"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-5.3 — Configurable Traffic Volume Thresholds

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations have the capability to reject or delay the processing of network communications traffic if audit logging information about such traffic is determined to exceed the storage capacity of the system audit logging function. The rejection or delay response is triggered by the established organizational traffic volume thresholds that can be adjusted based on changes to audit log storage capacity.

### Requirements and exact statement parts

- `au-5.3_smt`: Enforce configurable network communications traffic volume thresholds reflecting limits on audit log storage capacity and [PARAM au-05.03_odp] network traffic above those thresholds.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-5.3_smt — Enforce configurable network communications traffic volume thresholds reflecting limits on audit log storage capacity and [PARAM au-05.03_odp] network traffic above those thresholds.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-05.03_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-5.3_smt` — For “Enforce configurable network communications traffic volume thresholds reflecting limits on audit log storage capacity and [PARAM au-05.03_odp] network traffic above those thresholds.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-05.03_odp` — What approved value applies to **selection; choose one-or-more from: reject; delay**? Record the value, scope, approving authority, and decision source.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-5.3_obj-1` (au-5.3_smt): configurable network communications traffic volume thresholds reflecting limits on audit log storage capacity are enforced;

- `au-5.3_obj-2` (au-5.3_smt): network traffic is [PARAM au-05.03_odp] if network traffic volume is above configured thresholds.

#### EXAMINE — `au-5.3_asm-examine`

- Audit and accountability policy

- procedures addressing response to audit processing failures

- system design documentation

- system security plan

- privacy plan

- system configuration settings and associated documentation

- system audit records

- other relevant documents or records

#### INTERVIEW — `au-5.3_asm-interview`

- Organizational personnel with audit and accountability responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

- system developers

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-5.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `au-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
