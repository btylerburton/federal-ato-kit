---
title: "SI-3 \u2014 Malicious Code Protection"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SI-3 — Malicious Code Protection

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

System entry and exit points include firewalls, remote access servers, workstations, electronic mail servers, web servers, proxy servers, notebook computers, and mobile devices. Malicious code includes viruses, worms, Trojan horses, and spyware. Malicious code can also be encoded in various formats contained within compressed or hidden files or hidden in files using techniques such as steganography. Malicious code can be inserted into systems in a variety of ways, including by electronic mail, the world-wide web, and portable storage devices. Malicious code insertions occur through the exploitation of system vulnerabilities. A variety of technologies and methods exist to limit or eliminate the effects of malicious code.

Malicious code protection mechanisms include both signature- and nonsignature-based technologies. Nonsignature-based detection mechanisms include artificial intelligence techniques that use heuristics to detect, analyze, and describe the characteristics or behavior of malicious code and to provide controls against such code for which signatures do not yet exist or for which existing signatures may not be effective. Malicious code for which active signatures do not yet exist or may be ineffective includes polymorphic malicious code (i.e., code that changes signatures when it replicates). Nonsignature-based mechanisms also include reputation-based technologies. In addition to the above technologies, pervasive configuration management, comprehensive software integrity controls, and anti-exploitation software may be effective in preventing the execution of unauthorized code. Malicious code may be present in commercial off-the-shelf software as well as custom-built software and could include logic bombs, backdoors, and other types of attacks that could affect organizational mission and business functions.

In situations where malicious code cannot be detected by detection methods or technologies, organizations rely on other types of controls, including secure coding practices, configuration management and control, trusted procurement processes, and monitoring practices to ensure that software does not perform functions other than the functions intended. Organizations may determine that, in response to the detection of malicious code, different actions may be warranted. For example, organizations can define actions in response to malicious code detection during periodic scans, the detection of malicious downloads, or the detection of maliciousness when attempting to open or execute files.

### Requirements and exact statement parts

- `si-3_smt`: Statement grouping; see child parts.

- `si-3_smt.a`: Implement [PARAM si-03_odp.01] malicious code protection mechanisms at system entry and exit points to detect and eradicate malicious code;

- `si-3_smt.b`: Automatically update malicious code protection mechanisms as new releases are available in accordance with organizational configuration management policy and procedures;

- `si-3_smt.c`: Configure malicious code protection mechanisms to:

- `si-3_smt.c.1`: Perform periodic scans of the system [PARAM si-03_odp.02] and real-time scans of files from external sources at [PARAM si-03_odp.03] as the files are downloaded, opened, or executed in accordance with organizational policy; and

- `si-3_smt.c.2`: [PARAM si-03_odp.04] ; and send alert to [PARAM si-03_odp.06] in response to malicious code detection; and

- `si-3_smt.d`: Address the receipt of false positives during malicious code detection and eradication and the resulting potential impact on the availability of the system.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for si-3_smt.a — Implement [PARAM si-03_odp.01] malicious code protection mechanisms at system entry and exit points to detect and eradicate malicious code;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-3_smt.b — Automatically update malicious code protection mechanisms as new releases are available in accordance with organizational configuration management policy and procedures;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-3_smt.c — Configure malicious code protection mechanisms to:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-3_smt.c.1 — Perform periodic scans of the system [PARAM si-03_odp.02] and real-time scans of files from external sources at [PARAM si-03_odp.03] as the files are downloaded, opened, or executed in accordance with organizational policy; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-3_smt.c.2 — [PARAM si-03_odp.04] ; and send alert to [PARAM si-03_odp.06] in response to malicious code detection; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for si-3_smt.d — Address the receipt of false positives during malicious code detection and eradication and the resulting potential impact on the availability of the system.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter si-03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-03_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-03_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-03_odp.05: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter si-03_odp.06: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `si-3_smt.a` — For “Implement [PARAM si-03_odp.01] malicious code protection mechanisms at system entry and exit points to detect and eradicate malicious code;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-3_smt.b` — For “Automatically update malicious code protection mechanisms as new releases are available in accordance with organizational configuration management policy and procedures;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-3_smt.c` — For “Configure malicious code protection mechanisms to:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-3_smt.c.1` — For “Perform periodic scans of the system [PARAM si-03_odp.02] and real-time scans of files from external sources at [PARAM si-03_odp.03] as the files are downloaded, opened, or executed in accordance with organizational policy; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-3_smt.c.2` — For “[PARAM si-03_odp.04] ; and send alert to [PARAM si-03_odp.06] in response to malicious code detection; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `si-3_smt.d` — For “Address the receipt of false positives during malicious code detection and eradication and the resulting potential impact on the availability of the system.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `si-03_odp.01` — What approved value applies to **selection; choose one-or-more from: signature-based; non-signature-based**? Record the value, scope, approving authority, and decision source.

