---
title: "CP-9.3 \u2014 Separate Storage for Critical Information"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-9.3 — Separate Storage for Critical Information

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Separate storage for critical information applies to all critical information regardless of the type of backup storage media. Critical system software includes operating systems, middleware, cryptographic key management systems, and intrusion detection systems. Security-related information includes inventories of system hardware, software, and firmware components. Alternate storage sites, including geographically distributed architectures, serve as separate storage facilities for organizations. Organizations may provide separate storage by implementing automated backup processes at alternative storage sites (e.g., data centers). The General Services Administration (GSA) establishes standards and specifications for security and fire rated containers.

### Requirements and exact statement parts

- `cp-9.3_smt`: Store backup copies of [PARAM cp-09.03_odp] in a separate facility or in a fire rated container that is not collocated with the operational system.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-9.3_smt — Store backup copies of [PARAM cp-09.03_odp] in a separate facility or in a fire rated container that is not collocated with the operational system.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cp-09.03_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cp-9.3_smt` — For “Store backup copies of [PARAM cp-09.03_odp] in a separate facility or in a fire rated container that is not collocated with the operational system.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cp-09.03_odp` — What approved value applies to **critical system software and other security-related information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: critical system software and other security-related information backups to be stored in a separate facility are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-9.3_obj` (cp-9.3_smt): backup copies of [PARAM cp-09.03_odp] are stored in a separate facility or in a fire rated container that is not collocated with the operational system.

#### EXAMINE — `cp-9.3_asm-examine`

- Contingency planning policy

- procedures addressing system backup

- contingency plan

- backup storage location(s)

- system backup configurations and associated documentation

- system backup logs or records

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-9.3_asm-interview`

- Organizational personnel with contingency planning and plan implementation responsibilities

- organizational personnel with system backup responsibilities

- organizational personnel with information security responsibilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-9.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cp-9`.

- Catalog relationship **related**: `cm-2`.

- Catalog relationship **related**: `cm-6`.

- Catalog relationship **related**: `cm-8`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
