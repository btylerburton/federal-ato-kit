---
title: "PL-2 \u2014 System Security and Privacy Plans"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PL-2 — System Security and Privacy Plans

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

System security and privacy plans are scoped to the system and system components within the defined authorization boundary and contain an overview of the security and privacy requirements for the system and the controls selected to satisfy the requirements. The plans describe the intended application of each selected control in the context of the system with a sufficient level of detail to correctly implement the control and to subsequently assess the effectiveness of the control. The control documentation describes how system-specific and hybrid controls are implemented and the plans and expectations regarding the functionality of the system. System security and privacy plans can also be used in the design and development of systems in support of life cycle-based security and privacy engineering processes. System security and privacy plans are living documents that are updated and adapted throughout the system development life cycle (e.g., during capability determination, analysis of alternatives, requests for proposal, and design reviews). Section 2.1 (catalog reference: `#c3397cc9-83c6-4459-adb2-836739dc1b94`) describes the different types of requirements that are relevant to organizations during the system development life cycle and the relationship between requirements and controls.

Organizations may develop a single, integrated security and privacy plan or maintain separate plans. Security and privacy plans relate security and privacy requirements to a set of controls and control enhancements. The plans describe how the controls and control enhancements meet the security and privacy requirements but do not provide detailed, technical descriptions of the design or implementation of the controls and control enhancements. Security and privacy plans contain sufficient information (including specifications of control parameter values for selection and assignment operations explicitly or by reference) to enable a design and implementation that is unambiguously compliant with the intent of the plans and subsequent determinations of risk to organizational operations and assets, individuals, other organizations, and the Nation if the plan is implemented.

Security and privacy plans need not be single documents. The plans can be a collection of various documents, including documents that already exist. Effective security and privacy plans make extensive use of references to policies, procedures, and additional documents, including design and implementation specifications where more detailed information can be obtained. The use of references helps reduce the documentation associated with security and privacy programs and maintains the security- and privacy-related information in other established management and operational areas, including enterprise architecture, system development life cycle, systems engineering, and acquisition. Security and privacy plans need not contain detailed contingency plan or incident response plan information but can instead provide—explicitly or by reference—sufficient information to define what needs to be accomplished by those plans.

Security- and privacy-related activities that may require coordination and planning with other individuals or groups within the organization include assessments, audits, inspections, hardware and software maintenance, acquisition and supply chain risk management, patch management, and contingency plan testing. Planning and coordination include emergency and nonemergency (i.e., planned or non-urgent unplanned) situations. The process defined by organizations to plan and coordinate security- and privacy-related activities can also be included in other documents, as appropriate.

### Requirements and exact statement parts

- `pl-2_smt`: Statement grouping; see child parts.

- `pl-2_smt.a`: Develop security and privacy plans for the system that:

- `pl-2_smt.a.1`: Are consistent with the organization’s enterprise architecture;

- `pl-2_smt.a.2`: Explicitly define the constituent system components;

- `pl-2_smt.a.3`: Describe the operational context of the system in terms of mission and business processes;

- `pl-2_smt.a.4`: Identify the individuals that fulfill system roles and responsibilities;

- `pl-2_smt.a.5`: Identify the information types processed, stored, and transmitted by the system;

- `pl-2_smt.a.6`: Provide the security categorization of the system, including supporting rationale;

- `pl-2_smt.a.7`: Describe any specific threats to the system that are of concern to the organization;

- `pl-2_smt.a.8`: Provide the results of a privacy risk assessment for systems processing personally identifiable information;

- `pl-2_smt.a.9`: Describe the operational environment for the system and any dependencies on or connections to other systems or system components;

- `pl-2_smt.a.10`: Provide an overview of the security and privacy requirements for the system;

- `pl-2_smt.a.11`: Identify any relevant control baselines or overlays, if applicable;

- `pl-2_smt.a.12`: Describe the controls in place or planned for meeting the security and privacy requirements, including a rationale for any tailoring decisions;

- `pl-2_smt.a.13`: Include risk determinations for security and privacy architecture and design decisions;

- `pl-2_smt.a.14`: Include security- and privacy-related activities affecting the system that require planning and coordination with [PARAM pl-02_odp.01] ; and

- `pl-2_smt.a.15`: Are reviewed and approved by the authorizing official or designated representative prior to plan implementation.

- `pl-2_smt.b`: Distribute copies of the plans and communicate subsequent changes to the plans to [PARAM pl-02_odp.02];

