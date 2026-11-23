---
title: "PL-7 \u2014 Concept of Operations"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PL-7 — Concept of Operations

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The CONOPS may be included in the security or privacy plans for the system or in other system development life cycle documents. The CONOPS is a living document that requires updating throughout the system development life cycle. For example, during system design reviews, the concept of operations is checked to ensure that it remains consistent with the design for controls, the system architecture, and the operational procedures. Changes to the CONOPS are reflected in ongoing updates to the security and privacy plans, security and privacy architectures, and other organizational documents, such as procurement specifications, system development life cycle documents, and systems engineering documents.

### Requirements and exact statement parts

- `pl-7_smt`: Statement grouping; see child parts.

- `pl-7_smt.a`: Develop a Concept of Operations (CONOPS) for the system describing how the organization intends to operate the system from the perspective of information security and privacy; and

- `pl-7_smt.b`: Review and update the CONOPS [PARAM pl-07_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pl-7_smt.a — Develop a Concept of Operations (CONOPS) for the system describing how the organization intends to operate the system from the perspective of information security and privacy; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-7_smt.b — Review and update the CONOPS [PARAM pl-07_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pl-07_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pl-7_smt.a` — For “Develop a Concept of Operations (CONOPS) for the system describing how the organization intends to operate the system from the perspective of information security and privacy; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-7_smt.b` — For “Review and update the CONOPS [PARAM pl-07_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pl-07_odp` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency for review and update of the Concept of Operations (CONOPS) is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pl-7_obj.a` (pl-7_smt.a): a CONOPS for the system describing how the organization intends to operate the system from the perspective of information security and privacy is developed;

- `pl-7_obj.b` (pl-7_smt.b): the CONOPS is reviewed and updated [PARAM pl-07_odp].

#### EXAMINE — `pl-7_asm-examine`

- Security and privacy planning policy

- procedures addressing security and privacy CONOPS development

- procedures addressing security and privacy CONOPS reviews and updates

- security and privacy CONOPS for the system

- system security plan

- privacy plan

- records of security and privacy CONOPS reviews and updates

- other relevant documents or records

#### INTERVIEW — `pl-7_asm-interview`

- Organizational personnel with security and privacy planning and plan implementation responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `pl-7_asm-test`

- Organizational processes for developing, reviewing, and updating the security CONOPS

- mechanisms supporting and/or implementing the development, review, and update of the security CONOPS

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pl-7`. The library index records the exact source revision and hash.

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- Catalog relationship **related**: `pl-2`.

- Catalog relationship **related**: `sa-2`.

- Catalog relationship **related**: `si-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
