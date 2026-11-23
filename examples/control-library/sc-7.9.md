---
title: "SC-7.9 \u2014 Restrict Threatening Outgoing Communications Traffic"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-7.9 — Restrict Threatening Outgoing Communications Traffic

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Detecting outgoing communications traffic from internal actions that may pose threats to external systems is known as extrusion detection. Extrusion detection is carried out within the system at managed interfaces. Extrusion detection includes the analysis of incoming and outgoing communications traffic while searching for indications of internal threats to the security of external systems. Internal threats to external systems include traffic indicative of denial-of-service attacks, traffic with spoofed source addresses, and traffic that contains malicious code. Organizations have criteria to determine, update, and manage identified threats related to extrusion detection.

### Requirements and exact statement parts

- `sc-7.9_smt`: Statement grouping; see child parts.

- `sc-7.9_smt.a`: Detect and deny outgoing communications traffic posing a threat to external systems; and

- `sc-7.9_smt.b`: Audit the identity of internal users associated with denied communications.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-7.9_smt.a — Detect and deny outgoing communications traffic posing a threat to external systems; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sc-7.9_smt.b — Audit the identity of internal users associated with denied communications.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sc-7.9_smt.a` — For “Detect and deny outgoing communications traffic posing a threat to external systems; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sc-7.9_smt.b` — For “Audit the identity of internal users associated with denied communications.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-7.9_obj.a-1` (sc-7.9_smt.a): outgoing communications traffic posing a threat to external systems is detected;

- `sc-7.9_obj.a-2` (sc-7.9_smt.a): outgoing communications traffic posing a threat to external systems is denied;

- `sc-7.9_obj.b` (sc-7.9_smt.b): the identity of internal users associated with denied communications is audited.

#### EXAMINE — `sc-7.9_asm-examine`

- System and communications protection policy

- procedures addressing boundary protection

- system design documentation

- system hardware and software

- system architecture

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-7.9_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developer

- organizational personnel with boundary protection responsibilities

#### TEST — `sc-7.9_asm-test`

- Mechanisms implementing boundary protection capabilities

- mechanisms implementing the detection and denial of threatening outgoing communications traffic

- mechanisms implementing auditing of outgoing communications traffic

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-7.9`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sc-7`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `sc-5`.

- Catalog relationship **related**: `sc-38`.

- Catalog relationship **related**: `sc-44`.

- Catalog relationship **related**: `si-3`.

- Catalog relationship **related**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
