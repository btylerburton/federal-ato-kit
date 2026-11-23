---
title: "MA-4.6 \u2014 Cryptographic Protection"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-4.6 — Cryptographic Protection

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Failure to protect nonlocal maintenance and diagnostic communications can result in unauthorized individuals gaining access to organizational information. Unauthorized access during remote maintenance sessions can result in a variety of hostile actions, including malicious code insertion, unauthorized changes to system parameters, and exfiltration of organizational information. Such actions can result in the loss or degradation of mission or business capabilities.

### Requirements and exact statement parts

- `ma-4.6_smt`: Implement the following cryptographic mechanisms to protect the integrity and confidentiality of nonlocal maintenance and diagnostic communications: [PARAM ma-04.06_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-4.6_smt — Implement the following cryptographic mechanisms to protect the integrity and confidentiality of nonlocal maintenance and diagnostic communications: [PARAM ma-04.06_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ma-04.06_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ma-4.6_smt` — For “Implement the following cryptographic mechanisms to protect the integrity and confidentiality of nonlocal maintenance and diagnostic communications: [PARAM ma-04.06_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ma-04.06_odp` — What approved value applies to **cryptographic mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: cryptographic mechanisms to be implemented to protect the integrity and confidentiality of nonlocal maintenance and diagnostic communications are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-4.6_obj-1` (ma-4.6_smt): [PARAM ma-04.06_odp] are implemented to protect the integrity of nonlocal maintenance and diagnostic communications;

- `ma-4.6_obj-2` (ma-4.6_smt): [PARAM ma-04.06_odp] are implemented to protect the confidentiality of nonlocal maintenance and diagnostic communications.

#### EXAMINE — `ma-4.6_asm-examine`

- Maintenance policy

- procedures addressing nonlocal system maintenance

- system design documentation

- system configuration settings and associated documentation

- cryptographic mechanisms protecting nonlocal maintenance activities

- maintenance records

- diagnostic records

- audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-4.6_asm-interview`

- Organizational personnel with system maintenance responsibilities

- network engineers

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ma-4.6_asm-test`

- Cryptographic mechanisms protecting nonlocal maintenance and diagnostic communications

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-4.6`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ma-4`.

- Catalog relationship **related**: `sc-8`.

- Catalog relationship **related**: `sc-12`.

- Catalog relationship **related**: `sc-13`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
