---
title: "SI-3.10 \u2014 Malicious Code Analysis"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-3.10 — Malicious Code Analysis

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The use of malicious code analysis tools provides organizations with a more in-depth understanding of adversary tradecraft (i.e., tactics, techniques, and procedures) and the functionality and purpose of specific instances of malicious code. Understanding the characteristics of malicious code facilitates effective organizational responses to current and future threats. Organizations can conduct malicious code analyses by employing reverse engineering techniques or by monitoring the behavior of executing code.

### Requirements and exact statement parts

- `si-3.10_smt`: Statement grouping; see child parts.

- `si-3.10_smt.a`: Employ the following tools and techniques to analyze the characteristics and behavior of malicious code: [PARAM si-03.10_odp] ; and

- `si-3.10_smt.b`: Incorporate the results from malicious code analysis into organizational incident response and flaw remediation processes.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-3.10_smt.a — Employ the following tools and techniques to analyze the characteristics and behavior of malicious code: [PARAM si-03.10_odp] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-3.10_smt.b — Incorporate the results from malicious code analysis into organizational incident response and flaw remediation processes.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-03.10_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-3.10_smt.a` — For “Employ the following tools and techniques to analyze the characteristics and behavior of malicious code: [PARAM si-03.10_odp] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-3.10_smt.b` — For “Incorporate the results from malicious code analysis into organizational incident response and flaw remediation processes.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-03.10_odp` — What approved value applies to **tools and techniques**? Record the value, scope, approving authority, and decision source.

  - Catalog context: tools and techniques to be employed to analyze the characteristics and behavior of malicious code are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-3.10_obj.a` (si-3.10_smt.a): [PARAM si-03.10_odp] are employed to analyze the characteristics and behavior of malicious code;

- `si-3.10_obj.b-1` (si-3.10_smt.b): the results from malicious code analysis are incorporated into organizational incident response processes;

- `si-3.10_obj.b-2` (si-3.10_smt.b): the results from malicious code analysis are incorporated into organizational flaw remediation processes.

#### EXAMINE — `si-3.10_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing malicious code protection

- procedures addressing incident response

- procedures addressing flaw remediation

- system design documentation

- malicious code protection mechanisms, tools, and techniques

- system configuration settings and associated documentation

- results from malicious code analyses

- records of flaw remediation events resulting from malicious code analyses

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-3.10_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for malicious code protection

- organizational personnel responsible for flaw remediation

- organizational personnel responsible for incident response/management

#### TEST — `si-3.10_asm-test`

- Organizational process for incident response

- organizational process for flaw remediation

- mechanisms supporting and/or implementing malicious code protection capabilities

- tools and techniques for the analysis of malicious code characteristics and behavior

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-3.10`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
