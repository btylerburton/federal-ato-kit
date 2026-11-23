---
title: "IR-5.1 \u2014 Automated Tracking, Data Collection, and Analysis"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-5.1 — Automated Tracking, Data Collection, and Analysis

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Automated mechanisms for tracking incidents and collecting and analyzing incident information include Computer Incident Response Centers or other electronic databases of incidents and network monitoring devices.

### Requirements and exact statement parts

- `ir-5.1_smt`: Track incidents and collect and analyze incident information using [PARAM ir-5.1_prm_1].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-5.1_smt — Track incidents and collect and analyze incident information using [PARAM ir-5.1_prm_1].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ir-5.1_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ir-05.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ir-05.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ir-05.01_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ir-5.1_smt` — For “Track incidents and collect and analyze incident information using [PARAM ir-5.1_prm_1].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ir-5.1_prm_1` — What approved value applies to **organization-defined automated mechanisms**? Record the value, scope, approving authority, and decision source.

- `ir-05.01_odp.01` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used to track incidents are defined;

- `ir-05.01_odp.02` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used to collect incident information are defined;

- `ir-05.01_odp.03` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms used to analyze incident information are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-5.1_obj-1` (ir-5.1_smt): incidents are tracked using [PARAM ir-05.01_odp.01];

- `ir-5.1_obj-2` (ir-5.1_smt): incident information is collected using [PARAM ir-05.01_odp.02];

- `ir-5.1_obj-3` (ir-5.1_smt): incident information is analyzed using [PARAM ir-05.01_odp.03].

#### EXAMINE — `ir-5.1_asm-examine`

- Incident response policy

- procedures addressing incident monitoring

- incident response records and documentation

- system security plan

- incident response plan

- other relevant documents or records

#### INTERVIEW — `ir-5.1_asm-interview`

- Organizational personnel with incident monitoring responsibilities

- organizational personnel with information security responsibilities

#### TEST — `ir-5.1_asm-test`

- Incident monitoring capability for the organization

- automated mechanisms supporting and/or implementing the tracking and documenting of system security incidents

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-5.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ir-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
