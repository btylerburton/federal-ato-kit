---
title: "AC-4.20 \u2014 Approved Solutions"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4.20 — Approved Solutions

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations define approved solutions and configurations in cross-domain policies and guidance in accordance with the types of information flows across classification boundaries. The National Security Agency (NSA) National Cross Domain Strategy and Management Office provides a listing of approved cross-domain solutions. Contact ncdsmo@nsa.gov (catalog contact: `mailto:ncdsmo@nsa.gov`) for more information.

### Requirements and exact statement parts

- `ac-4.20_smt`: Employ [PARAM ac-04.20_odp.01] to control the flow of [PARAM ac-04.20_odp.02] across security domains.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4.20_smt — Employ [PARAM ac-04.20_odp.01] to control the flow of [PARAM ac-04.20_odp.02] across security domains.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-04.20_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.20_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-4.20_smt` — For “Employ [PARAM ac-04.20_odp.01] to control the flow of [PARAM ac-04.20_odp.02] across security domains.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-04.20_odp.01` — What approved value applies to **solutions in approved configurations**? Record the value, scope, approving authority, and decision source.

  - Catalog context: solutions in approved configurations to control the flow of information across security domains are defined;

- `ac-04.20_odp.02` — What approved value applies to **information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: information to be controlled when it flows across security domains is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4.20_obj` (ac-4.20_smt): [PARAM ac-04.20_odp.01] are employed to control the flow of [PARAM ac-04.20_odp.02] across security domains.

#### EXAMINE — `ac-4.20_asm-examine`

- Information flow enforcement policy

- information flow control policies

- procedures addressing information flow enforcement

- system design documentation

- system configuration settings and associated documentation

- list of solutions in approved configurations

- approved configuration baselines

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-4.20_asm-interview`

- Organizational personnel with information flow enforcement responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

#### TEST — `ac-4.20_asm-test`

- Mechanisms implementing information flow enforcement functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4.20`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
