---
title: "MA-3 \u2014 Maintenance Tools"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-3 — Maintenance Tools

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Approving, controlling, monitoring, and reviewing maintenance tools address security-related issues associated with maintenance tools that are not within system authorization boundaries and are used specifically for diagnostic and repair actions on organizational systems. Organizations have flexibility in determining roles for the approval of maintenance tools and how that approval is documented. A periodic review of maintenance tools facilitates the withdrawal of approval for outdated, unsupported, irrelevant, or no-longer-used tools. Maintenance tools can include hardware, software, and firmware items and may be pre-installed, brought in with maintenance personnel on media, cloud-based, or downloaded from a website. Such tools can be vehicles for transporting malicious code, either intentionally or unintentionally, into a facility and subsequently into systems. Maintenance tools can include hardware and software diagnostic test equipment and packet sniffers. The hardware and software components that support maintenance and are a part of the system (including the software implementing utilities such as "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch) are not addressed by maintenance tools.

### Requirements and exact statement parts

- `ma-3_smt`: Statement grouping; see child parts.

- `ma-3_smt.a`: Approve, control, and monitor the use of system maintenance tools; and

- `ma-3_smt.b`: Review previously approved system maintenance tools [PARAM ma-03_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-3_smt.a — Approve, control, and monitor the use of system maintenance tools; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-3_smt.b — Review previously approved system maintenance tools [PARAM ma-03_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ma-03_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ma-3_smt.a` — For “Approve, control, and monitor the use of system maintenance tools; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-3_smt.b` — For “Review previously approved system maintenance tools [PARAM ma-03_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ma-03_odp` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to review previously approved system maintenance tools is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-3_obj.a-1` (ma-3_smt.a): the use of system maintenance tools is approved;

- `ma-3_obj.a-2` (ma-3_smt.a): the use of system maintenance tools is controlled;

- `ma-3_obj.a-3` (ma-3_smt.a): the use of system maintenance tools is monitored;

- `ma-3_obj.b` (ma-3_smt.b): previously approved system maintenance tools are reviewed [PARAM ma-03_odp].

#### EXAMINE — `ma-3_asm-examine`

- Maintenance policy

- procedures addressing system maintenance tools

- system maintenance tools and associated documentation

- maintenance records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-3_asm-interview`

- Organizational personnel with system maintenance responsibilities

- organizational personnel with information security responsibilities

#### TEST — `ma-3_asm-test`

- Organizational processes for approving, controlling, and monitoring maintenance tools

- mechanisms supporting and/or implementing the approval, control, and/or monitoring of maintenance tools

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-3`. The library index records the exact source revision and hash.

- [SP 800-88](https://doi.org/10.6028/NIST.SP.800-88r1)

- Catalog relationship **related**: `ma-2`.

- Catalog relationship **related**: `pe-16`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