- `si-03_odp.02` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the frequency at which malicious code protection mechanisms perform scans is defined;

- `si-03_odp.03` — What approved value applies to **selection; choose one-or-more from: endpoint; network entry and exit points**? Record the value, scope, approving authority, and decision source.

- `si-03_odp.04` — What approved value applies to **selection; choose one-or-more from: block malicious code; quarantine malicious code; take [PARAM si-03_odp.05]**? Record the value, scope, approving authority, and decision source.

- `si-03_odp.05` — What approved value applies to **action**? Record the value, scope, approving authority, and decision source.

  - Catalog context: action to be taken in response to malicious code detection are defined (if selected);

- `si-03_odp.06` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to be alerted when malicious code is detected is/are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `si-3_obj.a-1` (si-3_smt.a): [PARAM si-03_odp.01] malicious code protection mechanisms are implemented at system entry and exit points to detect malicious code;

- `si-3_obj.a-2` (si-3_smt.a): [PARAM si-03_odp.01] malicious code protection mechanisms are implemented at system entry and exit points to eradicate malicious code;

- `si-3_obj.b` (si-3_smt.b): malicious code protection mechanisms are updated automatically as new releases are available in accordance with organizational configuration management policy and procedures;

- `si-3_obj.c.1-1` (si-3_smt.c.1): malicious code protection mechanisms are configured to perform periodic scans of the system [PARAM si-03_odp.02];

- `si-3_obj.c.1-2` (si-3_smt.c.1): malicious code protection mechanisms are configured to perform real-time scans of files from external sources at [PARAM si-03_odp.03] as the files are downloaded, opened, or executed in accordance with organizational policy;

- `si-3_obj.c.2-1` (si-3_smt.c.2): malicious code protection mechanisms are configured to [PARAM si-03_odp.04] in response to malicious code detection;

- `si-3_obj.c.2-2` (si-3_smt.c.2): malicious code protection mechanisms are configured to send alerts to [PARAM si-03_odp.06] in response to malicious code detection;

- `si-3_obj.d` (si-3_smt.d): the receipt of false positives during malicious code detection and eradication and the resulting potential impact on the availability of the system are addressed.

#### EXAMINE — `si-3_asm-examine`

- System and information integrity policy

- system and information integrity procedures

- configuration management policy and procedures

- procedures addressing malicious code protection

- malicious code protection mechanisms

- records of malicious code protection updates

- system design documentation

- system configuration settings and associated documentation

- scan results from malicious code protection mechanisms

- record of actions initiated by malicious code protection mechanisms in response to malicious code detection

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `si-3_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- organizational personnel installing, configuring, and/or maintaining the system

- organizational personnel responsible for malicious code protection

- organizational personnel with configuration management responsibilities

#### TEST — `si-3_asm-test`

- Organizational processes for employing, updating, and configuring malicious code protection mechanisms

- organizational processes for addressing false positives and resulting potential impacts

- mechanisms supporting and/or implementing, employing, updating, and configuring malicious code protection mechanisms

- mechanisms supporting and/or implementing malicious code scanning and subsequent actions

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `si-3`. The library index records the exact source revision and hash.

- [SP 800-83](https://doi.org/10.6028/NIST.SP.800-83r1)

- [SP 800-125B](https://doi.org/10.6028/NIST.SP.800-125B)

- [SP 800-177](https://doi.org/10.6028/NIST.SP.800-177r1)

- Catalog relationship **related**: `ac-4`.

- Catalog relationship **related**: `ac-19`.

- Catalog relationship **related**: `cm-3`.

- Catalog relationship **related**: `cm-8`.

- Catalog relationship **related**: `ir-4`.

- Catalog relationship **related**: `ma-3`.

- Catalog relationship **related**: `ma-4`.

- Catalog relationship **related**: `pl-9`.

- Catalog relationship **related**: `ra-5`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `sc-23`.

- Catalog relationship **related**: `sc-26`.

- Catalog relationship **related**: `sc-28`.

- Catalog relationship **related**: `sc-44`.

- Catalog relationship **related**: `si-2`.

- Catalog relationship **related**: `si-4`.

- Catalog relationship **related**: `si-7`.

- Catalog relationship **related**: `si-8`.

- Catalog relationship **related**: `si-15`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
