---
title: "IA-5.5 \u2014 Change Authenticators Prior to Delivery"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-5.5 — Change Authenticators Prior to Delivery

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Changing authenticators prior to the delivery and installation of system components extends the requirement for organizations to change default authenticators upon system installation by requiring developers and/or installers to provide unique authenticators or change default authenticators for system components prior to delivery and/or installation. However, it typically does not apply to developers of commercial off-the-shelf information technology products. Requirements for unique authenticators can be included in acquisition documents prepared by organizations when procuring systems or system components.

### Requirements and exact statement parts

- `ia-5.5_smt`: Require developers and installers of system components to provide unique authenticators or change default authenticators prior to delivery and installation.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-5.5_smt — Require developers and installers of system components to provide unique authenticators or change default authenticators prior to delivery and installation.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ia-5.5_smt` — For “Require developers and installers of system components to provide unique authenticators or change default authenticators prior to delivery and installation.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-5.5_obj` (ia-5.5_smt): developers and installers of system components are required to provide unique authenticators or change default authenticators prior to delivery and installation.

#### EXAMINE — `ia-5.5_asm-examine`

- Identification and authentication policy

- system security plan

- system and services acquisition policy

- procedures addressing authenticator management

- procedures addressing the integration of security requirements into the acquisition process

- acquisition documentation

- acquisition contracts for system procurements or services

- other relevant documents or records

#### INTERVIEW — `ia-5.5_asm-interview`

- Organizational personnel with authenticator management responsibilities

- organizational personnel with information security, acquisition, and contracting responsibilities

- system developers

#### TEST — `ia-5.5_asm-test`

- Mechanisms supporting and/or implementing authenticator management capability

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-5.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
