---
title: "PL-8.2 \u2014 Supplier Diversity"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PL-8.2 — Supplier Diversity

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Information technology products have different strengths and weaknesses. Providing a broad spectrum of products complements the individual offerings. For example, vendors offering malicious code protection typically update their products at different times, often developing solutions for known viruses, Trojans, or worms based on their priorities and development schedules. By deploying different products at different locations, there is an increased likelihood that at least one of the products will detect the malicious code. With respect to privacy, vendors may offer products that track personally identifiable information in systems. Products may use different tracking methods. Using multiple products may result in more assurance that personally identifiable information is inventoried.

### Requirements and exact statement parts

- `pl-8.2_smt`: Require that [PARAM pl-08.02_odp.01] allocated to [PARAM pl-08.02_odp.02] are obtained from different suppliers.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pl-8.2_smt — Require that [PARAM pl-08.02_odp.01] allocated to [PARAM pl-08.02_odp.02] are obtained from different suppliers.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pl-08.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pl-08.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pl-8.2_smt` — For “Require that [PARAM pl-08.02_odp.01] allocated to [PARAM pl-08.02_odp.02] are obtained from different suppliers.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pl-08.02_odp.01` — What approved value applies to **controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controls to be allocated are defined;

- `pl-08.02_odp.02` — What approved value applies to **locations and architectural layers**? Record the value, scope, approving authority, and decision source.

  - Catalog context: locations and architectural layers are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pl-8.2_obj` (pl-8.2_smt): [PARAM pl-08.02_odp.01] that are allocated to [PARAM pl-08.02_odp.02] are required to be obtained from different suppliers.

#### EXAMINE — `pl-8.2_asm-examine`

- Security and privacy planning policy

- procedures addressing information security and privacy architecture development

- enterprise architecture documentation

- information security and privacy architecture documentation

- system security plan

- privacy plan

- security and privacy CONOPS for the system

- IT acquisitions policy

- other relevant documents or records

#### INTERVIEW — `pl-8.2_asm-interview`

- Organizational personnel with security and privacy planning and plan implementation responsibilities

- organizational personnel with information security and privacy architecture development responsibilities

- organizational personnel with acquisition responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `pl-8.2_asm-test`

- Organizational processes for obtaining information security and privacy safeguards from different suppliers

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pl-8.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pl-8`.

- Catalog relationship **related**: `sc-29`.

- Catalog relationship **related**: `sr-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
