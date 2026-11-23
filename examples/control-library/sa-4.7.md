---
title: "SA-4.7 \u2014 NIAP-approved Protection Profiles"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-4.7 — NIAP-approved Protection Profiles

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

See NIAP CCEVS (catalog reference: `#795aff72-3e6c-4b6b-a80a-b14d84b7f544`) for additional information on NIAP. See NIST CMVP (catalog reference: `#1acdc775-aafb-4d11-9341-dc6a822e9d38`) for additional information on FIPS-validated cryptographic modules.

### Requirements and exact statement parts

- `sa-4.7_smt`: Statement grouping; see child parts.

- `sa-4.7_smt.a`: Limit the use of commercially provided information assurance and information assurance-enabled information technology products to those products that have been successfully evaluated against a National Information Assurance partnership (NIAP)-approved Protection Profile for a specific technology type, if such a profile exists; and

- `sa-4.7_smt.b`: Require, if no NIAP-approved Protection Profile exists for a specific technology type but a commercially provided information technology product relies on cryptographic functionality to enforce its security policy, that the cryptographic module is FIPS-validated or NSA-approved.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-4.7_smt.a — Limit the use of commercially provided information assurance and information assurance-enabled information technology products to those products that have been successfully evaluated against a National Information Assurance partnership (NIAP)-approved Protection Profile for a specific technology type, if such a profile exists; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sa-4.7_smt.b — Require, if no NIAP-approved Protection Profile exists for a specific technology type but a commercially provided information technology product relies on cryptographic functionality to enforce its security policy, that the cryptographic module is FIPS-validated or NSA-approved.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sa-4.7_smt.a` — For “Limit the use of commercially provided information assurance and information assurance-enabled information technology products to those products that have been successfully evaluated against a National Information Assurance partnership (NIAP)-approved Protection Profile for a specific technology type, if such a profile exists; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sa-4.7_smt.b` — For “Require, if no NIAP-approved Protection Profile exists for a specific technology type but a commercially provided information technology product relies on cryptographic functionality to enforce its security policy, that the cryptographic module is FIPS-validated or NSA-approved.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-4.7_obj.a` (sa-4.7_smt.a): the use of commercially provided information assurance and information assurance-enabled information technology products is limited to those products that have been successfully evaluated against a National Information Assurance partnership (NIAP)-approved Protection Profile for a specific technology type, if such a profile exists;

- `sa-4.7_obj.b` (sa-4.7_smt.b): if no NIAP-approved Protection Profile exists for a specific technology type but a commercially provided information technology product relies on cryptographic functionality to enforce its security policy, that cryptographic module is required to be FIPS-validated or NSA-approved.

#### EXAMINE — `sa-4.7_asm-examine`

- Supply chain risk management plan

- system and services acquisition policy

- procedures addressing the integration of security requirements, descriptions, and criteria into the acquisition process

- solicitation documents

- acquisition documentation

- acquisition contracts for the system, system component, or system service

- list of deployed IT products/solutions

- NAIP-approved protection profiles

- FIPS-validation information for cryptographic functionality

- system security plan

- other relevant documents or records

#### INTERVIEW — `sa-4.7_asm-interview`

- Organizational personnel with acquisition/contracting responsibilities

- organizational personnel with the responsibility for determining system security requirements

- organizational personnel responsible for ensuring that information assurance products have been evaluated against a NIAP-approved protection profile or for ensuring products relying on cryptographic functionality are FIPS-validated

- organizational personnel with information security responsibilities

#### TEST — `sa-4.7_asm-test`

- Organizational processes for selecting and employing products/services evaluated against a NIAP-approved protection profile or FIPS-validated products

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-4.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-4`.

- Catalog relationship **related**: `ia-7`.

- Catalog relationship **related**: `sc-12`.

- Catalog relationship **related**: `sc-13`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
