---
title: "AC-3.9 \u2014 Controlled Release"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-3.9 — Controlled Release

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations can only directly protect information when it resides within the system. Additional controls may be needed to ensure that organizational information is adequately protected once it is transmitted outside of the system. In situations where the system is unable to determine the adequacy of the protections provided by external entities, as a mitigation measure, organizations procedurally determine whether the external systems are providing adequate controls. The means used to determine the adequacy of controls provided by external systems include conducting periodic assessments (inspections/tests), establishing agreements between the organization and its counterpart organizations, or some other process. The means used by external entities to protect the information received need not be the same as those used by the organization, but the means employed are sufficient to provide consistent adjudication of the security and privacy policy to protect the information and individuals’ privacy.

Controlled release of information requires systems to implement technical or procedural means to validate the information prior to releasing it to external systems. For example, if the system passes information to a system controlled by another organization, technical means are employed to validate that the security and privacy attributes associated with the exported information are appropriate for the receiving system. Alternatively, if the system passes information to a printer in organization-controlled space, procedural means can be employed to ensure that only authorized individuals gain access to the printer.

### Requirements and exact statement parts

- `ac-3.9_smt`: Release information outside of the system only if:

- `ac-3.9_smt.a`: The receiving [PARAM ac-03.09_odp.01] provides [PARAM ac-03.09_odp.02] ; and

- `ac-3.9_smt.b`: [PARAM ac-03.09_odp.03] are used to validate the appropriateness of the information designated for release.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-3.9_smt — Release information outside of the system only if:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.9_smt.a — The receiving [PARAM ac-03.09_odp.01] provides [PARAM ac-03.09_odp.02] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ac-3.9_smt.b — [PARAM ac-03.09_odp.03] are used to validate the appropriateness of the information designated for release.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-03.09_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-03.09_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-03.09_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-3.9_smt` — For “Release information outside of the system only if:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.9_smt.a` — For “The receiving [PARAM ac-03.09_odp.01] provides [PARAM ac-03.09_odp.02] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ac-3.9_smt.b` — For “[PARAM ac-03.09_odp.03] are used to validate the appropriateness of the information designated for release.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-03.09_odp.01` — What approved value applies to **system or system component**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the outside system or system component to which to release information is defined;

- `ac-03.09_odp.02` — What approved value applies to **controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controls to be provided by the outside system or system component (defined in AC-03(09)_ODP[01]) are defined;

- `ac-03.09_odp.03` — What approved value applies to **controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controls used to validate appropriateness of information to be released are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-3.9_obj.a` (ac-3.9_smt.a): information is released outside of the system only if the receiving [PARAM ac-03.09_odp.01] provides [PARAM ac-03.09_odp.02];

- `ac-3.9_obj.b` (ac-3.9_smt.b): information is released outside of the system only if [PARAM ac-03.09_odp.03] are used to validate the appropriateness of the information designated for release.

#### EXAMINE — `ac-3.9_asm-examine`

- Access control policy

- procedures addressing access enforcement

- system design documentation

- system configuration settings and associated documentation

- list of security and privacy safeguards provided by receiving system or system components

- list of security and privacy safeguards validating appropriateness of information designated for release

- system audit records

- results of period assessments (inspections/tests) of the external system

- information sharing agreements

- memoranda of understanding

- acquisitions/contractual agreements

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ac-3.9_asm-interview`

- Organizational personnel with access enforcement responsibilities

- system/network administrators

- organizational personnel with information security and privacy responsibilities

- organizational personnel with responsibility for acquisitions/contractual agreements

- legal counsel

- system developers

#### TEST — `ac-3.9_asm-test`

- Mechanisms implementing access enforcement functions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-3.9`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-3`.

- Catalog relationship **related**: `ca-3`.

- Catalog relationship **related**: `pt-7`.

- Catalog relationship **related**: `pt-8`.

- Catalog relationship **related**: `sa-9`.

- Catalog relationship **related**: `sc-16`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
