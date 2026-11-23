---
title: "PE-2.2 \u2014 Two Forms of Identification"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PE-2.2 — Two Forms of Identification

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Acceptable forms of identification include passports, REAL ID-compliant drivers’ licenses, and Personal Identity Verification (PIV) cards. For gaining access to facilities using automated mechanisms, organizations may use PIV cards, key cards, PINs, and biometrics.

### Requirements and exact statement parts

- `pe-2.2_smt`: Require two forms of identification from the following forms of identification for visitor access to the facility where the system resides: [PARAM pe-02.02_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pe-2.2_smt — Require two forms of identification from the following forms of identification for visitor access to the facility where the system resides: [PARAM pe-02.02_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pe-02.02_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pe-2.2_smt` — For “Require two forms of identification from the following forms of identification for visitor access to the facility where the system resides: [PARAM pe-02.02_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pe-02.02_odp` — What approved value applies to **list of acceptable forms of identification**? Record the value, scope, approving authority, and decision source.

  - Catalog context: a list of acceptable forms of identification for visitor access to the facility where the system resides is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pe-2.2_obj` (pe-2.2_smt): two forms of identification are required from [PARAM pe-02.02_odp] for visitor access to the facility where the system resides.

#### EXAMINE — `pe-2.2_asm-examine`

- Physical and environmental protection policy

- procedures addressing physical access authorizations

- list of acceptable forms of identification for visitor access to the facility where the system resides

- access authorization forms

- access credentials

- physical access control logs or records

- system security plan

- other relevant documents or records

#### INTERVIEW — `pe-2.2_asm-interview`

- Organizational personnel with physical access authorization responsibilities

- organizational personnel with physical access to the system facility

- organizational personnel with information security responsibilities

#### TEST — `pe-2.2_asm-test`

- Organizational processes for physical access authorizations

- mechanisms supporting and/or implementing physical access authorizations

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pe-2.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pe-2`.

- Catalog relationship **related**: `ia-2`.

- Catalog relationship **related**: `ia-4`.

- Catalog relationship **related**: `ia-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
