---
title: "CM-4 \u2014 Impact Analyses"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-4 — Impact Analyses

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizational personnel with security or privacy responsibilities conduct impact analyses. Individuals conducting impact analyses possess the necessary skills and technical expertise to analyze the changes to systems as well as the security or privacy ramifications. Impact analyses include reviewing security and privacy plans, policies, and procedures to understand control requirements; reviewing system design documentation and operational procedures to understand control implementation and how specific system changes might affect the controls; reviewing the impact of changes on organizational supply chain partners with stakeholders; and determining how potential changes to a system create new risks to the privacy of individuals and the ability of implemented controls to mitigate those risks. Impact analyses also include risk assessments to understand the impact of the changes and determine if additional controls are required.

### Requirements and exact statement parts

- `cm-4_smt`: Analyze changes to the system to determine potential security and privacy impacts prior to change implementation.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-4_smt — Analyze changes to the system to determine potential security and privacy impacts prior to change implementation.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `cm-4_smt` — For “Analyze changes to the system to determine potential security and privacy impacts prior to change implementation.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-4_obj-1` (cm-4_smt): changes to the system are analyzed to determine potential security impacts prior to change implementation;

- `cm-4_obj-2` (cm-4_smt): changes to the system are analyzed to determine potential privacy impacts prior to change implementation.

#### EXAMINE — `cm-4_asm-examine`

- Configuration management policy

- procedures addressing security impact analyses for changes to the system

- procedures addressing privacy impact analyses for changes to the system

- configuration management plan

- security impact analysis documentation

- privacy impact analysis documentation

- privacy impact assessment

- privacy risk assessment documentation, system design documentation

- analysis tools and associated outputs

- change control records

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `cm-4_asm-interview`

- Organizational personnel with responsibility for conducting security impact analyses

- organizational personnel with responsibility for conducting privacy impact analyses

- organizational personnel with information security and privacy responsibilities

- system developer

- system/network administrators

- members of change control board or similar

#### TEST — `cm-4_asm-test`

- Organizational processes for security impact analyses

- organizational processes for privacy impact analyses

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-4`. The library index records the exact source revision and hash.

- [SP 800-128](https://doi.org/10.6028/NIST.SP.800-128)

- Catalog relationship **related**: `ca-7`.

- Catalog relationship **related**: `cm-3`.

- Catalog relationship **related**: `cm-8`.

- Catalog relationship **related**: `cm-9`.

- Catalog relationship **related**: `ma-2`.

- Catalog relationship **related**: `ra-3`.

- Catalog relationship **related**: `ra-5`.

- Catalog relationship **related**: `ra-8`.

- Catalog relationship **related**: `sa-5`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sa-10`.

- Catalog relationship **related**: `si-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
