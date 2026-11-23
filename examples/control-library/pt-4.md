---
title: "PT-4 \u2014 Consent"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PT-4 — Consent

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Consent allows individuals to participate in making decisions about the processing of their information and transfers some of the risk that arises from the processing of personally identifiable information from the organization to an individual. Consent may be required by applicable laws, executive orders, directives, regulations, policies, standards, or guidelines. Otherwise, when selecting consent as a control, organizations consider whether individuals can be reasonably expected to understand and accept the privacy risks that arise from their authorization. Organizations consider whether other controls may more effectively mitigate privacy risk either alone or in conjunction with consent. Organizations also consider any demographic or contextual factors that may influence the understanding or behavior of individuals with respect to the processing carried out by the system or organization. When soliciting consent from individuals, organizations consider the appropriate mechanism for obtaining consent, including the type of consent (e.g., opt-in, opt-out), how to properly authenticate and identity proof individuals and how to obtain consent through electronic means. In addition, organizations consider providing a mechanism for individuals to revoke consent once it has been provided, as appropriate. Finally, organizations consider usability factors to help individuals understand the risks being accepted when providing consent, including the use of plain language and avoiding technical jargon.

### Requirements and exact statement parts

- `pt-4_smt`: Implement [PARAM pt-04_odp] for individuals to consent to the processing of their personally identifiable information prior to its collection that facilitate individuals’ informed decision-making.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pt-4_smt — Implement [PARAM pt-04_odp] for individuals to consent to the processing of their personally identifiable information prior to its collection that facilitate individuals’ informed decision-making.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pt-04_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pt-4_smt` — For “Implement [PARAM pt-04_odp] for individuals to consent to the processing of their personally identifiable information prior to its collection that facilitate individuals’ informed decision-making.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pt-04_odp` — What approved value applies to **tools or mechanisms**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the tools or mechanisms to be implemented for individuals to consent to the processing of their personally identifiable information are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pt-4_obj` (pt-4_smt): the [PARAM pt-04_odp] are implemented for individuals to consent to the processing of their personally identifiable information prior to its collection that facilitate individuals’ informed decision-making.

#### EXAMINE — `pt-4_asm-examine`

- Personally identifiable information processing and transparency policy and procedures

- consent policies and procedures

- consent tools and mechanisms

- consent presentation or display (user interface)

- evidence of individuals’ consent

- privacy plan

- other relevant documents or records

#### INTERVIEW — `pt-4_asm-interview`

- Organizational personnel with personally identifiable information processing and transparency responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `pt-4_asm-test`

- Organizational processes for the collection of personally identifiable information

- consent tools or mechanisms for users to authorize the processing of their personally identifiable information

- mechanisms implementing consent

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pt-4`. The library index records the exact source revision and hash.

- [PRIVACT](https://www.govinfo.gov/content/pkg/STATUTE-88/pdf/STATUTE-88-Pg1896.pdf)

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [SP 800-63-3](https://doi.org/10.6028/NIST.SP.800-63-3)

- Catalog relationship **related**: `ac-16`.

- Catalog relationship **related**: `pt-2`.

- Catalog relationship **related**: `pt-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
