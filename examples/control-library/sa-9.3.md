---
title: "SA-9.3 \u2014 Establish and Maintain Trust Relationship with Providers"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-9.3 — Establish and Maintain Trust Relationship with Providers

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Trust relationships between organizations and external service providers reflect the degree of confidence that the risk from using external services is at an acceptable level. Trust relationships can help organizations gain increased levels of confidence that service providers are providing adequate protection for the services rendered and can also be useful when conducting incident response or when planning for upgrades or obsolescence. Trust relationships can be complicated due to the potentially large number of entities participating in the consumer-provider interactions, subordinate relationships and levels of trust, and types of interactions between the parties. In some cases, the degree of trust is based on the level of control that organizations can exert on external service providers regarding the controls necessary for the protection of the service, information, or individual privacy and the evidence brought forth as to the effectiveness of the implemented controls. The level of control is established by the terms and conditions of the contracts or service-level agreements.

### Requirements and exact statement parts

- `sa-9.3_smt`: Establish, document, and maintain trust relationships with external service providers based on the following requirements, properties, factors, or conditions: [PARAM sa-9.3_prm_1].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-9.3_smt — Establish, document, and maintain trust relationships with external service providers based on the following requirements, properties, factors, or conditions: [PARAM sa-9.3_prm_1].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sa-9.3_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sa-09.03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sa-09.03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sa-9.3_smt` — For “Establish, document, and maintain trust relationships with external service providers based on the following requirements, properties, factors, or conditions: [PARAM sa-9.3_prm_1].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sa-9.3_prm_1` — What approved value applies to **organization-defined security and privacy requirements, properties, factors, or conditions defining acceptable trust relationships**? Record the value, scope, approving authority, and decision source.

- `sa-09.03_odp.01` — What approved value applies to **security requirements, properties, factors, or conditions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security requirements, properties, factors, or conditions defining acceptable trust relationships on which a trust relationship is maintained are defined;

- `sa-09.03_odp.02` — What approved value applies to **privacy requirements, properties, factors, or conditions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: privacy requirements, properties, factors, or conditions defining acceptable trust relationships on which a trust relationship is maintained are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-9.3_obj-1` (sa-9.3_smt): trust relationships with external service provides based on [PARAM sa-09.03_odp.01] are established and documented;

- `sa-9.3_obj-2` (sa-9.3_smt): trust relationships with external service provides based on [PARAM sa-09.03_odp.01] are maintained;

- `sa-9.3_obj-3` (sa-9.3_smt): trust relationships with external service provides based on [PARAM sa-09.03_odp.02] are established and documented;

- `sa-9.3_obj-4` (sa-9.3_smt): trust relationships with external service provides based on [PARAM sa-09.03_odp.02] are maintained.

#### EXAMINE — `sa-9.3_asm-examine`

- System and services acquisition policy

- system and services acquisition procedures

- acquisition contracts for the system, system component, or system service

- acquisition documentation

- solicitation documentation

- service level agreements

- memorandum of understanding

- memorandum of agreements

- list of organizational security and privacy requirements, properties, factors, or conditions for external provider services

- documentation of trust relationships with external service providers

- system security plan

- privacy plan

- supply chain risk management plan

- other relevant documents or records

#### INTERVIEW — `sa-9.3_asm-interview`

- Organizational personnel with acquisition responsibilities

- organizational personnel with information security and privacy responsibilities

- external providers of system services

- organizational personnel with supply chain risk management responsibilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-9.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-9`.

- Catalog relationship **related**: `sr-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
