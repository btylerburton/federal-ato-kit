---
title: "SC-5.3 \u2014 Detection and Monitoring"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-5.3 — Detection and Monitoring

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations consider the utilization and capacity of system resources when managing risk associated with a denial of service due to malicious attacks. Denial-of-service attacks can originate from external or internal sources. System resources that are sensitive to denial of service include physical disk storage, memory, and CPU cycles. Techniques used to prevent denial-of-service attacks related to storage utilization and capacity include instituting disk quotas, configuring systems to automatically alert administrators when specific storage capacity thresholds are reached, using file compression technologies to maximize available storage space, and imposing separate partitions for system and user data.

### Requirements and exact statement parts

- `sc-5.3_smt`: Statement grouping; see child parts.

- `sc-5.3_smt.a`: Employ the following monitoring tools to detect indicators of denial-of-service attacks against, or launched from, the system: [PARAM sc-05.03_odp.01] ; and

- `sc-5.3_smt.b`: Monitor the following system resources to determine if sufficient resources exist to prevent effective denial-of-service attacks: [PARAM sc-05.03_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-5.3_smt.a — Employ the following monitoring tools to detect indicators of denial-of-service attacks against, or launched from, the system: [PARAM sc-05.03_odp.01] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sc-5.3_smt.b — Monitor the following system resources to determine if sufficient resources exist to prevent effective denial-of-service attacks: [PARAM sc-05.03_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-05.03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sc-05.03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-5.3_smt.a` — For “Employ the following monitoring tools to detect indicators of denial-of-service attacks against, or launched from, the system: [PARAM sc-05.03_odp.01] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sc-5.3_smt.b` — For “Monitor the following system resources to determine if sufficient resources exist to prevent effective denial-of-service attacks: [PARAM sc-05.03_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-05.03_odp.01` — What approved value applies to **monitoring tools**? Record the value, scope, approving authority, and decision source.

  - Catalog context: monitoring tools for detecting indicators of denial-of-service attacks are defined;

- `sc-05.03_odp.02` — What approved value applies to **system resources**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system resources to be monitored to determine if sufficient resources exist to prevent effective denial-of-service attacks are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-5.3_obj.a` (sc-5.3_smt.a): [PARAM sc-05.03_odp.01] are employed to detect indicators of denial-of-service attacks against or launched from the system;

- `sc-5.3_obj.b` (sc-5.3_smt.b): [PARAM sc-05.03_odp.02] are monitored to determine if sufficient resources exist to prevent effective denial-of-service attacks.

#### EXAMINE — `sc-5.3_asm-examine`

- System and communications protection policy

- procedures addressing denial-of-service protection

- system design documentation

- system monitoring tools and techniques documentation

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-5.3_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel with detection and monitoring responsibilities

#### TEST — `sc-5.3_asm-test`

- Mechanisms/tools implementing system monitoring for denial-of-service attacks

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-5.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sc-5`.

- Catalog relationship **related**: `ca-7`.

- Catalog relationship **related**: `si-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
