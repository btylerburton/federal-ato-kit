---
title: "SA-8.24 \u2014 Secure Failure and Recovery"
description: "Generated catalog-grounded illustrative control guidance"
status: draft
tier: 3
---

# SA-8.24 — Secure Failure and Recovery

## Catalog-grounded response guidance

Template guidance only. This material does not establish implementation, applicability, inheritance, or assessment status.

### Control-specific description (catalog guidance)

The principle of secure failure and recovery states that neither a failure in a system function or mechanism nor any recovery action in response to failure leads to a violation of security policy. The principle of secure failure and recovery parallels the principle of continuous protection to ensure that a system is capable of detecting (within limits) actual and impending failure at any stage of its operation (i.e., initialization, normal operation, shutdown, and maintenance) and to take appropriate steps to ensure that security policies are not violated. In addition, when specified, the system is capable of recovering from impending or actual failure to resume normal, degraded, or alternative secure operations while ensuring that a secure state is maintained such that security policies are not violated.

Failure is a condition in which the behavior of a component deviates from its specified or expected behavior for an explicitly documented input. Once a failed security function is detected, the system may reconfigure itself to circumvent the failed component while maintaining security and provide all or part of the functionality of the original system, or it may completely shut itself down to prevent any further violation of security policies. For this to occur, the reconfiguration functions of the system are designed to ensure continuous enforcement of security policy during the various phases of reconfiguration.

Another technique that can be used to recover from failures is to perform a rollback to a secure state (which may be the initial state) and then either shutdown or replace the service or component that failed such that secure operations may resume. Failure of a component may or may not be detectable to the components using it. The principle of secure failure indicates that components fail in a state that denies rather than grants access. For example, a nominally "atomic" operation interrupted before completion does not violate security policy and is designed to handle interruption events by employing higher-level atomicity and rollback mechanisms (e.g., transactions). If a service is being used, its atomicity properties are well-documented and characterized so that the component availing itself of that service can detect and handle interruption events appropriately. For example, a system is designed to gracefully respond to disconnection and support resynchronization and data consistency after disconnection.

Failure protection strategies that employ replication of policy enforcement mechanisms, sometimes called defense in depth, can allow the system to continue in a secure state even when one mechanism has failed to protect the system. If the mechanisms are similar, however, the additional protection may be illusory, as the adversary can simply attack in series. Similarly, in a networked system, breaking the security on one system or service may enable an attacker to do the same on other similar replicated systems and services. By employing multiple protection mechanisms whose features are significantly different, the possibility of attack replication or repetition can be reduced. Analyses are conducted to weigh the costs and benefits of such redundancy techniques against increased resource usage and adverse effects on the overall system performance. Additional analyses are conducted as the complexity of these mechanisms increases, as could be the case for dynamic behaviors. Increased complexity generally reduces trustworthiness. When a resource cannot be continuously protected, it is critical to detect and repair any security breaches before the resource is once again used in a secure context.

### Requirements and exact statement parts

- `sa-8.24_smt`: Implement the security design principle of secure failure and recovery in [PARAM sa-8.24_prm_1].

### Illustrative parameterized response

<!--
ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.

Replace every placeholder with verified system facts before using a response.

System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].

Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix].


Response for sa-8.24_smt — Implement the security design principle of secure failure and recovery in [PARAM sa-8.24_prm_1].
[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in [COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. Operation is triggered by [EVENT/FREQUENCY]. [EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. [EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.

Parameter sa-8.24_prm_1: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sa-08.24_odp.01: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].

Parameter sa-08.24_odp.02: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].
-->

### Questions to complete the real response

- `sa-8.24_smt` — For “Implement the security design principle of secure failure and recovery in [PARAM sa-8.24_prm_1].”, who performs the action, using which mechanism, on which components, and on what event or schedule? Cite evidence of the actual outcome and identify gaps. Apply the parent statement context to child parts.

### Parameter decisions

- `sa-8.24_prm_1` — What approved value applies to **organization-defined systems or system components**? Record the value, scope, approving authority, and decision source.

- `sa-08.24_odp.01` — What approved value applies to **systems or system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems or system components that implement the security design principle of secure failure are defined;

- `sa-08.24_odp.02` — What approved value applies to **systems or system components**? Record the value, scope, approving authority, and decision source.

  - Catalog context: systems or system components that implement the security design principle of secure recovery are defined;

### Catalog assessment objectives and evidence

These are catalog assessment targets, not collected evidence or passing results. Select applicable objects, register actual evidence, and record dated observations.

- `sa-8.24_obj-1` (sa-8.24_smt): [PARAM sa-08.24_odp.01] implement the security design principle of secure failure;

- `sa-8.24_obj-2` (sa-8.24_smt): [PARAM sa-08.24_odp.02] implement the security design principle of secure recovery.

#### EXAMINE — `sa-8.24_asm-examine`

- System and services acquisition policy

- system and communications protection policy

- contingency planning policy

- procedures addressing information system recovery and reconstitution

- procedures addressing the security design principle of secure failure and recovery used in the specification, design, development, implementation, and modification of the system

- contingency plan

- procedures addressing system backup

- contingency plan test documentation

- contingency plan test results

- system design documentation

- security and privacy requirements and specifications for the system

- system security and privacy architecture

- system security plan

- other relevant documents or records

#### INTERVIEW — `sa-8.24_asm-interview`

- Organizational personnel with the responsibility for determining system security and privacy requirements

- organizational personnel with system specification, design, development, implementation, and modification responsibilities

- organizational personnel with contingency plan testing responsibilities

- organizational personnel with system recovery and reconstitution responsibilities

- system developers

- organizational personnel with information security responsibilities

- organizational personnel with information system backup responsibilities

#### TEST — `sa-8.24_asm-test`

- Organizational processes for applying the security design principle of secure failure and recovery in system specification, design, development, implementation, and modification

- mechanisms supporting the application of the security design principle of secure failure and recovery in system specification, design, development, implementation, and modification

- mechanisms supporting and/or implementing secure failure

- organizational processes for contingency plan testing

- mechanisms supporting contingency plan testing

- mechanisms supporting recovery and reconstitution of the system

- organizational processes for conducting system backups

- mechanisms supporting and/or implementing system backups

### Authoritative sources

- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)

- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)

- Pinned OSCAL catalog version: 5.2.0; record ID: `sa-8.24`. The library index records the exact source revision and hash.

- Catalog relationship **required**: `sa-8`.

- Catalog relationship **related**: `cp-10`.

- Catalog relationship **related**: `cp-12`.

- Catalog relationship **related**: `sc-7`.

- Catalog relationship **related**: `sc-8`.

- Catalog relationship **related**: `sc-24`.

- Catalog relationship **related**: `si-13`.

## Toolkit documents and examples

- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)
- [Verification record template: capture actual checks](../../docs/templates/verification.md)
- [Synthetic evidence manifest example](../claims.json)
- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)

These help organize supporting evidence; their presence does not satisfy the control.
