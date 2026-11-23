---
title: "SC-5.1 \u2014 Restrict Ability to Attack Other Systems"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-5.1 — Restrict Ability to Attack Other Systems

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Restricting the ability of individuals to launch denial-of-service attacks requires the mechanisms commonly used for such attacks to be unavailable. Individuals of concern include hostile insiders or external adversaries who have breached or compromised the system and are using it to launch a denial-of-service attack. Organizations can restrict the ability of individuals to connect and transmit arbitrary information on the transport medium (i.e., wired networks, wireless networks, spoofed Internet protocol packets). Organizations can also limit the ability of individuals to use excessive system resources. Protection against individuals having the ability to launch denial-of-service attacks may be implemented on specific systems or boundary devices that prohibit egress to potential target systems.

### Requirements and exact statement parts

- `sc-5.1_smt`: Restrict the ability of individuals to launch the following denial-of-service attacks against other systems: [PARAM sc-05.01_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-5.1_smt — Restrict the ability of individuals to launch the following denial-of-service attacks against other systems: [PARAM sc-05.01_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-05.01_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-5.1_smt` — For “Restrict the ability of individuals to launch the following denial-of-service attacks against other systems: [PARAM sc-05.01_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-05.01_odp` — What approved value applies to **denial-of-service attacks**? Record the value, scope, approving authority, and decision source.

  - Catalog context: denial-of-service attacks for which to restrict the ability of individuals to launch are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-5.1_obj` (sc-5.1_smt): the ability of individuals to launch [PARAM sc-05.01_odp] against other systems is restricted.

#### EXAMINE — `sc-5.1_asm-examine`

- System and communications protection policy

- procedures addressing denial-of-service protection

- system design documentation

- list of denial-of-service attacks launched by individuals against systems

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-5.1_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel with incident response responsibilities

- system developer

#### TEST — `sc-5.1_asm-test`

- Mechanisms restricting the ability to launch denial-of-service attacks against other systems

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-5.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sc-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
