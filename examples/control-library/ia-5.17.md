---
title: "IA-5.17 \u2014 Presentation Attack Detection for Biometric Authenticators"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-5.17 — Presentation Attack Detection for Biometric Authenticators

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Biometric characteristics do not constitute secrets. Such characteristics can be obtained by online web accesses, taking a picture of someone with a camera phone to obtain facial images with or without their knowledge, lifting from objects that someone has touched (e.g., a latent fingerprint), or capturing a high-resolution image (e.g., an iris pattern). Presentation attack detection technologies including liveness detection, can mitigate the risk of these types of attacks by making it difficult to produce artifacts intended to defeat the biometric sensor.

### Requirements and exact statement parts

- `ia-5.17_smt`: Employ presentation attack detection mechanisms for biometric-based authentication.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-5.17_smt — Employ presentation attack detection mechanisms for biometric-based authentication.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ia-5.17_smt` — For “Employ presentation attack detection mechanisms for biometric-based authentication.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-5.17_obj` (ia-5.17_smt): presentation attack detection mechanisms are employed for biometric-based authentication.

#### EXAMINE — `ia-5.17_asm-examine`

- Identification and authentication policy

- procedures addressing identifier management

- system security plan

- system design documentation

- mechanisms providing dynamic binding of identifiers and authenticators

- system configuration settings and associated documentation

- system audit records

- other relevant documents or records

#### INTERVIEW — `ia-5.17_asm-interview`

- Organizational personnel with identification and authentication management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ia-5.17_asm-test`

- Mechanisms supporting and/or implementing account management capability

- mechanisms supporting and/or implementing identification and authentication management capabilities for the system

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-5.17`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-5`.

- Catalog relationship **related**: `ac-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
