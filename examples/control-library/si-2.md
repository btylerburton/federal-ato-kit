---
title: "SI-2 \u2014 Flaw Remediation"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-2 — Flaw Remediation

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The need to remediate system flaws applies to all types of software and firmware. Organizations identify systems affected by software flaws, including potential vulnerabilities resulting from those flaws, and report this information to designated organizational personnel with information security and privacy responsibilities. Organizations consider establishing a controlled patching environment for mission-critical systems. Security-relevant updates include patches, service packs, and malicious code signatures. Organizations also address flaws discovered during assessments, continuous monitoring, incident response activities, and system error handling. By incorporating flaw remediation into configuration management processes, required remediation actions can be tracked and verified.

Organization-defined time periods for updating security-relevant software and firmware may vary based on a variety of risk factors, including the security category of the system, the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw), the organizational risk tolerance, the mission supported by the system, or the threat environment. Some types of flaw remediation may require more testing than other types. Organizations determine the type of testing needed for the specific type of flaw remediation activity under consideration and the types of changes that are to be configuration-managed. Flaw remediation testing addresses both effectiveness of addressing security issues and for potential side effects on functionality, system and system component performance and operations. When implementing remediation activities, organizations consider the order and timing of updates to validate correct execution within the system environment, and to support system and component availability needs (i.e., implementing a staggered deployment strategy). In some situations, organizations may determine that the testing of software or firmware updates is not necessary or practical, such as when implementing simple malicious code signature updates. In testing decisions, organizations consider whether security-relevant software or firmware updates are obtained from authorized sources with appropriate digital signatures.

When implementing remediation activities, organizations consider the order and timing of updates to validate correct execution within the system environment, and to support system and component availability needs (i.e., implementing a staggered deployment strategy). Organizations verify that software and firmware updates come from authorized sources prior to downloading.

### Requirements and exact statement parts

- `si-2_smt`: Statement grouping; see child parts.

- `si-2_smt.a`: Identify, report, and correct system flaws;

- `si-2_smt.b`: Test software and firmware updates related to flaw remediation for effectiveness and potential side effects before installation;

- `si-2_smt.c`: Install security-relevant software and firmware updates within [PARAM si-02_odp] of the release of the updates; and

- `si-2_smt.d`: Incorporate flaw remediation into the organizational configuration management process.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-2_smt.a — Identify, report, and correct system flaws;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-2_smt.b — Test software and firmware updates related to flaw remediation for effectiveness and potential side effects before installation;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-2_smt.c — Install security-relevant software and firmware updates within [PARAM si-02_odp] of the release of the updates; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-2_smt.d — Incorporate flaw remediation into the organizational configuration management process.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-02_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-2_smt.a` — For “Identify, report, and correct system flaws;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-2_smt.b` — For “Test software and firmware updates related to flaw remediation for effectiveness and potential side effects before installation;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-2_smt.c` — For “Install security-relevant software and firmware updates within [PARAM si-02_odp] of the release of the updates; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-2_smt.d` — For “Incorporate flaw remediation into the organizational configuration management process.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-02_odp` — What approved value applies to **time period**? Record the value, scope, approving authority, and decision source.

  - Catalog context: time period within which to install security-relevant software updates after the release of the updates is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-2_obj.a-1` (si-2_smt.a): system flaws are identified;

- `si-2_obj.a-2` (si-2_smt.a): system flaws are reported;

- `si-2_obj.a-3` (si-2_smt.a): system flaws are corrected;

- `si-2_obj.b-1` (si-2_smt.b): software updates related to flaw remediation are tested for effectiveness before installation;

- `si-2_obj.b-2` (si-2_smt.b): software updates related to flaw remediation are tested for potential side effects before installation;

- `si-2_obj.b-3` (si-2_smt.b): firmware updates related to flaw remediation are tested for effectiveness before installation;

- `si-2_obj.b-4` (si-2_smt.b): firmware updates related to flaw remediation are tested for potential side effects before installation;

- `si-2_obj.c-1` (si-2_smt.c): security-relevant software updates are installed within [PARAM si-02_odp] of the release of the updates;

- `si-2_obj.c-2` (si-2_smt.c): security-relevant firmware updates are installed within [PARAM si-02_odp] of the release of the updates;

- `si-2_obj.d` (si-2_smt.d): flaw remediation is incorporated into the organizational configuration management process.

#### EXAMINE — `si-2_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- procedures addressing flaw remediation

- procedures addressing configuration management

- list of flaws and vulnerabilities potentially affecting the system

- list of recent security flaw remediation actions performed on the system (e.g., list of installed patches, service packs, hot fixes, and other software updates to correct system flaws)

- test results from the installation of software and firmware updates to correct system flaws

- installation/change control records for security-relevant software and firmware updates

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `si-2_asm-interview`

- System/network administrators

- organizational personnel with information security and privacy responsibilities

- organizational personnel responsible for installing, configuring, and/or maintaining the system

- organizational personnel responsible for flaw remediation

- organizational personnel with configuration management responsibilities

#### TEST — `si-2_asm-test`

- Organizational processes for identifying, reporting, and correcting system flaws

- organizational process for installing software and firmware updates

- mechanisms supporting and/or implementing the reporting and correcting of system flaws

- mechanisms supporting and/or implementing testing software and firmware updates

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-2`. The library index records the exact source revision and hash.

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [FIPS 140-3](https://doi.org/10.6028/NIST.FIPS.140-3)

- [FIPS 186-4](https://doi.org/10.6028/NIST.FIPS.186-4)

- [SP 800-39](https://doi.org/10.6028/NIST.SP.800-39)

- [SP 800-40](https://doi.org/10.6028/NIST.SP.800-40r3)

- [SP 800-128](https://doi.org/10.6028/NIST.SP.800-128)

- [IR 7788](https://doi.org/10.6028/NIST.IR.7788)

- [SP 800-81-2](https://doi.org/10.6028/NIST.SP.800-81-2)

- Catalog relationship **related**: `ca-5`.

- Catalog relationship **related**: `cm-3`.

- Catalog relationship **related**: `cm-4`.

- Catalog relationship **related**: `cm-5`.

- Catalog relationship **related**: `cm-6`.

- Catalog relationship **related**: `cm-8`.

- Catalog relationship **related**: `ma-2`.

- Catalog relationship **related**: `ra-5`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sa-10`.

- Catalog relationship **related**: `sa-11`.

- Catalog relationship **related**: `si-3`.

- Catalog relationship **related**: `si-5`.

- Catalog relationship **related**: `si-7`.

- Catalog relationship **related**: `si-11`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
