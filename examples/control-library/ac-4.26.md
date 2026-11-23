---
title: "AC-4.26 \u2014 Audit Filtering Actions"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4.26 — Audit Filtering Actions

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Content filtering is the process of inspecting information as it traverses a cross-domain solution and determines if the information meets a predefined policy. Content filtering actions and the results of filtering actions are recorded for individual messages to ensure that the correct filter actions were applied. Content filter reports are used to assist in troubleshooting actions by, for example, determining why message content was modified and/or why it failed the filtering process. Audit events are defined in AU-2 (catalog reference: `#au-2`) . Audit records are generated in AU-12 (catalog reference: `#au-12`).

### Requirements and exact statement parts

- `ac-4.26_smt`: When transferring information between different security domains, record and audit content filtering actions and results for the information being filtered.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4.26_smt — When transferring information between different security domains, record and audit content filtering actions and results for the information being filtered.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ac-4.26_smt` — For “When transferring information between different security domains, record and audit content filtering actions and results for the information being filtered.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4.26_obj-1` (ac-4.26_smt): when transferring information between different security domains, content-filtering actions are recorded and audited;

- `ac-4.26_obj-2` (ac-4.26_smt): when transferring information between different security domains, results for the information being filtered are recorded and audited.

#### EXAMINE — `ac-4.26_asm-examine`

- Information flow enforcement policy

- procedures addressing information flow enforcement

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ac-4.26_asm-interview`

- Organizational personnel with information flow enforcement responsibilities

- system/network administrators

- organizational personnel with information security responsibilities

#### TEST — `ac-4.26_asm-test`

- Mechanisms implementing information flow enforcement functions

- mechanisms implementing content filtering

- mechanisms recording and auditing content filtering

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4.26`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-4`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-3`.

- Catalog relationship **related**: `au-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
