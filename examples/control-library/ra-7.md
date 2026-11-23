---
title: "RA-7 \u2014 Risk Response"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# RA-7 — Risk Response

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations have many options for responding to risk including mitigating risk by implementing new controls or strengthening existing controls, accepting risk with appropriate justification or rationale, sharing or transferring risk, or avoiding risk. The risk tolerance of the organization influences risk response decisions and actions. Risk response addresses the need to determine an appropriate response to risk before generating a plan of action and milestones entry. For example, the response may be to accept risk or reject risk, or it may be possible to mitigate the risk immediately so that a plan of action and milestones entry is not needed. However, if the risk response is to mitigate the risk, and the mitigation cannot be completed immediately, a plan of action and milestones entry is generated.

### Requirements and exact statement parts

- `ra-7_smt`: Respond to findings from security and privacy assessments, monitoring, and audits in accordance with organizational risk tolerance.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ra-7_smt — Respond to findings from security and privacy assessments, monitoring, and audits in accordance with organizational risk tolerance.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ra-7_smt` — For “Respond to findings from security and privacy assessments, monitoring, and audits in accordance with organizational risk tolerance.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ra-7_obj-1` (ra-7_smt): findings from security assessments are responded to in accordance with organizational risk tolerance;

- `ra-7_obj-2` (ra-7_smt): findings from privacy assessments are responded to in accordance with organizational risk tolerance;

- `ra-7_obj-3` (ra-7_smt): findings from monitoring are responded to in accordance with organizational risk tolerance;

- `ra-7_obj-4` (ra-7_smt): findings from audits are responded to in accordance with organizational risk tolerance.

#### EXAMINE — `ra-7_asm-examine`

- Risk assessment policy

- assessment reports

- audit records/event logs

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ra-7_asm-interview`

- Organizational personnel with assessment and auditing responsibilities

- system/network administrators

- organizational personnel with security and privacy responsibilities

#### TEST — `ra-7_asm-test`

- Organizational processes for assessments and audits

- mechanisms/tools supporting and/or implementing assessments and auditing

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ra-7`. The library index records the exact source revision and hash.

- [FIPS 199](https://doi.org/10.6028/NIST.FIPS.199)

- [FIPS 200](https://doi.org/10.6028/NIST.FIPS.200)

- [SP 800-30](https://doi.org/10.6028/NIST.SP.800-30r1)

- [SP 800-37](https://doi.org/10.6028/NIST.SP.800-37r2)

- [SP 800-39](https://doi.org/10.6028/NIST.SP.800-39)

- [SP 800-160-1](https://doi.org/10.6028/NIST.SP.800-160v1)

- Catalog relationship **related**: `ca-5`.

- Catalog relationship **related**: `ir-9`.

- Catalog relationship **related**: `pm-4`.

- Catalog relationship **related**: `pm-28`.

- Catalog relationship **related**: `ra-2`.

- Catalog relationship **related**: `ra-3`.

- Catalog relationship **related**: `sr-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
