---
title: "AC-4.32 \u2014 Process Requirements for Information Transfer"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4.32 — Process Requirements for Information Transfer

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The processes transferring information between filter pipelines have minimum complexity and functionality to provide assurance that the processes operate correctly.

### Requirements and exact statement parts

- `ac-4.32_smt`: When transferring information between different security domains, the process that transfers information between filter pipelines:

- `ac-4.32_smt.a`: Does not filter message content;

- `ac-4.32_smt.b`: Validates filtering metadata;

- `ac-4.32_smt.c`: Ensures the content associated with the filtering metadata has successfully completed filtering; and

- `ac-4.32_smt.d`: Transfers the content to the destination filter pipeline.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4.32_smt — When transferring information between different security domains, the process that transfers information between filter pipelines:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-4.32_smt.a — Does not filter message content;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-4.32_smt.b — Validates filtering metadata;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-4.32_smt.c — Ensures the content associated with the filtering metadata has successfully completed filtering; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-4.32_smt.d — Transfers the content to the destination filter pipeline.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ac-4.32_smt` — For “When transferring information between different security domains, the process that transfers information between filter pipelines:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-4.32_smt.a` — For “Does not filter message content;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-4.32_smt.b` — For “Validates filtering metadata;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-4.32_smt.c` — For “Ensures the content associated with the filtering metadata has successfully completed filtering; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-4.32_smt.d` — For “Transfers the content to the destination filter pipeline.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4.32_obj.a` (ac-4.32_smt.a): when transferring information between different security domains, the process that transfers information between filter pipelines does not filter message content;

- `ac-4.32_obj.b` (ac-4.32_smt.b): when transferring information between different security domains, the process that transfers information between filter pipelines validates filtering metadata;

- `ac-4.32_obj.c` (ac-4.32_smt.c): when transferring information between different security domains, the process that transfers information between filter pipelines ensures that the content with the filtering metadata has successfully completed filtering;

- `ac-4.32_obj.d` (ac-4.32_smt.d): when transferring information between different security domains, the process that transfers information between filter pipelines transfers the content to the destination filter pipeline.

#### EXAMINE — `ac-4.32_asm-examine`

- Information flow enforcement policy

- procedures addressing information flow enforcement

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-4.32_asm-interview`

- Organizational personnel with information flow enforcement responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

#### TEST — `ac-4.32_asm-test`

- Mechanisms implementing information flow enforcement functions

- mechanisms implementing content filtering

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4.32`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
