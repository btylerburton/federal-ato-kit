---
title: "AU-6.9 \u2014 Correlation with Information from Nontechnical Sources"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-6.9 — Correlation with Information from Nontechnical Sources

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Nontechnical sources include records that document organizational policy violations related to harassment incidents and the improper use of information assets. Such information can lead to a directed analytical effort to detect potential malicious insider activity. Organizations limit access to information that is available from nontechnical sources due to its sensitive nature. Limited access minimizes the potential for inadvertent release of privacy-related information to individuals who do not have a need to know. The correlation of information from nontechnical sources with audit record information generally occurs only when individuals are suspected of being involved in an incident. Organizations obtain legal advice prior to initiating such actions.

### Requirements and exact statement parts

- `au-6.9_smt`: Correlate information from nontechnical sources with audit record information to enhance organization-wide situational awareness.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-6.9_smt — Correlate information from nontechnical sources with audit record information to enhance organization-wide situational awareness.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `au-6.9_smt` — For “Correlate information from nontechnical sources with audit record information to enhance organization-wide situational awareness.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-6.9_obj` (au-6.9_smt): information from non-technical sources is correlated with audit record information to enhance organization-wide situational awareness.

#### EXAMINE — `au-6.9_asm-examine`

- Audit and accountability policy

- system security plan

- privacy plan

- procedures addressing audit review, analysis, and reporting

- system design documentation

- system configuration settings and associated documentation

- documentation providing evidence of correlated information obtained from audit records and organization-defined non-technical sources

- list of information types from non-technical sources for correlation with audit information

- other relevant documents or records

#### INTERVIEW — `au-6.9_asm-interview`

- Organizational personnel with audit review, analysis, and reporting responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `au-6.9_asm-test`

- Mechanisms implementing capability to correlate information from non-technical sources

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-6.9`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `au-6`.

- Catalog relationship **related**: `pm-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
