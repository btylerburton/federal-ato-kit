---
title: "RA-2.1 \u2014 Impact-level Prioritization"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# RA-2.1 — Impact-level Prioritization

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations apply the "high-water mark" concept to each system categorized in accordance with FIPS 199 (catalog reference: `#628d22a1-6a11-4784-bc59-5cd9497b5445`) , resulting in systems designated as low impact, moderate impact, or high impact. Organizations that desire additional granularity in the system impact designations for risk-based decision-making, can further partition the systems into sub-categories of the initial system categorization. For example, an impact-level prioritization on a moderate-impact system can produce three new sub-categories: low-moderate systems, moderate-moderate systems, and high-moderate systems. Impact-level prioritization and the resulting sub-categories of the system give organizations an opportunity to focus their investments related to security control selection and the tailoring of control baselines in responding to identified risks. Impact-level prioritization can also be used to determine those systems that may be of heightened interest or value to adversaries or represent a critical loss to the federal enterprise, sometimes described as high value assets. For such high value assets, organizations may be more focused on complexity, aggregation, and information exchanges. Systems with high value assets can be prioritized by partitioning high-impact systems into low-high systems, moderate-high systems, and high-high systems. Alternatively, organizations can apply the guidance in CNSSI 1253 (catalog reference: `#4e4fbc93-333d-45e6-a875-de36b878b6b9`) for security objective-related categorization.

### Requirements and exact statement parts

- `ra-2.1_smt`: Conduct an impact-level prioritization of organizational systems to obtain additional granularity on system impact levels.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ra-2.1_smt — Conduct an impact-level prioritization of organizational systems to obtain additional granularity on system impact levels.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ra-2.1_smt` — For “Conduct an impact-level prioritization of organizational systems to obtain additional granularity on system impact levels.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ra-2.1_obj` (ra-2.1_smt): an impact-level prioritization of organizational systems is conducted to obtain additional granularity on system impact levels.

#### EXAMINE — `ra-2.1_asm-examine`

- Risk assessment policy

- security and privacy planning policy and procedures

- procedures addressing security categorization of organizational information and systems

- security categorization documentation

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ra-2.1_asm-interview`

- Organizational personnel with security categorization and risk assessment responsibilities

- organizational personnel with security and privacy responsibilities

#### TEST — `ra-2.1_asm-test`

- Organizational processes for security categorization

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ra-2.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ra-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
