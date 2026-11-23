---
title: "PT-7.1 \u2014 Social Security Numbers"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# PT-7.1 — Social Security Numbers

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Federal law and policy establish specific requirements for organizations’ processing of Social Security numbers. Organizations take steps to eliminate unnecessary uses of Social Security numbers and other sensitive information and observe any particular requirements that apply.

### Requirements and exact statement parts

- `pt-7.1_smt`: When a system processes Social Security numbers:

- `pt-7.1_smt.a`: Eliminate unnecessary collection, maintenance, and use of Social Security numbers, and explore alternatives to their use as a personal identifier;

- `pt-7.1_smt.b`: Do not deny any individual any right, benefit, or privilege provided by law because of such individual’s refusal to disclose his or her Social Security number; and

- `pt-7.1_smt.c`: Inform any individual who is asked to disclose his or her Social Security number whether that disclosure is mandatory or voluntary, by what statutory or other authority such number is solicited, and what uses will be made of it.

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for pt-7.1_smt — When a system processes Social Security numbers:
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pt-7.1_smt.a — Eliminate unnecessary collection, maintenance, and use of Social Security numbers, and explore alternatives to their use as a personal identifier;
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pt-7.1_smt.b — Do not deny any individual any right, benefit, or privilege provided by law because of such individual’s refusal to disclose his or her Social Security number; and
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.


Response for pt-7.1_smt.c — Inform any individual who is asked to disclose his or her Social Security number whether that disclosure is mandatory or voluntary, by what statutory or other authority such number is solicited, and what uses will be made of it.
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.
-->

### Questions to complete the real response

- `pt-7.1_smt` — For “When a system processes Social Security numbers:”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pt-7.1_smt.a` — For “Eliminate unnecessary collection, maintenance, and use of Social Security numbers, and explore alternatives to their use as a personal identifier;”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pt-7.1_smt.b` — For “Do not deny any individual any right, benefit, or privilege provided by law because of such individual’s refusal to disclose his or her Social Security number; and”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

- `pt-7.1_smt.c` — For “Inform any individual who is asked to disclose his or her Social Security number whether that disclosure is mandatory or voluntary, by what statutory or other authority such number is solicited, and what uses will be made of it.”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

The catalog defines no organization-assigned parameters for this control.

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `pt-7.1_obj.a-1` (pt-7.1_smt.a): when a system processes Social Security numbers, the unnecessary collection, maintenance, and use of Social Security numbers are eliminated;

- `pt-7.1_obj.a-2` (pt-7.1_smt.a): when a system processes Social Security numbers, alternatives to the use of Social Security Numbers as a personal identifier are explored;

- `pt-7.1_obj.b` (pt-7.1_smt.b): when a system processes Social Security numbers, individual rights, benefits, or privileges provided by law are not denied because of an individual’s refusal to disclose their Social Security number;

- `pt-7.1_obj.c-1` (pt-7.1_smt.c): when a system processes Social Security numbers, any individual who is asked to disclose their Social Security number is informed whether that disclosure is mandatory or voluntary, by what statutory or other authority such number is solicited, and what uses will be made of it;

- `pt-7.1_obj.c-2` (pt-7.1_smt.c): when a system processes Social Security numbers, any individual who is asked to disclose their Social Security number is informed by what statutory or other authority the number is solicited;

- `pt-7.1_obj.c-3` (pt-7.1_smt.c): when a system processes Social Security numbers, any individual who is asked to disclose their Social Security number is informed what uses will be made of it.

#### EXAMINE — `pt-7.1_asm-examine`

- Personally identifiable information processing and transparency policy and procedures

- privacy notice

- Privacy Act system of records

- privacy notice

- separate notice regarding the use of Social Security numbers

- privacy plan

- other relevant documents or records

#### INTERVIEW — `pt-7.1_asm-interview`

- Organizational personnel with personally identifiable information processing and transparency responsibilities

- organizational personnel with information security and privacy responsibilities

#### TEST — `pt-7.1_asm-test`

- Organizational processes for identifying, reviewing, and taking action to control the unnecessary use of Social Security numbers

- implementation of an alternative to Social Security numbers as identifiers

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `pt-7.1`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `pt-7`.

- Catalog relationship **related**: `ia-4`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
