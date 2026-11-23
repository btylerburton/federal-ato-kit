---
title: "IR-4.2 \u2014 Dynamic Reconfiguration"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# IR-4.2 — Dynamic Reconfiguration

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Dynamic reconfiguration includes changes to router rules, access control lists, intrusion detection or prevention system parameters, and filter rules for guards or firewalls. Organizations may perform dynamic reconfiguration of systems to stop attacks, misdirect attackers, and isolate components of systems, thus limiting the extent of the damage from breaches or compromises. Organizations include specific time frames for achieving the reconfiguration of systems in the definition of the reconfiguration capability, considering the potential need for rapid response to effectively address cyber threats.

### Requirements and exact statement parts

- `ir-4.2_smt`: Include the following types of dynamic reconfiguration for [PARAM ir-04.02_odp.02] as part of the incident response capability: [PARAM ir-04.02_odp.01].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ir-4.2_smt — Include the following types of dynamic reconfiguration for [PARAM ir-04.02_odp.02] as part of the incident response capability: [PARAM ir-04.02_odp.01].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ir-04.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ir-04.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ir-4.2_smt` — For “Include the following types of dynamic reconfiguration for [PARAM ir-04.02_odp.02] as part of the incident response capability: [PARAM ir-04.02_odp.01].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ir-04.02_odp.01` — What approved value applies to **types of dynamic reconfiguration**? Record the value, scope, approving authority, and decision source.

  - Catalog context: types of dynamic reconfiguration for system components are defined;

- `ir-04.02_odp.02` — What approved value applies to **system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system components that require dynamic reconfiguration are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ir-4.2_obj` (ir-4.2_smt): [PARAM ir-04.02_odp.01] for [PARAM ir-04.02_odp.02] are included as part of the incident response capability.

#### EXAMINE — `ir-4.2_asm-examine`

- Incident response policy

- procedures addressing incident handling

- mechanisms supporting incident handling

- list of system components to be dynamically reconfigured as part of incident response capability

- system design documentation

- system configuration settings and associated documentation

- system audit records

- incident response plan

- system security plan

- other relevant documents or records

#### INTERVIEW — `ir-4.2_asm-interview`

- Organizational personnel with incident handling responsibilities

- organizational personnel with information security responsibilities

#### TEST — `ir-4.2_asm-test`

- Mechanisms that support and/or implement the dynamic reconfiguration of components as part of incident response

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ir-4.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ir-4`.

- Catalog relationship **related**: `ac-2`.

- Catalog relationship **related**: `ac-4`.

- Catalog relationship **related**: `cm-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
