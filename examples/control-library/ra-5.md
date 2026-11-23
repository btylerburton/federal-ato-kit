---
title: "RA-5 \u2014 Vulnerability Monitoring and Scanning"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# RA-5 — Vulnerability Monitoring and Scanning

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Security categorization of information and systems guides the frequency and comprehensiveness of vulnerability monitoring (including scans). Organizations determine the required vulnerability monitoring for system components, ensuring that the potential sources of vulnerabilities—such as infrastructure components (e.g., switches, routers, guards, sensors), networked printers, scanners, and copiers—are not overlooked. The capability to readily update vulnerability monitoring tools as new vulnerabilities are discovered and announced and as new scanning methods are developed helps to ensure that new vulnerabilities are not missed by employed vulnerability monitoring tools. The vulnerability monitoring tool update process helps to ensure that potential vulnerabilities in the system are identified and addressed as quickly as possible. Vulnerability monitoring and analyses for custom software may require additional approaches, such as static analysis, dynamic analysis, binary analysis, or a hybrid of the three approaches. Organizations can use these analysis approaches in source code reviews and in a variety of tools, including web-based application scanners, static analysis tools, and binary analyzers.

Vulnerability monitoring includes scanning for patch levels; scanning for functions, ports, protocols, and services that should not be accessible to users or devices; and scanning for flow control mechanisms that are improperly configured or operating incorrectly. Vulnerability monitoring may also include continuous vulnerability monitoring tools that use instrumentation to continuously analyze components. Instrumentation-based tools may improve accuracy and may be run throughout an organization without scanning. Vulnerability monitoring tools that facilitate interoperability include tools that are Security Content Automated Protocol (SCAP)-validated. Thus, organizations consider using scanning tools that express vulnerabilities in the Common Vulnerabilities and Exposures (CVE) naming convention and that employ the Open Vulnerability Assessment Language (OVAL) to determine the presence of vulnerabilities. Sources for vulnerability information include the Common Weakness Enumeration (CWE) listing and the National Vulnerability Database (NVD). Control assessments, such as red team exercises, provide additional sources of potential vulnerabilities for which to scan. Organizations also consider using scanning tools that express vulnerability impact by the Common Vulnerability Scoring System (CVSS).

Vulnerability monitoring includes a channel and process for receiving reports of security vulnerabilities from the public at-large. Vulnerability disclosure programs can be as simple as publishing a monitored email address or web form that can receive reports, including notification authorizing good-faith research and disclosure of security vulnerabilities. Organizations generally expect that such research is happening with or without their authorization and can use public vulnerability disclosure channels to increase the likelihood that discovered vulnerabilities are reported directly to the organization for remediation.

Organizations may also employ the use of financial incentives (also known as "bug bounties" ) to further encourage external security researchers to report discovered vulnerabilities. Bug bounty programs can be tailored to the organization’s needs. Bounties can be operated indefinitely or over a defined period of time and can be offered to the general public or to a curated group. Organizations may run public and private bounties simultaneously and could choose to offer partially credentialed access to certain participants in order to evaluate security vulnerabilities from privileged vantage points.

### Requirements and exact statement parts

- `ra-5_smt`: Statement grouping; see child parts.

- `ra-5_smt.a`: Monitor and scan for vulnerabilities in the system and hosted applications [PARAM ra-5_prm_1] and when new vulnerabilities potentially affecting the system are identified and reported;

- `ra-5_smt.b`: Employ vulnerability monitoring tools and techniques that facilitate interoperability among tools and automate parts of the vulnerability management process by using standards for:

- `ra-5_smt.b.1`: Enumerating platforms, software flaws, and improper configurations;

- `ra-5_smt.b.2`: Formatting checklists and test procedures; and

- `ra-5_smt.b.3`: Measuring vulnerability impact;

- `ra-5_smt.c`: Analyze vulnerability scan reports and results from vulnerability monitoring;

