---
title: "SC-7.21 \u2014 Isolation of System Components"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-7.21 — Isolation of System Components

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations can isolate system components that perform different mission or business functions. Such isolation limits unauthorized information flows among system components and provides the opportunity to deploy greater levels of protection for selected system components. Isolating system components with boundary protection mechanisms provides the capability for increased protection of individual system components and to more effectively control information flows between those components. Isolating system components provides enhanced protection that limits the potential harm from hostile cyber-attacks and errors. The degree of isolation varies depending upon the mechanisms chosen. Boundary protection mechanisms include routers, gateways, and firewalls that separate system components into physically separate networks or subnetworks; cross-domain devices that separate subnetworks; virtualization techniques; and the encryption of information flows among system components using distinct encryption keys.

### Requirements and exact statement parts

- `sc-7.21_smt`: Employ boundary protection mechanisms to isolate [PARAM sc-07.21_odp.01] supporting [PARAM sc-07.21_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-7.21_smt — Employ boundary protection mechanisms to isolate [PARAM sc-07.21_odp.01] supporting [PARAM sc-07.21_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-07.21_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sc-07.21_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-7.21_smt` — For “Employ boundary protection mechanisms to isolate [PARAM sc-07.21_odp.01] supporting [PARAM sc-07.21_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-07.21_odp.01` — What approved value applies to **system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system components to be isolated by boundary protection mechanisms are defined;

- `sc-07.21_odp.02` — What approved value applies to **missions and/or business functions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: missions and/or business functions to be supported by system components isolated by boundary protection mechanisms are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-7.21_obj` (sc-7.21_smt): boundary protection mechanisms are employed to isolate [PARAM sc-07.21_odp.01] supporting [PARAM sc-07.21_odp.02].

#### EXAMINE — `sc-7.21_asm-examine`

- System and communications protection policy

- procedures addressing boundary protection

- system design documentation

- system hardware and software

- enterprise architecture documentation

- system architecture

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-7.21_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel with boundary protection responsibilities

#### TEST — `sc-7.21_asm-test`

- Mechanisms supporting and/or implementing the capability to separate system components supporting organizational missions and/or business functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-7.21`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sc-7`.

- Catalog relationship **related**: `ca-9`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
