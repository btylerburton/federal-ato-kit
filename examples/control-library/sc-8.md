---
title: "SC-8 \u2014 Transmission Confidentiality and Integrity"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-8 — Transmission Confidentiality and Integrity

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Protecting the confidentiality and integrity of transmitted information applies to internal and external networks as well as any system components that can transmit information, including servers, notebook computers, desktop computers, mobile devices, printers, copiers, scanners, facsimile machines, and radios. Unprotected communication paths are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of information can be accomplished by physical or logical means. Physical protection can be achieved by using protected distribution systems. A protected distribution system is a wireline or fiber-optics telecommunications system that includes terminals and adequate electromagnetic, acoustical, electrical, and physical controls to permit its use for the unencrypted transmission of classified information. Logical protection can be achieved by employing encryption techniques.

Organizations that rely on commercial providers who offer transmission services as commodity services rather than as fully dedicated services may find it difficult to obtain the necessary assurances regarding the implementation of needed controls for transmission confidentiality and integrity. In such situations, organizations determine what types of confidentiality or integrity services are available in standard, commercial telecommunications service packages. If it is not feasible to obtain the necessary controls and assurances of control effectiveness through appropriate contracting vehicles, organizations can implement appropriate compensating controls.

### Requirements and exact statement parts

- `sc-8_smt`: Protect the [PARAM sc-08_odp] of transmitted information.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-8_smt — Protect the [PARAM sc-08_odp] of transmitted information.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-08_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-8_smt` — For “Protect the [PARAM sc-08_odp] of transmitted information.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-08_odp` — What approved value applies to **selection; choose one-or-more from: confidentiality; integrity**? Record the value, scope, approving authority, and decision source.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-8_obj` (sc-8_smt): the [PARAM sc-08_odp] of transmitted information is/are protected.

#### EXAMINE — `sc-8_asm-examine`

- System and communications protection policy

- procedures addressing transmission confidentiality and integrity

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-8_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developer

#### TEST — `sc-8_asm-test`

- Mechanisms supporting and/or implementing transmission confidentiality and/or integrity

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-8`. The library index records the exact source revision and hash.

- [FIPS 140-3](https://doi.org/10.6028/NIST.FIPS.140-3)

- [FIPS 197](https://doi.org/10.6028/NIST.FIPS.197)

- [SP 800-52](https://doi.org/10.6028/NIST.SP.800-52r2)

- [SP 800-77](https://doi.org/10.6028/NIST.SP.800-77r1)

- [SP 800-81-2](https://doi.org/10.6028/NIST.SP.800-81-2)

- [SP 800-113](https://doi.org/10.6028/NIST.SP.800-113)

- [SP 800-177](https://doi.org/10.6028/NIST.SP.800-177r1)

- [IR 8023](https://doi.org/10.6028/NIST.IR.8023)

- Catalog relationship **related**: `ac-17`.

- Catalog relationship **related**: `ac-18`.

- Catalog relationship **related**: `au-10`.

- Catalog relationship **related**: `ia-3`.

- Catalog relationship **related**: `ia-8`.

- Catalog relationship **related**: `ia-9`.

- Catalog relationship **related**: `ma-4`.

- Catalog relationship **related**: `pe-4`.

- Catalog relationship **related**: `sa-4`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `sc-16`.

- Catalog relationship **related**: `sc-20`.

- Catalog relationship **related**: `sc-23`.

- Catalog relationship **related**: `sc-28`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
