---
title: "CA-9.1 \u2014 Compliance Checks"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CA-9.1 — Compliance Checks

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Compliance checks include verification of the relevant baseline configuration.

### Requirements and exact statement parts

- `ca-9.1_smt`: Perform security and privacy compliance checks on constituent system components prior to the establishment of the internal connection.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ca-9.1_smt — Perform security and privacy compliance checks on constituent system components prior to the establishment of the internal connection.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ca-9.1_smt` — For “Perform security and privacy compliance checks on constituent system components prior to the establishment of the internal connection.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ca-9.1_obj-1` (ca-9.1_smt): security compliance checks are performed on constituent system components prior to the establishment of the internal connection;

- `ca-9.1_obj-2` (ca-9.1_smt): privacy compliance checks are performed on constituent system components prior to the establishment of the internal connection.

#### EXAMINE — `ca-9.1_asm-examine`

- Assessment, authorization, and monitoring policy

- access control policy

- procedures addressing system connections

- system and communications protection policy

- system design documentation

- system configuration settings and associated documentation

- list of components or classes of components authorized as internal system connections

- assessment report

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ca-9.1_asm-interview`

- Organizational personnel with responsibilities for developing, implementing, or authorizing internal system connections

- organizational personnel with information security and privacy responsibilities

#### TEST — `ca-9.1_asm-test`

- Mechanisms supporting compliance checks

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ca-9.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ca-9`.

- Catalog relationship **related**: `cm-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
