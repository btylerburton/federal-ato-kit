---
title: "IA-8.5 \u2014 Acceptance of PIV-I Credentials"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-8.5 — Acceptance of PIV-I Credentials

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Acceptance of PIV-I credentials can be implemented by PIV, PIV-I, and other commercial or external identity providers. The acceptance and verification of PIV-I-compliant credentials apply to both logical and physical access control systems. The acceptance and verification of PIV-I credentials address nonfederal issuers of identity cards that desire to interoperate with United States Government PIV systems and that can be trusted by Federal Government-relying parties. The X.509 certificate policy for the Federal Bridge Certification Authority (FBCA) addresses PIV-I requirements. The PIV-I card is commensurate with the PIV credentials as defined in cited references. PIV-I credentials are the credentials issued by a PIV-I provider whose PIV-I certificate policy maps to the Federal Bridge PIV-I Certificate Policy. A PIV-I provider is cross-certified with the FBCA (directly or through another PKI bridge) with policies that have been mapped and approved as meeting the requirements of the PIV-I policies defined in the FBCA certificate policy.

### Requirements and exact statement parts

- `ia-8.5_smt`: Accept and verify federated or PKI credentials that meet [PARAM ia-08.05_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-8.5_smt — Accept and verify federated or PKI credentials that meet [PARAM ia-08.05_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ia-08.05_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ia-8.5_smt` — For “Accept and verify federated or PKI credentials that meet [PARAM ia-08.05_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ia-08.05_odp` — What approved value applies to **policy**? Record the value, scope, approving authority, and decision source.

  - Catalog context: a policy for using federated or PKI credentials is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-8.5_obj-1` (ia-8.5_smt): federated or PKI credentials that meet [PARAM ia-08.05_odp] are accepted;

- `ia-8.5_obj-2` (ia-8.5_smt): federated or PKI credentials that meet [PARAM ia-08.05_odp] are verified.

#### EXAMINE — `ia-8.5_asm-examine`

- Identification and authentication policy

- system security plan

- procedures addressing user identification and authentication

- system design documentation

- system configuration settings and associated documentation

- system audit records

- PIV-I verification records

- evidence of PIV-I credentials

- PIV-I credential authorizations

- other relevant documents or records

#### INTERVIEW — `ia-8.5_asm-interview`

- Organizational personnel with system operations responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

- organizational personnel with account management responsibilities

#### TEST — `ia-8.5_asm-test`

- Mechanisms supporting and/or implementing identification and authentication capabilities

- mechanisms that accept and verify PIV-I credentials

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-8.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
