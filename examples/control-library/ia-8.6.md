---
title: "IA-8.6 \u2014 Disassociability"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-8.6 — Disassociability

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Federated identity solutions can create increased privacy risks due to the tracking and profiling of individuals. Using identifier mapping tables or cryptographic techniques to blind credential service providers and relying parties from each other or to make identity attributes less visible to transmitting parties can reduce these privacy risks.

### Requirements and exact statement parts

- `ia-8.6_smt`: Implement the following measures to disassociate user attributes or identifier assertion relationships among individuals, credential service providers, and relying parties: [PARAM ia-08.06_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-8.6_smt — Implement the following measures to disassociate user attributes or identifier assertion relationships among individuals, credential service providers, and relying parties: [PARAM ia-08.06_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ia-08.06_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ia-8.6_smt` — For “Implement the following measures to disassociate user attributes or identifier assertion relationships among individuals, credential service providers, and relying parties: [PARAM ia-08.06_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ia-08.06_odp` — What approved value applies to **measures**? Record the value, scope, approving authority, and decision source.

  - Catalog context: disassociability measures are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-8.6_obj` (ia-8.6_smt): [PARAM ia-08.06_odp] to disassociate user attributes or identifier assertion relationships among individuals, credential service providers, and relying parties are implemented.

#### EXAMINE — `ia-8.6_asm-examine`

- Identification and authentication policy

- system security plan

- privacy plan

- procedures addressing user identification and authentication

- system design documentation

- system configuration settings and associated documentation

- system audit records

- other relevant documents or records

#### INTERVIEW — `ia-8.6_asm-interview`

- Organizational personnel with system operations responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

- system developers

- organizational personnel with account management responsibilities

#### TEST — `ia-8.6_asm-test`

- Mechanisms supporting and/or implementing identification and authentication capabilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-8.6`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
