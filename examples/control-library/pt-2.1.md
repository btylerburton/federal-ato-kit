---
title: "PT-2.1 \u2014 Data Tagging"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PT-2.1 — Data Tagging

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Data tags support the tracking and enforcement of authorized processing by conveying the types of processing that are authorized along with the relevant elements of personally identifiable information throughout the system. Data tags may also support the use of automated tools.

### Requirements and exact statement parts

- `pt-2.1_smt`: Attach data tags containing [PARAM pt-02.01_odp.01] to [PARAM pt-02.01_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pt-2.1_smt — Attach data tags containing [PARAM pt-02.01_odp.01] to [PARAM pt-02.01_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pt-02.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pt-02.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pt-2.1_smt` — For “Attach data tags containing [PARAM pt-02.01_odp.01] to [PARAM pt-02.01_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pt-02.01_odp.01` — What approved value applies to **authorized processing**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the authorized processing of personally identifiable information is defined;

- `pt-02.01_odp.02` — What approved value applies to **elements of personally identifiable information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: elements of personally identifiable information to be tagged are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pt-2.1_obj` (pt-2.1_smt): data tags containing [PARAM pt-02.01_odp.01] are attached to [PARAM pt-02.01_odp.02].

#### EXAMINE — `pt-2.1_asm-examine`

- Personally identifiable information processing and transparency policy and procedures including procedures addressing data tagging

- data tag definitions

- documented requirements for use and monitoring of data tagging

- data extracts with corresponding data tags

- privacy plan

- other relevant documents or records

#### INTERVIEW — `pt-2.1_asm-interview`

- Organizational personnel with personally identifiable information processing and transparency responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `pt-2.1_asm-test`

- Organizational processes for authorizing the processing of personally identifiable information

- organizational processes for data tagging

- mechanisms for applying and monitoring data tagging

- mechanisms supporting and/or implementing the restriction of personally identifiable information processing

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pt-2.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pt-2`.

- Catalog relationship **related**: `ac-16`.

- Catalog relationship **related**: `ca-6`.

- Catalog relationship **related**: `cm-12`.

- Catalog relationship **related**: `pm-5`.

- Catalog relationship **related**: `pm-22`.

- Catalog relationship **related**: `pt-4`.

- Catalog relationship **related**: `sc-16`.

- Catalog relationship **related**: `sc-43`.

- Catalog relationship **related**: `si-10`.

- Catalog relationship **related**: `si-15`.

- Catalog relationship **related**: `si-19`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
