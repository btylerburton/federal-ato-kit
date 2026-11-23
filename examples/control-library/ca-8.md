---
title: "CA-8 \u2014 Penetration Testing"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CA-8 — Penetration Testing

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Penetration testing is a specialized type of assessment conducted on systems or individual system components to identify vulnerabilities that could be exploited by adversaries. Penetration testing goes beyond automated vulnerability scanning and is conducted by agents and teams with demonstrable skills and experience that include technical expertise in network, operating system, and/or application level security. Penetration testing can be used to validate vulnerabilities or determine the degree of penetration resistance of systems to adversaries within specified constraints. Such constraints include time, resources, and skills. Penetration testing attempts to duplicate the actions of adversaries and provides a more in-depth analysis of security- and privacy-related weaknesses or deficiencies. Penetration testing is especially important when organizations are transitioning from older technologies to newer technologies (e.g., transitioning from IPv4 to IPv6 network protocols).

Organizations can use the results of vulnerability analyses to support penetration testing activities. Penetration testing can be conducted internally or externally on the hardware, software, or firmware components of a system and can exercise both physical and technical controls. A standard method for penetration testing includes a pretest analysis based on full knowledge of the system, pretest identification of potential vulnerabilities based on the pretest analysis, and testing designed to determine the exploitability of vulnerabilities. All parties agree to the rules of engagement before commencing penetration testing scenarios. Organizations correlate the rules of engagement for the penetration tests with the tools, techniques, and procedures that are anticipated to be employed by adversaries. Penetration testing may result in the exposure of information that is protected by laws or regulations, to individuals conducting the testing. Rules of engagement, contracts, or other appropriate mechanisms can be used to communicate expectations for how to protect this information. Risk assessments guide the decisions on the level of independence required for the personnel conducting penetration testing.

### Requirements and exact statement parts

- `ca-8_smt`: Conduct penetration testing [PARAM ca-08_odp.01] on [PARAM ca-08_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ca-8_smt — Conduct penetration testing [PARAM ca-08_odp.01] on [PARAM ca-08_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ca-08_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ca-08_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ca-8_smt` — For “Conduct penetration testing [PARAM ca-08_odp.01] on [PARAM ca-08_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ca-08_odp.01` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to conduct penetration testing on systems or system components is defined;

- `ca-08_odp.02` — What approved value applies to **system(s) or system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems or system components on which penetration testing is to be conducted are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ca-8_obj` (ca-8_smt): penetration testing is conducted [PARAM ca-08_odp.01] on [PARAM ca-08_odp.02].

#### EXAMINE — `ca-8_asm-examine`

- Assessment, authorization, and monitoring policy

- procedures addressing penetration testing

- assessment plan

- penetration test report

- assessment report

- assessment evidence

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ca-8_asm-interview`

- Organizational personnel with control assessment responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

#### TEST — `ca-8_asm-test`

- Mechanisms supporting penetration testing

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ca-8`. The library index records the exact source revision and hash.

- Catalog relationship **related**: `ra-5`.

- Catalog relationship **related**: `ra-10`.

- Catalog relationship **related**: `sa-11`.

- Catalog relationship **related**: `sr-5`.

- Catalog relationship **related**: `sr-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