- `pl-2_smt.c`: Review the plans [PARAM pl-02_odp.03];

- `pl-2_smt.d`: Update the plans to address changes to the system and environment of operation or problems identified during plan implementation or control assessments; and

- `pl-2_smt.e`: Protect the plans from unauthorized disclosure and modification.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pl-2_smt.a — Develop security and privacy plans for the system that:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.a.1 — Are consistent with the organization’s enterprise architecture;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.a.2 — Explicitly define the constituent system components;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.a.3 — Describe the operational context of the system in terms of mission and business processes;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.a.4 — Identify the individuals that fulfill system roles and responsibilities;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.a.5 — Identify the information types processed, stored, and transmitted by the system;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.a.6 — Provide the security categorization of the system, including supporting rationale;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.a.7 — Describe any specific threats to the system that are of concern to the organization;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.a.8 — Provide the results of a privacy risk assessment for systems processing personally identifiable information;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.a.9 — Describe the operational environment for the system and any dependencies on or connections to other systems or system components;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.a.10 — Provide an overview of the security and privacy requirements for the system;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.a.11 — Identify any relevant control baselines or overlays, if applicable;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.a.12 — Describe the controls in place or planned for meeting the security and privacy requirements, including a rationale for any tailoring decisions;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.a.13 — Include risk determinations for security and privacy architecture and design decisions;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.a.14 — Include security- and privacy-related activities affecting the system that require planning and coordination with [PARAM pl-02_odp.01] ; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.a.15 — Are reviewed and approved by the authorizing official or designated representative prior to plan implementation.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.b — Distribute copies of the plans and communicate subsequent changes to the plans to [PARAM pl-02_odp.02];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.c — Review the plans [PARAM pl-02_odp.03];
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.d — Update the plans to address changes to the system and environment of operation or problems identified during plan implementation or control assessments; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pl-2_smt.e — Protect the plans from unauthorized disclosure and modification.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pl-02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pl-02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pl-02_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pl-2_smt.a` — For “Develop security and privacy plans for the system that:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.a.1` — For “Are consistent with the organization’s enterprise architecture;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.a.2` — For “Explicitly define the constituent system components;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.a.3` — For “Describe the operational context of the system in terms of mission and business processes;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.a.4` — For “Identify the individuals that fulfill system roles and responsibilities;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.a.5` — For “Identify the information types processed, stored, and transmitted by the system;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.a.6` — For “Provide the security categorization of the system, including supporting rationale;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.a.7` — For “Describe any specific threats to the system that are of concern to the organization;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.a.8` — For “Provide the results of a privacy risk assessment for systems processing personally identifiable information;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.a.9` — For “Describe the operational environment for the system and any dependencies on or connections to other systems or system components;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.a.10` — For “Provide an overview of the security and privacy requirements for the system;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.a.11` — For “Identify any relevant control baselines or overlays, if applicable;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.a.12` — For “Describe the controls in place or planned for meeting the security and privacy requirements, including a rationale for any tailoring decisions;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.a.13` — For “Include risk determinations for security and privacy architecture and design decisions;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.a.14` — For “Include security- and privacy-related activities affecting the system that require planning and coordination with [PARAM pl-02_odp.01] ; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.a.15` — For “Are reviewed and approved by the authorizing official or designated representative prior to plan implementation.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.b` — For “Distribute copies of the plans and communicate subsequent changes to the plans to [PARAM pl-02_odp.02];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.c` — For “Review the plans [PARAM pl-02_odp.03];”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.d` — For “Update the plans to address changes to the system and environment of operation or problems identified during plan implementation or control assessments; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pl-2_smt.e` — For “Protect the plans from unauthorized disclosure and modification.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pl-02_odp.01` — What approved value applies to **individuals or groups**? Record the value, scope, approving authority, and decision source.

  - Catalog context: individuals or groups with whom security and privacy-related activities affecting the system that require planning and coordination is/are assigned;

- `pl-02_odp.02` — What approved value applies to **personnel or roles**? Record the value, scope, approving authority, and decision source.

  - Catalog context: personnel or roles to receive distributed copies of the system security and privacy plans is/are assigned;

- `pl-02_odp.03` — What approved value applies to **frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency to review system security and privacy plans is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pl-2_obj.a.1-1` (pl-2_smt.a.1): a security plan for the system is developed that is consistent with the organization’s enterprise architecture;

