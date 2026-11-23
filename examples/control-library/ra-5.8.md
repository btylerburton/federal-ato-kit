---
title: "RA-5.8 \u2014 Review Historic Audit Logs"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# RA-5.8 — Review Historic Audit Logs

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Reviewing historic audit logs to determine if a recently detected vulnerability in a system has been previously exploited by an adversary can provide important information for forensic analyses. Such analyses can help identify, for example, the extent of a previous intrusion, the trade craft employed during the attack, organizational information exfiltrated or modified, mission or business capabilities affected, and the duration of the attack.

### Requirements and exact statement parts

- `ra-5.8_smt`: Review historic audit logs to determine if a vulnerability identified in a [PARAM ra-05.08_odp.01] has been previously exploited within an [PARAM ra-05.08_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ra-5.8_smt — Review historic audit logs to determine if a vulnerability identified in a [PARAM ra-05.08_odp.01] has been previously exploited within an [PARAM ra-05.08_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ra-05.08_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ra-05.08_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ra-5.8_smt` — For “Review historic audit logs to determine if a vulnerability identified in a [PARAM ra-05.08_odp.01] has been previously exploited within an [PARAM ra-05.08_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ra-05.08_odp.01` — What approved value applies to **system**? Record the value, scope, approving authority, and decision source.

  - Catalog context: a system whose historic audit logs are to be reviewed is defined;

- `ra-05.08_odp.02` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: a time period for a potential previous exploit of a system is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ra-5.8_obj` (ra-5.8_smt): historic audit logs are reviewed to determine if a vulnerability identified in a [PARAM ra-05.08_odp.01] has been previously exploited within [PARAM ra-05.08_odp.02].

#### EXAMINE — `ra-5.8_asm-examine`

- Risk assessment policy

- procedures addressing vulnerability scanning

- audit logs

- records of audit log reviews

- vulnerability scanning results

- patch and vulnerability management records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ra-5.8_asm-interview`

- Organizational personnel with vulnerability scanning responsibilities

- organizational personnel with vulnerability scan analysis responsibilities

- organizational personnel with audit record review responsibilities

- system/network administrators

- organizational personnel with security responsibilities

#### TEST — `ra-5.8_asm-test`

- Organizational processes for vulnerability scanning

- organizational process for audit record review and response

- mechanisms/tools supporting and/or implementing vulnerability scanning

- mechanisms supporting and/or implementing audit record review

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ra-5.8`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ra-5`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-11`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
