---
title: "CM-4.2 \u2014 Verification of Controls"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-4.2 — Verification of Controls

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Implementation in this context refers to installing changed code in the operational system that may have an impact on security or privacy controls.

### Requirements and exact statement parts

- `cm-4.2_smt`: After system changes, verify that the impacted controls are implemented correctly, operating as intended, and producing the desired outcome with regard to meeting the security and privacy requirements for the system.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-4.2_smt — After system changes, verify that the impacted controls are implemented correctly, operating as intended, and producing the desired outcome with regard to meeting the security and privacy requirements for the system.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `cm-4.2_smt` — For “After system changes, verify that the impacted controls are implemented correctly, operating as intended, and producing the desired outcome with regard to meeting the security and privacy requirements for the system.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-4.2_obj-1` (cm-4.2_smt): the impacted controls are implemented correctly with regard to meeting the security requirements for the system after system changes;

- `cm-4.2_obj-2` (cm-4.2_smt): the impacted controls are implemented correctly with regard to meeting the privacy requirements for the system after system changes;

- `cm-4.2_obj-3` (cm-4.2_smt): the impacted controls are operating as intended with regard to meeting the security requirements for the system after system changes;

- `cm-4.2_obj-4` (cm-4.2_smt): the impacted controls are operating as intended with regard to meeting the privacy requirements for the system after system changes;

- `cm-4.2_obj-5` (cm-4.2_smt): the impacted controls are producing the desired outcome with regard to meeting the security requirements for the system after system changes;

- `cm-4.2_obj-6` (cm-4.2_smt): the impacted controls are producing the desired outcome with regard to meeting the privacy requirements for the system after system changes.

#### EXAMINE — `cm-4.2_asm-examine`

- Configuration management policy

- procedures addressing security impact analyses for changes to the system

- procedures addressing privacy impact analyses for changes to the system

- privacy risk assessment documentation

- configuration management plan

- security and privacy impact analysis documentation

- privacy impact assessment

- analysis tools and associated outputs

- change control records

- control assessment results

- system audit records

- system component inventory

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `cm-4.2_asm-interview`

- Organizational personnel with responsibility for conducting security and privacy impact analyses

- organizational personnel with information security and privacy responsibilities

- system/network administrators

- security and privacy assessors

#### TEST — `cm-4.2_asm-test`

- Organizational processes for security and privacy impact analyses

- mechanisms supporting and/or implementing security and privacy impact analyses of changes

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-4.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-4`.

- Catalog relationship **related**: `sa-11`.

- Catalog relationship **related**: `sc-3`.

- Catalog relationship **related**: `si-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
