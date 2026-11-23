---
title: "CP-9.1 \u2014 Testing for Reliability and Integrity"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-9.1 — Testing for Reliability and Integrity

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations need assurance that backup information can be reliably retrieved. Reliability pertains to the systems and system components where the backup information is stored, the operations used to retrieve the information, and the integrity of the information being retrieved. Independent and specialized tests can be used for each of the aspects of reliability. For example, decrypting and transporting (or transmitting) a random sample of backup files from the alternate storage or backup site and comparing the information to the same information at the primary processing site can provide such assurance.

### Requirements and exact statement parts

- `cp-9.1_smt`: Test backup information [PARAM cp-9.1_prm_1] to verify media reliability and information integrity.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-9.1_smt — Test backup information [PARAM cp-9.1_prm_1] to verify media reliability and information integrity.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter cp-9.1_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-09.01_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter cp-09.01_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `cp-9.1_smt` — For “Test backup information [PARAM cp-9.1_prm_1] to verify media reliability and information integrity.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `cp-9.1_prm_1` — What approved value applies to **organization-defined frequency**? Record the value, scope, approving authority, and decision source.

- `cp-09.01_odp.01` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to test backup information for media reliability is defined;

- `cp-09.01_odp.02` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to test backup information for information integrity is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-9.1_obj-1` (cp-9.1_smt): backup information is tested [PARAM cp-09.01_odp.01] to verify media reliability;

- `cp-9.1_obj-2` (cp-9.1_smt): backup information is tested [PARAM cp-09.01_odp.02] to verify information integrity.

#### EXAMINE — `cp-9.1_asm-examine`

- Contingency planning policy

- procedures addressing system backup

- contingency plan

- system backup test results

- contingency plan test documentation

- contingency plan test results

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-9.1_asm-interview`

- Organizational personnel with system backup responsibilities

- organizational personnel with information security responsibilities

#### TEST — `cp-9.1_asm-test`

- Organizational processes for conducting system backups

- mechanisms supporting and/or implementing system backups

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-9.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cp-9`.

- Catalog relationship **related**: `cp-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
