---
title: "IA-8.2 \u2014 Acceptance of External Authenticators"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-8.2 — Acceptance of External Authenticators

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Acceptance of only NIST-compliant external authenticators applies to organizational systems that are accessible to the public (e.g., public-facing websites). External authenticators are issued by nonfederal government entities and are compliant with SP 800-63B (catalog reference: `#e59c5a7c-8b1f-49ca-8de0-6ee0882180ce`) . Approved external authenticators meet or exceed the minimum Federal Government-wide technical, security, privacy, and organizational maturity requirements. Meeting or exceeding Federal requirements allows Federal Government relying parties to trust external authenticators in connection with an authentication transaction at a specified authenticator assurance level.

### Requirements and exact statement parts

- `ia-8.2_smt`: Statement grouping; see child parts.

- `ia-8.2_smt.a`: Accept only external authenticators that are NIST-compliant; and

- `ia-8.2_smt.b`: Document and maintain a list of accepted external authenticators.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-8.2_smt.a — Accept only external authenticators that are NIST-compliant; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-8.2_smt.b — Document and maintain a list of accepted external authenticators.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ia-8.2_smt.a` — For “Accept only external authenticators that are NIST-compliant; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-8.2_smt.b` — For “Document and maintain a list of accepted external authenticators.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-8.2_obj.a` (ia-8.2_smt.a): only external authenticators that are NIST-compliant are accepted;

- `ia-8.2_obj.b-1` (ia-8.2_smt.b): a list of accepted external authenticators is documented;

- `ia-8.2_obj.b-2` (ia-8.2_smt.b): a list of accepted external authenticators is maintained.

#### EXAMINE — `ia-8.2_asm-examine`

- Identification and authentication policy

- system security plan

- procedures addressing user identification and authentication

- system design documentation

- system configuration settings and associated documentation

- system audit records

- list of third-party credentialing products, components, or services procured and implemented by organization

- third-party credential verification records

- evidence of third-party credentials

- third-party credential authorizations

- other relevant documents or records

#### INTERVIEW — `ia-8.2_asm-interview`

- Organizational personnel with system operations responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

- organizational personnel with account management responsibilities

#### TEST — `ia-8.2_asm-test`

- Mechanisms supporting and/or implementing identification and authentication capabilities

- mechanisms that accept external credentials

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-8.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