- `pl-2_obj.a.1-2` (pl-2_smt.a.1): a privacy plan for the system is developed that is consistent with the organization’s enterprise architecture;

- `pl-2_obj.a.2-1` (pl-2_smt.a.2): a security plan for the system is developed that explicitly defines the constituent system components;

- `pl-2_obj.a.2-2` (pl-2_smt.a.2): a privacy plan for the system is developed that explicitly defines the constituent system components;

- `pl-2_obj.a.3-1` (pl-2_smt.a.3): a security plan for the system is developed that describes the operational context of the system in terms of mission and business processes;

- `pl-2_obj.a.3-2` (pl-2_smt.a.3): a privacy plan for the system is developed that describes the operational context of the system in terms of mission and business processes;

- `pl-2_obj.a.4-1` (pl-2_smt.a.4): a security plan for the system is developed that identifies the individuals that fulfill system roles and responsibilities;

- `pl-2_obj.a.4-2` (pl-2_smt.a.4): a privacy plan for the system is developed that identifies the individuals that fulfill system roles and responsibilities;

- `pl-2_obj.a.5-1` (pl-2_smt.a.5): a security plan for the system is developed that identifies the information types processed, stored, and transmitted by the system;

- `pl-2_obj.a.5-2` (pl-2_smt.a.5): a privacy plan for the system is developed that identifies the information types processed, stored, and transmitted by the system;

- `pl-2_obj.a.6-1` (pl-2_smt.a.6): a security plan for the system is developed that provides the security categorization of the system, including supporting rationale;

- `pl-2_obj.a.6-2` (pl-2_smt.a.6): a privacy plan for the system is developed that provides the security categorization of the system, including supporting rationale;

- `pl-2_obj.a.7-1` (pl-2_smt.a.7): a security plan for the system is developed that describes any specific threats to the system that are of concern to the organization;

- `pl-2_obj.a.7-2` (pl-2_smt.a.7): a privacy plan for the system is developed that describes any specific threats to the system that are of concern to the organization;

- `pl-2_obj.a.8-1` (pl-2_smt.a.8): a security plan for the system is developed that provides the results of a privacy risk assessment for systems processing personally identifiable information;

- `pl-2_obj.a.8-2` (pl-2_smt.a.8): a privacy plan for the system is developed that provides the results of a privacy risk assessment for systems processing personally identifiable information;

- `pl-2_obj.a.9-1` (pl-2_smt.a.9): a security plan for the system is developed that describes the operational environment for the system and any dependencies on or connections to other systems or system components;

- `pl-2_obj.a.9-2` (pl-2_smt.a.9): a privacy plan for the system is developed that describes the operational environment for the system and any dependencies on or connections to other systems or system components;

- `pl-2_obj.a.10-1` (pl-2_smt.a.10): a security plan for the system is developed that provides an overview of the security requirements for the system;

- `pl-2_obj.a.10-2` (pl-2_smt.a.10): a privacy plan for the system is developed that provides an overview of the privacy requirements for the system;

- `pl-2_obj.a.11-1` (pl-2_smt.a.11): a security plan for the system is developed that identifies any relevant control baselines or overlays, if applicable;

- `pl-2_obj.a.11-2` (pl-2_smt.a.11): a privacy plan for the system is developed that identifies any relevant control baselines or overlays, if applicable;

- `pl-2_obj.a.12-1` (pl-2_smt.a.12): a security plan for the system is developed that describes the controls in place or planned for meeting the security requirements, including rationale for any tailoring decisions;

- `pl-2_obj.a.12-2` (pl-2_smt.a.12): a privacy plan for the system is developed that describes the controls in place or planned for meeting the privacy requirements, including rationale for any tailoring decisions;

- `pl-2_obj.a.13-1` (pl-2_smt.a.13): a security plan for the system is developed that includes risk determinations for security architecture and design decisions;

- `pl-2_obj.a.13-2` (pl-2_smt.a.13): a privacy plan for the system is developed that includes risk determinations for privacy architecture and design decisions;

- `pl-2_obj.a.14-1` (pl-2_smt.a.14): a security plan for the system is developed that includes security-related activities affecting the system that require planning and coordination with [PARAM pl-02_odp.01];

- `pl-2_obj.a.14-2` (pl-2_smt.a.14): a privacy plan for the system is developed that includes privacy-related activities affecting the system that require planning and coordination with [PARAM pl-02_odp.01];

