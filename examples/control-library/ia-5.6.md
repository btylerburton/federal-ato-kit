---
title: "IA-5.6 \u2014 Protection of Authenticators"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-5.6 — Protection of Authenticators

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

For systems that contain multiple security categories of information without reliable physical or logical separation between categories, authenticators used to grant access to the systems are protected commensurate with the highest security category of information on the systems. Security categories of information are determined as part of the security categorization process.

### Requirements and exact statement parts

- `ia-5.6_smt`: Protect authenticators commensurate with the security category of the information to which use of the authenticator permits access.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-5.6_smt — Protect authenticators commensurate with the security category of the information to which use of the authenticator permits access.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ia-5.6_smt` — For “Protect authenticators commensurate with the security category of the information to which use of the authenticator permits access.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-5.6_obj` (ia-5.6_smt): authenticators are protected commensurate with the security category of the information to which use of the authenticator permits access.

#### EXAMINE — `ia-5.6_asm-examine`

- Identification and authentication policy

- procedures addressing authenticator management

- security categorization documentation for the system

- security assessments of authenticator protections

- risk assessment results

- system security plan

- other relevant documents or records

#### INTERVIEW — `ia-5.6_asm-interview`

- Organizational personnel with authenticator management responsibilities

- organizational personnel implementing and/or maintaining authenticator protections

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ia-5.6_asm-test`

- Mechanisms supporting and/or implementing authenticator management capability

- mechanisms protecting authenticators

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-5.6`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-5`.

- Catalog relationship **related**: `ra-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
