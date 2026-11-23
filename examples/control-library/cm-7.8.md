---
title: "CM-7.8 \u2014 Binary or Machine Executable Code"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-7.8 — Binary or Machine Executable Code

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Binary or machine executable code applies to all sources of binary or machine-executable code, including commercial software and firmware and open-source software. Organizations assess software products without accompanying source code or from sources with limited or no warranty for potential security impacts. The assessments address the fact that software products without the provision of source code may be difficult to review, repair, or extend. In addition, there may be no owners to make such repairs on behalf of organizations. If open-source software is used, the assessments address the fact that there is no warranty, the open-source software could contain back doors or malware, and there may be no support available.

### Requirements and exact statement parts

- `cm-7.8_smt`: Statement grouping; see child parts.

- `cm-7.8_smt.a`: Prohibit the use of binary or machine-executable code from sources with limited or no warranty or without the provision of source code; and

- `cm-7.8_smt.b`: Allow exceptions only for compelling mission or operational requirements and with the approval of the authorizing official.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-7.8_smt.a — Prohibit the use of binary or machine-executable code from sources with limited or no warranty or without the provision of source code; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for cm-7.8_smt.b — Allow exceptions only for compelling mission or operational requirements and with the approval of the authorizing official.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `cm-7.8_smt.a` — For “Prohibit the use of binary or machine-executable code from sources with limited or no warranty or without the provision of source code; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `cm-7.8_smt.b` — For “Allow exceptions only for compelling mission or operational requirements and with the approval of the authorizing official.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-7.8_obj.a` (cm-7.8_smt.a): the use of binary or machine-executable code is prohibited when it originates from sources with limited or no warranty or without the provision of source code;

- `cm-7.8_obj.b-1` (cm-7.8_smt.b): exceptions to the prohibition of binary or machine-executable code from sources with limited or no warranty or without the provision of source code are allowed only for compelling mission or operational requirements;

- `cm-7.8_obj.b-2` (cm-7.8_smt.b): exceptions to the prohibition of binary or machine-executable code from sources with limited or no warranty or without the provision of source code are allowed only with the approval of the authorizing official.

#### EXAMINE — `cm-7.8_asm-examine`

- Configuration management policy

- procedures addressing least functionality in the system

- configuration management plan

- system security plan

- system design documentation

- system configuration settings and associated documentation

- list or record of binary or machine-executable code

- system component inventory

- common secure configuration checklists

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-7.8_asm-interview`

- Organizational personnel with responsibilities for determining mission and operational requirements

- authorizing official for the system

- organizational personnel with information security responsibilities

- organizational personnel with software management responsibilities

- system/network administrators

#### TEST — `cm-7.8_asm-test`

- Organizational process for approving execution of binary or machine-executable code

- mechanisms supporting and/or implementing the prohibition of binary or machine-executable code

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-7.8`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-7`.

- Catalog relationship **related**: `sa-5`.

- Catalog relationship **related**: `sa-22`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
