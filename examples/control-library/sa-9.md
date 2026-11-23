---
title: "SA-9 \u2014 External System Services"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-9 — External System Services

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

External system services are provided by an external provider, and the organization has no direct control over the implementation of the required controls or the assessment of control effectiveness. Organizations establish relationships with external service providers in a variety of ways, including through business partnerships, contracts, interagency agreements, lines of business arrangements, licensing agreements, joint ventures, and supply chain exchanges. The responsibility for managing risks from the use of external system services remains with authorizing officials. For services external to organizations, a chain of trust requires that organizations establish and retain a certain level of confidence that each provider in the consumer-provider relationship provides adequate protection for the services rendered. The extent and nature of this chain of trust vary based on relationships between organizations and the external providers. Organizations document the basis for the trust relationships so that the relationships can be monitored. External system services documentation includes government, service providers, end user security roles and responsibilities, and service-level agreements. Service-level agreements define the expectations of performance for implemented controls, describe measurable outcomes, and identify remedies and response requirements for identified instances of noncompliance.

### Requirements and exact statement parts

- `sa-9_smt`: Statement grouping; see child parts.

- `sa-9_smt.a`: Require that providers of external system services comply with organizational security and privacy requirements and employ the following controls: [PARAM sa-09_odp.01];

- `sa-9_smt.b`: Define and document organizational oversight and user roles and responsibilities with regard to external system services; and

- `sa-9_smt.c`: Employ the following processes, methods, and techniques to monitor control compliance by external service providers on an ongoing basis: [PARAM sa-09_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-9_smt.a — Require that providers of external system services comply with organizational security and privacy requirements and employ the following controls: [PARAM sa-09_odp.01];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sa-9_smt.b — Define and document organizational oversight and user roles and responsibilities with regard to external system services; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sa-9_smt.c — Employ the following processes, methods, and techniques to monitor control compliance by external service providers on an ongoing basis: [PARAM sa-09_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sa-09_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sa-09_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sa-9_smt.a` — For “Require that providers of external system services comply with organizational security and privacy requirements and employ the following controls: [PARAM sa-09_odp.01];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sa-9_smt.b` — For “Define and document organizational oversight and user roles and responsibilities with regard to external system services; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sa-9_smt.c` — For “Employ the following processes, methods, and techniques to monitor control compliance by external service providers on an ongoing basis: [PARAM sa-09_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sa-09_odp.01` — What approved value applies to **controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controls to be employed by external system service providers are defined;

- `sa-09_odp.02` — What approved value applies to **processes, methods, and techniques**? Record the value, scope, approving authority, and decision source.

  - Catalog context: processes, methods, and techniques employed to monitor control compliance by external service providers are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-9_obj.a-1` (sa-9_smt.a): providers of external system services comply with organizational security requirements;

- `sa-9_obj.a-2` (sa-9_smt.a): providers of external system services comply with organizational privacy requirements;

- `sa-9_obj.a-3` (sa-9_smt.a): providers of external system services employ [PARAM sa-09_odp.01];

- `sa-9_obj.b-1` (sa-9_smt.b): organizational oversight with regard to external system services are defined and documented;

- `sa-9_obj.b-2` (sa-9_smt.b): user roles and responsibilities with regard to external system services are defined and documented;

- `sa-9_obj.c` (sa-9_smt.c): [PARAM sa-09_odp.02] are employed to monitor control compliance by external service providers on an ongoing basis.

#### EXAMINE — `sa-9_asm-examine`

- System and services acquisition policy

- system and services acquisition procedures

- procedures addressing methods and techniques for monitoring control compliance by external service providers of system services

- acquisition documentation

- contracts

- service level agreements

- interagency agreements

- licensing agreements

- list of organizational security and privacy requirements for external provider services

- control assessment results or reports from external providers of system services

- system security plan

- privacy plan

- supply chain risk management plan

- other relevant documents or records

#### INTERVIEW — `sa-9_asm-interview`

- Organizational personnel with acquisition responsibilities

- external providers of system services

- organizational personnel with information security and privacy responsibilities

- organizational personnel with supply chain risk management responsibilities

#### TEST — `sa-9_asm-test`

- Organizational processes for monitoring security and privacy control compliance by external service providers on an ongoing basis

- mechanisms for monitoring security and privacy control compliance by external service providers on an ongoing basis

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-9`. The library index records the exact source revision and hash.

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [SP 800-35](https://doi.org/10.6028/NIST.SP.800-35)

- [SP 800-160-1](https://doi.org/10.6028/NIST.SP.800-160v1)

- [SP 800-161](https://doi.org/10.6028/NIST.SP.800-161)

- [SP 800-171](https://doi.org/10.6028/NIST.SP.800-171r2)

- Catalog relationship **related**: `ac-20`.

- Catalog relationship **related**: `ca-3`.

- Catalog relationship **related**: `cp-2`.

- Catalog relationship **related**: `ir-4`.

- Catalog relationship **related**: `ir-7`.

- Catalog relationship **related**: `pl-10`.

- Catalog relationship **related**: `pl-11`.

- Catalog relationship **related**: `ps-7`.

- Catalog relationship **related**: `sa-2`.

- Catalog relationship **related**: `sa-4`.

- Catalog relationship **related**: `sr-3`.

- Catalog relationship **related**: `sr-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
