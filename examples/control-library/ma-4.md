---
title: "MA-4 \u2014 Nonlocal Maintenance"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-4 — Nonlocal Maintenance

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Nonlocal maintenance and diagnostic activities are conducted by individuals who communicate through either an external or internal network. Local maintenance and diagnostic activities are carried out by individuals who are physically present at the system location and not communicating across a network connection. Authentication techniques used to establish nonlocal maintenance and diagnostic sessions reflect the network access requirements in IA-2 (catalog reference: `#ia-2`) . Strong authentication requires authenticators that are resistant to replay attacks and employ multi-factor authentication. Strong authenticators include PKI where certificates are stored on a token protected by a password, passphrase, or biometric. Enforcing requirements in MA-4 (catalog reference: `#ma-4`) is accomplished, in part, by other controls. SP 800-63B (catalog reference: `#e59c5a7c-8b1f-49ca-8de0-6ee0882180ce`) provides additional guidance on strong authentication and authenticators.

### Requirements and exact statement parts

- `ma-4_smt`: Statement grouping; see child parts.

- `ma-4_smt.a`: Approve and monitor nonlocal maintenance and diagnostic activities;

- `ma-4_smt.b`: Allow the use of nonlocal maintenance and diagnostic tools only as consistent with organizational policy and documented in the security plan for the system;

- `ma-4_smt.c`: Employ strong authentication in the establishment of nonlocal maintenance and diagnostic sessions;

- `ma-4_smt.d`: Maintain records for nonlocal maintenance and diagnostic activities; and

- `ma-4_smt.e`: Terminate session and network connections when nonlocal maintenance is completed.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-4_smt.a — Approve and monitor nonlocal maintenance and diagnostic activities;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-4_smt.b — Allow the use of nonlocal maintenance and diagnostic tools only as consistent with organizational policy and documented in the security plan for the system;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-4_smt.c — Employ strong authentication in the establishment of nonlocal maintenance and diagnostic sessions;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-4_smt.d — Maintain records for nonlocal maintenance and diagnostic activities; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-4_smt.e — Terminate session and network connections when nonlocal maintenance is completed.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ma-4_smt.a` — For “Approve and monitor nonlocal maintenance and diagnostic activities;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-4_smt.b` — For “Allow the use of nonlocal maintenance and diagnostic tools only as consistent with organizational policy and documented in the security plan for the system;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-4_smt.c` — For “Employ strong authentication in the establishment of nonlocal maintenance and diagnostic sessions;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-4_smt.d` — For “Maintain records for nonlocal maintenance and diagnostic activities; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-4_smt.e` — For “Terminate session and network connections when nonlocal maintenance is completed.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-4_obj.a-1` (ma-4_smt.a): nonlocal maintenance and diagnostic activities are approved;

- `ma-4_obj.a-2` (ma-4_smt.a): nonlocal maintenance and diagnostic activities are monitored;

- `ma-4_obj.b-1` (ma-4_smt.b): the use of nonlocal maintenance and diagnostic tools are allowed only as consistent with organizational policy;

- `ma-4_obj.b-2` (ma-4_smt.b): the use of nonlocal maintenance and diagnostic tools are documented in the security plan for the system;

- `ma-4_obj.c` (ma-4_smt.c): strong authentication is employed in the establishment of nonlocal maintenance and diagnostic sessions;

- `ma-4_obj.d` (ma-4_smt.d): records for nonlocal maintenance and diagnostic activities are maintained;

- `ma-4_obj.e-1` (ma-4_smt.e): session connections are terminated when nonlocal maintenance is completed;

- `ma-4_obj.e-2` (ma-4_smt.e): network connections are terminated when nonlocal maintenance is completed.

#### EXAMINE — `ma-4_asm-examine`

- Maintenance policy

- procedures addressing nonlocal system maintenance

- remote access policy

- remote access procedures

- system design documentation

- system configuration settings and associated documentation

- maintenance records

- records of remote access

- diagnostic records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-4_asm-interview`

- Organizational personnel with system maintenance responsibilities

- organizational personnel with information security responsibilities

- system/network administrators

#### TEST — `ma-4_asm-test`

- Organizational processes for managing nonlocal maintenance

- mechanisms implementing, supporting, and/or managing nonlocal maintenance

- mechanisms for strong authentication of nonlocal maintenance diagnostic sessions

- mechanisms for terminating nonlocal maintenance sessions and network connections

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-4`. The library index records the exact source revision and hash.

- [FIPS 140-3](https://doi.org/10.6028/NIST.FIPS.140-3)

- [FIPS 197](https://doi.org/10.6028/NIST.FIPS.197)

- [FIPS 201-2](https://doi.org/10.6028/NIST.FIPS.201-2)

- [SP 800-63-3](https://doi.org/10.6028/NIST.SP.800-63-3)

- [SP 800-88](https://doi.org/10.6028/NIST.SP.800-88r1)

- Catalog relationship **related**: `ac-2`.

- Catalog relationship **related**: `ac-3`.

- Catalog relationship **related**: `ac-6`.

- Catalog relationship **related**: `ac-17`.

- Catalog relationship **related**: `au-2`.

- Catalog relationship **related**: `au-3`.

- Catalog relationship **related**: `ia-2`.

- Catalog relationship **related**: `ia-4`.

- Catalog relationship **related**: `ia-5`.

- Catalog relationship **related**: `ia-8`.

- Catalog relationship **related**: `ma-2`.

- Catalog relationship **related**: `ma-5`.

- Catalog relationship **related**: `pl-2`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `sc-10`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
