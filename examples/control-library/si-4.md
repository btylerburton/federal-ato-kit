---
title: "SI-4 \u2014 System Monitoring"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-4 — System Monitoring

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

System monitoring includes external and internal monitoring. External monitoring includes the observation of events occurring at external interfaces to the system. Internal monitoring includes the observation of events occurring within the system. Organizations monitor systems by observing audit activities in real time or by observing other system aspects such as access patterns, characteristics of access, and other actions. The monitoring objectives guide and inform the determination of the events. System monitoring capabilities are achieved through a variety of tools and techniques, including intrusion detection and prevention systems, malicious code protection software, scanning tools, audit record monitoring software, and network monitoring software.

Depending on the security architecture, the distribution and configuration of monitoring devices may impact throughput at key internal and external boundaries as well as at other locations across a network due to the introduction of network throughput latency. If throughput management is needed, such devices are strategically located and deployed as part of an established organization-wide security architecture. Strategic locations for monitoring devices include selected perimeter locations and near key servers and server farms that support critical applications. Monitoring devices are typically employed at the managed interfaces associated with controls SC-7 (catalog reference: `#sc-7`) and AC-17 (catalog reference: `#ac-17`) . The information collected is a function of the organizational monitoring objectives and the capability of systems to support such objectives. Specific types of transactions of interest include Hypertext Transfer Protocol (HTTP) traffic that bypasses HTTP proxies. System monitoring is an integral part of organizational continuous monitoring and incident response programs, and output from system monitoring serves as input to those programs. System monitoring requirements, including the need for specific types of system monitoring, may be referenced in other controls (e.g., AC-2g (catalog reference: `#ac-2_smt.g`), AC-2(7) (catalog reference: `#ac-2.7`), AC-2(12)(a) (catalog reference: `#ac-2.12_smt.a`), AC-17(1) (catalog reference: `#ac-17.1`), AU-13 (catalog reference: `#au-13`), AU-13(1) (catalog reference: `#au-13.1`), AU-13(2) (catalog reference: `#au-13.2`), CM-3f (catalog reference: `#cm-3_smt.f`), CM-6d (catalog reference: `#cm-6_smt.d`), MA-3a (catalog reference: `#ma-3_smt.a`), MA-4a (catalog reference: `#ma-4_smt.a`), SC-5(3)(b) (catalog reference: `#sc-5.3_smt.b`), SC-7a (catalog reference: `#sc-7_smt.a`), SC-7(24)(b) (catalog reference: `#sc-7.24_smt.b`), SC-18b (catalog reference: `#sc-18_smt.b`), SC-43b (catalog reference: `#sc-43_smt.b`) ). Adjustments to levels of system monitoring are based on law enforcement information, intelligence information, or other sources of information. The legality of system monitoring activities is based on applicable laws, executive orders, directives, regulations, policies, standards, and guidelines.

### Requirements and exact statement parts

- `si-4_smt`: Statement grouping; see child parts.

- `si-4_smt.a`: Monitor the system to detect:

- `si-4_smt.a.1`: Attacks and indicators of potential attacks in accordance with the following monitoring objectives: [PARAM si-04_odp.01] ; and

- `si-4_smt.a.2`: Unauthorized local, network, and remote connections;

- `si-4_smt.b`: Identify unauthorized use of the system through the following techniques and methods: [PARAM si-04_odp.02];

- `si-4_smt.c`: Invoke internal monitoring capabilities or deploy monitoring devices:

- `si-4_smt.c.1`: Strategically within the system to collect organization-determined essential information; and

- `si-4_smt.c.2`: At ad hoc locations within the system to track specific types of transactions of interest to the organization;

- `si-4_smt.d`: Analyze detected events and anomalies;

- `si-4_smt.e`: Adjust the level of system monitoring activity when there is a change in risk to organizational operations and assets, individuals, other organizations, or the Nation;

- `si-4_smt.f`: Obtain legal opinion regarding system monitoring activities; and

- `si-4_smt.g`: Provide [PARAM si-04_odp.03] to [PARAM si-04_odp.04] [PARAM si-04_odp.05].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-4_smt.a — Monitor the system to detect:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-4_smt.a.1 — Attacks and indicators of potential attacks in accordance with the following monitoring objectives: [PARAM si-04_odp.01] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-4_smt.a.2 — Unauthorized local, network, and remote connections;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-4_smt.b — Identify unauthorized use of the system through the following techniques and methods: [PARAM si-04_odp.02];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-4_smt.c — Invoke internal monitoring capabilities or deploy monitoring devices:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-4_smt.c.1 — Strategically within the system to collect organization-determined essential information; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-4_smt.c.2 — At ad hoc locations within the system to track specific types of transactions of interest to the organization;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-4_smt.d — Analyze detected events and anomalies;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-4_smt.e — Adjust the level of system monitoring activity when there is a change in risk to organizational operations and assets, individuals, other organizations, or the Nation;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-4_smt.f — Obtain legal opinion regarding system monitoring activities; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-4_smt.g — Provide [PARAM si-04_odp.03] to [PARAM si-04_odp.04] [PARAM si-04_odp.05].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-04_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-04_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-04_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-04_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-04_odp.05: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-04_odp.06: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-4_smt.a` — For “Monitor the system to detect:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-4_smt.a.1` — For “Attacks and indicators of potential attacks in accordance with the following monitoring objectives: [PARAM si-04_odp.01] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-4_smt.a.2` — For “Unauthorized local, network, and remote connections;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-4_smt.b` — For “Identify unauthorized use of the system through the following techniques and methods: [PARAM si-04_odp.02];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-4_smt.c` — For “Invoke internal monitoring capabilities or deploy monitoring devices:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-4_smt.c.1` — For “Strategically within the system to collect organization-determined essential information; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-4_smt.c.2` — For “At ad hoc locations within the system to track specific types of transactions of interest to the organization;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-4_smt.d` — For “Analyze detected events and anomalies;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-4_smt.e` — For “Adjust the level of system monitoring activity when there is a change in risk to organizational operations and assets, individuals, other organizations, or the Nation;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-4_smt.f` — For “Obtain legal opinion regarding system monitoring activities; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-4_smt.g` — For “Provide [PARAM si-04_odp.03] to [PARAM si-04_odp.04] [PARAM si-04_odp.05].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-04_odp.01` — What approved value applies to **monitoring objectives**? Record the value, scope, approving authority, and decision source.

  - Catalog context: monitoring objectives to detect attacks and indicators of potential attacks on the system are defined;

