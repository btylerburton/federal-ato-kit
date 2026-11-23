---
title: "MA-6.1 \u2014 Preventive Maintenance"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-6.1 — Preventive Maintenance

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Preventive maintenance includes proactive care and the servicing of system components to maintain organizational equipment and facilities in satisfactory operating condition. Such maintenance provides for the systematic inspection, tests, measurements, adjustments, parts replacement, detection, and correction of incipient failures either before they occur or before they develop into major defects. The primary goal of preventive maintenance is to avoid or mitigate the consequences of equipment failures. Preventive maintenance is designed to preserve and restore equipment reliability by replacing worn components before they fail. Methods of determining what preventive (or other) failure management policies to apply include original equipment manufacturer recommendations; statistical failure records; expert opinion; maintenance that has already been conducted on similar equipment; requirements of codes, laws, or regulations within a jurisdiction; or measured values and performance indications.

### Requirements and exact statement parts

- `ma-6.1_smt`: Perform preventive maintenance on [PARAM ma-06.01_odp.01] at [PARAM ma-06.01_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-6.1_smt — Perform preventive maintenance on [PARAM ma-06.01_odp.01] at [PARAM ma-06.01_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ma-06.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ma-06.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ma-6.1_smt` — For “Perform preventive maintenance on [PARAM ma-06.01_odp.01] at [PARAM ma-06.01_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ma-06.01_odp.01` — What approved value applies to **system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system components on which preventive maintenance is to be performed are defined;

- `ma-06.01_odp.02` — What approved value applies to **time intervals**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time intervals within which preventive maintenance is to be performed on system components are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-6.1_obj` (ma-6.1_smt): preventive maintenance is performed on [PARAM ma-06.01_odp.01] at [PARAM ma-06.01_odp.02].

#### EXAMINE — `ma-6.1_asm-examine`

- Maintenance policy

- procedures addressing system maintenance

- service provider contracts

- service-level agreements

- maintenance records

- list of system components requiring preventive maintenance

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-6.1_asm-interview`

- Organizational personnel with system maintenance responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ma-6.1_asm-test`

- Organizational processes for preventive maintenance

- mechanisms supporting and/or implementing preventive maintenance

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-6.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ma-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
