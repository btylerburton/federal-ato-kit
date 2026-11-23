---
title: "AU-5.4 \u2014 Shutdown on Failure"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AU-5.4 — Shutdown on Failure

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations determine the types of audit logging failures that can trigger automatic system shutdowns or degraded operations. Because of the importance of ensuring mission and business continuity, organizations may determine that the nature of the audit logging failure is not so severe that it warrants a complete shutdown of the system supporting the core organizational mission and business functions. In those instances, partial system shutdowns or operating in a degraded mode with reduced capability may be viable alternatives.

### Requirements and exact statement parts

- `au-5.4_smt`: Invoke a [PARAM au-05.04_odp.01] in the event of [PARAM au-05.04_odp.02] , unless an alternate audit logging capability exists.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for au-5.4_smt — Invoke a [PARAM au-05.04_odp.01] in the event of [PARAM au-05.04_odp.02] , unless an alternate audit logging capability exists.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter au-05.04_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter au-05.04_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `au-5.4_smt` — For “Invoke a [PARAM au-05.04_odp.01] in the event of [PARAM au-05.04_odp.02] , unless an alternate audit logging capability exists.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `au-05.04_odp.01` — What approved value applies to **selection; choose one-or-more from: full system shutdown; partial system shutdown; degraded operational mode with limited mission or business functionality available**? Record the value, scope, approving authority, and decision source.

- `au-05.04_odp.02` — What approved value applies to **audit logging failures**? Record the value, scope, approving authority, and decision source.

  - Catalog context: audit logging failures that trigger a change in operational mode are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `au-5.4_obj` (au-5.4_smt): [PARAM au-05.04_odp.01] is/are invoked in the event of [PARAM au-05.04_odp.02] , unless an alternate audit logging capability exists.

#### EXAMINE — `au-5.4_asm-examine`

- Audit and accountability policy

- procedures addressing response to audit processing failures

- system design documentation

- system security plan

- privacy plan

- system configuration settings and associated documentation

- system audit records

- other relevant documents or records

#### INTERVIEW — `au-5.4_asm-interview`

- Organizational personnel with audit and accountability responsibilities

- organizational personnel with information security and privacy responsibilities

- system/network administrators

- system developers

#### TEST — `au-5.4_asm-test`

- System capability invoking system shutdown or degraded operational mode in the event of an audit processing failure

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `au-5.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `au-5`.

- Catalog relationship **related**: `au-15`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
