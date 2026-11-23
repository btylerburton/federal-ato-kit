---
title: "PT-2 \u2014 Authority to Process Personally Identifiable Information"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PT-2 — Authority to Process Personally Identifiable Information

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The processing of personally identifiable information is an operation or set of operations that the information system or organization performs with respect to personally identifiable information across the information life cycle. Processing includes but is not limited to creation, collection, use, processing, storage, maintenance, dissemination, disclosure, and disposal. Processing operations also include logging, generation, and transformation, as well as analysis techniques, such as data mining.

Organizations may be subject to laws, executive orders, directives, regulations, or policies that establish the organization’s authority and thereby limit certain types of processing of personally identifiable information or establish other requirements related to the processing. Organizational personnel consult with the senior agency official for privacy and legal counsel regarding such authority, particularly if the organization is subject to multiple jurisdictions or sources of authority. For organizations whose processing is not determined according to legal authorities, the organization’s policies and determinations govern how they process personally identifiable information. While processing of personally identifiable information may be legally permissible, privacy risks may still arise. Privacy risk assessments can identify the privacy risks associated with the authorized processing of personally identifiable information and support solutions to manage such risks.

Organizations consider applicable requirements and organizational policies to determine how to document this authority. For federal agencies, the authority to process personally identifiable information is documented in privacy policies and notices, system of records notices, privacy impact assessments, PRIVACT (catalog reference: `#18e71fec-c6fd-475a-925a-5d8495cf8455`) statements, computer matching agreements and notices, contracts, information sharing agreements, memoranda of understanding, and other documentation.

Organizations take steps to ensure that personally identifiable information is only processed for authorized purposes, including training organizational personnel on the authorized processing of personally identifiable information and monitoring and auditing organizational use of personally identifiable information.

### Requirements and exact statement parts

- `pt-2_smt`: Statement grouping; see child parts.

- `pt-2_smt.a`: Determine and document the [PARAM pt-02_odp.01] that permits the [PARAM pt-02_odp.02] of personally identifiable information; and

- `pt-2_smt.b`: Restrict the [PARAM pt-02_odp.03] of personally identifiable information to only that which is authorized.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pt-2_smt.a — Determine and document the [PARAM pt-02_odp.01] that permits the [PARAM pt-02_odp.02] of personally identifiable information; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pt-2_smt.b — Restrict the [PARAM pt-02_odp.03] of personally identifiable information to only that which is authorized.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter pt-02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pt-02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter pt-02_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `pt-2_smt.a` — For “Determine and document the [PARAM pt-02_odp.01] that permits the [PARAM pt-02_odp.02] of personally identifiable information; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pt-2_smt.b` — For “Restrict the [PARAM pt-02_odp.03] of personally identifiable information to only that which is authorized.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `pt-02_odp.01` — What approved value applies to **authority**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the authority to permit the processing (defined in PT-02_ODP[02]) of personally identifiable information is defined;

- `pt-02_odp.02` — What approved value applies to **processing**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the type of processing of personally identifiable information is defined;

- `pt-02_odp.03` — What approved value applies to **processing**? Record the value, scope, approving authority, and decision source.

  - Catalog context: the type of processing of personally identifiable information to be restricted is defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pt-2_obj.a` (pt-2_smt.a): the [PARAM pt-02_odp.01] that permits the [PARAM pt-02_odp.02] of personally identifiable information is determined and documented;

- `pt-2_obj.b` (pt-2_smt.b): the [PARAM pt-02_odp.03] of personally identifiable information is restricted to only that which is authorized.

#### EXAMINE — `pt-2_asm-examine`

- Personally identifiable information processing and transparency policy and procedures

- privacy plan

- other relevant documents or records

#### INTERVIEW — `pt-2_asm-interview`

- Organizational personnel with personally identifiable information processing and transparency responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `pt-2_asm-test`

- Organizational processes for authorizing the processing of personally identifiable information

- mechanisms supporting and/or implementing the restriction of personally identifiable information processing

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pt-2`. The library index records the exact source revision and hash.

- [PRIVACT](https://www.govinfo.gov/content/pkg/STATUTE-88/pdf/STATUTE-88-Pg1896.pdf)

- [OMB A-130](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/circulars/A130/a130revised.pdf)

- [IR 8112](https://doi.org/10.6028/NIST.IR.8112)

- Catalog relationship **related**: `ac-2`.

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `cm-13`.

- Catalog relationship **related**: `ir-9`.

- Catalog relationship **related**: `pm-9`.

- Catalog relationship **related**: `pm-24`.

- Catalog relationship **related**: `pt-1`.

- Catalog relationship **related**: `pt-3`.

- Catalog relationship **related**: `pt-5`.

- Catalog relationship **related**: `pt-6`.

- Catalog relationship **related**: `ra-3`.

- Catalog relationship **related**: `ra-8`.

- Catalog relationship **related**: `si-12`.

- Catalog relationship **related**: `si-18`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
