---
title: "AU-4.1 \u2014 Transfer to Alternate Storage"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-4.1 — Transfer to Alternate Storage

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Audit log transfer, also known as off-loading, is a common process in systems with limited audit log storage capacity and thus supports availability of the audit logs. The initial audit log storage is only used in a transitory fashion until the system can communicate with the secondary or alternate system allocated to audit log storage, at which point the audit logs are transferred. Transferring audit logs to alternate storage is similar to AU-9(2) (catalog reference: `#au-9.2`) in that audit logs are transferred to a different entity. However, the purpose of selecting AU-9(2) (catalog reference: `#au-9.2`) is to protect the confidentiality and integrity of audit records. Organizations can select either control enhancement to obtain the benefit of increased audit log storage capacity and preserving the confidentiality, integrity, and availability of audit records and logs.

### Requirements and exact statement parts

- `au-4.1_smt`: Transfer audit logs [PARAM au-04.01_odp] to a different system, system component, or media other than the system or system component conducting the logging.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-4.1_smt — Transfer audit logs [PARAM au-04.01_odp] to a different system, system component, or media other than the system or system component conducting the logging.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-04.01_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-4.1_smt` — For “Transfer audit logs [PARAM au-04.01_odp] to a different system, system component, or media other than the system or system component conducting the logging.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-04.01_odp` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency of audit logs transferred to a different system, system component, or media other than the system or system component conducting the logging is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-4.1_obj` (au-4.1_smt): audit logs are transferred [PARAM au-04.01_odp] to a different system, system component, or media other than the system or system component conducting the logging.

#### EXAMINE — `au-4.1_asm-examine`

- Audit and accountability policy

- system security plan

- privacy plan

- procedures addressing audit storage capacity

- procedures addressing transfer of system audit records to secondary or alternate systems

- system design documentation

- system configuration settings and associated documentation

- logs of audit record transfers to secondary or alternate systems

- system audit records transferred to secondary or alternate systems

- other relevant documents or records

#### INTERVIEW — `au-4.1_asm-interview`

- Organizational personnel with audit storage capacity planning responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

#### TEST — `au-4.1_asm-test`

- Mechanisms supporting the transfer of audit records onto a different system

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-4.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `au-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
