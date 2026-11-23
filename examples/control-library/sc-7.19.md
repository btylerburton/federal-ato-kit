---
title: "SC-7.19 \u2014 Block Communication from Non-organizationally Configured Hosts"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-7.19 — Block Communication from Non-organizationally Configured Hosts

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Communication clients independently configured by end users and external service providers include instant messaging clients and video conferencing software and applications. Traffic blocking does not apply to communication clients that are configured by organizations to perform authorized functions.

### Requirements and exact statement parts

- `sc-7.19_smt`: Block inbound and outbound communications traffic between [PARAM sc-07.19_odp] that are independently configured by end users and external service providers.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-7.19_smt — Block inbound and outbound communications traffic between [PARAM sc-07.19_odp] that are independently configured by end users and external service providers.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-07.19_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-7.19_smt` — For “Block inbound and outbound communications traffic between [PARAM sc-07.19_odp] that are independently configured by end users and external service providers.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-07.19_odp` — What approved value applies to **communication clients**? Record the value, scope, approving authority, and decision source.

  - Catalog context: communication clients that are independently configured by end users and external service providers are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-7.19_obj-1` (sc-7.19_smt): inbound communications traffic is blocked between [PARAM sc-07.19_odp] that are independently configured by end users and external service providers;

- `sc-7.19_obj-2` (sc-7.19_smt): outbound communications traffic is blocked between [PARAM sc-07.19_odp] that are independently configured by end users and external service providers.

#### EXAMINE — `sc-7.19_asm-examine`

- System and communications protection policy

- procedures addressing boundary protection

- system design documentation

- system hardware and software

- system architecture

- system configuration settings and associated documentation

- list of communication clients independently configured by end users and external service providers

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-7.19_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel with boundary protection responsibilities

#### TEST — `sc-7.19_asm-test`

- Mechanisms supporting and/or implementing the blocking of inbound and outbound communications traffic between communication clients independently configured by end users and external service providers

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-7.19`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sc-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
