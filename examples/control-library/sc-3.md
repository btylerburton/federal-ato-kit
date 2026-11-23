---
title: "SC-3 \u2014 Security Function Isolation"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-3 — Security Function Isolation

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Security functions are isolated from nonsecurity functions by means of an isolation boundary implemented within a system via partitions and domains. The isolation boundary controls access to and protects the integrity of the hardware, software, and firmware that perform system security functions. Systems implement code separation in many ways, such as through the provision of security kernels via processor rings or processor modes. For non-kernel code, security function isolation is often achieved through file system protections that protect the code on disk and address space protections that protect executing code. Systems can restrict access to security functions using access control mechanisms and by implementing least privilege capabilities. While the ideal is for all code within the defined security function isolation boundary to only contain security-relevant code, it is sometimes necessary to include nonsecurity functions as an exception. The isolation of security functions from nonsecurity functions can be achieved by applying the systems security engineering design principles in SA-8 (catalog reference: `#sa-8`) , including SA-8(1) (catalog reference: `#sa-8.1`), SA-8(3) (catalog reference: `#sa-8.3`), SA-8(4) (catalog reference: `#sa-8.4`), SA-8(10) (catalog reference: `#sa-8.10`), SA-8(12) (catalog reference: `#sa-8.12`), SA-8(13) (catalog reference: `#sa-8.13`), SA-8(14) (catalog reference: `#sa-8.14`) , and SA-8(18) (catalog reference: `#sa-8.18`).

### Requirements and exact statement parts

- `sc-3_smt`: Isolate security functions from nonsecurity functions.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-3_smt — Isolate security functions from nonsecurity functions.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sc-3_smt` — For “Isolate security functions from nonsecurity functions.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-3_obj` (sc-3_smt): security functions are isolated from non-security functions.

#### EXAMINE — `sc-3_asm-examine`

- System and communications protection policy

- procedures addressing security function isolation

- list of security functions to be isolated from non-security functions

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-3_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developer

#### TEST — `sc-3_asm-test`

- Separation of security functions from non-security functions within the system

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-3`. The library index records the exact source revision and hash.

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-6`.

- Catalog relationship **related**: `ac-25`.

- Catalog relationship **related**: `cm-2`.

- Catalog relationship **related**: `cm-4`.

- Catalog relationship **related**: `sa-4`.

- Catalog relationship **related**: `sa-5`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sa-15`.

- Catalog relationship **related**: `sa-17`.

- Catalog relationship **related**: `sc-2`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `sc-32`.

- Catalog relationship **related**: `sc-39`.

- Catalog relationship **related**: `si-16`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
