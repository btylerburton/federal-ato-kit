---
title: "CM-6 \u2014 Configuration Settings"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-6 — Configuration Settings

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Configuration settings are the parameters that can be changed in the hardware, software, or firmware components of the system that affect the security and privacy posture or functionality of the system. Information technology products for which configuration settings can be defined include mainframe computers, servers, workstations, operating systems, mobile devices, input/output devices, protocols, and applications. Parameters that impact the security posture of systems include registry settings; account, file, or directory permission settings; and settings for functions, protocols, ports, services, and remote connections. Privacy parameters are parameters impacting the privacy posture of systems, including the parameters required to satisfy other privacy controls. Privacy parameters include settings for access controls, data processing preferences, and processing and retention permissions. Organizations establish organization-wide configuration settings and subsequently derive specific configuration settings for systems. The established settings become part of the configuration baseline for the system.

Common secure configurations (also known as security configuration checklists, lockdown and hardening guides, and security reference guides) provide recognized, standardized, and established benchmarks that stipulate secure configuration settings for information technology products and platforms as well as instructions for configuring those products or platforms to meet operational requirements. Common secure configurations can be developed by a variety of organizations, including information technology product developers, manufacturers, vendors, federal agencies, consortia, academia, industry, and other organizations in the public and private sectors.

Implementation of a common secure configuration may be mandated at the organization level, mission and business process level, system level, or at a higher level, including by a regulatory agency. Common secure configurations include the United States Government Configuration Baseline USGCB (catalog reference: `#98498928-3ca3-44b3-8b1e-f48685373087`) and security technical implementation guides (STIGs), which affect the implementation of CM-6 (catalog reference: `#cm-6`) and other controls such as AC-19 (catalog reference: `#ac-19`) and CM-7 (catalog reference: `#cm-7`) . The Security Content Automation Protocol (SCAP) and the defined standards within the protocol provide an effective method to uniquely identify, track, and control configuration settings.

### Requirements and exact statement parts

- `cm-6_smt`: Statement grouping; see child parts.

- `cm-6_smt.a`: Establish and document configuration settings for components employed within the system that reflect the most restrictive mode consistent with operational requirements using [PARAM cm-06_odp.01];

- `cm-6_smt.b`: Implement the configuration settings;

- `cm-6_smt.c`: Identify, document, and approve any deviations from established configuration settings for [PARAM cm-06_odp.02] based on [PARAM cm-06_odp.03] ; and

- `cm-6_smt.d`: Monitor and control changes to the configuration settings in accordance with organizational policies and procedures.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-6_smt.a — Establish and document configuration settings for components employed within the system that reflect the most restrictive mode consistent with operational requirements using [PARAM cm-06_odp.01];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-6_smt.b — Implement the configuration settings;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-6_smt.c — Identify, document, and approve any deviations from established configuration settings for [PARAM cm-06_odp.02] based on [PARAM cm-06_odp.03] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-6_smt.d — Monitor and control changes to the configuration settings in accordance with organizational policies and procedures.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-06_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-06_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-06_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-6_smt.a` — For “Establish and document configuration settings for components employed within the system that reflect the most restrictive mode consistent with operational requirements using [PARAM cm-06_odp.01];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-6_smt.b` — For “Implement the configuration settings;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-6_smt.c` — For “Identify, document, and approve any deviations from established configuration settings for [PARAM cm-06_odp.02] based on [PARAM cm-06_odp.03] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-6_smt.d` — For “Monitor and control changes to the configuration settings in accordance with organizational policies and procedures.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-06_odp.01` — What approved value applies to **common secure configurations**? Record the value, scope, approving authority, and decision source.

  - Catalog context: common secure configurations to establish and document configuration settings for components employed within the system are defined;

- `cm-06_odp.02` — What approved value applies to **system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system components for which approval of deviations is needed are defined;

- `cm-06_odp.03` — What approved value applies to **operational requirements**? Record the value, scope, approving authority, and decision source.

  - Catalog context: operational requirements necessitating approval of deviations are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-6_obj.a` (cm-6_smt.a): configuration settings that reflect the most restrictive mode consistent with operational requirements are established and documented for components employed within the system using [PARAM cm-06_odp.01];

- `cm-6_obj.b` (cm-6_smt.b): the configuration settings documented in CM-06a are implemented;

- `cm-6_obj.c-1` (cm-6_smt.c): any deviations from established configuration settings for [PARAM cm-06_odp.02] are identified and documented based on [PARAM cm-06_odp.03];

- `cm-6_obj.c-2` (cm-6_smt.c): any deviations from established configuration settings for [PARAM cm-06_odp.02] are approved;

- `cm-6_obj.d-1` (cm-6_smt.d): changes to the configuration settings are monitored in accordance with organizational policies and procedures;

- `cm-6_obj.d-2` (cm-6_smt.d): changes to the configuration settings are controlled in accordance with organizational policies and procedures.

#### EXAMINE — `cm-6_asm-examine`

- Configuration management policy

- procedures addressing configuration settings for the system

- configuration management plan

- system design documentation

- system configuration settings and associated documentation

- common secure configuration checklists

- system component inventory

- evidence supporting approved deviations from established configuration settings

- change control records

- system data processing and retention permissions

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `cm-6_asm-interview`

- Organizational personnel with security configuration management responsibilities

- organizational personnel with privacy configuration management responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

#### TEST — `cm-6_asm-test`

- Organizational processes for managing configuration settings

- mechanisms that implement, monitor, and/or control system configuration settings

- mechanisms that identify and/or document deviations from established configuration settings

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-6`. The library index records the exact source revision and hash.

- [SP 800-70](https://doi.org/10.6028/NIST.SP.800-70r4)

- [SP 800-126](https://doi.org/10.6028/NIST.SP.800-126r3)

- [SP 800-128](https://doi.org/10.6028/NIST.SP.800-128)

- [USGCB](https://csrc.nist.gov/projects/united-states-government-configuration-baseline)

- [NCPR](https://nvd.nist.gov/ncp/repository)

- [DOD STIG](https://public.cyber.mil/stigs)

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-19`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `ca-9`.

- Catalog relationship **related**: `cm-2`.

- Catalog relationship **related**: `cm-3`.

- Catalog relationship **related**: `cm-5`.

- Catalog relationship **related**: `cm-7`.

- Catalog relationship **related**: `cm-11`.

- Catalog relationship **related**: `cp-7`.

- Catalog relationship **related**: `cp-9`.

- Catalog relationship **related**: `cp-10`.

- Catalog relationship **related**: `ia-3`.

- Catalog relationship **related**: `ia-5`.

- Catalog relationship **related**: `pl-8`.

- Catalog relationship **related**: `pl-9`.

- Catalog relationship **related**: `ra-5`.

- Catalog relationship **related**: `sa-4`.

- Catalog relationship **related**: `sa-5`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sa-9`.

- Catalog relationship **related**: `sc-18`.

- Catalog relationship **related**: `sc-28`.

- Catalog relationship **related**: `sc-43`.

- Catalog relationship **related**: `si-2`.

- Catalog relationship **related**: `si-4`.

- Catalog relationship **related**: `si-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
