---
title: "RA-5.3 \u2014 Breadth and Depth of Coverage"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# RA-5.3 — Breadth and Depth of Coverage

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The breadth of vulnerability scanning coverage can be expressed as a percentage of components within the system, by the particular types of systems, by the criticality of systems, or by the number of vulnerabilities to be checked. Conversely, the depth of vulnerability scanning coverage can be expressed as the level of the system design that the organization intends to monitor (e.g., component, module, subsystem, element). Organizations can determine the sufficiency of vulnerability scanning coverage with regard to its risk tolerance and other factors. Scanning tools and how the tools are configured may affect the depth and coverage. Multiple scanning tools may be needed to achieve the desired depth and coverage. SP 800-53A (catalog reference: `#a21aef46-7330-48a0-b2e1-c5bb8b2dd11d`) provides additional information on the breadth and depth of coverage.

### Requirements and exact statement parts

- `ra-5.3_smt`: Define the breadth and depth of vulnerability scanning coverage.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ra-5.3_smt — Define the breadth and depth of vulnerability scanning coverage.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ra-5.3_smt` — For “Define the breadth and depth of vulnerability scanning coverage.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ra-5.3_obj` (ra-5.3_smt): the breadth and depth of vulnerability scanning coverage are defined.

#### EXAMINE — `ra-5.3_asm-examine`

- Procedures addressing vulnerability scanning

- assessment report

- vulnerability scanning tools and associated configuration documentation

- vulnerability scanning results

- patch and vulnerability management records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ra-5.3_asm-interview`

- Organizational personnel with vulnerability scanning responsibilities

- organizational personnel with vulnerability scan analysis responsibilities

- organizational personnel with security responsibilities

#### TEST — `ra-5.3_asm-test`

- Organizational processes for vulnerability scanning

- mechanisms/tools supporting and/or implementing vulnerability scanning

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ra-5.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ra-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
