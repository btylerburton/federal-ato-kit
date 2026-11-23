---
title: "RA-9 \u2014 Criticality Analysis"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# RA-9 — Criticality Analysis

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Not all system components, functions, or services necessarily require significant protections. For example, criticality analysis is a key tenet of supply chain risk management and informs the prioritization of protection activities. The identification of critical system components and functions considers applicable laws, executive orders, regulations, directives, policies, standards, system functionality requirements, system and component interfaces, and system and component dependencies. Systems engineers conduct a functional decomposition of a system to identify mission-critical functions and components. The functional decomposition includes the identification of organizational missions supported by the system, decomposition into the specific functions to perform those missions, and traceability to the hardware, software, and firmware components that implement those functions, including when the functions are shared by many components within and external to the system.

The operational environment of a system or a system component may impact the criticality, including the connections to and dependencies on cyber-physical systems, devices, system-of-systems, and outsourced IT services. System components that allow unmediated access to critical system components or functions are considered critical due to the inherent vulnerabilities that such components create. Component and function criticality are assessed in terms of the impact of a component or function failure on the organizational missions that are supported by the system that contains the components and functions.

Criticality analysis is performed when an architecture or design is being developed, modified, or upgraded. If such analysis is performed early in the system development life cycle, organizations may be able to modify the system design to reduce the critical nature of these components and functions, such as by adding redundancy or alternate paths into the system design. Criticality analysis can also influence the protection measures required by development contractors. In addition to criticality analysis for systems, system components, and system services, criticality analysis of information is an important consideration. Such analysis is conducted as part of security categorization in RA-2 (catalog reference: `#ra-2`).

### Requirements and exact statement parts

- `ra-9_smt`: Identify critical system components and functions by performing a criticality analysis for [PARAM ra-09_odp.01] at [PARAM ra-09_odp.02].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ra-9_smt — Identify critical system components and functions by performing a criticality analysis for [PARAM ra-09_odp.01] at [PARAM ra-09_odp.02].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ra-09_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ra-09_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ra-9_smt` — For “Identify critical system components and functions by performing a criticality analysis for [PARAM ra-09_odp.01] at [PARAM ra-09_odp.02].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ra-09_odp.01` — What approved value applies to **systems, system components, or system services**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems, system components, or system services to be analyzed for criticality are defined;

- `ra-09_odp.02` — What approved value applies to **decision points in the system development life cycle**? Record the value, scope, approving authority, and decision source.

  - Catalog context: decision points in the system development life cycle when a criticality analysis is to be performed are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ra-9_obj` (ra-9_smt): critical system components and functions are identified by performing a criticality analysis for [PARAM ra-09_odp.01] at [PARAM ra-09_odp.02].

#### EXAMINE — `ra-9_asm-examine`

- Risk assessment policy

- assessment reports

- criticality analysis/finalized criticality for each component/subcomponent

- audit records/event logs

- analysis reports

- system security plan

- other relevant documents or records

#### INTERVIEW — `ra-9_asm-interview`

- Organizational personnel with assessment and auditing responsibilities

- organizational personnel with criticality analysis responsibilities

- system/network administrators

- organizational personnel with security responsibilities

#### TEST — `ra-9_asm-test`

- Organizational processes for assessments and audits

- mechanisms/tools supporting and/or implementing assessments and auditing

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ra-9`. The library index records the exact source revision and hash.

- [IR 8179](https://doi.org/10.6028/NIST.IR.8179)

- Catalog relationship **related**: `cp-2`.

- Catalog relationship **related**: `pl-2`.

- Catalog relationship **related**: `pl-8`.

- Catalog relationship **related**: `pl-11`.

- Catalog relationship **related**: `pm-1`.

- Catalog relationship **related**: `pm-11`.

- Catalog relationship **related**: `ra-2`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sa-15`.

- Catalog relationship **related**: `sa-20`.

- Catalog relationship **related**: `sr-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