- `ra-5_smt.d`: Remediate legitimate vulnerabilities [PARAM ra-05_odp.03] in accordance with an organizational assessment of risk;

- `ra-5_smt.e`: Share information obtained from the vulnerability monitoring process and control assessments with [PARAM ra-05_odp.04] to help eliminate similar vulnerabilities in other systems; and

- `ra-5_smt.f`: Employ vulnerability monitoring tools that include the capability to readily update the vulnerabilities to be scanned.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ra-5_smt.a — Monitor and scan for vulnerabilities in the system and hosted applications [PARAM ra-5_prm_1] and when new vulnerabilities potentially affecting the system are identified and reported;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ra-5_smt.b — Employ vulnerability monitoring tools and techniques that facilitate interoperability among tools and automate parts of the vulnerability management process by using standards for:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ra-5_smt.b.1 — Enumerating platforms, software flaws, and improper configurations;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ra-5_smt.b.2 — Formatting checklists and test procedures; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ra-5_smt.b.3 — Measuring vulnerability impact;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ra-5_smt.c — Analyze vulnerability scan reports and results from vulnerability monitoring;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ra-5_smt.d — Remediate legitimate vulnerabilities [PARAM ra-05_odp.03] in accordance with an organizational assessment of risk;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ra-5_smt.e — Share information obtained from the vulnerability monitoring process and control assessments with [PARAM ra-05_odp.04] to help eliminate similar vulnerabilities in other systems; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ra-5_smt.f — Employ vulnerability monitoring tools that include the capability to readily update the vulnerabilities to be scanned.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ra-5_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ra-05_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ra-05_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ra-05_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ra-05_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ra-5_smt.a` — For “Monitor and scan for vulnerabilities in the system and hosted applications [PARAM ra-5_prm_1] and when new vulnerabilities potentially affecting the system are identified and reported;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ra-5_smt.b` — For “Employ vulnerability monitoring tools and techniques that facilitate interoperability among tools and automate parts of the vulnerability management process by using standards for:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ra-5_smt.b.1` — For “Enumerating platforms, software flaws, and improper configurations;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ra-5_smt.b.2` — For “Formatting checklists and test procedures; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ra-5_smt.b.3` — For “Measuring vulnerability impact;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ra-5_smt.c` — For “Analyze vulnerability scan reports and results from vulnerability monitoring;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ra-5_smt.d` — For “Remediate legitimate vulnerabilities [PARAM ra-05_odp.03] in accordance with an organizational assessment of risk;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ra-5_smt.e` — For “Share information obtained from the vulnerability monitoring process and control assessments with [PARAM ra-05_odp.04] to help eliminate similar vulnerabilities in other systems; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ra-5_smt.f` — For “Employ vulnerability monitoring tools that include the capability to readily update the vulnerabilities to be scanned.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ra-5_prm_1` — What approved value applies to **organization-defined frequency and/or randomly in accordance with organization-defined process**? Record the value, scope, approving authority, and decision source.

- `ra-05_odp.01` — What approved value applies to **frequency and/or randomly in accordance with organization-defined process**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency for monitoring systems and hosted applications for vulnerabilities is defined;

- `ra-05_odp.02` — What approved value applies to **frequency and/or randomly in accordance with organization-defined process**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency for scanning systems and hosted applications for vulnerabilities is defined;

- `ra-05_odp.03` — What approved value applies to **response times**? Record the value, scope, approving authority, and decision source.

  - Catalog context: response times to remediate legitimate vulnerabilities in accordance with an organizational assessment of risk are defined;

