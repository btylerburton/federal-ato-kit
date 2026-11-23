---
title: "PS-3.1 \u2014 Classified Information"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PS-3.1 — Classified Information

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Classified information is the most sensitive information that the Federal Government processes, stores, or transmits. It is imperative that individuals have the requisite security clearances and system access authorizations prior to gaining access to such information. Access authorizations are enforced by system access controls (see AC-3 (catalog reference: `#ac-3`) ) and flow controls (see AC-4 (catalog reference: `#ac-4`)).

### Requirements and exact statement parts

- `ps-3.1_smt`: Verify that individuals accessing a system processing, storing, or transmitting classified information are cleared and indoctrinated to the highest classification level of the information to which they have access on the system.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ps-3.1_smt — Verify that individuals accessing a system processing, storing, or transmitting classified information are cleared and indoctrinated to the highest classification level of the information to which they have access on the system.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ps-3.1_smt` — For “Verify that individuals accessing a system processing, storing, or transmitting classified information are cleared and indoctrinated to the highest classification level of the information to which they have access on the system.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ps-3.1_obj-1` (ps-3.1_smt): individuals accessing a system processing, storing, or transmitting classified information are cleared;

- `ps-3.1_obj-2` (ps-3.1_smt): individuals accessing a system processing, storing, or transmitting classified information are indoctrinated to the highest classification level of the information to which they have access on the system.

#### EXAMINE — `ps-3.1_asm-examine`

- Personnel security policy

- procedures addressing personnel screening

- records of screened personnel

- system security plan

- other relevant documents or records

#### INTERVIEW — `ps-3.1_asm-interview`

- Organizational personnel with personnel security responsibilities

- organizational personnel with information security responsibilities

#### TEST — `ps-3.1_asm-test`

- Organizational processes for clearing and indoctrinating personnel for access to classified information

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ps-3.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ps-3`.

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
