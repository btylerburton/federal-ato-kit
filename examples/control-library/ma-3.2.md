---
title: "MA-3.2 \u2014 Inspect Media"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-3.2 — Inspect Media

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

If, upon inspection of media containing maintenance, diagnostic, and test programs, organizations determine that the media contains malicious code, the incident is handled consistent with organizational incident handling policies and procedures.

### Requirements and exact statement parts

- `ma-3.2_smt`: Check media containing diagnostic and test programs for malicious code before the media are used in the system.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-3.2_smt — Check media containing diagnostic and test programs for malicious code before the media are used in the system.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ma-3.2_smt` — For “Check media containing diagnostic and test programs for malicious code before the media are used in the system.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-3.2_obj` (ma-3.2_smt): media containing diagnostic and test programs are checked for malicious code before the media are used in the system.

#### EXAMINE — `ma-3.2_asm-examine`

- Maintenance policy

- procedures addressing system maintenance tools

- system maintenance tools and associated documentation

- maintenance records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-3.2_asm-interview`

- Organizational personnel with system maintenance responsibilities

- organizational personnel with information security responsibilities

#### TEST — `ma-3.2_asm-test`

- Organizational process for inspecting media for malicious code

- mechanisms supporting and/or implementing the inspection of media used for maintenance

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-3.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ma-3`.

- Catalog relationship **related**: `si-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
