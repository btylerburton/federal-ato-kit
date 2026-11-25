---
title: "Use an optional shared source-review artifact before SSPP drafting"
description: "Draft MADR for cited, human-selected findings shared by text and diagrams"
status: draft
tier: 2
date: "2026-11-24"
last_updated: "2026-11-24"
decision_status: proposed
decision_makers: ["Repository owner"]
category: "Data Handling"
nist_controls: ["CM-3", "SA-5", "SA-11", "SI-10"]
ato_relevance: yes-internal
risk_treatment: mitigate
---

# Shared source review

## Context and Problem Statement

The diagram-only agent handoff did not help draft system descriptions or control narratives.
The user approved a shared pre-draft review, optional external/local runner, copyable UI and
proposal compatibility fixes. This kit does not establish the consuming system's impact level.

## Decision Drivers

- No LLM, network, credentials or provider selection required for manual authoring.
- Source citations and human inclusion decisions must remain distinct from control effectiveness.
- Preserve existing answers, review decisions and authored responses.
- Retain strict renderer identifiers without forcing agents to avoid common hyphenated IDs.

## Considered Options

1. Keep source analysis restricted to diagram nodes and ask users to repeat text review.
2. Automatically populate all controls from unrestricted generated prose.
3. Import a pinned-revision source artifact, review each finding and seed attributed candidates.

## Decision Outcome

Use option 3. `source-review/findings.json` records method, author, exact source commit,
findings/citations and optional diagram proposal. Human decisions are saved separately with
history. Only included findings inform drafts; suggested intake replacements require an explicit
preview confirmation. Baseline, owner, approval and inherited status are not inferred.

The existing trusted runner is reused only on explicit operation; it is not an OS sandbox.
Manual and approved-agent handoff use the same schema offline. No new dependency is needed.
Invalid optional diagram data is checked when sent to diagram review, independently of text.
Generation checks immutable findings, revision and existing managed-file hashes, seeds only
pristine/unchanged responses, and registers findings plus provenance in the assembled SSPP.

## Consequences

- Positive: one source pass can support both workflows; citation checks and review history are durable.
- Negative: citation existence is not semantic validation; users still assess source claims and runtime evidence.
- Compatibility: hyphenated IDs are retained in proposal/review data and mapped injectively to
  underscore-safe renderer aliases. Old proposals and existing authored responses remain supported.
- Clipboard uses Textual/terminal OSC 52 and a selectable text view; saved request files remain
  available when terminal clipboard delivery is disabled.

## Links

- [Workflow guide](source-review.md)
- [Agent/offline limits](agent-offline-assessment.md)
- [Work register](wizard-work.json) — WIZ-18
