---
title: "SC-2 \u2014 Separation of System and User Functionality"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-2 — Separation of System and User Functionality

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

System management functionality includes functions that are necessary to administer databases, network components, workstations, or servers. These functions typically require privileged user access. The separation of user functions from system management functions is physical or logical. Organizations may separate system management functions from user functions by using different computers, instances of operating systems, central processing units, or network addresses; by employing virtualization techniques; or some combination of these or other methods. Separation of system management functions from user functions includes web administrative interfaces that employ separate authentication methods for users of any other system resources. Separation of system and user functions may include isolating administrative interfaces on different domains and with additional access controls. The separation of system and user functionality can be achieved by applying the systems security engineering design principles in SA-8 (catalog reference: `#sa-8`) , including SA-8(1) (catalog reference: `#sa-8.1`), SA-8(3) (catalog reference: `#sa-8.3`), SA-8(4) (catalog reference: `#sa-8.4`), SA-8(10) (catalog reference: `#sa-8.10`), SA-8(12) (catalog reference: `#sa-8.12`), SA-8(13) (catalog reference: `#sa-8.13`), SA-8(14) (catalog reference: `#sa-8.14`) , and SA-8(18) (catalog reference: `#sa-8.18`).

### Requirements and exact statement parts

- `sc-2_smt`: Separate user functionality, including user interface services, from system management functionality.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-2_smt — Separate user functionality, including user interface services, from system management functionality.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sc-2_smt` — For “Separate user functionality, including user interface services, from system management functionality.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-2_obj` (sc-2_smt): user functionality, including user interface services, is separated from system management functionality.

#### EXAMINE — `sc-2_asm-examine`

- System and communications protection policy

- procedures addressing application partitioning

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-2_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developer

#### TEST — `sc-2_asm-test`

- Separation of user functionality from system management functionality

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-2`. The library index records the exact source revision and hash.

- Catalog relationship **related**: `ac-6`.

- Catalog relationship **related**: `sa-4`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sc-3`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `sc-22`.

- Catalog relationship **related**: `sc-32`.

- Catalog relationship **related**: `sc-39`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
