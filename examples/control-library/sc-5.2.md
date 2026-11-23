---
title: "SC-5.2 \u2014 Capacity, Bandwidth, and Redundancy"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-5.2 — Capacity, Bandwidth, and Redundancy

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Managing capacity ensures that sufficient capacity is available to counter flooding attacks. Managing capacity includes establishing selected usage priorities, quotas, partitioning, or load balancing.

### Requirements and exact statement parts

- `sc-5.2_smt`: Manage capacity, bandwidth, or other redundancy to limit the effects of information flooding denial-of-service attacks.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-5.2_smt — Manage capacity, bandwidth, or other redundancy to limit the effects of information flooding denial-of-service attacks.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sc-5.2_smt` — For “Manage capacity, bandwidth, or other redundancy to limit the effects of information flooding denial-of-service attacks.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-5.2_obj` (sc-5.2_smt): capacity, bandwidth, or other redundancies to limit the effects of information flooding denial-of-service attacks are managed.

#### EXAMINE — `sc-5.2_asm-examine`

- System and communications protection policy

- procedures addressing denial-of-service protection

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-5.2_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel with incident response responsibilities

- system developer

#### TEST — `sc-5.2_asm-test`

- Mechanisms implementing the management of system bandwidth, capacity, and redundancy to limit the effects of information flooding denial-of-service attacks

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-5.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sc-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