- `pl-2_obj.a.15-1` (pl-2_smt.a.15): a security plan for the system is developed that is reviewed and approved by the authorizing official or designated representative prior to plan implementation;

- `pl-2_obj.a.15-2` (pl-2_smt.a.15): a privacy plan for the system is developed that is reviewed and approved by the authorizing official or designated representative prior to plan implementation.

- `pl-2_obj.b-1` (pl-2_smt.b): copies of the plans are distributed to [PARAM pl-02_odp.02];

- `pl-2_obj.b-2` (pl-2_smt.b): subsequent changes to the plans are communicated to [PARAM pl-02_odp.02];

- `pl-2_obj.c` (pl-2_smt.c): plans are reviewed [PARAM pl-02_odp.03];

- `pl-2_obj.d-1` (pl-2_smt.d): plans are updated to address changes to the system and environment of operations;

- `pl-2_obj.d-2` (pl-2_smt.d): plans are updated to address problems identified during the plan implementation;

- `pl-2_obj.d-3` (pl-2_smt.d): plans are updated to address problems identified during control assessments;

- `pl-2_obj.e-1` (pl-2_smt.e): plans are protected from unauthorized disclosure;

- `pl-2_obj.e-2` (pl-2_smt.e): plans are protected from unauthorized modification.

#### EXAMINE — `pl-2_asm-examine`

- Security and privacy planning policy

- procedures addressing system security and privacy plan development and implementation

- procedures addressing security and privacy plan reviews and updates

- enterprise architecture documentation

- system security plan

- privacy plan

- records of system security and privacy plan reviews and updates

- security and privacy architecture and design documentation

- risk assessments

- risk assessment results

- control assessment documentation

- other relevant documents or records

#### INTERVIEW — `pl-2_asm-interview`

- Organizational personnel with system security and privacy planning and plan implementation responsibilities

- system developers

- organizational personnel with information security and privacy responsibilities

#### TEST — `pl-2_asm-test`

- Organizational processes for system security and privacy plan development, review, update, and approval

- mechanisms supporting the system security and privacy plan

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pl-2`. The library index records the exact source revision and hash.

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [SP 800-18](https://doi.org/10.6028/NIST.SP.800-18r1)

- [SP 800-37](https://doi.org/10.6028/NIST.SP.800-37r2)

- [SP 800-160-1](https://doi.org/10.6028/NIST.SP.800-160v1)

- [SP 800-160-2](https://doi.org/10.6028/NIST.SP.800-160v2)

- Catalog relationship **related**: `ac-2`.

- Catalog relationship **related**: `ac-6`.

- Catalog relationship **related**: `ac-14`.

- Catalog relationship **related**: `ac-17`.

- Catalog relationship **related**: `ac-20`.

- Catalog relationship **related**: `ca-2`.

- Catalog relationship **related**: `ca-3`.

- Catalog relationship **related**: `ca-7`.

- Catalog relationship **related**: `cm-9`.

- Catalog relationship **related**: `cm-13`.

- Catalog relationship **related**: `cp-2`.

- Catalog relationship **related**: `cp-4`.

- Catalog relationship **related**: `ir-4`.

- Catalog relationship **related**: `ir-8`.

- Catalog relationship **related**: `ma-4`.

- Catalog relationship **related**: `ma-5`.

- Catalog relationship **related**: `mp-4`.

- Catalog relationship **related**: `mp-5`.

- Catalog relationship **related**: `pl-7`.

- Catalog relationship **related**: `pl-8`.

- Catalog relationship **related**: `pl-10`.

- Catalog relationship **related**: `pl-11`.

- Catalog relationship **related**: `pm-1`.

- Catalog relationship **related**: `pm-7`.

- Catalog relationship **related**: `pm-8`.

- Catalog relationship **related**: `pm-9`.

- Catalog relationship **related**: `pm-10`.

- Catalog relationship **related**: `pm-11`.

- Catalog relationship **related**: `ra-3`.

- Catalog relationship **related**: `ra-8`.

- Catalog relationship **related**: `ra-9`.

- Catalog relationship **related**: `sa-5`.

- Catalog relationship **related**: `sa-17`.

- Catalog relationship **related**: `sa-22`.

- Catalog relationship **related**: `si-12`.

- Catalog relationship **related**: `sr-2`.

- Catalog relationship **related**: `sr-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
