---
title: "SA-9.5 \u2014 Processing, Storage, and Service Location"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-9.5 — Processing, Storage, and Service Location

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The location of information processing, information and data storage, or system services can have a direct impact on the ability of organizations to successfully execute their mission and business functions. The impact occurs when external providers control the location of processing, storage, or services. The criteria that external providers use for the selection of processing, storage, or service locations may be different from the criteria that organizations use. For example, organizations may desire that data or information storage locations be restricted to certain locations to help facilitate incident response activities in case of information security incidents or breaches. Incident response activities, including forensic analyses and after-the-fact investigations, may be adversely affected by the governing laws, policies, or protocols in the locations where processing and storage occur and/or the locations from which system services emanate.

### Requirements and exact statement parts

- `sa-9.5_smt`: Restrict the location of [PARAM sa-09.05_odp.01] to [PARAM sa-09.05_odp.02] based on [PARAM sa-09.05_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-9.5_smt — Restrict the location of [PARAM sa-09.05_odp.01] to [PARAM sa-09.05_odp.02] based on [PARAM sa-09.05_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sa-09.05_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sa-09.05_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sa-09.05_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sa-9.5_smt` — For “Restrict the location of [PARAM sa-09.05_odp.01] to [PARAM sa-09.05_odp.02] based on [PARAM sa-09.05_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sa-09.05_odp.01` — What approved value applies to **selection; choose one-or-more from: information processing; information or data; system services**? Record the value, scope, approving authority, and decision source.

- `sa-09.05_odp.02` — What approved value applies to **locations**? Record the value, scope, approving authority, and decision source.

  - Catalog context: locations where [PARAM sa-09.05_odp.01] is/are to be restricted are defined;

- `sa-09.05_odp.03` — What approved value applies to **requirements**? Record the value, scope, approving authority, and decision source.

  - Catalog context: requirements or conditions for restricting the location of [PARAM sa-09.05_odp.01] are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-9.5_obj` (sa-9.5_smt): based on [PARAM sa-09.05_odp.03], [PARAM sa-09.05_odp.01] is/are restricted to [PARAM sa-09.05_odp.02].

#### EXAMINE — `sa-9.5_asm-examine`

- System and services acquisition policy

- procedures addressing external system services

- acquisition contracts for the system, system component, or system service

- solicitation documentation

- acquisition documentation

- service level agreements

- restricted locations for information processing

- information/data and/or system services

- information processing, information/data, and/or system services to be maintained in restricted locations

- organizational security requirements or conditions for external providers

- system security plan

- supply chain risk management plan

- other relevant documents or records

#### INTERVIEW — `sa-9.5_asm-interview`

- Organizational personnel with system and service acquisition responsibilities

- organizational personnel with information security responsibilities

- external providers of system services

- organizational personnel with supply chain risk management responsibilities

#### TEST — `sa-9.5_asm-test`

- Organizational processes for defining the requirements to restrict locations of information processing, information/data, or information services

- organizational processes for ensuring the location is restricted in accordance with requirements or conditions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-9.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-9`.

- Catalog relationship **related**: `sa-5`.

- Catalog relationship **related**: `sr-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
