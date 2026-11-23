---
title: "CP-9.2 \u2014 Test Restoration Using Sampling"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-9.2 — Test Restoration Using Sampling

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations need assurance that system functions can be restored correctly and can support established organizational missions. To ensure that the selected system functions are thoroughly exercised during contingency plan testing, a sample of backup information is retrieved to determine whether the functions are operating as intended. Organizations can determine the sample size for the functions and backup information based on the level of assurance needed.

### Requirements and exact statement parts

- `cp-9.2_smt`: Use a sample of backup information in the restoration of selected system functions as part of contingency plan testing.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-9.2_smt — Use a sample of backup information in the restoration of selected system functions as part of contingency plan testing.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `cp-9.2_smt` — For “Use a sample of backup information in the restoration of selected system functions as part of contingency plan testing.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-9.2_obj` (cp-9.2_smt): a sample of backup information in the restoration of selected system functions is used as part of contingency plan testing.

#### EXAMINE — `cp-9.2_asm-examine`

- Contingency planning policy

- procedures addressing system backup

- contingency plan

- system backup test results

- contingency plan test documentation

- contingency plan test results

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-9.2_asm-interview`

- Organizational personnel with system backup responsibilities

- organizational personnel with contingency planning/contingency plan testing responsibilities

- organizational personnel with information security responsibilities

#### TEST — `cp-9.2_asm-test`

- Organizational processes for conducting system backups

- mechanisms supporting and/or implementing system backups

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-9.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cp-9`.

- Catalog relationship **related**: `cp-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
