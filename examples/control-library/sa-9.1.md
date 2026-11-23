---
title: "SA-9.1 \u2014 Risk Assessments and Organizational Approvals"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-9.1 — Risk Assessments and Organizational Approvals

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Information security services include the operation of security devices, such as firewalls or key management services as well as incident monitoring, analysis, and response. Risks assessed can include system, mission or business, security, privacy, or supply chain risks.

### Requirements and exact statement parts

- `sa-9.1_smt`: Statement grouping; see child parts.

- `sa-9.1_smt.a`: Conduct an organizational assessment of risk prior to the acquisition or outsourcing of information security services; and

- `sa-9.1_smt.b`: Verify that the acquisition or outsourcing of dedicated information security services is approved by [PARAM sa-09.01_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-9.1_smt.a — Conduct an organizational assessment of risk prior to the acquisition or outsourcing of information security services; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sa-9.1_smt.b — Verify that the acquisition or outsourcing of dedicated information security services is approved by [PARAM sa-09.01_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sa-09.01_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sa-9.1_smt.a` — For “Conduct an organizational assessment of risk prior to the acquisition or outsourcing of information security services; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sa-9.1_smt.b` — For “Verify that the acquisition or outsourcing of dedicated information security services is approved by [PARAM sa-09.01_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sa-09.01_odp` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles that approve the acquisition or outsourcing of dedicated information security services is/are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-9.1_obj.a` (sa-9.1_smt.a): an organizational assessment of risk is conducted prior to the acquisition or outsourcing of information security services;

- `sa-9.1_obj.b` (sa-9.1_smt.b): [PARAM sa-09.01_odp] approve the acquisition or outsourcing of dedicated information security services.

#### EXAMINE — `sa-9.1_asm-examine`

- System and services acquisition policy

- supply chain risk management policy and procedures

- procedures addressing external system services

- acquisition documentation

- acquisition contracts for the system, system component, or system service

- risk assessment reports

- approval records for the acquisition or outsourcing of dedicated security services

- system security plan

- supply chain risk management plan

- other relevant documents or records

#### INTERVIEW — `sa-9.1_asm-interview`

- Organizational personnel with system and service acquisition responsibilities

- organizational personnel with system security responsibilities

- external providers of system services

- organizational personnel with information security responsibilities

- organizational personnel with supply chain risk management responsibilities

#### TEST — `sa-9.1_asm-test`

- Organizational processes for conducting a risk assessment prior to acquiring or outsourcing dedicated security services

- organizational processes for approving the outsourcing of dedicated security services

- mechanisms supporting and/or implementing risk assessment

- mechanisms supporting and/or implementing approval processes

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-9.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-9`.

- Catalog relationship **related**: `ca-6`.

- Catalog relationship **related**: `ra-3`.

- Catalog relationship **related**: `ra-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
