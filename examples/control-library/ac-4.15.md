---
title: "AC-4.15 \u2014 Detection of Unsanctioned Information"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# AC-4.15 — Detection of Unsanctioned Information

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Unsanctioned information includes malicious code, information that is inappropriate for release from the source network, or executable code that could disrupt or harm the services or systems on the destination network.

### Requirements and exact statement parts

- `ac-4.15_smt`: When transferring information between different security domains, examine the information for the presence of [PARAM ac-04.15_odp.01] and prohibit the transfer of such information in accordance with the [PARAM ac-4.15_prm_2].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ac-4.15_smt — When transferring information between different security domains, examine the information for the presence of [PARAM ac-04.15_odp.01] and prohibit the transfer of such information in accordance with the [PARAM ac-4.15_prm_2].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ac-4.15_prm_2: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.15_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.15_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ac-04.15_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ac-4.15_smt` — For “When transferring information between different security domains, examine the information for the presence of [PARAM ac-04.15_odp.01] and prohibit the transfer of such information in accordance with the [PARAM ac-4.15_prm_2].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ac-4.15_prm_2` — What approved value applies to **organization-defined security or privacy policy**? Record the value, scope, approving authority, and decision source.

- `ac-04.15_odp.01` — What approved value applies to **unsanctioned information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: unsanctioned information to be detected is defined;

- `ac-04.15_odp.02` — What approved value applies to **security policy**? Record the value, scope, approving authority, and decision source.

  - Catalog context: security policy that requires the transfer of unsanctioned information between different security domains to be prohibited is defined (if selected);

- `ac-04.15_odp.03` — What approved value applies to **privacy policy**? Record the value, scope, approving authority, and decision source.

  - Catalog context: privacy policy that requires the transfer of organization-defined unsanctioned information between different security domains to be prohibited is defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ac-4.15_obj-1` (ac-4.15_smt): when transferring information between different security domains, information is examined for the presence of [PARAM ac-04.15_odp.01];

- `ac-4.15_obj-2` (ac-4.15_smt): when transferring information between different security domains, transfer of [PARAM ac-04.15_odp.01] is prohibited in accordance with the [PARAM ac-04.15_odp.02];

- `ac-4.15_obj-3` (ac-4.15_smt): when transferring information between different security domains, transfer of [PARAM ac-04.15_odp.01] is prohibited in accordance with the [PARAM ac-04.15_odp.03].

#### EXAMINE — `ac-4.15_asm-examine`

- Access control policy

- information flow control policies

- procedures addressing information flow enforcement

- system design documentation

- system configuration settings and associated documentation

- list of unsanctioned information types and associated information

- system audit records

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ac-4.15_asm-interview`

- Organizational personnel with information security responsibilities

- organizational personnel with privacy responsibilities

- system developers

#### TEST — `ac-4.15_asm-test`

- Mechanisms implementing information flow enforcement policy

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ac-4.15`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ac-4`.

- Catalog relationship **related**: `si-3`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
