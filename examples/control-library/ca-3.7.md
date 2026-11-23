---
title: "CA-3.7 \u2014 Transitive Information Exchanges"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CA-3.7 — Transitive Information Exchanges

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Transitive or "downstream" information exchanges are information exchanges between the system or systems with which the organizational system exchanges information and other systems. For mission-essential systems, services, and applications, including high value assets, it is necessary to identify such information exchanges. The transparency of the controls or protection measures in place in such downstream systems connected directly or indirectly to organizational systems is essential to understanding the security and privacy risks resulting from those information exchanges. Organizational systems can inherit risk from downstream systems through transitive connections and information exchanges, which can make the organizational systems more susceptible to threats, hazards, and adverse impacts.

### Requirements and exact statement parts

- `ca-3.7_smt`: Statement grouping; see child parts.

- `ca-3.7_smt.a`: Identify transitive (downstream) information exchanges with other systems through the systems identified in CA-3a (catalog reference: `#ca-3_smt.a`) ; and

- `ca-3.7_smt.b`: Take measures to ensure that transitive (downstream) information exchanges cease when the controls on identified transitive (downstream) systems cannot be verified or validated.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ca-3.7_smt.a — Identify transitive (downstream) information exchanges with other systems through the systems identified in CA-3a (catalog reference: `#ca-3_smt.a`) ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ca-3.7_smt.b — Take measures to ensure that transitive (downstream) information exchanges cease when the controls on identified transitive (downstream) systems cannot be verified or validated.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ca-3.7_smt.a` — For “Identify transitive (downstream) information exchanges with other systems through the systems identified in CA-3a (catalog reference: `#ca-3_smt.a`) ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ca-3.7_smt.b` — For “Take measures to ensure that transitive (downstream) information exchanges cease when the controls on identified transitive (downstream) systems cannot be verified or validated.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ca-3.7_obj.a` (ca-3.7_smt.a): transitive (downstream) information exchanges with other systems through the systems identified in CA-03a are identified;

- `ca-3.7_obj.b` (ca-3.7_smt.b): measures are taken to ensure that transitive (downstream) information exchanges cease when the controls on identified transitive (downstream) systems cannot be verified or validated.

#### EXAMINE — `ca-3.7_asm-examine`

- Access control policy

- procedures addressing system connections

- system and communications protection policy

- system interconnection agreements

- information exchange security agreements

- memoranda of understanding or agreements

- service level agreements

- non-disclosure agreements

- system design documentation

- system configuration settings and associated documentation

- control assessment report

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ca-3.7_asm-interview`

- Organizational personnel with responsibilities for managing connections to external systems

- network administrators

- organizational personnel with information security and privacy responsibilities

#### TEST — `ca-3.7_asm-test`

- Mechanisms implementing restrictions on external system connections

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ca-3.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ca-3`.

- Catalog relationship **related**: `sc-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
