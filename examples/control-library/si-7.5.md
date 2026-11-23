---
title: "SI-7.5 \u2014 Automated Response to Integrity Violations"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-7.5 — Automated Response to Integrity Violations

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations may define different integrity-checking responses by type of information, specific information, or a combination of both. Types of information include firmware, software, and user data. Specific information includes boot firmware for certain types of machines. The automatic implementation of controls within organizational systems includes reversing the changes, halting the system, or triggering audit alerts when unauthorized modifications to critical security files occur.

### Requirements and exact statement parts

- `si-7.5_smt`: Automatically [PARAM si-07.05_odp.01] when integrity violations are discovered.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-7.5_smt — Automatically [PARAM si-07.05_odp.01] when integrity violations are discovered.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-07.05_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-07.05_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-7.5_smt` — For “Automatically [PARAM si-07.05_odp.01] when integrity violations are discovered.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-07.05_odp.01` — What approved value applies to **selection; choose one-or-more from: shut down the system; restart the system; implement [PARAM si-07.05_odp.02]**? Record the value, scope, approving authority, and decision source.

- `si-07.05_odp.02` — What approved value applies to **controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controls to be implemented automatically when integrity violations are discovered are defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-7.5_obj` (si-7.5_smt): [PARAM si-07.05_odp.01] are automatically performed when integrity violations are discovered.

#### EXAMINE — `si-7.5_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing software, firmware, and information integrity

- system design documentation

- system configuration settings and associated documentation

- integrity verification tools and associated documentation

- records of integrity scans

- records of integrity checks and responses to integrity violations

- audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-7.5_asm-interview`

- Organizational personnel responsible for software, firmware, and/or information integrity

- organizational personnel with information security responsibilities

- system/network administrators

- system developer

#### TEST — `si-7.5_asm-test`

- Software, firmware, and information integrity verification tools

- mechanisms providing an automated response to integrity violations

- mechanisms supporting and/or implementing security safeguards to be implemented when integrity violations are discovered

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-7.5`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `si-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
