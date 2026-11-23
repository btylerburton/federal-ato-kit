---
title: "AC-4 \u2014 Information Flow Enforcement"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4 — Information Flow Enforcement

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Information flow control regulates where information can travel within a system and between systems (in contrast to who is allowed to access the information) and without regard to subsequent accesses to that information. Flow control restrictions include blocking external traffic that claims to be from within the organization, keeping export-controlled information from being transmitted in the clear to the Internet, restricting web requests that are not from the internal web proxy server, and limiting information transfers between organizations based on data structures and content. Transferring information between organizations may require an agreement specifying how the information flow is enforced (see CA-3 (catalog reference: `#ca-3`) ). Transferring information between systems in different security or privacy domains with different security or privacy policies introduces the risk that such transfers violate one or more domain security or privacy policies. In such situations, information owners/stewards provide guidance at designated policy enforcement points between connected systems. Organizations consider mandating specific architectural solutions to enforce specific security and privacy policies. Enforcement includes prohibiting information transfers between connected systems (i.e., allowing access only), verifying write permissions before accepting information from another security or privacy domain or connected system, employing hardware mechanisms to enforce one-way information flows, and implementing trustworthy regrading mechanisms to reassign security or privacy attributes and labels.

Organizations commonly employ information flow control policies and enforcement mechanisms to control the flow of information between designated sources and destinations within systems and between connected systems. Flow control is based on the characteristics of the information and/or the information path. Enforcement occurs, for example, in boundary protection devices that employ rule sets or establish configuration settings that restrict system services, provide a packet-filtering capability based on header information, or provide a message-filtering capability based on message content. Organizations also consider the trustworthiness of filtering and/or inspection mechanisms (i.e., hardware, firmware, and software components) that are critical to information flow enforcement. Control enhancements 3 through 32 primarily address cross-domain solution needs that focus on more advanced filtering techniques, in-depth analysis, and stronger flow enforcement mechanisms implemented in cross-domain products, such as high-assurance guards. Such capabilities are generally not available in commercial off-the-shelf products. Information flow enforcement also applies to control plane traffic (e.g., routing and DNS).

### Requirements and exact statement parts

- `ac-4_smt`: Enforce approved authorizations for controlling the flow of information within the system and between connected systems based on [PARAM ac-04_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4_smt — Enforce approved authorizations for controlling the flow of information within the system and between connected systems based on [PARAM ac-04_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-04_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-4_smt` — For “Enforce approved authorizations for controlling the flow of information within the system and between connected systems based on [PARAM ac-04_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-04_odp` — What approved value applies to **information flow control policies**? Record the value, scope, approving authority, and decision source.

  - Catalog context: information flow control policies within the system and between connected systems are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4_obj` (ac-4_smt): approved authorizations are enforced for controlling the flow of information within the system and between connected systems based on [PARAM ac-04_odp].

#### EXAMINE — `ac-4_asm-examine`

- Access control policy

- information flow control policies

- procedures addressing information flow enforcement

- security architecture documentation

- privacy architecture documentation

- system design documentation

- system configuration settings and associated documentation

- system baseline configuration

- list of information flow authorizations

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ac-4_asm-interview`

- System/network administrators

- organizational personnel with information security and privacy architecture development responsibilities

- organizational personnel with information security and privacy responsibilities

- system developers

#### TEST — `ac-4_asm-test`

- Mechanisms implementing information flow enforcement policy

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4`. The library index records the exact source revision and hash.

- [SP 800-160-1](https://doi.org/10.6028/NIST.SP.800-160v1)

- [SP 800-162](https://doi.org/10.6028/NIST.SP.800-162)

- [SP 800-178](https://doi.org/10.6028/NIST.SP.800-178)

- [IR 8112](https://doi.org/10.6028/NIST.IR.8112)

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-6`.

- Catalog relationship **related**: `ac-16`.

- Catalog relationship **related**: `ac-17`.

- Catalog relationship **related**: `ac-19`.

- Catalog relationship **related**: `ac-21`.

- Catalog relationship **related**: `au-10`.

- Catalog relationship **related**: `ca-3`.

- Catalog relationship **related**: `ca-9`.

- Catalog relationship **related**: `cm-7`.

- Catalog relationship **related**: `pl-9`.

- Catalog relationship **related**: `pm-24`.

- Catalog relationship **related**: `sa-17`.

- Catalog relationship **related**: `sc-4`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `sc-16`.

- Catalog relationship **related**: `sc-31`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
