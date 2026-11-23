---
title: "SC-5 \u2014 Denial-of-service Protection"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-5 — Denial-of-service Protection

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Denial-of-service events may occur due to a variety of internal and external causes, such as an attack by an adversary or a lack of planning to support organizational needs with respect to capacity and bandwidth. Such attacks can occur across a wide range of network protocols (e.g., IPv4, IPv6). A variety of technologies are available to limit or eliminate the origination and effects of denial-of-service events. For example, boundary protection devices can filter certain types of packets to protect system components on internal networks from being directly affected by or the source of denial-of-service attacks. Employing increased network capacity and bandwidth combined with service redundancy also reduces the susceptibility to denial-of-service events.

### Requirements and exact statement parts

- `sc-5_smt`: Statement grouping; see child parts.

- `sc-5_smt.a`: [PARAM sc-05_odp.02] the effects of the following types of denial-of-service events: [PARAM sc-05_odp.01] ; and

- `sc-5_smt.b`: Employ the following controls to achieve the denial-of-service objective: [PARAM sc-05_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-5_smt.a — [PARAM sc-05_odp.02] the effects of the following types of denial-of-service events: [PARAM sc-05_odp.01] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sc-5_smt.b — Employ the following controls to achieve the denial-of-service objective: [PARAM sc-05_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-05_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sc-05_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sc-05_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-5_smt.a` — For “[PARAM sc-05_odp.02] the effects of the following types of denial-of-service events: [PARAM sc-05_odp.01] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sc-5_smt.b` — For “Employ the following controls to achieve the denial-of-service objective: [PARAM sc-05_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-05_odp.01` — What approved value applies to **types of denial-of-service events**? Record the value, scope, approving authority, and decision source.

  - Catalog context: types of denial-of-service events to be protected against or limited are defined;

- `sc-05_odp.02` — What approved value applies to **selection; choose one from: protect against; limit**? Record the value, scope, approving authority, and decision source.

- `sc-05_odp.03` — What approved value applies to **controls by type of denial-of-service event**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controls to achieve the denial-of-service objective by type of denial-of-service event are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-5_obj.a` (sc-5_smt.a): the effects of [PARAM sc-05_odp.01] are [PARAM sc-05_odp.02];

- `sc-5_obj.b` (sc-5_smt.b): [PARAM sc-05_odp.03] are employed to achieve the denial-of-service protection objective.

#### EXAMINE — `sc-5_asm-examine`

- System and communications protection policy

- procedures addressing denial-of-service protection

- system design documentation

- list of denial-of-service attacks requiring employment of security safeguards to protect against or limit effects of such attacks

- list of security safeguards protecting against or limiting the effects of denial-of-service attacks

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-5_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel with incident response responsibilities

- system developer

#### TEST — `sc-5_asm-test`

- Mechanisms protecting against or limiting the effects of denial-of-service attacks

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-5`. The library index records the exact source revision and hash.

- [SP 800-189](https://doi.org/10.6028/NIST.SP.800-189)

- Catalog relationship **related**: `cp-2`.

- Catalog relationship **related**: `ir-4`.

- Catalog relationship **related**: `sc-6`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `sc-40`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
