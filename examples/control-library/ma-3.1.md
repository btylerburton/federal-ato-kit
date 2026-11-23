---
title: "MA-3.1 \u2014 Inspect Tools"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-3.1 — Inspect Tools

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Maintenance tools can be directly brought into a facility by maintenance personnel or downloaded from a vendor’s website. If, upon inspection of the maintenance tools, organizations determine that the tools have been modified in an improper manner or the tools contain malicious code, the incident is handled consistent with organizational policies and procedures for incident handling.

### Requirements and exact statement parts

- `ma-3.1_smt`: Inspect the maintenance tools used by maintenance personnel for improper or unauthorized modifications.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-3.1_smt — Inspect the maintenance tools used by maintenance personnel for improper or unauthorized modifications.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ma-3.1_smt` — For “Inspect the maintenance tools used by maintenance personnel for improper or unauthorized modifications.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-3.1_obj` (ma-3.1_smt): maintenance tools used by maintenance personnel are inspected for improper or unauthorized modifications.

#### EXAMINE — `ma-3.1_asm-examine`

- Maintenance policy

- procedures addressing system maintenance tools

- system maintenance tools and associated documentation

- maintenance tool inspection records

- maintenance records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-3.1_asm-interview`

- Organizational personnel with system maintenance responsibilities

- organizational personnel with information security responsibilities

#### TEST — `ma-3.1_asm-test`

- Organizational processes for inspecting maintenance tools

- mechanisms supporting and/or implementing the inspection of maintenance tools

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-3.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ma-3`.

- Catalog relationship **related**: `si-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
