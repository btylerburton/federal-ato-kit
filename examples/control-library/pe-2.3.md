---
title: "PE-2.3 \u2014 Restrict Unescorted Access"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PE-2.3 — Restrict Unescorted Access

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Individuals without required security clearances, access approvals, or need to know are escorted by individuals with appropriate physical access authorizations to ensure that information is not exposed or otherwise compromised.

### Requirements and exact statement parts

- `pe-2.3_smt`: Restrict unescorted access to the facility where the system resides to personnel with [PARAM pe-02.03_odp.01].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pe-2.3_smt — Restrict unescorted access to the facility where the system resides to personnel with [PARAM pe-02.03_odp.01].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pe-02.03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pe-02.03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pe-2.3_smt` — For “Restrict unescorted access to the facility where the system resides to personnel with [PARAM pe-02.03_odp.01].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pe-02.03_odp.01` — What approved value applies to **selection; choose one-or-more from: security clearances for all information contained within the system; formal access authorizations for all information contained within the system; need for access to all information contained within the system; [PARAM pe-02.03_odp.02]**? Record the value, scope, approving authority, and decision source.

- `pe-02.03_odp.02` — What approved value applies to **physical access authorizations**? Record the value, scope, approving authority, and decision source.

  - Catalog context: physical access authorizations for unescorted access to the facility where the system resides are defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pe-2.3_obj` (pe-2.3_smt): unescorted access to the facility where the system resides is restricted to personnel with [PARAM pe-02.03_odp.01].

#### EXAMINE — `pe-2.3_asm-examine`

- Physical and environmental protection policy

- procedures addressing physical access authorizations

- authorized personnel access list

- security clearances

- access authorizations

- access credentials

- physical access control logs or records

- system security plan

- other relevant documents or records

#### INTERVIEW — `pe-2.3_asm-interview`

- Organizational personnel with physical access authorization responsibilities

- organizational personnel with physical access to the system facility

- organizational personnel with information security responsibilities

#### TEST — `pe-2.3_asm-test`

- Organizational processes for physical access authorizations

- mechanisms supporting and/or implementing physical access authorizations

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pe-2.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pe-2`.

- Catalog relationship **related**: `ps-2`.

- Catalog relationship **related**: `ps-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
