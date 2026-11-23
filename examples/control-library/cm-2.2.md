---
title: "CM-2.2 \u2014 Automation Support for Accuracy and Currency"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-2.2 — Automation Support for Accuracy and Currency

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Automated mechanisms that help organizations maintain consistent baseline configurations for systems include configuration management tools, hardware, software, firmware inventory tools, and network management tools. Automated tools can be used at the organization level, mission and business process level, or system level on workstations, servers, notebook computers, network components, or mobile devices. Tools can be used to track version numbers on operating systems, applications, types of software installed, and current patch levels. Automation support for accuracy and currency can be satisfied by the implementation of CM-8(2) (catalog reference: `#cm-8.2`) for organizations that combine system component inventory and baseline configuration activities.

### Requirements and exact statement parts

- `cm-2.2_smt`: Maintain the currency, completeness, accuracy, and availability of the baseline configuration of the system using [PARAM cm-02.02_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-2.2_smt — Maintain the currency, completeness, accuracy, and availability of the baseline configuration of the system using [PARAM cm-02.02_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-02.02_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-2.2_smt` — For “Maintain the currency, completeness, accuracy, and availability of the baseline configuration of the system using [PARAM cm-02.02_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-02.02_odp` — What approved value applies to **automated mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: automated mechanisms for maintaining baseline configuration of the system are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-2.2_obj-1` (cm-2.2_smt): the currency of the baseline configuration of the system is maintained using [PARAM cm-02.02_odp];

- `cm-2.2_obj-2` (cm-2.2_smt): the completeness of the baseline configuration of the system is maintained using [PARAM cm-02.02_odp];

- `cm-2.2_obj-3` (cm-2.2_smt): the accuracy of the baseline configuration of the system is maintained using [PARAM cm-02.02_odp];

- `cm-2.2_obj-4` (cm-2.2_smt): the availability of the baseline configuration of the system is maintained using [PARAM cm-02.02_odp].

#### EXAMINE — `cm-2.2_asm-examine`

- Configuration management policy

- procedures addressing the baseline configuration of the system

- configuration management plan

- system design documentation

- system architecture and configuration documentation

- system configuration settings and associated documentation

- system component inventory

- configuration change control records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-2.2_asm-interview`

- Organizational personnel with configuration management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `cm-2.2_asm-test`

- Organizational processes for managing baseline configurations

- automated mechanisms implementing baseline configuration maintenance

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-2.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-2`.

- Catalog relationship **related**: `cm-7`.

- Catalog relationship **related**: `ia-3`.

- Catalog relationship **related**: `ra-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
