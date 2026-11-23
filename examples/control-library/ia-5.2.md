---
title: "IA-5.2 \u2014 Public Key-based Authentication"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IA-5.2 — Public Key-based Authentication

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Public key cryptography is a valid authentication mechanism for individuals, machines, and devices. For PKI solutions, status information for certification paths includes certificate revocation lists or certificate status protocol responses. For PIV cards, certificate validation involves the construction and verification of a certification path to the Common Policy Root trust anchor, which includes certificate policy processing. Implementing a local cache of revocation data to support path discovery and validation also supports system availability in situations where organizations are unable to access revocation information via the network.

### Requirements and exact statement parts

- `ia-5.2_smt`: Statement grouping; see child parts.

- `ia-5.2_smt.a`: For public key-based authentication:

- `ia-5.2_smt.a.1`: Enforce authorized access to the corresponding private key; and

- `ia-5.2_smt.a.2`: Map the authenticated identity to the account of the individual or group; and

- `ia-5.2_smt.b`: When public key infrastructure (PKI) is used:

- `ia-5.2_smt.b.1`: Validate certificates by constructing and verifying a certification path to an accepted trust anchor, including checking certificate status information; and

- `ia-5.2_smt.b.2`: Implement a local cache of revocation data to support path discovery and validation.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ia-5.2_smt.a — For public key-based authentication:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5.2_smt.a.1 — Enforce authorized access to the corresponding private key; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5.2_smt.a.2 — Map the authenticated identity to the account of the individual or group; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5.2_smt.b — When public key infrastructure (PKI) is used:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5.2_smt.b.1 — Validate certificates by constructing and verifying a certification path to an accepted trust anchor, including checking certificate status information; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ia-5.2_smt.b.2 — Implement a local cache of revocation data to support path discovery and validation.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ia-5.2_smt.a` — For “For public key-based authentication:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5.2_smt.a.1` — For “Enforce authorized access to the corresponding private key; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5.2_smt.a.2` — For “Map the authenticated identity to the account of the individual or group; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5.2_smt.b` — For “When public key infrastructure (PKI) is used:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5.2_smt.b.1` — For “Validate certificates by constructing and verifying a certification path to an accepted trust anchor, including checking certificate status information; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ia-5.2_smt.b.2` — For “Implement a local cache of revocation data to support path discovery and validation.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ia-5.2_obj.a.1` (ia-5.2_smt.a.1): authorized access to the corresponding private key is enforced for public key-based authentication;

- `ia-5.2_obj.a.2` (ia-5.2_smt.a.2): the authenticated identity is mapped to the account of the individual or group for public key-based authentication;

- `ia-5.2_obj.b.1` (ia-5.2_smt.b.1): when public key infrastructure (PKI) is used, certificates are validated by constructing and verifying a certification path to an accepted trust anchor, including checking certificate status information;

- `ia-5.2_obj.b.2` (ia-5.2_smt.b.2): when public key infrastructure (PKI) is used, a local cache of revocation data is implemented to support path discovery and validation.

#### EXAMINE — `ia-5.2_asm-examine`

- Identification and authentication policy

- procedures addressing authenticator management

- system security plan

- system design documentation

- system configuration settings and associated documentation

- PKI certification validation records

- PKI certification revocation lists

- other relevant documents or records

#### INTERVIEW — `ia-5.2_asm-interview`

- Organizational personnel with PKI-based, authenticator management responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

- system developers

#### TEST — `ia-5.2_asm-test`

- Mechanisms supporting and/or implementing PKI-based, authenticator management capability

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ia-5.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ia-5`.

- Catalog relationship **related**: `ia-3`.

- Catalog relationship **related**: `sc-17`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
