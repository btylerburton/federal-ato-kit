---
title: "CM-2.6 \u2014 Development and Test Environments"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-2.6 — Development and Test Environments

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Establishing separate baseline configurations for development, testing, and operational environments protects systems from unplanned or unexpected events related to development and testing activities. Separate baseline configurations allow organizations to apply the configuration management that is most appropriate for each type of configuration. For example, the management of operational configurations typically emphasizes the need for stability, while the management of development or test configurations requires greater flexibility. Configurations in the test environment mirror configurations in the operational environment to the extent practicable so that the results of the testing are representative of the proposed changes to the operational systems. Separate baseline configurations do not necessarily require separate physical environments.

### Requirements and exact statement parts

- `cm-2.6_smt`: Maintain a baseline configuration for system development and test environments that is managed separately from the operational baseline configuration.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-2.6_smt — Maintain a baseline configuration for system development and test environments that is managed separately from the operational baseline configuration.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `cm-2.6_smt` — For “Maintain a baseline configuration for system development and test environments that is managed separately from the operational baseline configuration.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-2.6_obj-1` (cm-2.6_smt): a baseline configuration for system development environments that is managed separately from the operational baseline configuration is maintained;

- `cm-2.6_obj-2` (cm-2.6_smt): a baseline configuration for test environments that is managed separately from the operational baseline configuration is maintained.

#### EXAMINE — `cm-2.6_asm-examine`

- Configuration management policy

- procedures addressing the baseline configuration of the system

- configuration management plan

- system design documentation

- system architecture and configuration documentation

- system configuration settings and associated documentation

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-2.6_asm-interview`

- Organizational personnel with configuration management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `cm-2.6_asm-test`

- Organizational processes for managing baseline configurations

- mechanisms implementing separate baseline configurations for development, test, and operational environments

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-2.6`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-2`.

- Catalog relationship **related**: `cm-4`.

- Catalog relationship **related**: `sc-3`.

- Catalog relationship **related**: `sc-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
