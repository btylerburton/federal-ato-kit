---
title: "SC-7.11 \u2014 Restrict Incoming Communications Traffic"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-7.11 — Restrict Incoming Communications Traffic

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

General source address validation techniques are applied to restrict the use of illegal and unallocated source addresses as well as source addresses that should only be used within the system. The restriction of incoming communications traffic provides determinations that source and destination address pairs represent authorized or allowed communications. Determinations can be based on several factors, including the presence of such address pairs in the lists of authorized or allowed communications, the absence of such address pairs in lists of unauthorized or disallowed pairs, or meeting more general rules for authorized or allowed source and destination pairs. Strong authentication of network addresses is not possible without the use of explicit security protocols, and thus, addresses can often be spoofed. Further, identity-based incoming traffic restriction methods can be employed, including router access control lists and firewall rules.

### Requirements and exact statement parts

- `sc-7.11_smt`: Only allow incoming communications from [PARAM sc-07.11_odp.01] to be routed to [PARAM sc-07.11_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-7.11_smt — Only allow incoming communications from [PARAM sc-07.11_odp.01] to be routed to [PARAM sc-07.11_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-07.11_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sc-07.11_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-7.11_smt` — For “Only allow incoming communications from [PARAM sc-07.11_odp.01] to be routed to [PARAM sc-07.11_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-07.11_odp.01` — What approved value applies to **authorized sources**? Record the value, scope, approving authority, and decision source.

  - Catalog context: authorized sources of incoming communications to be routed are defined;

- `sc-07.11_odp.02` — What approved value applies to **authorized destinations**? Record the value, scope, approving authority, and decision source.

  - Catalog context: authorized destinations to which incoming communications from authorized sources may be routed are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-7.11_obj` (sc-7.11_smt): only incoming communications from [PARAM sc-07.11_odp.01] are allowed to be routed to [PARAM sc-07.11_odp.02].

#### EXAMINE — `sc-7.11_asm-examine`

- System and communications protection policy

- procedures addressing boundary protection

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-7.11_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developer

- organizational personnel with boundary protection responsibilities

#### TEST — `sc-7.11_asm-test`

- Mechanisms implementing boundary protection capabilities with respect to source/destination address pairs

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-7.11`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sc-7`.

- Catalog relationship **related**: `ac-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
