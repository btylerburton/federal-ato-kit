---
title: "MA-5.2 \u2014 Security Clearances for Classified Systems"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-5.2 — Security Clearances for Classified Systems

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Personnel who conduct maintenance on organizational systems may be exposed to classified information during the course of their maintenance activities. To mitigate the inherent risk of such exposure, organizations use maintenance personnel that are cleared (i.e., possess security clearances) to the classification level of the information stored on the system.

### Requirements and exact statement parts

- `ma-5.2_smt`: Verify that personnel performing maintenance and diagnostic activities on a system processing, storing, or transmitting classified information possess security clearances and formal access approvals for at least the highest classification level and for compartments of information on the system.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-5.2_smt — Verify that personnel performing maintenance and diagnostic activities on a system processing, storing, or transmitting classified information possess security clearances and formal access approvals for at least the highest classification level and for compartments of information on the system.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ma-5.2_smt` — For “Verify that personnel performing maintenance and diagnostic activities on a system processing, storing, or transmitting classified information possess security clearances and formal access approvals for at least the highest classification level and for compartments of information on the system.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-5.2_obj-1` (ma-5.2_smt): personnel performing maintenance and diagnostic activities on a system processing, storing, or transmitting classified information possess security clearances for at least the highest classification level and for compartments of information on the system;

- `ma-5.2_obj-2` (ma-5.2_smt): personnel performing maintenance and diagnostic activities on a system processing, storing, or transmitting classified information possess formal access approvals for at least the highest classification level and for compartments of information on the system.

#### EXAMINE — `ma-5.2_asm-examine`

- Maintenance policy

- procedures addressing maintenance personnel

- personnel records

- maintenance records

- access control records

- access credentials

- access authorizations

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-5.2_asm-interview`

- Organizational personnel with system maintenance responsibilities

- organizational personnel with personnel security responsibilities

- organizational personnel with physical access control responsibilities

- organizational personnel with information security responsibilities

#### TEST — `ma-5.2_asm-test`

- Organizational processes for managing security clearances for maintenance personnel

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-5.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ma-5`.

- Catalog relationship **related**: `ps-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
