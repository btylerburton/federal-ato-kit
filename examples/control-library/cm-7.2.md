---
title: "CM-7.2 \u2014 Prevent Program Execution"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-7.2 — Prevent Program Execution

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Prevention of program execution addresses organizational policies, rules of behavior, and/or access agreements that restrict software usage and the terms and conditions imposed by the developer or manufacturer, including software licensing and copyrights. Restrictions include prohibiting auto-execute features, restricting roles allowed to approve program execution, permitting or prohibiting specific software programs, or restricting the number of program instances executed at the same time.

### Requirements and exact statement parts

- `cm-7.2_smt`: Prevent program execution in accordance with [PARAM cm-07.02_odp.01].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-7.2_smt — Prevent program execution in accordance with [PARAM cm-07.02_odp.01].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-07.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cm-07.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-7.2_smt` — For “Prevent program execution in accordance with [PARAM cm-07.02_odp.01].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-07.02_odp.01` — What approved value applies to **selection; choose one-or-more from: [PARAM cm-07.02_odp.02]; rules authorizing the terms and conditions of software program usage**? Record the value, scope, approving authority, and decision source.

- `cm-07.02_odp.02` — What approved value applies to **policies, rules of behavior, and/or access agreements regarding software program usage and restrictions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: policies, rules of behavior, and/or access agreements regarding software program usage and restrictions are defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-7.2_obj` (cm-7.2_smt): program execution is prevented in accordance with [PARAM cm-07.02_odp.01].

#### EXAMINE — `cm-7.2_asm-examine`

- Configuration management policy

- procedures addressing least functionality in the system

- configuration management plan

- system design documentation

- system configuration settings and associated documentation

- system component inventory

- common secure configuration checklists

- specifications for preventing software program execution

- change control records

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-7.2_asm-interview`

- Organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `cm-7.2_asm-test`

- Organizational processes preventing program execution on the system

- organizational processes for software program usage and restrictions

- mechanisms preventing program execution on the system

- mechanisms supporting and/or implementing software program usage and restrictions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-7.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-7`.

- Catalog relationship **related**: `cm-8`.

- Catalog relationship **related**: `pl-4`.

- Catalog relationship **related**: `pl-9`.

- Catalog relationship **related**: `pm-5`.

- Catalog relationship **related**: `ps-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
