---
title: "SC-7.25 \u2014 Unclassified National Security System Connections"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-7.25 — Unclassified National Security System Connections

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

A direct connection is a dedicated physical or virtual connection between two or more systems. Organizations typically do not have complete control over external networks, including the Internet. Boundary protection devices (e.g., firewalls, gateways, and routers) mediate communications and information flows between unclassified national security systems and external networks.

### Requirements and exact statement parts

- `sc-7.25_smt`: Prohibit the direct connection of [PARAM sc-07.25_odp.01] to an external network without the use of [PARAM sc-07.25_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-7.25_smt — Prohibit the direct connection of [PARAM sc-07.25_odp.01] to an external network without the use of [PARAM sc-07.25_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-07.25_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sc-07.25_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-7.25_smt` — For “Prohibit the direct connection of [PARAM sc-07.25_odp.01] to an external network without the use of [PARAM sc-07.25_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-07.25_odp.01` — What approved value applies to **unclassified national security system**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the unclassified national security system prohibited from directly connecting to an external network is defined;

- `sc-07.25_odp.02` — What approved value applies to **boundary protection device**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the boundary protection device required for a direct connection to an external network is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-7.25_obj` (sc-7.25_smt): the direct connection of [PARAM sc-07.25_odp.01] to an external network without the use of [PARAM sc-07.25_odp.02] is prohibited.

#### EXAMINE — `sc-7.25_asm-examine`

- System and communications protection policy

- procedures addressing boundary protection

- system design documentation

- system hardware and software

- system architecture

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-7.25_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developer

- organizational personnel with boundary protection responsibilities

#### TEST — `sc-7.25_asm-test`

- Mechanisms prohibiting the direct connection of unclassified national security systems to an external network

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-7.25`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sc-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
