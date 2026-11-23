---
title: "SA-9.4 \u2014 Consistent Interests of Consumers and Providers"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-9.4 — Consistent Interests of Consumers and Providers

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

As organizations increasingly use external service providers, it is possible that the interests of the service providers may diverge from organizational interests. In such situations, simply having the required technical, management, or operational controls in place may not be sufficient if the providers that implement and manage those controls are not operating in a manner consistent with the interests of the consuming organizations. Actions that organizations take to address such concerns include requiring background checks for selected service provider personnel; examining ownership records; employing only trustworthy service providers, such as providers with which organizations have had successful trust relationships; and conducting routine, periodic, unscheduled visits to service provider facilities.

### Requirements and exact statement parts

- `sa-9.4_smt`: Take the following actions to verify that the interests of [PARAM sa-09.04_odp.01] are consistent with and reflect organizational interests: [PARAM sa-09.04_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-9.4_smt — Take the following actions to verify that the interests of [PARAM sa-09.04_odp.01] are consistent with and reflect organizational interests: [PARAM sa-09.04_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sa-09.04_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sa-09.04_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sa-9.4_smt` — For “Take the following actions to verify that the interests of [PARAM sa-09.04_odp.01] are consistent with and reflect organizational interests: [PARAM sa-09.04_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sa-09.04_odp.01` — What approved value applies to **external service providers**? Record the value, scope, approving authority, and decision source.

  - Catalog context: external service providers are defined;

- `sa-09.04_odp.02` — What approved value applies to **actions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: actions to be taken to verify that the interests of external service providers are consistent with and reflect organizational interests are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-9.4_obj` (sa-9.4_smt): [PARAM sa-09.04_odp.02] are taken to verify that the interests of [PARAM sa-09.04_odp.01] are consistent with and reflect organizational interests.

#### EXAMINE — `sa-9.4_asm-examine`

- System and services acquisition policy

- procedures addressing external system services

- acquisition contracts for the system, system component, or system service

- solicitation documentation

- acquisition documentation

- service level agreements

- organizational security requirements/safeguards for external service providers

- personnel security policies for external service providers

- assessments performed on external service providers

- system security plan

- supply chain risk management plan

- other relevant documents or records

#### INTERVIEW — `sa-9.4_asm-interview`

- Organizational personnel with system and service acquisition responsibilities

- organizational personnel with information security responsibilities

- external providers of system services

- organizational personnel with supply chain risk management responsibilities

#### TEST — `sa-9.4_asm-test`

- Organizational processes for defining and employing safeguards to ensure consistent interests with external service providers

- mechanisms supporting and/or implementing safeguards to ensure consistent interests with external service providers

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-9.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-9`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
