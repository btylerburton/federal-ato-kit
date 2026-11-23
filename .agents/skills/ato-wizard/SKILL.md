---
name: ato-wizard
title: "Repository-to-SSPP draft wizard"
description: "Guide repository intake, clarifications and baseline-selected SSPP drafting with diagrams"
status: draft
tier: 2
---

# ATO wizard

Use the kit's `docs/kit/wizard.md` workflow to produce an editable review draft for a consuming
project. Identify yourself as an AI author. Read project AGENTS instructions and obtain the
scope/permissions required there before code inspection, installs, edits or live checks.

1. Run local `wizard.py intake` against the selected repository and save outputs in its separate
   documentation workspace. Review existing owner answers before asking again.
2. Ask unresolved `questions.json` items in a concise batch. Do not infer system categorization,
   LATO eligibility, authority, provider approval or actual deployment from filenames.
3. Explain the selected baseline and preserve the user's source/environment/revision choices.
4. Build proposed node/flow inventory from user answers and, when authorized, bounded source
   review. Cite exact revision/path evidence; label assumptions and unresolved components.
5. Run generation and fill selected response files from real source observations and evidence.
   Use the per-control library's questions and commented examples as guidance. Never uncomment
   an example and present it as an observed implementation without supporting evidence.
6. Connect responsibility, per-part implementation, parameter decisions and evidence references.
   Leave missing values UNFILLED/NOT_ASSESSED and track owner/trigger instead of inventing them.
7. Run the pipeline with approved local tools. Review diagrams, controls, references and output
   content. Report actual results; a successful export is not authorization or effectiveness.

Work in small durable batches. Prefer local files and explicit source pins. No repository
content or credentials are sent to external services by the wizard CLI. The generic CLI's
intake is only tracked-path discovery; semantic assessment is the agent's separately scoped work.
