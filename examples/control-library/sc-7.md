---
title: "SC-7 \u2014 Boundary Protection"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-7 — Boundary Protection

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Managed interfaces include gateways, routers, firewalls, guards, network-based malicious code analysis, virtualization systems, or encrypted tunnels implemented within a security architecture. Subnetworks that are physically or logically separated from internal networks are referred to as demilitarized zones or DMZs. Restricting or prohibiting interfaces within organizational systems includes restricting external web traffic to designated web servers within managed interfaces, prohibiting external traffic that appears to be spoofing internal addresses, and prohibiting internal traffic that appears to be spoofing external addresses. SP 800-189 (catalog reference: `#f5edfe51-d1f2-422e-9b27-5d0e90b49c72`) provides additional information on source address validation techniques to prevent ingress and egress of traffic with spoofed addresses. Commercial telecommunications services are provided by network components and consolidated management systems shared by customers. These services may also include third party-provided access lines and other service elements. Such services may represent sources of increased risk despite contract security provisions. Boundary protection may be implemented as a common control for all or part of an organizational network such that the boundary to be protected is greater than a system-specific boundary (i.e., an authorization boundary).

### Requirements and exact statement parts

- `sc-7_smt`: Statement grouping; see child parts.

- `sc-7_smt.a`: Monitor and control communications at the external managed interfaces to the system and at key internal managed interfaces within the system;

- `sc-7_smt.b`: Implement subnetworks for publicly accessible system components that are [PARAM sc-07_odp] separated from internal organizational networks; and

- `sc-7_smt.c`: Connect to external networks or systems only through managed interfaces consisting of boundary protection devices arranged in accordance with an organizational security and privacy architecture.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-7_smt.a — Monitor and control communications at the external managed interfaces to the system and at key internal managed interfaces within the system;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sc-7_smt.b — Implement subnetworks for publicly accessible system components that are [PARAM sc-07_odp] separated from internal organizational networks; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for sc-7_smt.c — Connect to external networks or systems only through managed interfaces consisting of boundary protection devices arranged in accordance with an organizational security and privacy architecture.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-07_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-7_smt.a` — For “Monitor and control communications at the external managed interfaces to the system and at key internal managed interfaces within the system;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sc-7_smt.b` — For “Implement subnetworks for publicly accessible system components that are [PARAM sc-07_odp] separated from internal organizational networks; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `sc-7_smt.c` — For “Connect to external networks or systems only through managed interfaces consisting of boundary protection devices arranged in accordance with an organizational security and privacy architecture.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-07_odp` — What approved value applies to **selection; choose one from: physically; logically**? Record the value, scope, approving authority, and decision source.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-7_obj.a-1` (sc-7_smt.a): communications at external managed interfaces to the system are monitored;

- `sc-7_obj.a-2` (sc-7_smt.a): communications at external managed interfaces to the system are controlled;

- `sc-7_obj.a-3` (sc-7_smt.a): communications at key internal managed interfaces within the system are monitored;

- `sc-7_obj.a-4` (sc-7_smt.a): communications at key internal managed interfaces within the system are controlled;

- `sc-7_obj.b` (sc-7_smt.b): subnetworks for publicly accessible system components are [PARAM sc-07_odp] separated from internal organizational networks;

- `sc-7_obj.c` (sc-7_smt.c): external networks or systems are only connected to through managed interfaces consisting of boundary protection devices arranged in accordance with an organizational security and privacy architecture.

#### EXAMINE — `sc-7_asm-examine`

- System and communications protection policy

- procedures addressing boundary protection

- list of key internal boundaries of the system

- system design documentation

- boundary protection hardware and software

- system configuration settings and associated documentation

- enterprise security architecture documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-7_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developer

- organizational personnel with boundary protection responsibilities

#### TEST — `sc-7_asm-test`

- Mechanisms implementing boundary protection capabilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-7`. The library index records the exact source revision and hash.

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [FIPS 199](https://doi.org/10.6028/NIST.FIPS.199)

- [SP 800-37](https://doi.org/10.6028/NIST.SP.800-37r2)

- [SP 800-41](https://doi.org/10.6028/NIST.SP.800-41r1)

- [SP 800-77](https://doi.org/10.6028/NIST.SP.800-77r1)

- [SP 800-189](https://doi.org/10.6028/NIST.SP.800-189)

- Catalog relationship **related**: `ac-4`.

- Catalog relationship **related**: `ac-17`.

- Catalog relationship **related**: `ac-18`.

- Catalog relationship **related**: `ac-19`.

- Catalog relationship **related**: `ac-20`.

- Catalog relationship **related**: `au-13`.

- Catalog relationship **related**: `ca-3`.

- Catalog relationship **related**: `cm-2`.

- Catalog relationship **related**: `cm-4`.

- Catalog relationship **related**: `cm-7`.

- Catalog relationship **related**: `cm-10`.

- Catalog relationship **related**: `cp-8`.

- Catalog relationship **related**: `cp-10`.

- Catalog relationship **related**: `ir-4`.

- Catalog relationship **related**: `ma-4`.

- Catalog relationship **related**: `pe-3`.

- Catalog relationship **related**: `pl-8`.

- Catalog relationship **related**: `pm-12`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sa-17`.

- Catalog relationship **related**: `sc-5`.

- Catalog relationship **related**: `sc-26`.

- Catalog relationship **related**: `sc-32`.

- Catalog relationship **related**: `sc-35`.

- Catalog relationship **related**: `sc-43`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
