---
title: "IR-4.11 \u2014 Integrated Incident Response Team"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-4.11 — Integrated Incident Response Team

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

An integrated incident response team is a team of experts that assesses, documents, and responds to incidents so that organizational systems and networks can recover quickly and implement the necessary controls to avoid future incidents. Incident response team personnel include forensic and malicious code analysts, tool developers, systems security and privacy engineers, and real-time operations personnel. The incident handling capability includes performing rapid forensic preservation of evidence and analysis of and response to intrusions. For some organizations, the incident response team can be a cross-organizational entity.

An integrated incident response team facilitates information sharing and allows organizational personnel (e.g., developers, implementers, and operators) to leverage team knowledge of the threat and implement defensive measures that enable organizations to deter intrusions more effectively. Moreover, integrated teams promote the rapid detection of intrusions, the development of appropriate mitigations, and the deployment of effective defensive measures. For example, when an intrusion is detected, the integrated team can rapidly develop an appropriate response for operators to implement, correlate the new incident with information on past intrusions, and augment ongoing cyber intelligence development. Integrated incident response teams are better able to identify adversary tactics, techniques, and procedures that are linked to the operations tempo or specific mission and business functions and to define responsive actions in a way that does not disrupt those mission and business functions. Incident response teams can be distributed within organizations to make the capability resilient.

### Requirements and exact statement parts

- `ir-4.11_smt`: Establish and maintain an integrated incident response team that can be deployed to any location identified by the organization in [PARAM ir-04.11_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-4.11_smt — Establish and maintain an integrated incident response team that can be deployed to any location identified by the organization in [PARAM ir-04.11_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ir-04.11_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ir-4.11_smt` — For “Establish and maintain an integrated incident response team that can be deployed to any location identified by the organization in [PARAM ir-04.11_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ir-04.11_odp` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the time period within which an integrated incident response team can be deployed is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-4.11_obj-1` (ir-4.11_smt): an integrated incident response team is established and maintained;

- `ir-4.11_obj-2` (ir-4.11_smt): the integrated incident response team can be deployed to any location identified by the organization in [PARAM ir-04.11_odp].

#### EXAMINE — `ir-4.11_asm-examine`

- Incident response policy

- procedures addressing incident handling

- procedures addressing incident response planning

- incident response plan

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ir-4.11_asm-interview`

- Organizational personnel with incident handling responsibilities

- organizational personnel with information security and privacy responsibilities

- members of the integrated incident response team

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-4.11`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ir-4`.

- Catalog relationship **related**: `at-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
