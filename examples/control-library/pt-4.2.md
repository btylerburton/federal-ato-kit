---
title: "PT-4.2 \u2014 Just-in-time Consent"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PT-4.2 — Just-in-time Consent

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Just-in-time consent enables individuals to participate in how their personally identifiable information is being processed at the time or in conjunction with specific types of data processing when such participation may be most useful to the individual. Individual assumptions about how personally identifiable information is being processed might not be accurate or reliable if time has passed since the individual last gave consent or the type of processing creates significant privacy risk. Organizations use discretion to determine when to use just-in-time consent and may use supporting information on demographics, focus groups, or surveys to learn more about individuals’ privacy interests and concerns.

### Requirements and exact statement parts

- `pt-4.2_smt`: Present [PARAM pt-04.02_odp.01] to individuals at [PARAM pt-04.02_odp.02] and in conjunction with [PARAM pt-04.02_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pt-4.2_smt — Present [PARAM pt-04.02_odp.01] to individuals at [PARAM pt-04.02_odp.02] and in conjunction with [PARAM pt-04.02_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pt-04.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pt-04.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pt-04.02_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pt-4.2_smt` — For “Present [PARAM pt-04.02_odp.01] to individuals at [PARAM pt-04.02_odp.02] and in conjunction with [PARAM pt-04.02_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pt-04.02_odp.01` — What approved value applies to **consent mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: consent mechanisms to be presented to individuals are defined;

- `pt-04.02_odp.02` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which to present consent mechanisms to individuals is defined;

- `pt-04.02_odp.03` — What approved value applies to **personally identifiable information processing**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personally identifiable information processing to be presented in conjunction with organization-defined consent mechanisms is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pt-4.2_obj` (pt-4.2_smt): [PARAM pt-04.02_odp.01] are presented to individuals [PARAM pt-04.02_odp.02] and in conjunction with [PARAM pt-04.02_odp.03].

#### EXAMINE — `pt-4.2_asm-examine`

- Personally identifiable information processing and transparency policy and procedures

- consent policies and procedures

- privacy plan

- other relevant documents or records

#### INTERVIEW — `pt-4.2_asm-interview`

- Organizational personnel with personally identifiable information processing and transparency responsibilities

- organizational personnel with user interface or user experience responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `pt-4.2_asm-test`

- Organizational processes for the collection of personally identifiable information

- mechanisms for obtaining just-in-time consent from users for the processing of their personally identifiable information

- mechanisms implementing just-in-time consent

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pt-4.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pt-4`.

- Catalog relationship **related**: `pt-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