- `si-04_odp.02` — What approved value applies to **techniques and methods**? Record the value, scope, approving authority, and decision source.

  - Catalog context: techniques and methods used to identify unauthorized use of the system are defined;

- `si-04_odp.03` — What approved value applies to **system monitoring information**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system monitoring information to be provided to personnel or roles is defined;

- `si-04_odp.04` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to whom system monitoring information is to be provided is/are defined;

- `si-04_odp.05` — What approved value applies to **selection; choose one-or-more from: as needed; [PARAM si-04_odp.06]**? Record the value, scope, approving authority, and decision source.

- `si-04_odp.06` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: a frequency for providing system monitoring to personnel or roles is defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-4_obj.a.1` (si-4_smt.a.1): the system is monitored to detect attacks and indicators of potential attacks in accordance with [PARAM si-04_odp.01];

- `si-4_obj.a.2-1` (si-4_smt.a.2): the system is monitored to detect unauthorized local connections;

- `si-4_obj.a.2-2` (si-4_smt.a.2): the system is monitored to detect unauthorized network connections;

- `si-4_obj.a.2-3` (si-4_smt.a.2): the system is monitored to detect unauthorized remote connections;

- `si-4_obj.b` (si-4_smt.b): unauthorized use of the system is identified through [PARAM si-04_odp.02];

- `si-4_obj.c.1` (si-4_smt.c.1): internal monitoring capabilities are invoked or monitoring devices are deployed strategically within the system to collect organization-determined essential information;

- `si-4_obj.c.2` (si-4_smt.c.2): internal monitoring capabilities are invoked or monitoring devices are deployed at ad hoc locations within the system to track specific types of transactions of interest to the organization;

- `si-4_obj.d-1` (si-4_smt.d): detected events are analyzed;

- `si-4_obj.d-2` (si-4_smt.d): detected anomalies are analyzed;

- `si-4_obj.e` (si-4_smt.e): the level of system monitoring activity is adjusted when there is a change in risk to organizational operations and assets, individuals, other organizations, or the Nation;

- `si-4_obj.f` (si-4_smt.f): a legal opinion regarding system monitoring activities is obtained;

- `si-4_obj.g` (si-4_smt.g): [PARAM si-04_odp.03] is provided to [PARAM si-04_odp.04] [PARAM si-04_odp.05].

#### EXAMINE — `si-4_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing system monitoring tools and techniques

- continuous monitoring strategy

- facility diagram/layout

- system design documentation

- system monitoring tools and techniques documentation

- locations within the system where monitoring devices are deployed

- system configuration settings and associated documentation

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-4_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for monitoring the system

#### TEST — `si-4_asm-test`

- Organizational processes for system monitoring

- mechanisms supporting and/or implementing system monitoring capabilities

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-4`. The library index records the exact source revision and hash.

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [FIPS 140-3](https://doi.org/10.6028/NIST.FIPS.140-3)

- [SP 800-61](https://doi.org/10.6028/NIST.SP.800-61r2)

- [SP 800-83](https://doi.org/10.6028/NIST.SP.800-83r1)

- [SP 800-92](https://doi.org/10.6028/NIST.SP.800-92)

- [SP 800-94](https://doi.org/10.6028/NIST.SP.800-94)

- [SP 800-137](https://doi.org/10.6028/NIST.SP.800-137)

- Catalog relationship **related**: `ac-2`.

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-4`.

- Catalog relationship **related**: `ac-8`.

- Catalog relationship **related**: `ac-17`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-6`.

- Catalog relationship **related**: `au-7`.

- Catalog relationship **related**: `au-9`.

- Catalog relationship **related**: `au-12`.

- Catalog relationship **related**: `au-13`.

- Catalog relationship **related**: `au-14`.

- Catalog relationship **related**: `ca-7`.

- Catalog relationship **related**: `cm-3`.

- Catalog relationship **related**: `cm-6`.

- Catalog relationship **related**: `cm-8`.

- Catalog relationship **related**: `cm-11`.

- Catalog relationship **related**: `ia-10`.

- Catalog relationship **related**: `ir-4`.

- Catalog relationship **related**: `ma-3`.

- Catalog relationship **related**: `ma-4`.

- Catalog relationship **related**: `pl-9`.

- Catalog relationship **related**: `pm-12`.

- Catalog relationship **related**: `ra-5`.

- Catalog relationship **related**: `ra-10`.

- Catalog relationship **related**: `sc-5`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `sc-18`.

- Catalog relationship **related**: `sc-26`.

- Catalog relationship **related**: `sc-31`.

- Catalog relationship **related**: `sc-35`.

- Catalog relationship **related**: `sc-36`.

- Catalog relationship **related**: `sc-37`.

- Catalog relationship **related**: `sc-43`.

- Catalog relationship **related**: `si-3`.

- Catalog relationship **related**: `si-6`.

- Catalog relationship **related**: `si-7`.

- Catalog relationship **related**: `sr-9`.

- Catalog relationship **related**: `sr-10`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
