---
title: "PL-8.1 \u2014 Defense in Depth"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PL-8.1 — Defense in Depth

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations strategically allocate security and privacy controls in the security and privacy architectures so that adversaries must overcome multiple controls to achieve their objective. Requiring adversaries to defeat multiple controls makes it more difficult to attack information resources by increasing the work factor of the adversary; it also increases the likelihood of detection. The coordination of allocated controls is essential to ensure that an attack that involves one control does not create adverse, unintended consequences by interfering with other controls. Unintended consequences can include system lockout and cascading alarms. The placement of controls in systems and organizations is an important activity that requires thoughtful analysis. The value of organizational assets is an important consideration in providing additional layering. Defense-in-depth architectural approaches include modularity and layering (see SA-8(3) (catalog reference: `#sa-8.3`) ), separation of system and user functionality (see SC-2 (catalog reference: `#sc-2`) ), and security function isolation (see SC-3 (catalog reference: `#sc-3`)).

### Requirements and exact statement parts

- `pl-8.1_smt`: Design the security and privacy architectures for the system using a defense-in-depth approach that:

- `pl-8.1_smt.a`: Allocates [PARAM pl-08.01_odp.01] to [PARAM pl-08.01_odp.02] ; and

- `pl-8.1_smt.b`: Ensures that the allocated controls operate in a coordinated and mutually reinforcing manner.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pl-8.1_smt — Design the security and privacy architectures for the system using a defense-in-depth approach that:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-8.1_smt.a — Allocates [PARAM pl-08.01_odp.01] to [PARAM pl-08.01_odp.02] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-8.1_smt.b — Ensures that the allocated controls operate in a coordinated and mutually reinforcing manner.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pl-08.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pl-08.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pl-8.1_smt` — For “Design the security and privacy architectures for the system using a defense-in-depth approach that:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-8.1_smt.a` — For “Allocates [PARAM pl-08.01_odp.01] to [PARAM pl-08.01_odp.02] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-8.1_smt.b` — For “Ensures that the allocated controls operate in a coordinated and mutually reinforcing manner.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pl-08.01_odp.01` — What approved value applies to **controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controls to be allocated are defined;

- `pl-08.01_odp.02` — What approved value applies to **locations and architectural layers**? Record the value, scope, approving authority, and decision source.

  - Catalog context: locations and architectural layers are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pl-8.1_obj.a-1` (pl-8.1_smt.a): the security architecture for the system is designed using a defense-in-depth approach that allocates [PARAM pl-08.01_odp.01] to [PARAM pl-08.01_odp.02];

- `pl-8.1_obj.a-2` (pl-8.1_smt.a): the privacy architecture for the system is designed using a defense-in-depth approach that allocates [PARAM pl-08.01_odp.01] to [PARAM pl-08.01_odp.02];

- `pl-8.1_obj.b-1` (pl-8.1_smt.b): the security architecture for the system is designed using a defense-in-depth approach that ensures the allocated controls operate in a coordinated and mutually reinforcing manner;

- `pl-8.1_obj.b-2` (pl-8.1_smt.b): the privacy architecture for the system is designed using a defense-in-depth approach that ensures the allocated controls operate in a coordinated and mutually reinforcing manner.

#### EXAMINE — `pl-8.1_asm-examine`

- Security and privacy planning policy

- procedures addressing information security and privacy architecture development

- enterprise architecture documentation

- information security and privacy architecture documentation

- system security plan

- privacy plan

- security and privacy CONOPS for the system

- other relevant documents or records

#### INTERVIEW — `pl-8.1_asm-interview`

- Organizational personnel with security and privacy planning and plan implementation responsibilities

- organizational personnel with information security and privacy architecture development responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `pl-8.1_asm-test`

- Organizational processes for designing the information security and privacy architecture

- mechanisms supporting and/or implementing the design of the information security and privacy architecture

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pl-8.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pl-8`.

- Catalog relationship **related**: `sc-2`.

- Catalog relationship **related**: `sc-3`.

- Catalog relationship **related**: `sc-29`.

- Catalog relationship **related**: `sc-36`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
