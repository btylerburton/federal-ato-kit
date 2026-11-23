---
title: "PL-8 \u2014 Security and Privacy Architectures"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PL-8 — Security and Privacy Architectures

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The security and privacy architectures at the system level are consistent with the organization-wide security and privacy architectures described in PM-7 (catalog reference: `#pm-7`) , which are integral to and developed as part of the enterprise architecture. The architectures include an architectural description, the allocation of security and privacy functionality (including controls), security- and privacy-related information for external interfaces, information being exchanged across the interfaces, and the protection mechanisms associated with each interface. The architectures can also include other information, such as user roles and the access privileges assigned to each role; security and privacy requirements; types of information processed, stored, and transmitted by the system; supply chain risk management requirements; restoration priorities of information and system services; and other protection needs.

SP 800-160-1 (catalog reference: `#e3cc0520-a366-4fc9-abc2-5272db7e3564`) provides guidance on the use of security architectures as part of the system development life cycle process. OMB M-19-03 (catalog reference: `#c5e11048-1d38-4af3-b00b-0d88dc26860c`) requires the use of the systems security engineering concepts described in SP 800-160-1 (catalog reference: `#e3cc0520-a366-4fc9-abc2-5272db7e3564`) for high value assets. Security and privacy architectures are reviewed and updated throughout the system development life cycle, from analysis of alternatives through review of the proposed architecture in the RFP responses to the design reviews before and during implementation (e.g., during preliminary design reviews and critical design reviews).

In today’s modern computing architectures, it is becoming less common for organizations to control all information resources. There may be key dependencies on external information services and service providers. Describing such dependencies in the security and privacy architectures is necessary for developing a comprehensive mission and business protection strategy. Establishing, developing, documenting, and maintaining under configuration control a baseline configuration for organizational systems is critical to implementing and maintaining effective architectures. The development of the architectures is coordinated with the senior agency information security officer and the senior agency official for privacy to ensure that the controls needed to support security and privacy requirements are identified and effectively implemented. In many circumstances, there may be no distinction between the security and privacy architecture for a system. In other circumstances, security objectives may be adequately satisfied, but privacy objectives may only be partially satisfied by the security requirements. In these cases, consideration of the privacy requirements needed to achieve satisfaction will result in a distinct privacy architecture. The documentation, however, may simply reflect the combined architectures.

PL-8 (catalog reference: `#pl-8`) is primarily directed at organizations to ensure that architectures are developed for the system and, moreover, that the architectures are integrated with or tightly coupled to the enterprise architecture. In contrast, SA-17 (catalog reference: `#sa-17`) is primarily directed at the external information technology product and system developers and integrators. SA-17 (catalog reference: `#sa-17`) , which is complementary to PL-8 (catalog reference: `#pl-8`) , is selected when organizations outsource the development of systems or components to external entities and when there is a need to demonstrate consistency with the organization’s enterprise architecture and security and privacy architectures.

### Requirements and exact statement parts

- `pl-8_smt`: Statement grouping; see child parts.

- `pl-8_smt.a`: Develop security and privacy architectures for the system that:

- `pl-8_smt.a.1`: Describe the requirements and approach to be taken for protecting the confidentiality, integrity, and availability of organizational information;

- `pl-8_smt.a.2`: Describe the requirements and approach to be taken for processing personally identifiable information to minimize privacy risk to individuals;

- `pl-8_smt.a.3`: Describe how the architectures are integrated into and support the enterprise architecture; and

- `pl-8_smt.a.4`: Describe any assumptions about, and dependencies on, external systems and services;

- `pl-8_smt.b`: Review and update the architectures [PARAM pl-08_odp] to reflect changes in the enterprise architecture; and

