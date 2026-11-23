---
title: "CM-2.7 \u2014 Configure Systems and Components for High-risk Areas"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-2.7 — Configure Systems and Components for High-risk Areas

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

When it is known that systems or system components will be in high-risk areas external to the organization, additional controls may be implemented to counter the increased threat in such areas. For example, organizations can take actions for notebook computers used by individuals departing on and returning from travel. Actions include determining the locations that are of concern, defining the required configurations for the components, ensuring that components are configured as intended before travel is initiated, and applying controls to the components after travel is completed. Specially configured notebook computers include computers with sanitized hard drives, limited applications, and more stringent configuration settings. Controls applied to mobile devices upon return from travel include examining the mobile device for signs of physical tampering and purging and reimaging disk drives. Protecting information that resides on mobile devices is addressed in the MP (catalog reference: `#mp`) (Media Protection) family.

### Requirements and exact statement parts

- `cm-2.7_smt`: Statement grouping; see child parts.

- `cm-2.7_smt.a`: Issue [PARAM cm-02.07_odp.01] with [PARAM cm-02.07_odp.02] to individuals traveling to locations that the organization deems to be of significant risk; and

- `cm-2.7_smt.b`: Apply the following controls to the systems or components when the individuals return from travel: [PARAM cm-02.07_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-2.7_smt.a — Issue [PARAM cm-02.07_odp.01] with [PARAM cm-02.07_odp.02] to individuals traveling to locations that the organization deems to be of significant risk; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-2.7_smt.b — Apply the following controls to the systems or components when the individuals return from travel: [PARAM cm-02.07_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-02.07_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-02.07_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-02.07_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-2.7_smt.a` — For “Issue [PARAM cm-02.07_odp.01] with [PARAM cm-02.07_odp.02] to individuals traveling to locations that the organization deems to be of significant risk; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-2.7_smt.b` — For “Apply the following controls to the systems or components when the individuals return from travel: [PARAM cm-02.07_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-02.07_odp.01` — What approved value applies to **systems or system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the systems or system components to be issued when individuals travel to high-risk areas are defined;

- `cm-02.07_odp.02` — What approved value applies to **configurations**? Record the value, scope, approving authority, and decision source.

  - Catalog context: configurations for systems or system components to be issued when individuals travel to high-risk areas are defined;

- `cm-02.07_odp.03` — What approved value applies to **controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the controls to be applied when the individuals return from travel are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-2.7_obj.a` (cm-2.7_smt.a): [PARAM cm-02.07_odp.01] with [PARAM cm-02.07_odp.02] are issued to individuals traveling to locations that the organization deems to be of significant risk;

- `cm-2.7_obj.b` (cm-2.7_smt.b): [PARAM cm-02.07_odp.03] are applied to the systems or system components when the individuals return from travel.

#### EXAMINE — `cm-2.7_asm-examine`

- Configuration management policy

- configuration management plan

- procedures addressing the baseline configuration of the system

- procedures addressing system component installations and upgrades

- system architecture and configuration documentation

- system configuration settings and associated documentation

- system component inventory

- records of system baseline configuration reviews and updates

- system component installations/upgrades and associated records

- change control records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-2.7_asm-interview`

- Organizational personnel with configuration management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `cm-2.7_asm-test`

- Organizational processes for managing baseline configurations

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-2.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-2`.

- Catalog relationship **related**: `mp-4`.

- Catalog relationship **related**: `mp-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
