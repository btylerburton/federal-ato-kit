---
title: "Synthetic source-cited diagram proposal"
description: "Editable standalone diagram proposal example with explicit unknowns and hypotheses"
status: draft
tier: 3
last_updated: "2026-11-24"
related_files:
  - docs/kit/diagram-review.md
  - examples/diagram-proposal/proposal.json
  - examples/diagram-proposal/source.txt
---

# Synthetic diagram proposal

This AI-authored example illustrates the JSON contract. It does not assess an application.
The all-zero `repository_revision` is intentionally invalid: replace it with the full commit
from your prepared `diagramming/session.json`, and replace citation paths/ranges with real
reviewed source from that commit. Copy the proposal into the external workspace before editing.

`source.txt` is synthetic documentation demonstrating the example citation ranges. Once these
example files are committed, a session prepared against that exact kit commit can cite this
fixture; they are not evidence for a consuming application.

The draft leaves the database boundary and public request authentication unknown, marks the
database as a hypothesis, and records a deployment assumption. A reviewer must resolve these
before explicitly confirming review and generating the four views. See
[`docs/kit/diagram-review.md`](../../docs/kit/diagram-review.md) for the full CLI workflow.
