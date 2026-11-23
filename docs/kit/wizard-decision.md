---
title: "Use explicit answers and pinned profiles for repository-driven SSPP drafts"
description: "Draft architecture decision for control guidance and wizard automation"
status: draft
tier: 2
date: "2026-11-23"
decision_status: proposed
decision_makers: ["Repository owner"]
category: "Deployment and Infrastructure"
nist_controls: ["PL-2", "CM-2", "SA-5", "SA-11"]
ato_relevance: yes-internal
---

# Repository-driven draft generation

## Context

Teams want to point the kit at a repository, answer clarifying questions and generate a
LATO or full ATO preparation document with diagrams. The repository can establish paths and,
under separate review, source mechanisms; it cannot establish every owner, legal, provider,
categorization or operational-evidence fact.

## Drivers and options

Use the existing scaffold/composer/diagram pipeline instead of building another renderer.
Alternatives considered: infer a baseline and implementation from filenames; require a fully
manual monolithic SSPP; or use an explicit-question, pinned-selection draft pipeline.

## Decision

Use the explicit-question pipeline. The initial CLI performs only tracked-path discovery,
persists questions/answers, and generates a review project after essential answers are supplied.
The agent skill separately guides code-semantic review and evidence-backed narrative drafting.
All controls receive catalog-grounded guidance and commented examples; these do not become
active implementation statements. NIST Low/Moderate/High profiles and the approved LATO
reference select exact IDs. Additional privacy/agency tailoring is an owner decision.

## Consequences

The CLI can automate repeatable structure and exports without external model services or
repository code execution. It cannot honestly claim to produce a signed authorization or
fully assessed SSPP from a checkout alone. The first topology comes from user-supplied facts,
with four editable proposed views. More precise automated source-to-control mapping and
view-specific architecture extraction remain tracked increments, not implied features.

Stable project identities and team edits survive reruns. Publication remains a separate
owner-reviewed stage. No new Python dependency or external service is introduced by the CLI.
