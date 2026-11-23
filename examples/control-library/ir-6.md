---
title: "IR-6 \u2014 Incident Reporting"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-6 — Incident Reporting

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The types of incidents reported, the content and timeliness of the reports, and the designated reporting authorities reflect applicable laws, executive orders, directives, regulations, policies, standards, and guidelines. Incident information can inform risk assessments, control effectiveness assessments, security requirements for acquisitions, and selection criteria for technology products.

### Requirements and exact statement parts

- `ir-6_smt`: Statement grouping; see child parts.

- `ir-6_smt.a`: Require personnel to report suspected incidents to the organizational incident response capability within [PARAM ir-06_odp.01] ; and

- `ir-6_smt.b`: Report incident information to [PARAM ir-06_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-6_smt.a — Require personnel to report suspected incidents to the organizational incident response capability within [PARAM ir-06_odp.01] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ir-6_smt.b — Report incident information to [PARAM ir-06_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ir-06_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ir-06_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ir-6_smt.a` — For “Require personnel to report suspected incidents to the organizational incident response capability within [PARAM ir-06_odp.01] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ir-6_smt.b` — For “Report incident information to [PARAM ir-06_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ir-06_odp.01` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period for personnel to report suspected incidents to the organizational incident response capability is defined;

- `ir-06_odp.02` — What approved value applies to **authorities**? Record the value, scope, approving authority, and decision source.

  - Catalog context: authorities to whom incident information is to be reported are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-6_obj.a` (ir-6_smt.a): personnel is/are required to report suspected incidents to the organizational incident response capability within [PARAM ir-06_odp.01];

- `ir-6_obj.b` (ir-6_smt.b): incident information is reported to [PARAM ir-06_odp.02].

#### EXAMINE — `ir-6_asm-examine`

- Incident response policy

- procedures addressing incident reporting

- incident reporting records and documentation

- incident response plan

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ir-6_asm-interview`

- Organizational personnel with incident reporting responsibilities

- organizational personnel with information security and privacy responsibilities

- personnel who have/should have reported incidents

- personnel (authorities) to whom incident information is to be reported

- system users

#### TEST — `ir-6_asm-test`

- Organizational processes for incident reporting

- mechanisms supporting and/or implementing incident reporting

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-6`. The library index records the exact source revision and hash.

- [FASC18](https://www.congress.gov/bill/115th-congress/senate-bill/3085)

- [41 CFR 201](https://www.federalregister.gov/d/2020-18939)

- [USCERT IR](https://us-cert.cisa.gov/incident-notification-guidelines)

- [SP 800-61](https://doi.org/10.6028/NIST.SP.800-61r2)

- Catalog relationship **related**: `cm-6`.

- Catalog relationship **related**: `cp-2`.

- Catalog relationship **related**: `ir-4`.

- Catalog relationship **related**: `ir-5`.

- Catalog relationship **related**: `ir-8`.

- Catalog relationship **related**: `ir-9`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
