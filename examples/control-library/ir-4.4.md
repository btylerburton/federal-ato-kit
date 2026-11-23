---
title: "IR-4.4 \u2014 Information Correlation"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-4.4 — Information Correlation

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Sometimes, a threat event, such as a hostile cyber-attack, can only be observed by bringing together information from different sources, including various reports and reporting procedures established by organizations.

### Requirements and exact statement parts

- `ir-4.4_smt`: Correlate incident information and individual incident responses to achieve an organization-wide perspective on incident awareness and response.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-4.4_smt — Correlate incident information and individual incident responses to achieve an organization-wide perspective on incident awareness and response.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ir-4.4_smt` — For “Correlate incident information and individual incident responses to achieve an organization-wide perspective on incident awareness and response.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-4.4_obj` (ir-4.4_smt): incident information and individual incident responses are correlated to achieve an organization-wide perspective on incident awareness and response.

#### EXAMINE — `ir-4.4_asm-examine`

- Incident response policy

- procedures addressing incident handling

- incident response plan

- privacy plan

- mechanisms supporting incident and event correlation

- system design documentation

- system configuration settings and associated documentation

- system security plan

- privacy plan

- incident management correlation logs

- event management correlation logs

- security information and event management logs

- incident management correlation reports

- event management correlation reports

- security information and event management reports

- audit records

- other relevant documents or records

#### INTERVIEW — `ir-4.4_asm-interview`

- Organizational personnel with incident handling responsibilities

- organizational personnel with information security and privacy responsibilities

- organizational personnel with whom incident information and individual incident responses are to be correlated

#### TEST — `ir-4.4_asm-test`

- Organizational processes for correlating incident information and individual incident responses

- mechanisms that support and or implement the correlation of incident response information with individual incident responses

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-4.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ir-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
