---
title: "Use a state-aware diagram dashboard with an explicit trusted runner"
description: "Draft decision for automated proposal detection and separately authorized agent execution"
status: draft
tier: 2
date: "2026-11-24"
decision_status: proposed
decision_makers: ["Repository owner"]
category: "Agent Authorization"
nist_controls: ["AC-6", "CM-3", "SA-5", "SA-11"]
ato_relevance: yes-internal
---

# Diagram dashboard and runner boundary

## Context

Users repeatedly ran prepare/review without the missing agent-generated proposal. The CLI
correctly refused review but did not provide a coherent start/resume experience. The user
approved a separate Textual dashboard, automatic valid-proposal detection, readable questions
and a configurable agent handoff.

## Decision

Reuse the existing diagram_flow and attachment contracts behind a state-aware UI. Derive
readiness from current review/file hashes; retain human questions and explicit confirmation.
Without a runner, show a durable exact request. With one, require an operator-owned external
argv configuration and explicit user execution action. Opening/resuming never invokes an agent.
No new model API or dependency is introduced; the wrapper supplies authorized provider policy.

Alternatives considered: automatically run a guessed provider CLI; retain manual command
sequencing; or explicit wrapper plus observable state. Choose the third to avoid provider
assumptions and preserve the user's control of source processing.

## Consequences

The wrapper is trusted local code, not sandboxed application data. No shell is used; command
timeouts are bounded. Logs persist run outcome/hashes rather than provider output or environment
values. Failed output is quarantined and not silently imported. A valid imported proposal is
still only source-cited draft content; no human review is inferred from an agent exit code.

Textual previews are structured text and generated source, not terminal raster rendering.
Actual rendered files and DOCX media checks remain owned by the existing pipeline. Owner
architecture acceptance, provider/network approval and release-environment pinning stay separate.
