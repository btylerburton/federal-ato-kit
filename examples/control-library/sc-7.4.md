---
title: "SC-7.4 \u2014 External Telecommunications Services"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-7.4 — External Telecommunications Services

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

External telecommunications services can provide data and/or voice communications services. Examples of control plane traffic include Border Gateway Protocol (BGP) routing, Domain Name System (DNS), and management protocols. See SP 800-189 (catalog reference: `#f5edfe51-d1f2-422e-9b27-5d0e90b49c72`) for additional information on the use of the resource public key infrastructure (RPKI) to protect BGP routes and detect unauthorized BGP announcements.

### Requirements and exact statement parts

- `sc-7.4_smt`: Statement grouping; see child parts.

- `sc-7.4_smt.a`: Implement a managed interface for each external telecommunication service;

- `sc-7.4_smt.b`: Establish a traffic flow policy for each managed interface;

- `sc-7.4_smt.c`: Protect the confidentiality and integrity of the information being transmitted across each interface;

- `sc-7.4_smt.d`: Document each exception to the traffic flow policy with a supporting mission or business need and duration of that need;

- `sc-7.4_smt.e`: Review exceptions to the traffic flow policy [PARAM sc-07.04_odp] and remove exceptions that are no longer supported by an explicit mission or business need;

- `sc-7.4_smt.f`: Prevent unauthorized exchange of control plane traffic with external networks;

- `sc-7.4_smt.g`: Publish information to enable remote networks to detect unauthorized control plane traffic from internal networks; and

- `sc-7.4_smt.h`: Filter unauthorized control plane traffic from external networks.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-7.4_smt.a — Implement a managed interface for each external telecommunication service;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sc-7.4_smt.b — Establish a traffic flow policy for each managed interface;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sc-7.4_smt.c — Protect the confidentiality and integrity of the information being transmitted across each interface;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sc-7.4_smt.d — Document each exception to the traffic flow policy with a supporting mission or business need and duration of that need;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sc-7.4_smt.e — Review exceptions to the traffic flow policy [PARAM sc-07.04_odp] and remove exceptions that are no longer supported by an explicit mission or business need;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sc-7.4_smt.f — Prevent unauthorized exchange of control plane traffic with external networks;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sc-7.4_smt.g — Publish information to enable remote networks to detect unauthorized control plane traffic from internal networks; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sc-7.4_smt.h — Filter unauthorized control plane traffic from external networks.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-07.04_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-7.4_smt.a` — For “Implement a managed interface for each external telecommunication service;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sc-7.4_smt.b` — For “Establish a traffic flow policy for each managed interface;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sc-7.4_smt.c` — For “Protect the confidentiality and integrity of the information being transmitted across each interface;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sc-7.4_smt.d` — For “Document each exception to the traffic flow policy with a supporting mission or business need and duration of that need;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sc-7.4_smt.e` — For “Review exceptions to the traffic flow policy [PARAM sc-07.04_odp] and remove exceptions that are no longer supported by an explicit mission or business need;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sc-7.4_smt.f` — For “Prevent unauthorized exchange of control plane traffic with external networks;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sc-7.4_smt.g` — For “Publish information to enable remote networks to detect unauthorized control plane traffic from internal networks; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sc-7.4_smt.h` — For “Filter unauthorized control plane traffic from external networks.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-07.04_odp` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which to review exceptions to traffic flow policy is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-7.4_obj.a` (sc-7.4_smt.a): a managed interface is implemented for each external telecommunication service;

- `sc-7.4_obj.b` (sc-7.4_smt.b): a traffic flow policy is established for each managed interface;

- `sc-7.4_obj.c-1` (sc-7.4_smt.c): the confidentiality of the information being transmitted across each interface is protected;

- `sc-7.4_obj.c-2` (sc-7.4_smt.c): the integrity of the information being transmitted across each interface is protected;

- `sc-7.4_obj.d` (sc-7.4_smt.d): each exception to the traffic flow policy is documented with a supporting mission or business need and duration of that need;

- `sc-7.4_obj.e-1` (sc-7.4_smt.e): exceptions to the traffic flow policy are reviewed [PARAM sc-07.04_odp];

- `sc-7.4_obj.e-2` (sc-7.4_smt.e): exceptions to the traffic flow policy that are no longer supported by an explicit mission or business need are removed;

- `sc-7.4_obj.f` (sc-7.4_smt.f): unauthorized exchanges of control plan traffic with external networks are prevented;

- `sc-7.4_obj.g` (sc-7.4_smt.g): information is published to enable remote networks to detect unauthorized control plane traffic from internal networks;

- `sc-7.4_obj.h` (sc-7.4_smt.h): unauthorized control plane traffic is filtered from external networks.

#### EXAMINE — `sc-7.4_asm-examine`

- System and communications protection policy

- traffic flow policy

- information flow control policy

- procedures addressing boundary protection

- system security architecture

- system design documentation

- boundary protection hardware and software

- system architecture and configuration documentation

- system configuration settings and associated documentation

- records of traffic flow policy exceptions

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-7.4_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel with boundary protection responsibilities

#### TEST — `sc-7.4_asm-test`

- Organizational processes for documenting and reviewing exceptions to the traffic flow policy

- organizational processes for removing exceptions to the traffic flow policy

- mechanisms implementing boundary protection capabilities

- managed interfaces implementing traffic flow policy

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-7.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sc-7`.

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `sc-8`.

- Catalog relationship **related**: `sc-20`.

- Catalog relationship **related**: `sc-21`.

- Catalog relationship **related**: `sc-22`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
