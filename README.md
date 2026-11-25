---
title: "Portable ATO Kit"
description: "Reusable evidence-readiness toolkit and modular SSPP assembly framework"
status: draft
tier: 1
last_updated: "2026-11-24"
---

# Portable ATO Kit

Reusable local tools for preparing traceable ATO/SSPP review artifacts. This repository
holds two parts that ship together:

| Part | Location | Purpose |
| --- | --- | --- |
| Evidence toolkit | `tools/ato/` | Offline validators for evidence integrity, freshness and package inventory; prints JSON and uses exit codes (0 PASS, 1 failure, 2 BLOCKED/NOT_ASSESSED). |
| SSPP assembly framework | `sspp-assembly-framework/` | Manifest-driven assembly of an SSPP from versioned modules; optional Trestle/Pandoc/PlantUML rendering to DOCX. See its [README](sspp-assembly-framework/README.md). |

Keep system controls, source imports, evidence, decisions, logs and assessment results in
each consuming project. Nothing here is an agency baseline, an accepted federal policy or
evidence that any control is effective. Test-system examples are synthetic; the four
user-supplied [component definitions](examples/component-definitions/README.md) are real
versioned reference assertions, explicitly requiring current applicability review.

## Quick start

For repository-guided LATO/full-ATO preparation, start with the
[draft wizard workflow](docs/kit/wizard.md). It records repository observations, asks for
missing system context, selects a pinned baseline and creates an editable draft with diagrams.
The optional `ato-wizard` agent skill adds a source/evidence review workflow; CLI path discovery
alone is not an implementation assessment.

The [control library](examples/control-library/README.md) covers the full pinned catalog with
descriptions, commented illustrative responses, questions, evidence guidance and source links.
The original `examples/package/` remains a minimal validator fixture; use the control library
and wizard for authoring guidance.

The wizard includes hosting/common-control questions and produces candidate part-level
inheritance mappings from cloud.gov, cg-egress-proxy, GSA common controls and org dependency
management reference definitions. See the reference README for SHA-pinning examples and
the distinction between provider assertions and verified application responsibility.

Python 3.11+ and nothing else (no installs, no network):

```sh
python3 check.py
```

This runs both focused suites (the toolkit's checks and the framework's unit tests) and
exits non-zero if either fails. It works by absolute path from any directory. Live
renderer integration tests are skipped unless `TRESTLE_TEST_BIN`, `PANDOC_TEST_BIN` and
`PLANTUML_TEST_JAR` are set; a skip is not a pass.

