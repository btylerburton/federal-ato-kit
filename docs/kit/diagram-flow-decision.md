---
title: "Separate text configuration from source-proposed diagram review"
description: "Draft decision for independent wizard text and architecture review workflows"
status: draft
tier: 2
date: "2026-11-24"
decision_status: proposed
decision_makers: ["Repository owner"]
category: "Deployment and Infrastructure"
nist_controls: ["PL-2", "PL-8", "SA-5", "SA-11"]
ato_relevance: yes-internal
---

# Independent diagram review flow

The user found manual topology entry disruptive to text configuration. The approved change
separates system/scope/inheritance questions from diagrams. Text drafts now generate without
topology; an explicit diagram-readiness gap describes remaining work. Existing topology answers
and diagram sources are retained, not silently reinterpreted or overwritten.

Options considered: keep topology mandatory; silently infer a diagram from filenames; or use
a separate, evidence-cited agent proposal and focused clarification workflow. Choose the third.
An authorized agent/LLM source-review pass proposes nodes and relationships at an exact revision.
The diagram flow validates the proposal, retains assumptions, asks for unresolved properties,
records human corrections and renders only after review. Source citations are support for
claims, not evidence of actual deployment or automatic authorization-boundary approval.

The text wizard's informal boundary summary remains a prose scope question. It no longer
requires node/flow JSON, a diagram renderer or a topology screen. Text-only DOCX rendering
requires Pandoc only. The standalone catalog scaffold keeps its opt-in-by-API starter behavior
for existing consumers; the wizard calls it with diagram generation disabled.

The proposal entrypoint accepts an agent-generated artifact; it does not invoke a remote model
or pretend the path-only repository inventory has extracted an architecture. The agent skill
defines that handoff. Distinct view generation must keep components/relationships, inclusion
boundaries and named data flows separate; owner verification of completeness remains necessary.

No new dependency is introduced. Reuse existing source pinning, ownership, renderer and
document composition checks. Preserve staged author work and detect stale/colliding artifacts.
