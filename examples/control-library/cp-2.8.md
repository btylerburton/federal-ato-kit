---
title: "CP-2.8 \u2014 Identify Critical Assets"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-2.8 — Identify Critical Assets

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations may choose to identify critical assets as part of criticality analysis, business continuity planning, or business impact analyses. Organizations identify critical system assets so that additional controls can be employed (beyond the controls routinely implemented) to help ensure that organizational mission and business functions can continue to be conducted during contingency operations. The identification of critical information assets also facilitates the prioritization of organizational resources. Critical system assets include technical and operational aspects. Technical aspects include system components, information technology services, information technology products, and mechanisms. Operational aspects include procedures (i.e., manually executed operations) and personnel (i.e., individuals operating technical controls and/or executing manual procedures). Organizational program protection plans can assist in identifying critical assets. If critical assets are resident within or supported by external service providers, organizations consider implementing CP-2(7) (catalog reference: `#cp-2.7`) as a control enhancement.

### Requirements and exact statement parts

- `cp-2.8_smt`: Identify critical system assets supporting [PARAM cp-02.08_odp] mission and business functions.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-2.8_smt — Identify critical system assets supporting [PARAM cp-02.08_odp] mission and business functions.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cp-02.08_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cp-2.8_smt` — For “Identify critical system assets supporting [PARAM cp-02.08_odp] mission and business functions.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cp-02.08_odp` — What approved value applies to **selection; choose one from: all; essential**? Record the value, scope, approving authority, and decision source.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-2.8_obj` (cp-2.8_smt): critical system assets supporting [PARAM cp-02.08_odp] mission and business functions are identified.

#### EXAMINE — `cp-2.8_asm-examine`

- Contingency planning policy

- procedures addressing contingency operations for the system

- contingency plan

- business impact assessment

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-2.8_asm-interview`

- Organizational personnel with contingency planning and plan implementation responsibilities

- organizational personnel with knowledge of requirements for mission and business functions

- organizational personnel with information security responsibilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-2.8`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cp-2`.

- Catalog relationship **related**: `cm-8`.

- Catalog relationship **related**: `ra-9`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
