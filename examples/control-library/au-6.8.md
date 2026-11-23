---
title: "AU-6.8 \u2014 Full Text Analysis of Privileged Commands"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-6.8 — Full Text Analysis of Privileged Commands

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Full text analysis of privileged commands requires a distinct environment for the analysis of audit record information related to privileged users without compromising such information on the system where the users have elevated privileges, including the capability to execute privileged commands. Full text analysis refers to analysis that considers the full text of privileged commands (i.e., commands and parameters) as opposed to analysis that considers only the name of the command. Full text analysis includes the use of pattern matching and heuristics.

### Requirements and exact statement parts

- `au-6.8_smt`: Perform a full text analysis of logged privileged commands in a physically distinct component or subsystem of the system, or other system that is dedicated to that analysis.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-6.8_smt — Perform a full text analysis of logged privileged commands in a physically distinct component or subsystem of the system, or other system that is dedicated to that analysis.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `au-6.8_smt` — For “Perform a full text analysis of logged privileged commands in a physically distinct component or subsystem of the system, or other system that is dedicated to that analysis.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-6.8_obj` (au-6.8_smt): a full text analysis of logged privileged commands in a physically distinct component or subsystem of the system or other system that is dedicated to that analysis is performed.

#### EXAMINE — `au-6.8_asm-examine`

- Audit and accountability policy

- procedures addressing audit review, analysis, and reporting

- system design documentation

- system configuration settings and associated documentation

- text analysis tools and techniques

- text analysis documentation of audited privileged commands

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `au-6.8_asm-interview`

- Organizational personnel with audit review, analysis, and reporting responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `au-6.8_asm-test`

- Mechanisms implementing the capability to perform a full text analysis of audited privilege commands

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-6.8`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `au-6`.

- Catalog relationship **related**: `au-3`.

- Catalog relationship **related**: `au-9`.

- Catalog relationship **related**: `au-11`.

- Catalog relationship **related**: `au-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
