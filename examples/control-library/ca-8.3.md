---
title: "CA-8.3 \u2014 Facility Penetration Testing"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CA-8.3 — Facility Penetration Testing

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Penetration testing of physical access points can provide information on critical vulnerabilities in the operating environments of organizational systems. Such information can be used to correct weaknesses or deficiencies in physical controls that are necessary to protect organizational systems.

### Requirements and exact statement parts

- `ca-8.3_smt`: Employ a penetration testing process that includes [PARAM ca-08.03_odp.01] [PARAM ca-08.03_odp.02] attempts to bypass or circumvent controls associated with physical access points to the facility.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ca-8.3_smt — Employ a penetration testing process that includes [PARAM ca-08.03_odp.01] [PARAM ca-08.03_odp.02] attempts to bypass or circumvent controls associated with physical access points to the facility.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ca-08.03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ca-08.03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ca-8.3_smt` — For “Employ a penetration testing process that includes [PARAM ca-08.03_odp.01] [PARAM ca-08.03_odp.02] attempts to bypass or circumvent controls associated with physical access points to the facility.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ca-08.03_odp.01` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to employ penetration testing that attempts to bypass or circumvent controls associated with physical access points to the facility is defined;

- `ca-08.03_odp.02` — What approved value applies to **selection; choose one-or-more from: announced; unannounced**? Record the value, scope, approving authority, and decision source.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ca-8.3_obj` (ca-8.3_smt): the penetration testing process includes [PARAM ca-08.03_odp.01] [PARAM ca-08.03_odp.02] attempts to bypass or circumvent controls associated with physical access points to facility.

#### EXAMINE — `ca-8.3_asm-examine`

- Assessment, authorization, and monitoring policy

- procedures addressing penetration testing

- procedures addressing red team exercises

- assessment plan

- results of red team exercises

- penetration test report

- assessment report

- rules of engagement

- assessment evidence

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ca-8.3_asm-interview`

- Organizational personnel with assessment responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

#### TEST — `ca-8.3_asm-test`

- Automated mechanisms supporting the employment of red team exercises

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ca-8.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ca-8`.

- Catalog relationship **related**: `ca-2`.

- Catalog relationship **related**: `pe-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
