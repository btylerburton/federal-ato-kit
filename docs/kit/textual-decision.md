---
title: "Use optional Textual UI with a durable wizard session"
description: "Defaults, validation and resumable state for interactive SSPP authoring"
status: draft
tier: 2
date: "2026-11-24"
decision_status: proposed
decision_makers: ["Repository owner"]
category: "Deployment and Infrastructure"
nist_controls: ["CM-3", "SA-5", "SA-11"]
ato_relevance: yes-internal
---

# Textual wizard interface

## Context

The user reproduced a failed intake: a blank date, uppercase LATO and absent topology were
accepted until final validation; rerunning intake then refused to resume. The user explicitly
selected Textual and approved a local pinned dependency installation and migration backup.

## Decision

Use optional Textual 8.2.8 (MIT) with a standard-library session/validation layer shared with
the existing CLI. Keep the existing evidence toolkit and noninteractive assembly usable without
Textual. Alternative options were repairing only sequential prompts or adopting a different
terminal framework; Textual supplies tested form widgets and a headless interaction API.

Persist partial answers atomically and remember the selected section. Normalize mode/baseline
case; default an empty date once to today's date; suggest the repository name only when the
name is empty. Do not infer categorization, topology, approval or inherited-control applicability.
The user can save incomplete work but generation shows actionable field errors until ready.
Legacy intake is backed up before normalization and tied to a repository/session identity.

## Consequences

The UI provides step navigation, editable saved answers, topology node/flow forms, review,
and background draft generation with failures visible. Optional Textual tests run in its own
hash-locked environment. Headless interaction tests do not prove every terminal or assistive
technology layout. Concurrent disk changes are detected before writes; the UI is still a
single-author workflow, not a collaborative transactional database.

The UI does not solve the separately tracked same-topology diagram semantics issue, perform
semantic application assessment, or infer authorization. The existing generation engine
continues to own output preservation and source provenance.

## Dependency review

Exact dependencies and hashes are in `sspp-assembly-framework/requirements-tui.txt`; direct
requirement is Textual 8.2.8. PyPI version metadata was checked for all nine resolved packages
before installation and reported no advisories. This is a bounded advisory-source check, not
proof of absence of vulnerabilities. Dependency licenses: MIT (Textual, Rich, platformdirs,
linkify-it-py and the Markdown parser/plugins/URL utilities), BSD-2-Clause (Pygments), PSF-2.0
(typing-extensions). License files for packages without populated PyPI license fields were
inspected in their installed distribution. No global packages or web server were installed.
