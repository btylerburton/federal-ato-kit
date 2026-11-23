---
title: "IR-4.12 \u2014 Malicious Code and Forensic Analysis"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-4.12 — Malicious Code and Forensic Analysis

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

When conducted carefully in an isolated environment, analysis of malicious code and other residual artifacts of a security incident or breach can give the organization insight into adversary tactics, techniques, and procedures. It can also indicate the identity or some defining characteristics of the adversary. In addition, malicious code analysis can help the organization develop responses to future incidents.

### Requirements and exact statement parts

- `ir-4.12_smt`: Analyze malicious code and/or other residual artifacts remaining in the system after the incident.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-4.12_smt — Analyze malicious code and/or other residual artifacts remaining in the system after the incident.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ir-4.12_smt` — For “Analyze malicious code and/or other residual artifacts remaining in the system after the incident.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-4.12_obj-1` (ir-4.12_smt): malicious code remaining in the system is analyzed after the incident;

- `ir-4.12_obj-2` (ir-4.12_smt): other residual artifacts remaining in the system (if any) are analyzed after the incident.

#### EXAMINE — `ir-4.12_asm-examine`

- Incident response policy

- procedures addressing incident handling

- procedures addressing code and forensic analysis

- procedures addressing incident response

- incident response plan

- system design documentation

- malicious code protection mechanisms, tools, and techniques

- results from malicious code analyses

- system security plan

- system audit records

- other relevant documents or records

#### INTERVIEW — `ir-4.12_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel with responsibility for malicious code protection

- organizational personnel responsible for incident response/management

#### TEST — `ir-4.12_asm-test`

- Organizational process for incident response

- organizational processes for conducting forensic analysis

- tools and techniques for analysis of malicious code characteristics and behavior

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-4.12`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ir-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
