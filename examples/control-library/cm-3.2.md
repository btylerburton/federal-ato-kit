---
title: "CM-3.2 \u2014 Testing, Validation, and Documentation of Changes"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CM-3.2 — Testing, Validation, and Documentation of Changes

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Changes to systems include modifications to hardware, software, or firmware components and configuration settings defined in CM-6 (catalog reference: `#cm-6`) . Organizations ensure that testing does not interfere with system operations that support organizational mission and business functions. Individuals or groups conducting tests understand security and privacy policies and procedures, system security and privacy policies and procedures, and the health, safety, and environmental risks associated with specific facilities or processes. Operational systems may need to be taken offline, or replicated to the extent feasible, before testing can be conducted. If systems must be taken offline for testing, the tests are scheduled to occur during planned system outages whenever possible. If the testing cannot be conducted on operational systems, organizations employ compensating controls.

### Requirements and exact statement parts

- `cm-3.2_smt`: Test, validate, and document changes to the system before finalizing the implementation of the changes.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cm-3.2_smt — Test, validate, and document changes to the system before finalizing the implementation of the changes.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `cm-3.2_smt` — For “Test, validate, and document changes to the system before finalizing the implementation of the changes.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cm-3.2_obj-1` (cm-3.2_smt): changes to the system are tested before finalizing the implementation of the changes;

- `cm-3.2_obj-2` (cm-3.2_smt): changes to the system are validated before finalizing the implementation of the changes;

- `cm-3.2_obj-3` (cm-3.2_smt): changes to the system are documented before finalizing the implementation of the changes.

#### EXAMINE — `cm-3.2_asm-examine`

- Configuration management policy

- configuration management plan

- procedures addressing system configuration change control

- system design documentation

- system architecture and configuration documentation

- system configuration settings and associated documentation

- test records

- validation records

- change control records

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cm-3.2_asm-interview`

- Organizational personnel with configuration change control responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

- members of change control board or similar

#### TEST — `cm-3.2_asm-test`

- Organizational processes for configuration change control

- mechanisms supporting and/or implementing, testing, validating, and documenting system changes

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cm-3.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cm-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
