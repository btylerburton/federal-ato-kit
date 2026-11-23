---
title: "Claim verification and testing toolkit"
description: "Proof-oriented test selection, evidence contracts, and library integration"
status: draft
tier: 2
last_updated: "2026-11-06"
---

# Test claims, not prose

`tools/ato/registry.json` describes available tool entrypoints and optional dependencies.
Use standard-library integrity checks immediately; dependency-backed adapters
require pinned installation and actual observed execution before they earn PASS.

| Claim | Suitable evidence/test | What it cannot prove |
| --- | --- | --- |
| Migrated excerpt unchanged | SHA-256 comparison to migration manifest and original export | Original narrative accuracy |
| Controls use required profile | OSCAL model validation plus profile resolution/coverage | Implementation effectiveness |
| Report bytes go only to intended endpoint | Browser interception plus approved real-network flow, redirect/error/upload tests | Provider internal processing |
| Sensitive fields excluded from logs | Sentinel-driven tests at all logging/feedback/crash paths; deployed sink inspection | Universal absence of PII from regex filtering |
| Attachment is deleted | Provider delete acknowledgement plus authorized retrieval/retention evidence | Deletion of backups absent provider evidence |
| Identity assurance enforced | Signature/issuer/audience/nonce/expiry/ACR negative tests and authorized real IdP flow | Production configuration from a mock |
| Vulnerabilities assessed | Versioned SAST, secrets, SCA and DAST outputs with scope | Absence of all vulnerabilities |
| Crypto is appropriately validated | Deployment/module certificate evidence and configuration | FIPS validation from TLS/AES labels |

Candidate integrations: compliance-trestle (OSCAL), jsonschema (evidence/model
schemas), pytest/Hypothesis (invariants), Playwright and existing Vitest suites
(browser flows), Semgrep/Bandit (SAST), Gitleaks (secrets), pip-audit/OSV plus the
application package manager's audit (SCA), and approved ZAP/TLS tooling (DAST).
The registry distinguishes standard-library tools from optional integrations.
Trestle, jsonschema, pytest, Hypothesis, pip-audit and Bandit have an optional
hash-locked dependency set. Installation and scan results belong to each environment;
the shared kit does not carry a project's installed-state assertion. Pin versions at adoption,
review licenses and advisories, and avoid overlapping scanners without a purpose.

## Evidence ledger

The initial claim manifest is JSON with `schema_version: 1`, `claims`, and
`evidence`. Each claim has an ID, statement, control IDs, environment,
source revision, required evidence kind, and evidence IDs. Each evidence item
has ID, kind, environment/revision, observation and expiry timestamps, artifact
path/hash, method, result, and concise observed output. Artifact paths are
validated against an explicitly selected evidence root. Do not put raw PII,
tokens, or confidential report text in the ledger.

The CLI verifies this narrow contract and file integrity; it does not authenticate
the observer or decide whether the observation logically proves the claim.
A human/agent reviewer must assess the evidence's relevance and sufficiency.
Missing/expired/wrong-scope evidence cannot yield PASS. A matching FAIL remains
FAIL. Unsupported evidence kinds are rejected rather than guessed.

## Efficient execution

Batch independent read-only inventory checks. Reuse evidence keyed by revision,
scope, tool version/configuration, and artifact digest; invalidate on changes.
Record wall-clock duration and assessed/blocked counts. Have each new guard fail
against a meaningful negative fixture before accepting its positive result.
Run live tests only with explicit target/environment/data authorization. Record
blocked tests, and route operational/process objectives to interviews or provider
evidence rather than inventing an automated pass.
