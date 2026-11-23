---
title: "SA-3.2 \u2014 Use of Live or Operational Data"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-3.2 — Use of Live or Operational Data

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Live data is also referred to as operational data. The use of live or operational data in preproduction (i.e., development, test, and integration) environments can result in significant risks to organizations. In addition, the use of personally identifiable information in testing, research, and training increases the risk of unauthorized disclosure or misuse of such information. Therefore, it is important for the organization to manage any additional risks that may result from the use of live or operational data. Organizations can minimize such risks by using test or dummy data during the design, development, and testing of systems, system components, and system services. Risk assessment techniques may be used to determine if the risk of using live or operational data is acceptable.

### Requirements and exact statement parts

- `sa-3.2_smt`: Statement grouping; see child parts.

- `sa-3.2_smt.a`: Approve, document, and control the use of live data in preproduction environments for the system, system component, or system service; and

- `sa-3.2_smt.b`: Protect preproduction environments for the system, system component, or system service at the same impact or classification level as any live data in use within the preproduction environments.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-3.2_smt.a — Approve, document, and control the use of live data in preproduction environments for the system, system component, or system service; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sa-3.2_smt.b — Protect preproduction environments for the system, system component, or system service at the same impact or classification level as any live data in use within the preproduction environments.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sa-3.2_smt.a` — For “Approve, document, and control the use of live data in preproduction environments for the system, system component, or system service; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sa-3.2_smt.b` — For “Protect preproduction environments for the system, system component, or system service at the same impact or classification level as any live data in use within the preproduction environments.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-3.2_obj.a-1` (sa-3.2_smt.a): the use of live data in pre-production environments is approved for the system, system component, or system service;

- `sa-3.2_obj.a-2` (sa-3.2_smt.a): the use of live data in pre-production environments is documented for the system, system component, or system service;

- `sa-3.2_obj.a-3` (sa-3.2_smt.a): the use of live data in pre-production environments is controlled for the system, system component, or system service;

- `sa-3.2_obj.b` (sa-3.2_smt.b): pre-production environments for the system, system component, or system service are protected at the same impact or classification level as any live data in use within the pre-production environments.

#### EXAMINE — `sa-3.2_asm-examine`

- System and services acquisition policy

- system and services acquisition procedures

- procedures addressing the integration of security and privacy into the system development life cycle process

- system development life cycle documentation

- security risk assessment documentation

- privacy impact assessment

- privacy risk assessment documentation

- system security plan

- privacy plan

- data mapping documentation

- personally identifiable information processing policy

- procedures addressing the authority to test with personally identifiable information

- procedures addressing the minimization of personally identifiable information used in testing, training, and research

- other relevant documents or records

#### INTERVIEW — `sa-3.2_asm-interview`

- Organizational personnel with information security and privacy responsibility

- organizational personnel with system life cycle development responsibilities

#### TEST — `sa-3.2_asm-test`

- Organizational processes the use of live data in pre-production environments

- mechanisms for protecting live data in pre-production environments

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-3.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-3`.

- Catalog relationship **related**: `pm-25`.

- Catalog relationship **related**: `ra-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
