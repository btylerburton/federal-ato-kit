---
title: "IR-4.13 \u2014 Behavior Analysis"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-4.13 — Behavior Analysis

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

If the organization maintains a deception environment, an analysis of behaviors in that environment, including resources targeted by the adversary and timing of the incident or event, can provide insight into adversarial tactics, techniques, and procedures. External to a deception environment, the analysis of anomalous adversarial behavior (e.g., changes in system performance or usage patterns) or suspected behavior (e.g., changes in searches for the location of specific resources) can give the organization such insight.

### Requirements and exact statement parts

- `ir-4.13_smt`: Analyze anomalous or suspected adversarial behavior in or related to [PARAM ir-04.13_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-4.13_smt — Analyze anomalous or suspected adversarial behavior in or related to [PARAM ir-04.13_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ir-04.13_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ir-4.13_smt` — For “Analyze anomalous or suspected adversarial behavior in or related to [PARAM ir-04.13_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ir-04.13_odp` — What approved value applies to **environments or resources**? Record the value, scope, approving authority, and decision source.

  - Catalog context: environments or resources which may contain or may be related to anomalous or suspected adversarial behavior are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-4.13_obj` (ir-4.13_smt): anomalous or suspected adversarial behavior in or related to [PARAM ir-04.13_odp] are analyzed.

#### EXAMINE — `ir-4.13_asm-examine`

- Incident response policy

- procedures addressing system monitoring tools and techniques

- incident response plan

- system monitoring logs or records

- system monitoring tools and techniques documentation

- system configuration settings and associated documentation

- security plan

- system component inventory

- network diagram

- system protocols documentation

- list of acceptable thresholds for false positives and false negatives

- system security plan

- other relevant documents or records

#### INTERVIEW — `ir-4.13_asm-interview`

- Organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ir-4.13_asm-test`

- Organizational processes for detecting anomalous behavior

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-4.13`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ir-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
