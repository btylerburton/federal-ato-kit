---
title: "SR-9.1 \u2014 Multiple Stages of System Development Life Cycle"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SR-9.1 — Multiple Stages of System Development Life Cycle

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The system development life cycle includes research and development, design, manufacturing, acquisition, delivery, integration, operations and maintenance, and disposal. Organizations use a combination of hardware and software techniques for tamper resistance and detection. Organizations use obfuscation and self-checking to make reverse engineering and modifications more difficult, time-consuming, and expensive for adversaries. The customization of systems and system components can make substitutions easier to detect and therefore limit damage.

### Requirements and exact statement parts

- `sr-9.1_smt`: Employ anti-tamper technologies, tools, and techniques throughout the system development life cycle.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sr-9.1_smt — Employ anti-tamper technologies, tools, and techniques throughout the system development life cycle.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sr-9.1_smt` — For “Employ anti-tamper technologies, tools, and techniques throughout the system development life cycle.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sr-9.1_obj` (sr-9.1_smt): anti-tamper technologies, tools, and techniques are employed throughout the system development life cycle.

#### EXAMINE — `sr-9.1_asm-examine`

- Supply chain risk management policy and procedures

- supply chain risk management plan

- system and services acquisition policy

- procedures addressing tamper resistance and detection

- tamper protection program documentation

- tamper protection tools and techniques documentation

- tamper resistance and detection tools (technologies) and techniques documentation

- system development life cycle documentation

- procedures addressing supply chain protection

- system development life cycle procedures

- acquisition documentation

- service level agreements

- acquisition contracts for the system, system component, or system service

- inter-organizational agreements and procedures

- system security plan

- other relevant documents or records

#### INTERVIEW — `sr-9.1_asm-interview`

- Organizational personnel with system and services acquisition responsibilities

- organizational personnel with information security responsibilities

- organizational personnel with supply chain risk management responsibilities

- organizational personnel with SDLC responsibilities

#### TEST — `sr-9.1_asm-test`

- Organizational processes for employing anti-tamper technologies

- mechanisms supporting and/or implementing anti-tamper technologies

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sr-9.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sr-9`.

- Catalog relationship **related**: `sa-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