Try the examples from any working directory (use this repository's absolute path):

```sh
KIT=/absolute/path/to/this/repository
python3 "$KIT/tools/ato/verify.py" claims --manifest "$KIT/examples/claims.json" --evidence-root "$KIT/examples"
python3 "$KIT/sspp-assembly-framework/tools/build.py" \
  "$KIT/sspp-assembly-framework/examples/minimal/manifest.json" --output /tmp/minimal-sspp
```

The first command intentionally exits 2 (the example claims are unevidenced). The second
writes `document.md`, an inventory and copied assets to a directory you choose.

## Try the wizard on a sibling repository

Example: `searchgov-spider` is cloned beside this kit. Install the optional pinned Textual
interface once, then use the same command to start **or resume**:

```sh
bash setup-tui.sh
./ato-wizard ../searchgov-spider
```

The launcher offers **Text draft** and **Diagrams**, keeping those workflows separate inside
one entry screen. It resolves the checkout, shows local tool availability, and offers to resume
an existing wizard-owned workspace. For a new workspace click **New workspace**: it proposes
`<repo>/docs` when that name is unused, otherwise `<repo>/docs-<unix-timestamp>`. Existing
documentation is not adopted or overwritten. A timestamp collision gets a numeric suffix.
Nothing is created until you choose a workflow.

**Text draft** first offers [optional shared source review](docs/kit/source-review.md).
Copy its request to an approved LLM, use an explicitly configured runner, or continue manually
without AI. Review findings before including them in system descriptions and candidate control
narratives. The same analysis may supply topology for the separate diagram review.
Use **F4** to copy a focused field or visible screen text; prompts also have explicit copy buttons.

To keep using an existing external workspace:

```sh
./ato-wizard ../searchgov-spider --workspace ../searchgov-spider-ato
```

Exiting either workflow returns to the launcher. Quit there to end the session. A claimed
in-repo workspace contains `.ato-workspace.json`, tied to the checkout path, plus `intake/`,
`project/`, `diagramming/` and optional `export/`. The marker is an ownership convention, not
an authorization or secret store. It permits writes only to the selected documentation area.
Generated docs are excluded from subsequent source discovery. Git may show these documents
as new files; the launcher does not automatically commit or change repository ignore rules.
Moving/cloning a marked workspace requires deliberate repository-path reconciliation.

Run the launcher by absolute path from any directory. `--runner`, `--plantuml-jar`, and
`--pandoc` pass explicit optional diagram tools through; no model or dependency is downloaded
automatically. Missing Textual yields the setup command. Run `./ato-wizard --help` without setup
to inspect usage.

### Startup troubleshooting

```sh
./ato-wizard -v ../searchgov-spider
# Or choose the local diagnostic destination:
./ato-wizard -v --log /path/to/startup.log ../searchgov-spider
```

The default log is `tmp/ato-wizard.log` under the kit. It appends UTC timestamps and startup
stages (interpreter selection, UI imports, chooser mount and first render), plus error types
and stack locations. Verbose mode also prints pre-UI stages to stderr. Logs do not capture
answers, command arguments, environment values, repository contents or raw exception messages.
They can contain local interpreter paths. Do not run two sessions against one workspace.

`--help` bypasses optional-environment switching. The launcher switches interpreters at most
once; a mismatched virtual environment produces an actionable error instead of a restart loop.
Interpreter switching clears inherited Python home/path and macOS launcher overrides and
uses Python isolated mode. `setup-tui.sh` verifies the actual environment prefix and package
isolation **before pip runs**, and verifies Textual's local installation afterward. If setup
lists packages in a base pyenv directory, do not treat that as a working local environment.
The script changes environment variables only for its own process, not your shell configuration.
If no log is created at all, Python may not have reached the wrapper; check your `python3`
command/pyenv configuration. A recorded first-render event narrows a blank screen to terminal
display behavior rather than assuming that interpreter startup is the cause.

The text UI has section progress, Back/Next, inline validation, autosave and Save & Exit.
Diagramming is a separate proposal/review flow after an agent has inspected the source;
manual topology no longer blocks text configuration or generation. Existing intake answers
are backed up before migration; uppercase `LATO` is
normalized and an empty date defaults to today once. Existing dates and owner answers remain
unchanged. A placeholder such as `default` is not accepted as an actual boundary description.
Review the text scope before using Generate draft. Ctrl+S saves; Ctrl+Q saves
and exits. The command runs locally and does not launch an agent or execute application scripts.

The dependency-free CLI remains available. To resume its saved answers without the TUI, run
`python3 sspp-assembly-framework/tools/wizard.py ask --answers ../searchgov-spider-ato/intake/answers.json`.
Do not rerun `intake` over existing answers. Once required answers are complete:

```sh
python3 sspp-assembly-framework/tools/wizard.py generate \
  --repository ../searchgov-spider \
  --answers ../searchgov-spider-ato/intake/answers.json \
  --output ../searchgov-spider-ato/project
```

Editable control statements appear under
`../searchgov-spider-ato/project/controls/<family>/*.response.md`, alongside generated
`*.requirement.md` files. Chapters, proposed diagram sources and candidate inheritance
reports live in the same project directory. DOCX rendering additionally requires the local
tools described in the [wizard guide](docs/kit/wizard.md). The kit supplies a draft, not a
completed assessment or authorization. See [AGENTS.md](AGENTS.md) for the agent-assisted flow.

## Separate diagramming after source review

**Recommended start/resume command:**

```sh
./ato-wizard ../searchgov-spider
```

Select **Diagrams**. Use `--workspace ../searchgov-spider-ato` to reopen the external workspace
used by earlier examples. Advanced direct commands remain supported:

```sh
.venv-tui/bin/python sspp-assembly-framework/tools/diagram_flow.py tui \
  --repository ../searchgov-spider --workspace ../searchgov-spider-ato
```

The [diagram dashboard](docs/kit/diagram-dashboard.md) shows current state and next action,
automatically validates/imports a saved proposal, asks readable questions and exposes review,
generation, rendering and attachment. Without a configured agent runner it shows an exact
source-review request; with `--runner`, analysis runs only after your explicit button action.
Opening the dashboard does not itself run an LLM. The commands below remain available for
advanced CLI operation.

The text wizard no longer has a Topology screen. First ask an authorized agent/LLM to inspect
the source and propose nodes/relationships with revision/path citations and uncertainties.
Then use the [standalone diagram review flow](docs/kit/diagram-review.md):

```sh
python3 sspp-assembly-framework/tools/diagram_flow.py prepare \
  --repository ../searchgov-spider --workspace ../searchgov-spider-ato
```

**Stop here for the source-review pass.** `prepare` does not create `proposal.json` or run
an LLM. Ask your coding agent:

> Review the repository at the revision in diagramming/session.json without executing it or
> reading secret files. Write proposal.json in the external workspace using the example schema,
> cite paths/lines for proposed components and relationships, and leave uncertain deployment,
> boundary and data-handling facts unresolved for me to answer.

After the agent has saved that file, import it and start clarification:

```sh
python3 sspp-assembly-framework/tools/diagram_flow.py import \
  --repository ../searchgov-spider --workspace ../searchgov-spider-ato \
  --proposal ../searchgov-spider-ato/proposal.json && \
python3 sspp-assembly-framework/tools/diagram_flow.py review \
  --repository ../searchgov-spider --workspace ../searchgov-spider-ato
```

The proposal is an agent-produced input, not a file inferred by `prepare`. Review asks only
pending or uncertain fields and preserves answers. After explicit human review, generate/render
the independent diagrams and attach them with `attach_diagrams.py`. The guide gives the full
commands and a proposal example. No remote LLM call is made by this CLI.

## Optional setup

Only needed for Trestle, property tests and scanners. It downloads hash-locked packages
from PyPI, so run it only after approving dependency downloads:

```sh
bash setup.sh          # delegates to tools/ato/setup.sh; creates ./.venv-ato
bash setup.sh --help   # also lists the separate optional renderer steps
```

Optional renderers are explicit, separate steps and are never run by `setup.sh`:

- Pandoc and the pinned catalog: `sspp-assembly-framework/tools/setup_assembly.py --project /abs/project.json` (Linux ARM64/AMD64, downloads pinned assets).
- PlantUML: `sspp-assembly-framework/tools/setup_diagrams.py --destination /abs/plantuml.jar` (also requires a Java runtime you provide).

The lock was resolved on Linux/Python 3.14; verify wheel availability for your platform.
Recreate `.venv-ato` after moving the repository rather than moving an installed one.

## Use from another project

Run from your project root; arguments select the project and the tools never search
neighboring directories:

```sh
python3 /path/to/this/repository/tools/ato/verify.py package --package docs/compliance
python3 /path/to/this/repository/tools/ato/verify.py claims --manifest docs/compliance/assessment/claims.json --evidence-root .
```

`sspp-assembly-framework/tools/kit.py` is a thin launcher for the toolkit
(`check`, `verify`, `environment_report`, `heartbeat`). By default it uses the toolkit in
this repository; set `FEDERAL_ATO_KIT` to an absolute directory to use another copy. An
explicitly set but invalid value fails; it never falls back to the default. It keeps the
caller's working directory and returns the toolkit's exact exit status.

## Contents

- [Workflow](docs/kit/README.md) and [input formats](docs/kit/formats.md).
- `tools/ato/`: validators, synthetic tests, optional dependency lock and setup.
- `sspp-assembly-framework/`: assembly tools, design, tests and synthetic examples.
- `examples/`: synthetic claim and package examples.
- `docs/templates/`: project intake and verification templates.
- `docs/kit/packaging-work.json`: tracked remaining work to publish this repository.
- `.agents/skills/ato-sspp/`: reusable skill source. Moving this repository does not
  register the skill with an agent harness; use your harness's own mechanism.

Files named `*verification.md` record results observed in the source repository before
consolidation. They are historical, not a verification of this repository.

## Provenance, license and review

AI-assisted extraction by OpenCode AI / GPT 6 Astra from a project-specific
implementation; this repository contains generalized methodology and synthetic fixtures,
not that project's documents, contacts, evidence or build outputs. **The publication
license and ownership decision is pending**; no license grant is inferred. Dependency
licenses and hashes are in the lock and package metadata. Human review is required
before operational adoption. Remaining work is tracked in `docs/kit/packaging-work.json`.
