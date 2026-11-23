---
title: "IA-5.15 \u2014 GSA-approved Products and Services"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-5.15 — GSA-approved Products and Services

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

General Services Administration (GSA)-approved products and services are products and services that have been approved through the GSA conformance program, where applicable, and posted to the GSA Approved Products List. GSA provides guidance for teams to design and build functional and secure systems that comply with Federal Identity, Credential, and Access Management (FICAM) policies, technologies, and implementation patterns.

### Requirements and exact statement parts

- `ia-5.15_smt`: Use only General Services Administration-approved products and services for identity, credential, and access management.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-5.15_smt — Use only General Services Administration-approved products and services for identity, credential, and access management.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ia-5.15_smt` — For “Use only General Services Administration-approved products and services for identity, credential, and access management.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-5.15_obj` (ia-5.15_smt): only General Services Administration-approved products and services are used for identity, credential, and access management.

#### EXAMINE — `ia-5.15_asm-examine`

- Identification and authentication policy

- procedures addressing identifier management

- system security plan

- system design documentation

- mechanisms providing dynamic binding of identifiers and authenticators

- system configuration settings and associated documentation

- system audit records

- other relevant documents or records

#### INTERVIEW — `ia-5.15_asm-interview`

- Organizational personnel with identification and authentication management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ia-5.15_asm-test`

- Mechanisms supporting and/or implementing account management capability

- mechanisms supporting and/or implementing identification and authentication management capabilities for the system

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-5.15`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
