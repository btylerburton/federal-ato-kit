---
title: "SI-4.17 \u2014 Integrated Situational Awareness"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-4.17 — Integrated Situational Awareness

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Correlating monitoring information from a more diverse set of information sources helps to achieve integrated situational awareness. Integrated situational awareness from a combination of physical, cyber, and supply chain monitoring activities enhances the capability of organizations to more quickly detect sophisticated attacks and investigate the methods and techniques employed to carry out such attacks. In contrast to SI-4(16) (catalog reference: `#si-4.16`) , which correlates the various cyber monitoring information, integrated situational awareness is intended to correlate monitoring beyond the cyber domain. Correlation of monitoring information from multiple activities may help reveal attacks on organizations that are operating across multiple attack vectors.

### Requirements and exact statement parts

- `si-4.17_smt`: Correlate information from monitoring physical, cyber, and supply chain activities to achieve integrated, organization-wide situational awareness.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-4.17_smt — Correlate information from monitoring physical, cyber, and supply chain activities to achieve integrated, organization-wide situational awareness.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `si-4.17_smt` — For “Correlate information from monitoring physical, cyber, and supply chain activities to achieve integrated, organization-wide situational awareness.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-4.17_obj` (si-4.17_smt): information from monitoring physical, cyber, and supply chain activities are correlated to achieve integrated, organization-wide situational awareness.

#### EXAMINE — `si-4.17_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing system monitoring tools and techniques

- system design documentation

- system monitoring tools and techniques documentation

- system configuration settings and associated documentation

- event correlation logs or records resulting from physical, cyber, and supply chain activities

- system audit records

- system security plan

- supply chain risk management plan

- other relevant documents or records

#### INTERVIEW — `si-4.17_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for monitoring the system

- organizational personnel responsible for the intrusion detection system

#### TEST — `si-4.17_asm-test`

- Organizational processes for intrusion detection and system monitoring

- mechanisms supporting and/or implementing intrusion detection and system monitoring capabilities

- mechanisms supporting and/or implementing the correlation of information from monitoring tools

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-4.17`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-4`.

- Catalog relationship **related**: `au-16`.

- Catalog relationship **related**: `pe-6`.

- Catalog relationship **related**: `sr-2`.

- Catalog relationship **related**: `sr-4`.

- Catalog relationship **related**: `sr-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
