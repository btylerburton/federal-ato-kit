---
title: "RA-5.6 \u2014 Automated Trend Analyses"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# RA-5.6 — Automated Trend Analyses

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Using automated mechanisms to analyze multiple vulnerability scans over time can help determine trends in system vulnerabilities and identify patterns of attack.

### Requirements and exact statement parts

- `ra-5.6_smt`: Compare the results of multiple vulnerability scans using [PARAM ra-05.06_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ra-5.6_smt — Compare the results of multiple vulnerability scans using [PARAM ra-05.06_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ra-05.06_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ra-5.6_smt` — For “Compare the results of multiple vulnerability scans using [PARAM ra-05.06_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ra-05.06_odp` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms to compare the results of multiple vulnerability scans are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ra-5.6_obj` (ra-5.6_smt): the results of multiple vulnerability scans are compared using [PARAM ra-05.06_odp].

#### EXAMINE — `ra-5.6_asm-examine`

- Risk assessment policy

- procedures addressing vulnerability scanning

- system design documentation

- vulnerability scanning tools and techniques documentation

- vulnerability scanning results

- system security plan

- other relevant documents or records

#### INTERVIEW — `ra-5.6_asm-interview`

- Organizational personnel with vulnerability scanning responsibilities

- organizational personnel with vulnerability scan analysis responsibilities

- organizational personnel with security responsibilities

#### TEST — `ra-5.6_asm-test`

- Organizational processes for vulnerability scanning

- automated mechanisms/tools supporting and/or implementing vulnerability scanning

- automated mechanisms supporting and/or implementing trend analysis of vulnerability scan results

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ra-5.6`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ra-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
