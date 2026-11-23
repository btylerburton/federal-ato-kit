---
title: "SI-6.3 \u2014 Report Verification Results"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-6.3 — Report Verification Results

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizational personnel with potential interest in the results of the verification of security and privacy functions include systems security officers, senior agency information security officers, and senior agency officials for privacy.

### Requirements and exact statement parts

- `si-6.3_smt`: Report the results of security and privacy function verification to [PARAM si-06.03_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-6.3_smt — Report the results of security and privacy function verification to [PARAM si-06.03_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-06.03_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-6.3_smt` — For “Report the results of security and privacy function verification to [PARAM si-06.03_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-06.03_odp` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles designated to receive the results of security and privacy function verification is/are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-6.3_obj-1` (si-6.3_smt): the results of security function verification are reported to [PARAM si-06.03_odp];

- `si-6.3_obj-2` (si-6.3_smt): the results of privacy function verification are reported to [PARAM si-06.03_odp].

#### EXAMINE — `si-6.3_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing security and privacy function verification

- system design documentation

- system configuration settings and associated documentation

- reports of security and privacy function verification results

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `si-6.3_asm-interview`

- Organizational personnel with security and privacy function verification responsibilities

- organizational personnel who are recipients of security and privacy function verification reports

- organizational personnel with information security and privacy responsibilities

#### TEST — `si-6.3_asm-test`

- Organizational processes for reporting security and privacy function verification results

- mechanisms supporting and/or implementing the reporting of security and privacy function verification results

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-6.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-6`.

- Catalog relationship **related**: `si-4`.

- Catalog relationship **related**: `sr-4`.

- Catalog relationship **related**: `sr-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
