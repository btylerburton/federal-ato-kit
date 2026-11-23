---
title: "CM-7.7 \u2014 Code Execution in Protected Environments"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-7.7 — Code Execution in Protected Environments

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Code execution in protected environments applies to all sources of binary or machine-executable code, including commercial software and firmware and open-source software.

### Requirements and exact statement parts

- `cm-7.7_smt`: Allow execution of binary or machine-executable code only in confined physical or virtual machine environments and with the explicit approval of [PARAM cm-07.07_odp] when such code is:

- `cm-7.7_smt.a`: Obtained from sources with limited or no warranty; and/or

- `cm-7.7_smt.b`: Without the provision of source code.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-7.7_smt — Allow execution of binary or machine-executable code only in confined physical or virtual machine environments and with the explicit approval of [PARAM cm-07.07_odp] when such code is:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-7.7_smt.a — Obtained from sources with limited or no warranty; and/or
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-7.7_smt.b — Without the provision of source code.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cm-07.07_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cm-7.7_smt` — For “Allow execution of binary or machine-executable code only in confined physical or virtual machine environments and with the explicit approval of [PARAM cm-07.07_odp] when such code is:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-7.7_smt.a` — For “Obtained from sources with limited or no warranty; and/or”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-7.7_smt.b` — For “Without the provision of source code.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cm-07.07_odp` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to explicitly approve execution of binary or machine-executable code is/are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-7.7_obj` (cm-7.7_smt): the execution of binary or machine-executable code is only allowed in confined physical or virtual machine environments;

- `cm-7.7_obj.a` (cm-7.7_smt.a): the execution of binary or machine-executable code obtained from sources with limited or no warranty is only allowed with the explicit approval of [PARAM cm-07.07_odp];

- `cm-7.7_obj.b` (cm-7.7_smt.b): the execution of binary or machine-executable code without the provision of source code is only allowed with the explicit approval of [PARAM cm-07.07_odp].

#### EXAMINE — `cm-7.7_asm-examine`

- Configuration management policy

- procedures addressing least functionality in the system

- configuration management plan

- system design documentation

- system configuration settings and associated documentation

- list or record of binary or machine-executable code

- system component inventory

- common secure configuration checklists

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-7.7_asm-interview`

- Organizational personnel with responsibilities for approving execution of binary or machine-executable code

- organizational personnel with information security responsibilities

- organizational personnel with software management responsibilities

- system/network administrators

- system developers

#### TEST — `cm-7.7_asm-test`

- Organizational process for approving execution of binary or machine-executable code

- organizational process for confining binary or machine-executable code to physical or virtual machine environments

- mechanisms supporting and/or implementing the confinement of binary or machine-executable code to physical or virtual machine environments

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-7.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-7`.

- Catalog relationship **related**: `cm-10`.

- Catalog relationship **related**: `sc-44`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
