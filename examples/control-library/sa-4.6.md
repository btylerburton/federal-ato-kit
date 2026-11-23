---
title: "SA-4.6 \u2014 Use of Information Assurance Products"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-4.6 — Use of Information Assurance Products

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Commercial off-the-shelf IA or IA-enabled information technology products used to protect classified information by cryptographic means may be required to use NSA-approved key management. See NSA CSFC (catalog reference: `#3d575737-98cb-459d-b41c-d7e82b73ad78`).

### Requirements and exact statement parts

- `sa-4.6_smt`: Statement grouping; see child parts.

- `sa-4.6_smt.a`: Employ only government off-the-shelf or commercial off-the-shelf information assurance and information assurance-enabled information technology products that compose an NSA-approved solution to protect classified information when the networks used to transmit the information are at a lower classification level than the information being transmitted; and

- `sa-4.6_smt.b`: Ensure that these products have been evaluated and/or validated by NSA or in accordance with NSA-approved procedures.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-4.6_smt.a — Employ only government off-the-shelf or commercial off-the-shelf information assurance and information assurance-enabled information technology products that compose an NSA-approved solution to protect classified information when the networks used to transmit the information are at a lower classification level than the information being transmitted; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sa-4.6_smt.b — Ensure that these products have been evaluated and/or validated by NSA or in accordance with NSA-approved procedures.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sa-4.6_smt.a` — For “Employ only government off-the-shelf or commercial off-the-shelf information assurance and information assurance-enabled information technology products that compose an NSA-approved solution to protect classified information when the networks used to transmit the information are at a lower classification level than the information being transmitted; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sa-4.6_smt.b` — For “Ensure that these products have been evaluated and/or validated by NSA or in accordance with NSA-approved procedures.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-4.6_obj.a` (sa-4.6_smt.a): only government off-the-shelf or commercial off-the-shelf information assurance and information assurance-enabled information technology products that compose an NSA-approved solution to protect classified information when the networks used to transmit the information are at a lower classification level than the information being transmitted are employed;

- `sa-4.6_obj.b` (sa-4.6_smt.b): these products have been evaluated and/or validated by NSA or in accordance with NSA-approved procedures.

#### EXAMINE — `sa-4.6_asm-examine`

- Supply chain risk management plan

- system and services acquisition policy

- procedures addressing the integration of security requirements, descriptions, and criteria into the acquisition process

- solicitation documents

- acquisition documentation

- acquisition contracts for the system, system component, or system service

- security configurations to be implemented by the developer of the system, system component, or system service

- service level agreements

- list of deployed IT products/solutions

- NSA-approved list

- system security plan

- other relevant documents or records

#### INTERVIEW — `sa-4.6_asm-interview`

- Organizational personnel with acquisition/contracting responsibilities

- organizational personnel with the responsibility to determine system security requirements

- organizational personnel responsible for ensuring information assurance products are NSA-approved and are evaluated and/or validated products in accordance with NSA-approved procedures

- organizational personnel with information security responsibilities

#### TEST — `sa-4.6_asm-test`

- Organizational processes for selecting and employing evaluated and/or validated information assurance products and services that compose an NSA-approved solution to protect classified information

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-4.6`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-4`.

- Catalog relationship **related**: `sc-8`.

- Catalog relationship **related**: `sc-12`.

- Catalog relationship **related**: `sc-13`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
