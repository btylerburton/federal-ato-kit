---
title: "RA-2 \u2014 Security Categorization"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# RA-2 — Security Categorization

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Security categories describe the potential adverse impacts or negative consequences to organizational operations, organizational assets, and individuals if organizational information and systems are compromised through a loss of confidentiality, integrity, or availability. Security categorization is also a type of asset loss characterization in systems security engineering processes that is carried out throughout the system development life cycle. Organizations can use privacy risk assessments or privacy impact assessments to better understand the potential adverse effects on individuals. CNSSI 1253 (catalog reference: `#4e4fbc93-333d-45e6-a875-de36b878b6b9`) provides additional guidance on categorization for national security systems.

Organizations conduct the security categorization process as an organization-wide activity with the direct involvement of chief information officers, senior agency information security officers, senior agency officials for privacy, system owners, mission and business owners, and information owners or stewards. Organizations consider the potential adverse impacts to other organizations and, in accordance with USA PATRIOT (catalog reference: `#13f0c39d-eaf7-417a-baef-69a041878bb5`) and Homeland Security Presidential Directives, potential national-level adverse impacts.

Security categorization processes facilitate the development of inventories of information assets and, along with CM-8 (catalog reference: `#cm-8`) , mappings to specific system components where information is processed, stored, or transmitted. The security categorization process is revisited throughout the system development life cycle to ensure that the security categories remain accurate and relevant.

### Requirements and exact statement parts

- `ra-2_smt`: Statement grouping; see child parts.

- `ra-2_smt.a`: Categorize the system and information it processes, stores, and transmits;

- `ra-2_smt.b`: Document the security categorization results, including supporting rationale, in the security plan for the system; and

- `ra-2_smt.c`: Verify that the authorizing official or authorizing official designated representative reviews and approves the security categorization decision.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ra-2_smt.a — Categorize the system and information it processes, stores, and transmits;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ra-2_smt.b — Document the security categorization results, including supporting rationale, in the security plan for the system; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ra-2_smt.c — Verify that the authorizing official or authorizing official designated representative reviews and approves the security categorization decision.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ra-2_smt.a` — For “Categorize the system and information it processes, stores, and transmits;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ra-2_smt.b` — For “Document the security categorization results, including supporting rationale, in the security plan for the system; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ra-2_smt.c` — For “Verify that the authorizing official or authorizing official designated representative reviews and approves the security categorization decision.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ra-2_obj.a` (ra-2_smt.a): the system and the information it processes, stores, and transmits are categorized;

- `ra-2_obj.b` (ra-2_smt.b): the security categorization results, including supporting rationale, are documented in the security plan for the system;

- `ra-2_obj.c` (ra-2_smt.c): the authorizing official or authorizing official designated representative reviews and approves the security categorization decision.

#### EXAMINE — `ra-2_asm-examine`

- Risk assessment policy

- security planning policy and procedures

- procedures addressing security categorization of organizational information and systems

- security categorization documentation

- system security plan

- privacy plan

- other relevant documents or records

#### INTERVIEW — `ra-2_asm-interview`

- Organizational personnel with security categorization and risk assessment responsibilities

- organizational personnel with security and privacy responsibilities

#### TEST — `ra-2_asm-test`

- Organizational processes for security categorization

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ra-2`. The library index records the exact source revision and hash.

- [FIPS 199](https://doi.org/10.6028/NIST.FIPS.199)

- [FIPS 200](https://doi.org/10.6028/NIST.FIPS.200)

- [SP 800-30](https://doi.org/10.6028/NIST.SP.800-30r1)

- [SP 800-37](https://doi.org/10.6028/NIST.SP.800-37r2)

- [SP 800-39](https://doi.org/10.6028/NIST.SP.800-39)

- [SP 800-60-1](https://doi.org/10.6028/NIST.SP.800-60v1r1)

- [SP 800-60-2](https://doi.org/10.6028/NIST.SP.800-60v2r1)

- [SP 800-160-1](https://doi.org/10.6028/NIST.SP.800-160v1)

- [CNSSI 1253](https://www.cnss.gov/CNSS/issuances/Instructions.cfm)

- [NARA CUI](https://www.archives.gov/cui)

- Catalog relationship **related**: `cm-8`.

- Catalog relationship **related**: `mp-4`.

- Catalog relationship **related**: `pl-2`.

- Catalog relationship **related**: `pl-10`.

- Catalog relationship **related**: `pl-11`.

- Catalog relationship **related**: `pm-7`.

- Catalog relationship **related**: `ra-3`.

- Catalog relationship **related**: `ra-5`.

- Catalog relationship **related**: `ra-7`.

- Catalog relationship **related**: `ra-8`.

- Catalog relationship **related**: `sa-8`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `sc-38`.

- Catalog relationship **related**: `si-12`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
