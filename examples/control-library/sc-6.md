---
title: "SC-6 \u2014 Resource Availability"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-6 — Resource Availability

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Priority protection prevents lower-priority processes from delaying or interfering with the system that services higher-priority processes. Quotas prevent users or processes from obtaining more than predetermined amounts of resources.

### Requirements and exact statement parts

- `sc-6_smt`: Protect the availability of resources by allocating [PARAM sc-06_odp.01] by [PARAM sc-06_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-6_smt — Protect the availability of resources by allocating [PARAM sc-06_odp.01] by [PARAM sc-06_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-06_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sc-06_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sc-06_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-6_smt` — For “Protect the availability of resources by allocating [PARAM sc-06_odp.01] by [PARAM sc-06_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-06_odp.01` — What approved value applies to **resources**? Record the value, scope, approving authority, and decision source.

  - Catalog context: resources to be allocated to protect the availability of resources are defined;

- `sc-06_odp.02` — What approved value applies to **selection; choose one-or-more from: priority; quota; [PARAM sc-06_odp.03]**? Record the value, scope, approving authority, and decision source.

- `sc-06_odp.03` — What approved value applies to **controls**? Record the value, scope, approving authority, and decision source.

  - Catalog context: controls to protect the availability of resources are defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-6_obj` (sc-6_smt): the availability of resources is protected by allocating [PARAM sc-06_odp.01] by [PARAM sc-06_odp.02].

#### EXAMINE — `sc-6_asm-examine`

- System and communications protection policy

- procedures addressing prioritization of system resources

- system design documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-6_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developer

#### TEST — `sc-6_asm-test`

- Mechanisms supporting and/or implementing a resource allocation capability

- safeguards employed to protect availability of resources

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-6`. The library index records the exact source revision and hash.

- [OMB M-08-05](https://obamawhitehouse.archives.gov/sites/default/files/omb/assets/omb/memoranda/fy2008/m08-05.pdf)

- [DHS TIC](https://www.dhs.gov/trusted-internet-connections)

- Catalog relationship **related**: `sc-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
