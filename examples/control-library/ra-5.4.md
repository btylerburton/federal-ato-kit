---
title: "RA-5.4 \u2014 Discoverable Information"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# RA-5.4 — Discoverable Information

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Discoverable information includes information that adversaries could obtain without compromising or breaching the system, such as by collecting information that the system is exposing or by conducting extensive web searches. Corrective actions include notifying appropriate organizational personnel, removing designated information, or changing the system to make the designated information less relevant or attractive to adversaries. This enhancement excludes intentionally discoverable information that may be part of a decoy capability (e.g., honeypots, honeynets, or deception nets) deployed by the organization.

### Requirements and exact statement parts

- `ra-5.4_smt`: Determine information about the system that is discoverable and take [PARAM ra-05.04_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ra-5.4_smt — Determine information about the system that is discoverable and take [PARAM ra-05.04_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ra-05.04_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ra-5.4_smt` — For “Determine information about the system that is discoverable and take [PARAM ra-05.04_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ra-05.04_odp` — What approved value applies to **corrective actions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: corrective actions to be taken if information about the system is discoverable are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ra-5.4_obj-1` (ra-5.4_smt): information about the system is discoverable;

- `ra-5.4_obj-2` (ra-5.4_smt): [PARAM ra-05.04_odp] are taken when information about the system is confirmed as discoverable.

#### EXAMINE — `ra-5.4_asm-examine`

- Procedures addressing vulnerability scanning

- assessment report

- penetration test results

- vulnerability scanning results

- risk assessment report

- records of corrective actions taken

- incident response records

- audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ra-5.4_asm-interview`

- Organizational personnel with vulnerability scanning and/or penetration testing responsibilities

- organizational personnel with vulnerability scan analysis responsibilities

- organizational personnel responsible for risk response

- organizational personnel responsible for incident management and response

- organizational personnel with security responsibilities

#### TEST — `ra-5.4_asm-test`

- Organizational processes for vulnerability scanning

- organizational processes for risk response

- organizational processes for incident management and response

- mechanisms/tools supporting and/or implementing vulnerability scanning

- mechanisms supporting and/or implementing risk response

- mechanisms supporting and/or implementing incident management and response

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ra-5.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ra-5`.

- Catalog relationship **related**: `au-13`.

- Catalog relationship **related**: `sc-26`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
