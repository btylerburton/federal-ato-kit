---
title: "IA-2.12 \u2014 Acceptance of PIV Credentials"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-2.12 — Acceptance of PIV Credentials

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Acceptance of Personal Identity Verification (PIV)-compliant credentials applies to organizations implementing logical access control and physical access control systems. PIV-compliant credentials are those credentials issued by federal agencies that conform to FIPS Publication 201 and supporting guidance documents. The adequacy and reliability of PIV card issuers are authorized using SP 800-79-2 (catalog reference: `#10963761-58fc-4b20-b3d6-b44a54daba03`) . Acceptance of PIV-compliant credentials includes derived PIV credentials, the use of which is addressed in SP 800-166 (catalog reference: `#e8552d48-cf41-40aa-8b06-f45f7fb4706c`) . The DOD Common Access Card (CAC) is an example of a PIV credential.

### Requirements and exact statement parts

- `ia-2.12_smt`: Accept and electronically verify Personal Identity Verification-compliant credentials.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-2.12_smt — Accept and electronically verify Personal Identity Verification-compliant credentials.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ia-2.12_smt` — For “Accept and electronically verify Personal Identity Verification-compliant credentials.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-2.12_obj` (ia-2.12_smt): Personal Identity Verification-compliant credentials are accepted and electronically verified.

#### EXAMINE — `ia-2.12_asm-examine`

- Identification and authentication policy

- system security plan

- procedures addressing user identification and authentication

- system design documentation

- system configuration settings and associated documentation

- system audit records

- PIV verification records

- evidence of PIV credentials

- PIV credential authorizations

- other relevant documents or records

#### INTERVIEW — `ia-2.12_asm-interview`

- Organizational personnel with system operations responsibilities

- organizational personnel with account management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `ia-2.12_asm-test`

- Mechanisms supporting and/or implementing acceptance and verification of PIV credentials

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-2.12`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
