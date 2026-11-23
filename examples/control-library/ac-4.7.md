---
title: "AC-4.7 \u2014 One-way Flow Mechanisms"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4.7 — One-way Flow Mechanisms

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

One-way flow mechanisms may also be referred to as a unidirectional network, unidirectional security gateway, or data diode. One-way flow mechanisms can be used to prevent data from being exported from a higher impact or classified domain or system while permitting data from a lower impact or unclassified domain or system to be imported.

### Requirements and exact statement parts

- `ac-4.7_smt`: Enforce one-way information flows through hardware-based flow control mechanisms.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4.7_smt — Enforce one-way information flows through hardware-based flow control mechanisms.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ac-4.7_smt` — For “Enforce one-way information flows through hardware-based flow control mechanisms.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4.7_obj` (ac-4.7_smt): one-way information flows are enforced through hardware-based flow control mechanisms.

#### EXAMINE — `ac-4.7_asm-examine`

- Access control policy

- information flow control policies

- procedures addressing information flow enforcement

- system design documentation

- system configuration settings and associated documentation

- system hardware mechanisms and associated configurations

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-4.7_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developers

#### TEST — `ac-4.7_asm-test`

- Hardware mechanisms implementing information flow enforcement policy

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
