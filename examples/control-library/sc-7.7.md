---
title: "SC-7.7 \u2014 Split Tunneling for Remote Devices"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SC-7.7 — Split Tunneling for Remote Devices

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

Split tunneling is the process of allowing a remote user or device to establish a non-remote connection with a system and simultaneously communicate via some other connection to a resource in an external network. This method of network access enables a user to access remote devices and simultaneously, access uncontrolled networks. Split tunneling might be desirable by remote users to communicate with local system resources, such as printers or file servers. However, split tunneling can facilitate unauthorized external connections, making the system vulnerable to attack and to exfiltration of organizational information. Split tunneling can be prevented by disabling configuration settings that allow such capability in remote devices and by preventing those configuration settings from being configurable by users. Prevention can also be achieved by the detection of split tunneling (or of configuration settings that allow split tunneling) in the remote device, and by prohibiting the connection if the remote device is using split tunneling. A virtual private network (VPN) can be used to securely provision a split tunnel. A securely provisioned VPN includes locking connectivity to exclusive, managed, and named environments, or to a specific set of pre-approved addresses, without user control.

### Requirements and exact statement parts

- `sc-7.7_smt`: Prevent split tunneling for remote devices connecting to organizational systems unless the split tunnel is securely provisioned using [PARAM sc-07.07_odp].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sc-7.7_smt — Prevent split tunneling for remote devices connecting to organizational systems unless the split tunnel is securely provisioned using [PARAM sc-07.07_odp].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sc-07.07_odp: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sc-7.7_smt` — For “Prevent split tunneling for remote devices connecting to organizational systems unless the split tunnel is securely provisioned using [PARAM sc-07.07_odp].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sc-07.07_odp` — What approved value applies to **safeguards**? Record the value, scope, approving authority, and decision source.

  - Catalog context: safeguards to securely provision split tunneling are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sc-7.7_obj` (sc-7.7_smt): split tunneling is prevented for remote devices connecting to organizational systems unless the split tunnel is securely provisioned using [PARAM sc-07.07_odp].

#### EXAMINE — `sc-7.7_asm-examine`

- System and communications protection policy

- procedures addressing boundary protection

- system design documentation

- system hardware and software

- system architecture

- system configuration settings and associated documentation

- system audit records

- system security plan

- other relevant documents or records

#### INTERVIEW — `sc-7.7_asm-interview`

- System/network administrators

- organizational personnel with information security responsibilities

- system developer

- organizational personnel with boundary protection responsibilities

#### TEST — `sc-7.7_asm-test`

- Mechanisms implementing boundary protection capabilities

- mechanisms supporting/restricting non-remote connections

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sc-7.7`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sc-7`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
