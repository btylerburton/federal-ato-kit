---
title: "CA-3 \u2014 Information Exchange"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CA-3 — Information Exchange

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

System information exchange requirements apply to information exchanges between two or more systems. System information exchanges include connections via leased lines or virtual private networks, connections to internet service providers, database sharing or exchanges of database transaction information, connections and exchanges with cloud services, exchanges via web-based services, or exchanges of files via file transfer protocols, network protocols (e.g., IPv4, IPv6), email, or other organization-to-organization communications. Organizations consider the risk related to new or increased threats that may be introduced when systems exchange information with other systems that may have different security and privacy requirements and controls. This includes systems within the same organization and systems that are external to the organization. A joint authorization of the systems exchanging information, as described in CA-6(1) (catalog reference: `#ca-6.1`) or CA-6(2) (catalog reference: `#ca-6.2`) , may help to communicate and reduce risk.

Authorizing officials determine the risk associated with system information exchange and the controls needed for appropriate risk mitigation. The types of agreements selected are based on factors such as the impact level of the information being exchanged, the relationship between the organizations exchanging information (e.g., government to government, government to business, business to business, government or business to service provider, government or business to individual), or the level of access to the organizational system by users of the other system. If systems that exchange information have the same authorizing official, organizations need not develop agreements. Instead, the interface characteristics between the systems (e.g., how the information is being exchanged. how the information is protected) are described in the respective security and privacy plans. If the systems that exchange information have different authorizing officials within the same organization, the organizations can develop agreements or provide the same information that would be provided in the appropriate agreement type from CA-3a (catalog reference: `#ca-3_smt.a`) in the respective security and privacy plans for the systems. Organizations may incorporate agreement information into formal contracts, especially for information exchanges established between federal agencies and nonfederal organizations (including service providers, contractors, system developers, and system integrators). Risk considerations include systems that share the same networks.

### Requirements and exact statement parts

- `ca-3_smt`: Statement grouping; see child parts.

- `ca-3_smt.a`: Approve and manage the exchange of information between the system and other systems using [PARAM ca-03_odp.01];

- `ca-3_smt.b`: Document, as part of each exchange agreement, the interface characteristics, security and privacy requirements, controls, and responsibilities for each system, and the impact level of the information communicated; and

- `ca-3_smt.c`: Review and update the agreements [PARAM ca-03_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ca-3_smt.a — Approve and manage the exchange of information between the system and other systems using [PARAM ca-03_odp.01];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ca-3_smt.b — Document, as part of each exchange agreement, the interface characteristics, security and privacy requirements, controls, and responsibilities for each system, and the impact level of the information communicated; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ca-3_smt.c — Review and update the agreements [PARAM ca-03_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ca-03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ca-03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ca-03_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ca-3_smt.a` — For “Approve and manage the exchange of information between the system and other systems using [PARAM ca-03_odp.01];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ca-3_smt.b` — For “Document, as part of each exchange agreement, the interface characteristics, security and privacy requirements, controls, and responsibilities for each system, and the impact level of the information communicated; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ca-3_smt.c` — For “Review and update the agreements [PARAM ca-03_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ca-03_odp.01` — What approved value applies to **selection; choose one-or-more from: interconnection security agreements; information exchange security agreements; memoranda of understanding or agreement; service level agreements; user agreements; non-disclosure agreements; [PARAM ca-03_odp.02]**? Record the value, scope, approving authority, and decision source.

- `ca-03_odp.02` — What approved value applies to **type of agreement**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the type of agreement used to approve and manage the exchange of information is defined (if selected);

- `ca-03_odp.03` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which to review and update agreements is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ca-3_obj.a` (ca-3_smt.a): the exchange of information between the system and other systems is approved and managed using [PARAM ca-03_odp.01];

- `ca-3_obj.b-1` (ca-3_smt.b): the interface characteristics are documented as part of each exchange agreement;

- `ca-3_obj.b-2` (ca-3_smt.b): security requirements are documented as part of each exchange agreement;

- `ca-3_obj.b-3` (ca-3_smt.b): privacy requirements are documented as part of each exchange agreement;

- `ca-3_obj.b-4` (ca-3_smt.b): controls are documented as part of each exchange agreement;

- `ca-3_obj.b-5` (ca-3_smt.b): responsibilities for each system are documented as part of each exchange agreement;

- `ca-3_obj.b-6` (ca-3_smt.b): the impact level of the information communicated is documented as part of each exchange agreement;

- `ca-3_obj.c` (ca-3_smt.c): agreements are reviewed and updated [PARAM ca-03_odp.03].

#### EXAMINE — `ca-3_asm-examine`

- Access control policy

- procedures addressing system connections

- system and communications protection policy

- system interconnection security agreements

- information exchange security agreements

- memoranda of understanding or agreements

- service level agreements

- non-disclosure agreements

- system design documentation

- enterprise architecture

- system architecture

- system configuration settings and associated documentation

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ca-3_asm-interview`

- Organizational personnel with responsibilities for developing, implementing, or approving system interconnection agreements

- organizational personnel with information security and privacy responsibilities

- personnel managing the system(s) to which the interconnection security agreement applies

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ca-3`. The library index records the exact source revision and hash.

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [FIPS 199](https://doi.org/10.6028/NIST.FIPS.199)

- [SP 800-47](https://doi.org/10.6028/NIST.SP.800-47)

- Catalog relationship **related**: `ac-4`.

- Catalog relationship **related**: `ac-20`.

- Catalog relationship **related**: `au-16`.

- Catalog relationship **related**: `ca-6`.

- Catalog relationship **related**: `ia-3`.

- Catalog relationship **related**: `ir-4`.

- Catalog relationship **related**: `pl-2`.

- Catalog relationship **related**: `pt-7`.

- Catalog relationship **related**: `ra-3`.

- Catalog relationship **related**: `sa-9`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `si-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
