---
title: "CP-9.6 \u2014 Redundant Secondary System"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-9.6 — Redundant Secondary System

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The effect of system backup can be achieved by maintaining a redundant secondary system that mirrors the primary system, including the replication of information. If this type of redundancy is in place and there is sufficient geographic separation between the two systems, the secondary system can also serve as the alternate processing site.

### Requirements and exact statement parts

- `cp-9.6_smt`: Conduct system backup by maintaining a redundant secondary system that is not collocated with the primary system and that can be activated without loss of information or disruption to operations.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-9.6_smt — Conduct system backup by maintaining a redundant secondary system that is not collocated with the primary system and that can be activated without loss of information or disruption to operations.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `cp-9.6_smt` — For “Conduct system backup by maintaining a redundant secondary system that is not collocated with the primary system and that can be activated without loss of information or disruption to operations.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-9.6_obj-1` (cp-9.6_smt): system backup is conducted by maintaining a redundant secondary system that is not collocated with the primary system;

- `cp-9.6_obj-2` (cp-9.6_smt): system backup is conducted by maintaining a redundant secondary system that can be activated without loss of information or disruption to operations.

#### EXAMINE — `cp-9.6_asm-examine`

- Contingency planning policy

- procedures addressing system backup

- contingency plan

- system backup test results

- contingency plan test results

- contingency plan test documentation

- redundant secondary system for system backups

- location(s) of redundant secondary backup system(s)

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-9.6_asm-interview`

- Organizational personnel with system backup responsibilities

- organizational personnel with information security responsibilities

- organizational personnel with responsibility for the redundant secondary system

#### TEST — `cp-9.6_asm-test`

- Organizational processes for maintaining redundant secondary systems

- mechanisms supporting and/or implementing system backups

- mechanisms supporting and/or implementing information transfer to a redundant secondary system

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-9.6`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cp-9`.

- Catalog relationship **related**: `cp-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
