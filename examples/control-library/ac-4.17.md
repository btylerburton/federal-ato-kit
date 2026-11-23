---
title: "AC-4.17 \u2014 Domain Authentication"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4.17 — Domain Authentication

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Attribution is a critical component of a security and privacy concept of operations. The ability to identify source and destination points for information flowing within systems allows the forensic reconstruction of events and encourages policy compliance by attributing policy violations to specific organizations or individuals. Successful domain authentication requires that system labels distinguish among systems, organizations, and individuals involved in preparing, sending, receiving, or disseminating information. Attribution also allows organizations to better maintain the lineage of personally identifiable information processing as it flows through systems and can facilitate consent tracking, as well as correction, deletion, or access requests from individuals.

### Requirements and exact statement parts

- `ac-4.17_smt`: Uniquely identify and authenticate source and destination points by [PARAM ac-04.17_odp] for information transfer.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4.17_smt — Uniquely identify and authenticate source and destination points by [PARAM ac-04.17_odp] for information transfer.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-04.17_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-4.17_smt` — For “Uniquely identify and authenticate source and destination points by [PARAM ac-04.17_odp] for information transfer.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-04.17_odp` — What approved value applies to **selection; choose one-or-more from: organization, system, application, service, individual**? Record the value, scope, approving authority, and decision source.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4.17_obj` (ac-4.17_smt): source and destination points are uniquely identified and authenticated by [PARAM ac-04.17_odp] for information transfer.

#### EXAMINE — `ac-4.17_asm-examine`

- Access control policy

- information flow control policies

- procedures addressing information flow enforcement

- procedures addressing source and destination domain identification and authentication

- system design documentation

- system configuration settings and associated documentation

- system audit records

- list of system labels

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ac-4.17_asm-interview`

- System/network administrators

- organizational personnel with information security and privacy responsibilities

- system developers

#### TEST — `ac-4.17_asm-test`

- Mechanisms implementing information flow enforcement policy

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4.17`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-4`.

- Catalog relationship **related**: `ia-2`.

- Catalog relationship **related**: `ia-3`.

- Catalog relationship **related**: `ia-9`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
