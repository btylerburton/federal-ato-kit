---
title: "CM-2 \u2014 Baseline Configuration"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-2 — Baseline Configuration

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Baseline configurations for systems and system components include connectivity, operational, and communications aspects of systems. Baseline configurations are documented, formally reviewed, and agreed-upon specifications for systems or configuration items within those systems. Baseline configurations serve as a basis for future builds, releases, or changes to systems and include security and privacy control implementations, operational procedures, information about system components, network topology, and logical placement of components in the system architecture. Maintaining baseline configurations requires creating new baselines as organizational systems change over time. Baseline configurations of systems reflect the current enterprise architecture.

### Requirements and exact statement parts

- `cm-2_smt`: Statement grouping; see child parts.

- `cm-2_smt.a`: Develop, document, and maintain under configuration control, a current baseline configuration of the system; and

- `cm-2_smt.b`: Review and update the baseline configuration of the system:

- `cm-2_smt.b.1`: [PARAM cm-02_odp.01];

- `cm-2_smt.b.2`: When required due to [PARAM cm-02_odp.02] ; and

- `cm-2_smt.b.3`: When system components are installed or upgraded.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-2_smt.a — Develop, document, and maintain under configuration control, a current baseline configuration of the system; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-2_smt.b — Review and update the baseline configuration of the system:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-2_smt.b.1 — [PARAM cm-02_odp.01];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-2_smt.b.2 — When required due to [PARAM cm-02_odp.02] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-2_smt.b.3 — When system components are installed or upgraded.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-2_smt.a` — For “Develop, document, and maintain under configuration control, a current baseline configuration of the system; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-2_smt.b` — For “Review and update the baseline configuration of the system:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-2_smt.b.1` — For “[PARAM cm-02_odp.01];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-2_smt.b.2` — For “When required due to [PARAM cm-02_odp.02] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-2_smt.b.3` — For “When system components are installed or upgraded.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-02_odp.01` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency of baseline configuration review and update is defined;

- `cm-02_odp.02` — What approved value applies to **circumstances**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the circumstances requiring baseline configuration review and update are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-2_obj.a-1` (cm-2_smt.a): a current baseline configuration of the system is developed and documented;

- `cm-2_obj.a-2` (cm-2_smt.a): a current baseline configuration of the system is maintained under configuration control;

- `cm-2_obj.b.1` (cm-2_smt.b.1): the baseline configuration of the system is reviewed and updated [PARAM cm-02_odp.01];

- `cm-2_obj.b.2` (cm-2_smt.b.2): the baseline configuration of the system is reviewed and updated when required due to [PARAM cm-02_odp.02];

- `cm-2_obj.b.3` (cm-2_smt.b.3): the baseline configuration of the system is reviewed and updated when system components are installed or upgraded.

#### EXAMINE — `cm-2_asm-examine`

- Configuration management policy

- procedures addressing the baseline configuration of the system

- configuration management plan

- enterprise architecture documentation

- system design documentation

- system security plan

- privacy plan

- system architecture and configuration documentation

- system configuration settings and associated documentation

- system component inventory

- change control records

- other relevant documents or records

#### INTERVIEW — `cm-2_asm-interview`

- Organizational personnel with configuration management responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

#### TEST — `cm-2_asm-test`

- Organizational processes for managing baseline configurations

- mechanisms supporting configuration control of the baseline configuration

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-2`. The library index records the exact source revision and hash.

- [SP 800-124](https://doi.org/10.6028/NIST.SP.800-124r1)

- [SP 800-128](https://doi.org/10.6028/NIST.SP.800-128)

- Catalog relationship **related**: `ac-19`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `ca-9`.

- Catalog relationship **related**: `cm-1`.

- Catalog relationship **related**: `cm-3`.

- Catalog relationship **related**: `cm-5`.

- Catalog relationship **related**: `cm-6`.

- Catalog relationship **related**: `cm-8`.

- Catalog relationship **related**: `cm-9`.

- Catalog relationship **related**: `cp-9`.

- Catalog relationship **related**: `cp-10`.

- Catalog relationship **related**: `cp-12`.

- Catalog relationship **related**: `ma-2`.

- Catalog relationship **related**: `pl-8`.

- Catalog relationship **related**: `pm-5`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sa-10`.

- Catalog relationship **related**: `sa-15`.

- Catalog relationship **related**: `sc-18`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
