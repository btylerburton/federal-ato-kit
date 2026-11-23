---
title: "CA-2.3 \u2014 Leveraging Results from External Organizations"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# CA-2.3 — Leveraging Results from External Organizations

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizations may rely on control assessments of organizational systems by other (external) organizations. Using such assessments and reusing existing assessment evidence can decrease the time and resources required for assessments by limiting the independent assessment activities that organizations need to perform. The factors that organizations consider in determining whether to accept assessment results from external organizations can vary. Such factors include the organization’s past experience with the organization that conducted the assessment, the reputation of the assessment organization, the level of detail of supporting assessment evidence provided, and mandates imposed by applicable laws, executive orders, directives, regulations, policies, standards, and guidelines. Accredited testing laboratories that support the Common Criteria Program ISO 15408-1 (catalog reference: `#6afc1b04-c9d6-4023-adbc-f8fbe33a3c73`) , the NIST Cryptographic Module Validation Program (CMVP), or the NIST Cryptographic Algorithm Validation Program (CAVP) can provide independent assessment results that organizations can leverage.

### Requirements and exact statement parts

- `ca-2.3_smt`: Leverage the results of control assessments performed by [PARAM ca-02.03_odp.01] on [PARAM ca-02.03_odp.02] when the assessment meets [PARAM ca-02.03_odp.03].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ca-2.3_smt — Leverage the results of control assessments performed by [PARAM ca-02.03_odp.01] on [PARAM ca-02.03_odp.02] when the assessment meets [PARAM ca-02.03_odp.03].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter ca-02.03_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ca-02.03_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter ca-02.03_odp.03: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `ca-2.3_smt` — For “Leverage the results of control assessments performed by [PARAM ca-02.03_odp.01] on [PARAM ca-02.03_odp.02] when the assessment meets [PARAM ca-02.03_odp.03].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `ca-02.03_odp.01` — What approved value applies to **external organization(s)**? Record the value, scope, approving authority, and decision source.

  - Catalog context: external organization(s) from which the results of control assessments are leveraged are defined;

- `ca-02.03_odp.02` — What approved value applies to **system**? Record the value, scope, approving authority, and decision source.

  - Catalog context: system on which a control assessment was performed by an external organization is defined;

- `ca-02.03_odp.03` — What approved value applies to **requirements**? Record the value, scope, approving authority, and decision source.

  - Catalog context: requirements to be met by the control assessment performed by an external organization on the system are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ca-2.3_obj` (ca-2.3_smt): the results of control assessments performed by [PARAM ca-02.03_odp.01] on [PARAM ca-02.03_odp.02] are leveraged when the assessment meets [PARAM ca-02.03_odp.03].

#### EXAMINE — `ca-2.3_asm-examine`

- Assessment, authorization, and monitoring policy

- procedures addressing control assessments

- control assessment requirements

- control assessment plan

- control assessment report

- control assessment evidence

- plan of action and milestones

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ca-2.3_asm-interview`

- Organizational personnel with control assessment responsibilities

- organizational personnel with information security and privacy responsibilities

- personnel performing control assessments for the specified external organization

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ca-2.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ca-2`.

- Catalog relationship **related**: `sa-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
