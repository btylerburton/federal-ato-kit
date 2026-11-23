---
title: "CM-8 \u2014 System Component Inventory"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-8 — System Component Inventory

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

System components are discrete, identifiable information technology assets that include hardware, software, and firmware. Organizations may choose to implement centralized system component inventories that include components from all organizational systems. In such situations, organizations ensure that the inventories include system-specific information required for component accountability. The information necessary for effective accountability of system components includes the system name, software owners, software version numbers, hardware inventory specifications, software license information, and for networked components, the machine names and network addresses across all implemented protocols (e.g., IPv4, IPv6). Inventory specifications include date of receipt, cost, model, serial number, manufacturer, supplier information, component type, and physical location.

Preventing duplicate accounting of system components addresses the lack of accountability that occurs when component ownership and system association is not known, especially in large or complex connected systems. Effective prevention of duplicate accounting of system components necessitates use of a unique identifier for each component. For software inventory, centrally managed software that is accessed via other systems is addressed as a component of the system on which it is installed and managed. Software installed on multiple organizational systems and managed at the system level is addressed for each individual system and may appear more than once in a centralized component inventory, necessitating a system association for each software instance in the centralized inventory to avoid duplicate accounting of components. Scanning systems implementing multiple network protocols (e.g., IPv4 and IPv6) can result in duplicate components being identified in different address spaces. The implementation of CM-8(7) (catalog reference: `#cm-8.7`) can help to eliminate duplicate accounting of components.

### Requirements and exact statement parts

- `cm-8_smt`: Statement grouping; see child parts.

- `cm-8_smt.a`: Develop and document an inventory of system components that:

- `cm-8_smt.a.1`: Accurately reflects the system;

- `cm-8_smt.a.2`: Includes all components within the system;

- `cm-8_smt.a.3`: Does not include duplicate accounting of components or components assigned to any other system;

- `cm-8_smt.a.4`: Is at the level of granularity deemed necessary for tracking and reporting; and

- `cm-8_smt.a.5`: Includes the following information to achieve system component accountability: [PARAM cm-08_odp.01] ; and

- `cm-8_smt.b`: Review and update the system component inventory [PARAM cm-08_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-8_smt.a — Develop and document an inventory of system components that:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-8_smt.a.1 — Accurately reflects the system;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-8_smt.a.2 — Includes all components within the system;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-8_smt.a.3 — Does not include duplicate accounting of components or components assigned to any other system;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-8_smt.a.4 — Is at the level of granularity deemed necessary for tracking and reporting; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-8_smt.a.5 — Includes the following information to achieve system component accountability: [PARAM cm-08_odp.01] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-8_smt.b — Review and update the system component inventory [PARAM cm-08_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-08_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-08_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-8_smt.a` — For “Develop and document an inventory of system components that:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-8_smt.a.1` — For “Accurately reflects the system;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-8_smt.a.2` — For “Includes all components within the system;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-8_smt.a.3` — For “Does not include duplicate accounting of components or components assigned to any other system;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-8_smt.a.4` — For “Is at the level of granularity deemed necessary for tracking and reporting; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-8_smt.a.5` — For “Includes the following information to achieve system component accountability: [PARAM cm-08_odp.01] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-8_smt.b` — For “Review and update the system component inventory [PARAM cm-08_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-08_odp.01` — What approved value applies to **information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: information deemed necessary to achieve effective system component accountability is defined;

- `cm-08_odp.02` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to review and update the system component inventory is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-8_obj.a.1` (cm-8_smt.a.1): an inventory of system components that accurately reflects the system is developed and documented;

- `cm-8_obj.a.2` (cm-8_smt.a.2): an inventory of system components that includes all components within the system is developed and documented;

- `cm-8_obj.a.3` (cm-8_smt.a.3): an inventory of system components that does not include duplicate accounting of components or components assigned to any other system is developed and documented;

- `cm-8_obj.a.4` (cm-8_smt.a.4): an inventory of system components that is at the level of granularity deemed necessary for tracking and reporting is developed and documented;

- `cm-8_obj.a.5` (cm-8_smt.a.5): an inventory of system components that includes [PARAM cm-08_odp.01] is developed and documented;

- `cm-8_obj.b` (cm-8_smt.b): the system component inventory is reviewed and updated [PARAM cm-08_odp.02].

#### EXAMINE — `cm-8_asm-examine`

- Configuration management policy

- procedures addressing system component inventory

- configuration management plan

- system security plan

- system design documentation

- system component inventory

- inventory reviews and update records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-8_asm-interview`

- Organizational personnel with component inventory management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `cm-8_asm-test`

- Organizational processes for managing the system component inventory

- mechanisms supporting and/or implementing system component inventory

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-8`. The library index records the exact source revision and hash.

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [SP 800-57-1](https://doi.org/10.6028/NIST.SP.800-57pt1r5)

- [SP 800-57-2](https://doi.org/10.6028/NIST.SP.800-57pt2r1)

- [SP 800-57-3](https://doi.org/10.6028/NIST.SP.800-57pt3r1)

- [SP 800-128](https://doi.org/10.6028/NIST.SP.800-128)

- [IR 8011-2](https://doi.org/10.6028/NIST.IR.8011-2)

- [IR 8011-3](https://doi.org/10.6028/NIST.IR.8011-3)

- Catalog relationship **related**: `cm-2`.

- Catalog relationship **related**: `cm-7`.

- Catalog relationship **related**: `cm-9`.

- Catalog relationship **related**: `cm-10`.

- Catalog relationship **related**: `cm-11`.

- Catalog relationship **related**: `cm-13`.

- Catalog relationship **related**: `cp-2`.

- Catalog relationship **related**: `cp-9`.

- Catalog relationship **related**: `ma-2`.

- Catalog relationship **related**: `ma-6`.

- Catalog relationship **related**: `pe-20`.

- Catalog relationship **related**: `pl-9`.

- Catalog relationship **related**: `pm-5`.

- Catalog relationship **related**: `sa-4`.

- Catalog relationship **related**: `sa-5`.

- Catalog relationship **related**: `si-2`.

- Catalog relationship **related**: `sr-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
