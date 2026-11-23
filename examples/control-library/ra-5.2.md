---
title: "RA-5.2 \u2014 Update Vulnerabilities to Be Scanned"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# RA-5.2 — Update Vulnerabilities to Be Scanned

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Due to the complexity of modern software, systems, and other factors, new vulnerabilities are discovered on a regular basis. It is important that newly discovered vulnerabilities are added to the list of vulnerabilities to be scanned to ensure that the organization can take steps to mitigate those vulnerabilities in a timely manner.

### Requirements and exact statement parts

- `ra-5.2_smt`: Update the system vulnerabilities to be scanned [PARAM ra-05.02_odp.01].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ra-5.2_smt — Update the system vulnerabilities to be scanned [PARAM ra-05.02_odp.01].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ra-05.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ra-05.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ra-5.2_smt` — For “Update the system vulnerabilities to be scanned [PARAM ra-05.02_odp.01].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ra-05.02_odp.01` — What approved value applies to **selection; choose one-or-more from: [PARAM ra-05.02_odp.02]; prior to a new scan; when new vulnerabilities are identified and reported**? Record the value, scope, approving authority, and decision source.

- `ra-05.02_odp.02` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency for updating the system vulnerabilities to be scanned is defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ra-5.2_obj` (ra-5.2_smt): the system vulnerabilities to be scanned are updated [PARAM ra-05.02_odp.01].

#### EXAMINE — `ra-5.2_asm-examine`

- Procedures addressing vulnerability scanning

- assessment report

- vulnerability scanning tools and associated configuration documentation

- vulnerability scanning results

- patch and vulnerability management records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ra-5.2_asm-interview`

- Organizational personnel with vulnerability scanning responsibilities

- organizational personnel with vulnerability scan analysis responsibilities

- organizational personnel with security responsibilities

- system/network administrators

#### TEST — `ra-5.2_asm-test`

- Organizational processes for vulnerability scanning

- mechanisms/tools supporting and/or implementing vulnerability scanning

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ra-5.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ra-5`.

- Catalog relationship **related**: `si-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
