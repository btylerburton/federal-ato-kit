---
title: "RA-5.10 \u2014 Correlate Scanning Information"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# RA-5.10 — Correlate Scanning Information

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

An attack vector is a path or means by which an adversary can gain access to a system in order to deliver malicious code or exfiltrate information. Organizations can use attack trees to show how hostile activities by adversaries interact and combine to produce adverse impacts or negative consequences to systems and organizations. Such information, together with correlated data from vulnerability scanning tools, can provide greater clarity regarding multi-vulnerability and multi-hop attack vectors. The correlation of vulnerability scanning information is especially important when organizations are transitioning from older technologies to newer technologies (e.g., transitioning from IPv4 to IPv6 network protocols). During such transitions, some system components may inadvertently be unmanaged and create opportunities for adversary exploitation.

### Requirements and exact statement parts

- `ra-5.10_smt`: Correlate the output from vulnerability scanning tools to determine the presence of multi-vulnerability and multi-hop attack vectors.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for ra-5.10_smt — Correlate the output from vulnerability scanning tools to determine the presence of multi-vulnerability and multi-hop attack vectors.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `ra-5.10_smt` — For “Correlate the output from vulnerability scanning tools to determine the presence of multi-vulnerability and multi-hop attack vectors.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `ra-5.10_obj` (ra-5.10_smt): the output from vulnerability scanning tools is correlated to determine the presence of multi-vulnerability and multi-hop attack vectors.

#### EXAMINE — `ra-5.10_asm-examine`

- Risk assessment policy

- procedures addressing vulnerability scanning

- risk assessment

- vulnerability scanning tools and techniques documentation

- vulnerability scanning results

- vulnerability management records

- audit records

- event/vulnerability correlation logs

- system security plan

- other relevant documents or records

#### INTERVIEW — `ra-5.10_asm-interview`

- Organizational personnel with vulnerability scanning responsibilities

- organizational personnel with vulnerability scan analysis responsibilities

- organizational personnel with security responsibilities

#### TEST — `ra-5.10_asm-test`

- Organizational processes for vulnerability scanning

- mechanisms/tools supporting and/or implementing vulnerability scanning

- mechanisms implementing the correlation of vulnerability scan results

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `ra-5.10`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `ra-5`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
