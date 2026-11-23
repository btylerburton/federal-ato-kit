---
title: "AU-3.1 \u2014 Additional Audit Information"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-3.1 — Additional Audit Information

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The ability to add information generated in audit records is dependent on system functionality to configure the audit record content. Organizations may consider additional information in audit records including, but not limited to, access control or flow control rules invoked and individual identities of group account users. Organizations may also consider limiting additional audit record information to only information that is explicitly needed for audit requirements. This facilitates the use of audit trails and audit logs by not including information in audit records that could potentially be misleading, make it more difficult to locate information of interest, or increase the risk to individuals' privacy.

### Requirements and exact statement parts

- `au-3.1_smt`: Generate audit records containing the following additional information: [PARAM au-03.01_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-3.1_smt — Generate audit records containing the following additional information: [PARAM au-03.01_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-03.01_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-3.1_smt` — For “Generate audit records containing the following additional information: [PARAM au-03.01_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-03.01_odp` — What approved value applies to **additional information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: additional information to be included in audit records is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-3.1_obj` (au-3.1_smt): generated audit records contain the following [PARAM au-03.01_odp].

#### EXAMINE — `au-3.1_asm-examine`

- Audit and accountability policy

- procedures addressing content of audit records

- system security plan

- privacy plan

- system design documentation

- system configuration settings and associated documentation

- list of organization-defined auditable events

- system audit records

- other relevant documents or records

#### INTERVIEW — `au-3.1_asm-interview`

- Organizational personnel with audit and accountability responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

- system developers

#### TEST — `au-3.1_asm-test`

- system audit capability

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-3.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `au-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
