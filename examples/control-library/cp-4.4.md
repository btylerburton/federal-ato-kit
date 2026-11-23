---
title: "CP-4.4 \u2014 Full Recovery and Reconstitution"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CP-4.4 — Full Recovery and Reconstitution

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Recovery is executing contingency plan activities to restore organizational mission and business functions. Reconstitution takes place following recovery and includes activities for returning systems to fully operational states. Organizations establish a known state for systems that includes system state information for hardware, software programs, and data. Preserving system state information facilitates system restart and return to the operational mode of organizations with less disruption of mission and business processes.

### Requirements and exact statement parts

- `cp-4.4_smt`: Include a full recovery and reconstitution of the system to a known state as part of contingency plan testing.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for cp-4.4_smt — Include a full recovery and reconstitution of the system to a known state as part of contingency plan testing.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `cp-4.4_smt` — For “Include a full recovery and reconstitution of the system to a known state as part of contingency plan testing.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `cp-4.4_obj-1` (cp-4.4_smt): a full recovery of the system to a known state is included as part of contingency plan testing;

- `cp-4.4_obj-2` (cp-4.4_smt): a full reconstitution of the system to a known state is included as part of contingency plan testing.

#### EXAMINE — `cp-4.4_asm-examine`

- Contingency planning policy

- procedures addressing system recovery and reconstitution

- contingency plan

- contingency plan test documentation

- contingency plan test results

- system security plan

- other relevant documents or records

#### INTERVIEW — `cp-4.4_asm-interview`

- Organizational personnel with contingency plan testing responsibilities

- organizational personnel with system recovery and reconstitution responsibilities

- organizational personnel with information security responsibilities

#### TEST — `cp-4.4_asm-test`

- Organizational processes for contingency plan testing

- mechanisms supporting contingency plan testing

- mechanisms supporting recovery and reconstitution of the system

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `cp-4.4`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `cp-4`.

- Catalog relationship **related**: `cp-10`.

- Catalog relationship **related**: `sc-24`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
