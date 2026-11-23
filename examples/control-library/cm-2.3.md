---
title: "CM-2.3 \u2014 Retention of Previous Configurations"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-2.3 — Retention of Previous Configurations

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Retaining previous versions of baseline configurations to support rollback include hardware, software, firmware, configuration files, configuration records, and associated documentation.

### Requirements and exact statement parts

- `cm-2.3_smt`: Retain [PARAM cm-02.03_odp] of previous versions of baseline configurations of the system to support rollback.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-2.3_smt — Retain [PARAM cm-02.03_odp] of previous versions of baseline configurations of the system to support rollback.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-02.03_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-2.3_smt` — For “Retain [PARAM cm-02.03_odp] of previous versions of baseline configurations of the system to support rollback.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-02.03_odp` — What approved value applies to **number**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the number of previous baseline configuration versions to be retained is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-2.3_obj` (cm-2.3_smt): [PARAM cm-02.03_odp] of previous baseline configuration version(s) of the system is/are retained to support rollback.

#### EXAMINE — `cm-2.3_asm-examine`

- Configuration management policy

- procedures addressing the baseline configuration of the system

- configuration management plan

- system architecture and configuration documentation

- system configuration settings and associated documentation

- copies of previous baseline configuration versions

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-2.3_asm-interview`

- Organizational personnel with configuration management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `cm-2.3_asm-test`

- Organizational processes for managing baseline configurations

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-2.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
