---
title: "SR-4 \u2014 Provenance"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SR-4 — Provenance

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Every system and system component has a point of origin and may be changed throughout its existence. Provenance is the chronology of the origin, development, ownership, location, and changes to a system or system component and associated data. It may also include personnel and processes used to interact with or make modifications to the system, component, or associated data. Organizations consider developing procedures (see SR-1 (catalog reference: `#sr-1`) ) for allocating responsibilities for the creation, maintenance, and monitoring of provenance for systems and system components; transferring provenance documentation and responsibility between organizations; and preventing and monitoring for unauthorized changes to the provenance records. Organizations have methods to document, monitor, and maintain valid provenance baselines for systems, system components, and related data. These actions help track, assess, and document any changes to the provenance, including changes in supply chain elements or configuration, and help ensure non-repudiation of provenance information and the provenance change records. Provenance considerations are addressed throughout the system development life cycle and incorporated into contracts and other arrangements, as appropriate.

### Requirements and exact statement parts

- `sr-4_smt`: Document, monitor, and maintain valid provenance of the following systems, system components, and associated data: [PARAM sr-04_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sr-4_smt — Document, monitor, and maintain valid provenance of the following systems, system components, and associated data: [PARAM sr-04_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sr-04_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sr-4_smt` — For “Document, monitor, and maintain valid provenance of the following systems, system components, and associated data: [PARAM sr-04_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sr-04_odp` — What approved value applies to **systems, system components, and associated data**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems, system components, and associated data that require valid provenance are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sr-4_obj-1` (sr-4_smt): valid provenance is documented for [PARAM sr-04_odp];

- `sr-4_obj-2` (sr-4_smt): valid provenance is monitored for [PARAM sr-04_odp];

- `sr-4_obj-3` (sr-4_smt): valid provenance is maintained for [PARAM sr-04_odp].

#### EXAMINE — `sr-4_asm-examine`

- Supply chain risk management policy

- supply chain risk management procedures

- supply chain risk management plan

- documentation of critical systems, critical system components, and associated data

- documentation showing the history of ownership, custody, and location of and changes to critical systems or critical system components

- system architecture

- inter-organizational agreements and procedures

- contracts

- system security plan

- privacy plan

- personally identifiable information processing policy

- other relevant documents or records

#### INTERVIEW — `sr-4_asm-interview`

- Organizational personnel with acquisition responsibilities

- organizational personnel with information security and privacy responsibilities

- organizational personnel with supply chain risk management responsibilities

#### TEST — `sr-4_asm-test`

- Organizational processes for identifying the provenance of critical systems and critical system components

- mechanisms used to document, monitor, or maintain provenance

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sr-4`. The library index records the exact source revision and hash.

- [FASC18](https://www.congress.gov/bill/115th-congress/senate-bill/3085)

- [41 CFR 201](https://www.federalregister.gov/d/2020-18939)

- [EO 13873](https://www.whitehouse.gov/presidential-actions/executive-order-securing-information-communications-technology-services-supply-chain)

- [ISO 27036](https://www.iso.org/standard/59648.html)

- [ISO 20243](https://www.iso.org/standard/74399.html)

- [SP 800-160-1](https://doi.org/10.6028/NIST.SP.800-160v1)

- [SP 800-161](https://doi.org/10.6028/NIST.SP.800-161)

- [IR 7622](https://doi.org/10.6028/NIST.IR.7622)

- [IR 8112](https://doi.org/10.6028/NIST.IR.8112)

- [IR 8272](https://doi.org/10.6028/NIST.IR.8272)

- Catalog relationship **related**: `cm-8`.

- Catalog relationship **related**: `ma-2`.

- Catalog relationship **related**: `ma-6`.

- Catalog relationship **related**: `ra-9`.

- Catalog relationship **related**: `sa-3`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
