---
title: "IR-5 \u2014 Incident Monitoring"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-5 — Incident Monitoring

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Documenting incidents includes maintaining records about each incident, the status of the incident, and other pertinent information necessary for forensics as well as evaluating incident details, trends, and handling. Incident information can be obtained from a variety of sources, including network monitoring, incident reports, incident response teams, user complaints, supply chain partners, audit monitoring, physical access monitoring, and user and administrator reports. IR-4 (catalog reference: `#ir-4`) provides information on the types of incidents that are appropriate for monitoring.

### Requirements and exact statement parts

- `ir-5_smt`: Track and document incidents.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-5_smt — Track and document incidents.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ir-5_smt` — For “Track and document incidents.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-5_obj-1` (ir-5_smt): incidents are tracked;

- `ir-5_obj-2` (ir-5_smt): incidents are documented.

#### EXAMINE — `ir-5_asm-examine`

- Incident response policy

- procedures addressing incident monitoring

- incident response records and documentation

- incident response plan

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ir-5_asm-interview`

- Organizational personnel with incident monitoring responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `ir-5_asm-test`

- Incident monitoring capability for the organization

- mechanisms supporting and/or implementing the tracking and documenting of system security incidents

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-5`. The library index records the exact source revision and hash.

- [SP 800-61](https://doi.org/10.6028/NIST.SP.800-61r2)

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-7`.

- Catalog relationship **related**: `ir-4`.

- Catalog relationship **related**: `ir-6`.

- Catalog relationship **related**: `ir-8`.

- Catalog relationship **related**: `pe-6`.

- Catalog relationship **related**: `pm-5`.

- Catalog relationship **related**: `sc-5`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `si-3`.

- Catalog relationship **related**: `si-4`.

- Catalog relationship **related**: `si-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
