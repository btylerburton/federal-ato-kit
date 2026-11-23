---
title: "CA-2.2 \u2014 Specialized Assessments"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CA-2.2 — Specialized Assessments

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations can conduct specialized assessments, including verification and validation, system monitoring, insider threat assessments, malicious user testing, and other forms of testing. These assessments can improve readiness by exercising organizational capabilities and indicating current levels of performance as a means of focusing actions to improve security and privacy. Organizations conduct specialized assessments in accordance with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines. Authorizing officials approve the assessment methods in coordination with the organizational risk executive function. Organizations can include vulnerabilities uncovered during assessments into vulnerability remediation processes. Specialized assessments can also be conducted early in the system development life cycle (e.g., during initial design, development, and unit testing).

### Requirements and exact statement parts

- `ca-2.2_smt`: Include as part of control assessments, [PARAM ca-02.02_odp.01], [PARAM ca-02.02_odp.02], [PARAM ca-02.02_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ca-2.2_smt — Include as part of control assessments, [PARAM ca-02.02_odp.01], [PARAM ca-02.02_odp.02], [PARAM ca-02.02_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ca-02.02_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ca-02.02_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ca-02.02_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ca-02.02_odp.04: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ca-2.2_smt` — For “Include as part of control assessments, [PARAM ca-02.02_odp.01], [PARAM ca-02.02_odp.02], [PARAM ca-02.02_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ca-02.02_odp.01` — What approved value applies to **specialized assessment frequency**? Record the value, scope, approving authority, and decision source.

  - Catalog context: frequency at which to include specialized assessments as part of the control assessment is defined;

- `ca-02.02_odp.02` — What approved value applies to **selection; choose one from: announced; unannounced**? Record the value, scope, approving authority, and decision source.

- `ca-02.02_odp.03` — What approved value applies to **selection; choose one-or-more from: in-depth monitoring; security instrumentation; automated security test cases; vulnerability scanning; malicious user testing; insider threat assessment; performance and load testing; data leakage or data loss assessment; [PARAM ca-02.02_odp.04]**? Record the value, scope, approving authority, and decision source.

- `ca-02.02_odp.04` — What approved value applies to **other forms of assessment**? Record the value, scope, approving authority, and decision source.

  - Catalog context: other forms of assessment are defined (if selected);

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ca-2.2_obj` (ca-2.2_smt): [PARAM ca-02.02_odp.01] [PARAM ca-02.02_odp.02] [PARAM ca-02.02_odp.03] are included as part of control assessments.

#### EXAMINE — `ca-2.2_asm-examine`

- Assessment, authorization, and monitoring policy

- procedures addressing control assessments

- control assessment plan

- control assessment report

- control assessment evidence

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ca-2.2_asm-interview`

- Organizational personnel with control assessment responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `ca-2.2_asm-test`

- Mechanisms supporting control assessment

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ca-2.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ca-2`.

- Catalog relationship **related**: `pe-3`.

- Catalog relationship **related**: `si-2`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
