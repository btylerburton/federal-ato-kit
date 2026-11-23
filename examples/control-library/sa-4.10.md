---
title: "SA-4.10 \u2014 Use of Approved PIV Products"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-4.10 — Use of Approved PIV Products

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Products on the FIPS 201-approved products list meet NIST requirements for Personal Identity Verification (PIV) of Federal Employees and Contractors. PIV cards are used for multi-factor authentication in systems and organizations.

### Requirements and exact statement parts

- `sa-4.10_smt`: Employ only information technology products on the FIPS 201-approved products list for Personal Identity Verification (PIV) capability implemented within organizational systems.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-4.10_smt — Employ only information technology products on the FIPS 201-approved products list for Personal Identity Verification (PIV) capability implemented within organizational systems.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sa-4.10_smt` — For “Employ only information technology products on the FIPS 201-approved products list for Personal Identity Verification (PIV) capability implemented within organizational systems.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-4.10_obj` (sa-4.10_smt): only information technology products on the FIPS 201-approved products list for the Personal Identity Verification (PIV) capability implemented within organizational systems are employed.

#### EXAMINE — `sa-4.10_asm-examine`

- Supply chain risk management plan

- system and services acquisition policy

- procedures addressing the integration of security requirements, descriptions, and criteria into the acquisition process

- solicitation documentation

- acquisition documentation

- acquisition contracts for the system, system component, or system service

- service level agreements

- FIPS 201 approved products list

- system security plan

- other relevant documents or records

#### INTERVIEW — `sa-4.10_asm-interview`

- Organizational personnel with acquisition/contracting responsibilities

- organizational personnel with the responsibility for determining system security requirements

- organizational personnel with the responsibility for ensuring that only FIPS 201- approved products are implemented

- organizational personnel with information security responsibilities

#### TEST — `sa-4.10_asm-test`

- Organizational processes for selecting and employing FIPS 201-approved products

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-4.10`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-4`.

- Catalog relationship **related**: `ia-2`.

- Catalog relationship **related**: `ia-8`.

- Catalog relationship **related**: `pm-9`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
