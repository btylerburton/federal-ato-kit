---
title: "IR-6.2 \u2014 Vulnerabilities Related to Incidents"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-6.2 — Vulnerabilities Related to Incidents

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Reported incidents that uncover system vulnerabilities are analyzed by organizational personnel including system owners, mission and business owners, senior agency information security officers, senior agency officials for privacy, authorizing officials, and the risk executive (function). The analysis can serve to prioritize and initiate mitigation actions to address the discovered system vulnerability.

### Requirements and exact statement parts

- `ir-6.2_smt`: Report system vulnerabilities associated with reported incidents to [PARAM ir-06.02_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-6.2_smt — Report system vulnerabilities associated with reported incidents to [PARAM ir-06.02_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ir-06.02_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ir-6.2_smt` — For “Report system vulnerabilities associated with reported incidents to [PARAM ir-06.02_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ir-06.02_odp` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to whom system vulnerabilities associated with reported incidents are reported to is/are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-6.2_obj` (ir-6.2_smt): system vulnerabilities associated with reported incidents are reported to [PARAM ir-06.02_odp].

#### EXAMINE — `ir-6.2_asm-examine`

- Incident response policy

- procedures addressing incident reporting

- incident response plan

- system security plan

- privacy plan

- security incident reports and associated system vulnerabilities

- other relevant documents or records

#### INTERVIEW — `ir-6.2_asm-interview`

- Organizational personnel with incident reporting responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

- personnel to whom vulnerabilities associated with security incidents are to be reported

#### TEST — `ir-6.2_asm-test`

- Organizational processes for incident reporting

- mechanisms supporting and/or implementing the reporting of vulnerabilities associated with security incidents

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-6.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ir-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