- `ra-05_odp.04` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles with whom information obtained from the vulnerability scanning process and control assessments is to be shared;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ra-5_obj.a-1` (ra-5_smt.a): systems and hosted applications are monitored for vulnerabilities [PARAM ra-05_odp.01] and when new vulnerabilities potentially affecting the system are identified and reported;

- `ra-5_obj.a-2` (ra-5_smt.a): systems and hosted applications are scanned for vulnerabilities [PARAM ra-05_odp.02] and when new vulnerabilities potentially affecting the system are identified and reported;

- `ra-5_obj.b` (ra-5_smt.b): vulnerability monitoring tools and techniques are employed to facilitate interoperability among tools;

- `ra-5_obj.b.1` (ra-5_smt.b.1): vulnerability monitoring tools and techniques are employed to automate parts of the vulnerability management process by using standards for enumerating platforms, software flaws, and improper configurations;

- `ra-5_obj.b.2` (ra-5_smt.b.2): vulnerability monitoring tools and techniques are employed to facilitate interoperability among tools and to automate parts of the vulnerability management process by using standards for formatting checklists and test procedures;

- `ra-5_obj.b.3` (ra-5_smt.b.3): vulnerability monitoring tools and techniques are employed to facilitate interoperability among tools and to automate parts of the vulnerability management process by using standards for measuring vulnerability impact;

- `ra-5_obj.c` (ra-5_smt.c): vulnerability scan reports and results from vulnerability monitoring are analyzed;

- `ra-5_obj.d` (ra-5_smt.d): legitimate vulnerabilities are remediated [PARAM ra-05_odp.03] in accordance with an organizational assessment of risk;

- `ra-5_obj.e` (ra-5_smt.e): information obtained from the vulnerability monitoring process and control assessments is shared with [PARAM ra-05_odp.04] to help eliminate similar vulnerabilities in other systems;

- `ra-5_obj.f` (ra-5_smt.f): vulnerability monitoring tools that include the capability to readily update the vulnerabilities to be scanned are employed.

#### EXAMINE — `ra-5_asm-examine`

- Risk assessment policy

- procedures addressing vulnerability scanning

- risk assessment

- assessment report

- vulnerability scanning tools and associated configuration documentation

- vulnerability scanning results

- patch and vulnerability management records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ra-5_asm-interview`

- Organizational personnel with risk assessment, control assessment, and vulnerability scanning responsibilities

- organizational personnel with vulnerability scan analysis responsibilities

- organizational personnel with vulnerability remediation responsibilities

- organizational personnel with security responsibilities

- system/network administrators

#### TEST — `ra-5_asm-test`

- Organizational processes for vulnerability scanning, analysis, remediation, and information sharing

- mechanisms supporting and/or implementing vulnerability scanning, analysis, remediation, and information sharing

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ra-5`. The library index records the exact source revision and hash.

- [ISO 29147](https://www.iso.org/standard/72311.html)

- [SP 800-40](https://doi.org/10.6028/NIST.SP.800-40r3)

- [SP 800-53A](https://doi.org/10.6028/NIST.SP.800-53Ar4)

- [SP 800-70](https://doi.org/10.6028/NIST.SP.800-70r4)

- [SP 800-115](https://doi.org/10.6028/NIST.SP.800-115)

- [SP 800-126](https://doi.org/10.6028/NIST.SP.800-126r3)

- [IR 7788](https://doi.org/10.6028/NIST.IR.7788)

- [IR 8011-4](https://doi.org/10.6028/NIST.IR.8011-4)

- [IR 8023](https://doi.org/10.6028/NIST.IR.8023)

- Catalog relationship **related**: `ca-2`.

- Catalog relationship **related**: `ca-7`.

- Catalog relationship **related**: `ca-8`.

- Catalog relationship **related**: `cm-2`.

- Catalog relationship **related**: `cm-4`.

- Catalog relationship **related**: `cm-6`.

- Catalog relationship **related**: `cm-8`.

- Catalog relationship **related**: `ra-2`.

- Catalog relationship **related**: `ra-3`.

- Catalog relationship **related**: `sa-11`.

- Catalog relationship **related**: `sa-15`.

- Catalog relationship **related**: `sc-38`.

- Catalog relationship **related**: `si-2`.

- Catalog relationship **related**: `si-3`.

- Catalog relationship **related**: `si-4`.

- Catalog relationship **related**: `si-7`.

- Catalog relationship **related**: `sr-11`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
