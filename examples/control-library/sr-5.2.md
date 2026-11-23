---
title: "SR-5.2 \u2014 Assessments Prior to Selection, Acceptance, Modification, or Update"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SR-5.2 — Assessments Prior to Selection, Acceptance, Modification, or Update

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Organizational personnel or independent, external entities conduct assessments of systems, components, products, tools, and services to uncover evidence of tampering, unintentional and intentional vulnerabilities, or evidence of non-compliance with supply chain controls. These include malicious code, malicious processes, defective software, backdoors, and counterfeits. Assessments can include evaluations; design proposal reviews; visual or physical inspection; static and dynamic analyses; visual, x-ray, or magnetic particle inspections; simulations; white, gray, or black box testing; fuzz testing; stress testing; and penetration testing (see SR-6(1) (catalog reference: `#sr-6.1`) ). Evidence generated during assessments is documented for follow-on actions by organizations. The evidence generated during the organizational or independent assessments of supply chain elements may be used to improve supply chain processes and inform the supply chain risk management process. The evidence can be leveraged in follow-on assessments. Evidence and other documentation may be shared in accordance with organizational agreements.

### Requirements and exact statement parts

- `sr-5.2_smt`: Assess the system, system component, or system service prior to selection, acceptance, modification, or update.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sr-5.2_smt — Assess the system, system component, or system service prior to selection, acceptance, modification, or update.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `sr-5.2_smt` — For “Assess the system, system component, or system service prior to selection, acceptance, modification, or update.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sr-5.2_obj-1` (sr-5.2_smt): the system, system component, or system service is assessed prior to selection;

- `sr-5.2_obj-2` (sr-5.2_smt): the system, system component, or system service is assessed prior to acceptance;

- `sr-5.2_obj-3` (sr-5.2_smt): the system, system component, or system service is assessed prior to modification;

- `sr-5.2_obj-4` (sr-5.2_smt): the system, system component, or system service is assessed prior to update.

#### EXAMINE — `sr-5.2_asm-examine`

- System security plan

- system and services acquisition policy

- procedures addressing supply chain protection

- procedures addressing the integration of information security requirements into the acquisition process

- security test and evaluation results

- vulnerability assessment results

- penetration testing results

- organizational risk assessment results

- system security plan

- other relevant documents or records

#### INTERVIEW — `sr-5.2_asm-interview`

- Organizational personnel with system and services acquisition responsibilities

- organizational personnel with information security responsibilities

- organizational personnel with supply chain protection responsibilities

#### TEST — `sr-5.2_asm-test`

- Organizational processes for conducting assessments prior to selection, acceptance, or update

- mechanisms supporting and/or implementing the conducting of assessments prior to selection, acceptance, or update

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sr-5.2`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sr-5`.

- Catalog relationship **related**: `ca-8`.

- Catalog relationship **related**: `ra-5`.

- Catalog relationship **related**: `sa-11`.

- Catalog relationship **related**: `si-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
