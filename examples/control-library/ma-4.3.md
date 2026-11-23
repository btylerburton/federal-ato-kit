---
title: "MA-4.3 \u2014 Comparable Security and Sanitization"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# MA-4.3 — Comparable Security and Sanitization

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Comparable security capability on systems, diagnostic tools, and equipment providing maintenance services implies that the implemented controls on those systems, tools, and equipment are at least as comprehensive as the controls on the system being serviced.

### Requirements and exact statement parts

- `ma-4.3_smt`: Statement grouping; see child parts.

- `ma-4.3_smt.a`: Require that nonlocal maintenance and diagnostic services be performed from a system that implements a security capability comparable to the capability implemented on the system being serviced; or

- `ma-4.3_smt.b`: Remove the component to be serviced from the system prior to nonlocal maintenance or diagnostic services; sanitize the component (for organizational information); and after the service is performed, inspect and sanitize the component (for potentially malicious software) before reconnecting the component to the system.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ma-4.3_smt.a — Require that nonlocal maintenance and diagnostic services be performed from a system that implements a security capability comparable to the capability implemented on the system being serviced; or
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for ma-4.3_smt.b — Remove the component to be serviced from the system prior to nonlocal maintenance or diagnostic services; sanitize the component (for organizational information); and after the service is performed, inspect and sanitize the component (for potentially malicious software) before reconnecting the component to the system.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ma-4.3_smt.a` — For “Require that nonlocal maintenance and diagnostic services be performed from a system that implements a security capability comparable to the capability implemented on the system being serviced; or”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `ma-4.3_smt.b` — For “Remove the component to be serviced from the system prior to nonlocal maintenance or diagnostic services; sanitize the component (for organizational information); and after the service is performed, inspect and sanitize the component (for potentially malicious software) before reconnecting the component to the system.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ma-4.3_obj.a-1` (ma-4.3_smt.a): nonlocal maintenance services are required to be performed from a system that implements a security capability comparable to the capability implemented on the system being serviced;

- `ma-4.3_obj.a-2` (ma-4.3_smt.a): nonlocal diagnostic services are required to be performed from a system that implements a security capability comparable to the capability implemented on the system being serviced; or

- `ma-4.3_obj.b-1` (ma-4.3_smt.b): the component to be serviced is removed from the system prior to nonlocal maintenance or diagnostic services;

- `ma-4.3_obj.b-2` (ma-4.3_smt.b): the component to be serviced is sanitized (for organizational information);

- `ma-4.3_obj.b-3` (ma-4.3_smt.b): the component is inspected and sanitized (for potentially malicious software) after the service is performed and before reconnecting the component to the system.

#### EXAMINE — `ma-4.3_asm-examine`

- Maintenance policy

- procedures addressing nonlocal system maintenance

- service provider contracts and/or service-level agreements

- maintenance records

- inspection records

- audit records

- equipment sanitization records

- media sanitization records

- system security plan

- other relevant documents or records

#### INTERVIEW — `ma-4.3_asm-interview`

- Organizational personnel with system maintenance responsibilities

- system maintenance provider

- organizational personnel with information security responsibilities

- organizational personnel responsible for media sanitization

- system/network administrators

#### TEST — `ma-4.3_asm-test`

- Organizational processes for comparable security and sanitization for nonlocal maintenance

- organizational processes for the removal, sanitization, and inspection of components serviced via nonlocal maintenance

- mechanisms supporting and/or implementing component sanitization and inspection

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ma-4.3`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ma-4`.

- Catalog relationship **related**: `mp-6`.

- Catalog relationship **related**: `si-3`.

- Catalog relationship **related**: `si-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
