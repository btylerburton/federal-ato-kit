---
title: "MP-6.8 \u2014 Remote Purging or Wiping of Information"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MP-6.8 — Remote Purging or Wiping of Information

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Remote purging or wiping of information protects information on organizational systems and system components if systems or components are obtained by unauthorized individuals. Remote purge or wipe commands require strong authentication to help mitigate the risk of unauthorized individuals purging or wiping the system, component, or device. The purge or wipe function can be implemented in a variety of ways, including by overwriting data or information multiple times or by destroying the key necessary to decrypt encrypted data.

### Requirements and exact statement parts

- `mp-6.8_smt`: Provide the capability to purge or wipe information from [PARAM mp-06.08_odp.01] [PARAM mp-06.08_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for mp-6.8_smt — Provide the capability to purge or wipe information from [PARAM mp-06.08_odp.01] [PARAM mp-06.08_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter mp-06.08_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-06.08_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter mp-06.08_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `mp-6.8_smt` — For “Provide the capability to purge or wipe information from [PARAM mp-06.08_odp.01] [PARAM mp-06.08_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `mp-06.08_odp.01` — What approved value applies to **systems or system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems or system components to purge or wipe information either remotely or under specific conditions are defined;

- `mp-06.08_odp.02` — What approved value applies to **selection; choose one from: remotely; under [PARAM mp-06.08_odp.03]**? Record the value, scope, approving authority, and decision source.

- `mp-06.08_odp.03` — What approved value applies to **conditions**? Record the value, scope, approving authority, and decision source.

  - Catalog context: conditions under which information is to be purged or wiped are defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `mp-6.8_obj` (mp-6.8_smt): the capability to purge or wipe information from [PARAM mp-06.08_odp.01] [PARAM mp-06.08_odp.02] is provided.

#### EXAMINE — `mp-6.8_asm-examine`

- System media protection policy

- procedures addressing media sanitization and disposal

- system design documentation

- system configuration settings and associated documentation

- authorization records

- media sanitization records

- audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `mp-6.8_asm-interview`

- Organizational personnel with system media sanitization responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `mp-6.8_asm-test`

- Organizational processes for purging/wiping media

- mechanisms supporting and/or implementing purge/wipe capabilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `mp-6.8`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `mp-6`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