- `pl-8_smt.c`: Reflect planned architecture changes in security and privacy plans, Concept of Operations (CONOPS), criticality analysis, organizational procedures, and procurements and acquisitions.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pl-8_smt.a — Develop security and privacy architectures for the system that:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-8_smt.a.1 — Describe the requirements and approach to be taken for protecting the confidentiality, integrity, and availability of organizational information;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-8_smt.a.2 — Describe the requirements and approach to be taken for processing personally identifiable information to minimize privacy risk to individuals;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-8_smt.a.3 — Describe how the architectures are integrated into and support the enterprise architecture; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-8_smt.a.4 — Describe any assumptions about, and dependencies on, external systems and services;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-8_smt.b — Review and update the architectures [PARAM pl-08_odp] to reflect changes in the enterprise architecture; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-8_smt.c — Reflect planned architecture changes in security and privacy plans, Concept of Operations (CONOPS), criticality analysis, organizational procedures, and procurements and acquisitions.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pl-08_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pl-8_smt.a` — For “Develop security and privacy architectures for the system that:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-8_smt.a.1` — For “Describe the requirements and approach to be taken for protecting the confidentiality, integrity, and availability of organizational information;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-8_smt.a.2` — For “Describe the requirements and approach to be taken for processing personally identifiable information to minimize privacy risk to individuals;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-8_smt.a.3` — For “Describe how the architectures are integrated into and support the enterprise architecture; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-8_smt.a.4` — For “Describe any assumptions about, and dependencies on, external systems and services;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-8_smt.b` — For “Review and update the architectures [PARAM pl-08_odp] to reflect changes in the enterprise architecture; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-8_smt.c` — For “Reflect planned architecture changes in security and privacy plans, Concept of Operations (CONOPS), criticality analysis, organizational procedures, and procurements and acquisitions.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pl-08_odp` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency for review and update to reflect changes in the enterprise architecture;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pl-8_obj.a.1` (pl-8_smt.a.1): a security architecture for the system describes the requirements and approach to be taken for protecting the confidentiality, integrity, and availability of organizational information;

- `pl-8_obj.a.2` (pl-8_smt.a.2): a privacy architecture describes the requirements and approach to be taken for processing personally identifiable information to minimize privacy risk to individuals;

- `pl-8_obj.a.3-1` (pl-8_smt.a.3): a security architecture for the system describes how the architecture is integrated into and supports the enterprise architecture;

- `pl-8_obj.a.3-2` (pl-8_smt.a.3): a privacy architecture for the system describes how the architecture is integrated into and supports the enterprise architecture;

- `pl-8_obj.a.4-1` (pl-8_smt.a.4): a security architecture for the system describes any assumptions about and dependencies on external systems and services;

- `pl-8_obj.a.4-2` (pl-8_smt.a.4): a privacy architecture for the system describes any assumptions about and dependencies on external systems and services;

- `pl-8_obj.b` (pl-8_smt.b): changes in the enterprise architecture are reviewed and updated [PARAM pl-08_odp] to reflect changes in the enterprise architecture;

- `pl-8_obj.c-1` (pl-8_smt.c): planned architecture changes are reflected in the security plan;

- `pl-8_obj.c-2` (pl-8_smt.c): planned architecture changes are reflected in the privacy plan;

- `pl-8_obj.c-3` (pl-8_smt.c): planned architecture changes are reflected in the Concept of Operations (CONOPS);

- `pl-8_obj.c-4` (pl-8_smt.c): planned architecture changes are reflected in criticality analysis;

- `pl-8_obj.c-5` (pl-8_smt.c): planned architecture changes are reflected in organizational procedures;

- `pl-8_obj.c-6` (pl-8_smt.c): planned architecture changes are reflected in procurements and acquisitions.

#### EXAMINE — `pl-8_asm-examine`

- Security and privacy planning policy

- procedures addressing information security and privacy architecture development

- procedures addressing information security and privacy architecture reviews and updates

- enterprise architecture documentation

- information security and privacy architecture documentation

- system security plan

- privacy plan

- security and privacy CONOPS for the system

- records of information security and privacy architecture reviews and updates

- other relevant documents or records

#### INTERVIEW — `pl-8_asm-interview`

- Organizational personnel with security and privacy planning and plan implementation responsibilities

- organizational personnel with information security and privacy architecture development responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `pl-8_asm-test`

- Organizational processes for developing, reviewing, and updating the information security and privacy architecture

- mechanisms supporting and/or implementing the development, review, and update of the information security and privacy architecture

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pl-8`. The library index records the exact source revision and hash.

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [SP 800-160-1](https://doi.org/10.6028/NIST.SP.800-160v1)

- [SP 800-160-2](https://doi.org/10.6028/NIST.SP.800-160v2)

- Catalog relationship **related**: `cm-2`.

- Catalog relationship **related**: `cm-6`.

- Catalog relationship **related**: `pl-2`.

- Catalog relationship **related**: `pl-7`.

- Catalog relationship **related**: `pl-9`.

- Catalog relationship **related**: `pm-5`.

- Catalog relationship **related**: `pm-7`.

- Catalog relationship **related**: `ra-9`.

- Catalog relationship **related**: `sa-3`.

- Catalog relationship **related**: `sa-5`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sa-17`.

- Catalog relationship **related**: `sc-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
