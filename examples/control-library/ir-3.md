---
title: "IR-3 \u2014 Incident Response Testing"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-3 — Incident Response Testing

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations test incident response capabilities to determine their effectiveness and identify potential weaknesses or deficiencies. Incident response testing includes the use of checklists, walk-through or tabletop exercises, and simulations (parallel or full interrupt). Incident response testing can include a determination of the effects on organizational operations and assets and individuals due to incident response. The use of qualitative and quantitative data aids in determining the effectiveness of incident response processes.

### Requirements and exact statement parts

- `ir-3_smt`: Test the effectiveness of the incident response capability for the system [PARAM ir-03_odp.01] using the following tests: [PARAM ir-03_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-3_smt — Test the effectiveness of the incident response capability for the system [PARAM ir-03_odp.01] using the following tests: [PARAM ir-03_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ir-03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ir-03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ir-3_smt` — For “Test the effectiveness of the incident response capability for the system [PARAM ir-03_odp.01] using the following tests: [PARAM ir-03_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ir-03_odp.01` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to test the effectiveness of the incident response capability for the system is defined;

- `ir-03_odp.02` — What approved value applies to **tests**? Record the value, scope, approving authority, and decision source.

  - Catalog context: tests used to test the effectiveness of the incident response capability for the system are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-3_obj` (ir-3_smt): the effectiveness of the incident response capability for the system is tested [PARAM ir-03_odp.01] using [PARAM ir-03_odp.02].

#### EXAMINE — `ir-3_asm-examine`

- Incident response policy

- contingency planning policy

- procedures addressing incident response testing

- procedures addressing contingency plan testing

- incident response testing material

- incident response test results

- incident response test plan

- incident response plan

- contingency plan

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ir-3_asm-interview`

- Organizational personnel with incident response testing responsibilities

- organizational personnel with information security and privacy responsibilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-3`. The library index records the exact source revision and hash.

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [SP 800-84](https://doi.org/10.6028/NIST.SP.800-84)

- [SP 800-115](https://doi.org/10.6028/NIST.SP.800-115)

- Catalog relationship **related**: `cp-3`.

- Catalog relationship **related**: `cp-4`.

- Catalog relationship **related**: `ir-2`.

- Catalog relationship **related**: `ir-4`.

- Catalog relationship **related**: `ir-8`.

- Catalog relationship **related**: `pm-14`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
