---
title: "Use one launcher and explicitly owned documentation workspaces"
description: "Draft decision for lowercase docs defaults, collision-safe naming and source exclusion"
status: draft
tier: 2
date: "2026-11-24"
decision_status: proposed
decision_makers: ["Repository owner"]
category: "Data Handling"
nist_controls: ["CM-3", "SA-5", "SA-11"]
ato_relevance: yes-internal
---

# Unified launcher and documentation workspaces

The user requested a short `./ato-wizard <repository>` command, lowercase in-repo `docs` as
the new-workspace default and Unix-timestamp names when that folder is occupied. The prior
tools required external outputs and separate text/diagram entrypoints.

Use a workspace chooser that performs only reads until the user selects Text draft or Diagrams.
A new empty location is explicitly claimed with `.ato-workspace.json`; an existing unrelated
folder is never adopted. Internal workspaces must be direct repository children named `docs`
or `docs-<timestamp>` (numeric suffix on collision). Existing registered workspaces can resume;
explicit external workspaces remain supported. Symlinks, repo roots/parents and arbitrary
application directories are rejected.

Marker ownership is a preservation convention, not a security boundary. It records the checkout
path; relocated clones require deliberate write reassociation. For source discovery, recognition
is broader: a matching marker format still excludes generated docs even after relocation.
This prevents generated narratives from becoming circular application evidence.

The optional local Textual environment is selected by the root launcher if available, without
installing anything. The workflow chooser returns before entering either app and reopens when
the workflow exits. Provider execution remains independently explicit. No global configuration,
automatic Git commit or ignore-policy change is made in consuming repositories.

Alternatives were continuing long direct commands, blindly reusing existing docs, or using only
external directories. Explicit owned in-repo workspaces preserve the user's requested layout
while retaining conservative overwrite behavior. Tests cover actual generation and attachment
inside an owned docs tree, relocation exclusions and conventional CLI path semantics.
