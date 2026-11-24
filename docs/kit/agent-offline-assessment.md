---
title: "Agent access and offline-operation assessment"
description: "Verified current capabilities and proposed support for manual, restricted and disconnected use"
status: draft
tier: 2
last_updated: "2026-11-24"
---

# Agent access and offline operation

OpenCode AI coordinator and independent read-only audit. This assessment follows the tested
diagram dashboard increment. It proposes follow-up work; it does not establish network
isolation, model-provider approval or an implemented offline installer.

## Main conclusions

1. An LLM must be optional. The proposal importer already accepts person-authored JSON;
   the agent-first language and lack of a manual authoring screen obscure that capability.
2. No runner is configured or invoked by default. The kit itself chooses no model, discovers
   no provider credentials and calls no model API. External-agent handoff is optional.
3. A configured runner is a trusted process with caller permissions, inherited environment,
   filesystem access and network access. Absolute paths, argument arrays, timeouts and a
   consent checkbox are workflow controls, not an OS sandbox or data-transfer policy.
4. Local draft generation can operate with provisioned local inputs. Current normal setup
   downloads packages/tools; offline provisioning is not yet a turnkey supported workflow.
5. A local model executable is not proof of offline inference. Model downloads, telemetry,
   endpoints and credential use need independent configuration and verification.

## Current mode assessment

| Mode | What works now | Gap / proposed next step |
| --- | --- | --- |
| No LLM | Text intake/questions/generation; manually authored diagram proposal import, clarification and source generation | First-class manual option, neutral authorship and optional guided proposal editing |
| Existing approved coding agent | Saved request and locally supplied proposal; no kit runner needed | Explain allowed source/transfer scope and preserve author-supplied provenance |
| Local model | Operator wrapper can produce the same proposal contract | No bundled adapter or local-only enforcement; operator must pre-provision model/runtime |
| Approved hosted model | Explicit wrapper action can contact its approved provider | No approval/endpoint/retention validation by kit; no automatic fallback to hosted inference |
| Disconnected environment | Standard-library CLI and bundled catalog/reference data; local rendering with supplied tools | Offline wheelhouse/tool bundle, platform-specific setup and disconnected acceptance test |

## Code-verified boundaries

- `diagram_runner.py`: Popen has no environment override, so it inherits caller variables.
  stdout/stderr/argv/environment values are not retained in receipts. Source-read permissions
  and outbound transfer are not restricted. Configuration outside the source checkout does
  not prove OS ownership or trustworthiness of the wrapper or scripts in its arguments.
- `diagram_dashboard.py`: refresh validates/imports a proposal; it does not run analysis.
  Failed/timed-out runner output is quarantined. A proposal file and zero process exit are
  not evidence of valid inference, authorized source transfer or human review.
- `diagram_flow.py`: citations use exact commit/blob/path/range checks and exclude named
  sensitive paths. Filename filtering is not content classification or redaction. The
  current generated record says AI-assisted even for person-authored input; this needs an
  authorship field rather than a blanket label.
- `repository_intake.py`: text intake discovers tracked paths and working-tree status;
  it does not perform semantic source analysis. Diagram citation validation is a different
  evidence layer from this path inventory.
- `setup-tui.sh` and `tools/ato/setup.sh`: exact hash-locked binary dependencies, but normal
  installation uses package indexes. TUI setup uses ambient pip index configuration. A
  disconnected run must not invoke these online acquisition paths accidentally.
- `setup_assembly.py` downloads Pandoc on invocation; `setup_diagrams.py` avoids downloading
  an existing correctly pinned JAR. Render/build commands are separate from acquisition.
- `diagrams.py` checks the JAR hash and self-contained source. Pandoc runtime is version-checked,
  not content-hash checked; Java/fonts remain environment inputs. No cross-platform or whole-
  workflow deterministic guarantee follows merely from pinned Python packages.

## Proposed product behavior

Begin with a persistent capability choice: **Manual**, **Existing approved agent**,
**Local runner**, or **Approved hosted runner**. Default to Manual/no automatic execution.
An independent network policy describes whether any external processing is permitted.
Detect installed tools locally; never probe provider endpoints, discover secrets, download
models or fall back to a hosted provider just because a configured capability is unavailable.

Offer explicit statuses: available, not installed, prohibited by selected policy, or needs
operator configuration. Missing LLM access must not block text authoring, baseline selection,
manual diagram review, or local document generation. Renderer absence permits source-only
output and an actionable provisioning message.

Separate connected preparation from disconnected installation/run. Prepare exact-version,
hash-verified wheels, catalog/profile/reference files, renderers and required runtime/font
artifacts for the target OS/Python/architecture. Offline installation should use only an
explicit local wheelhouse (`--no-index`) and fail on missing artifacts, never retrieve them.
Credentials, provider tokens and model weights do not belong in generic sample bundles.

If stronger execution isolation is required, define its actual enforcing environment before
implementation: approved container/VM, filesystem mounts, credential allowlist, and egress
rules. A UI setting can prohibit the kit from launching a runner, but cannot honestly claim to
block network access by an arbitrary trusted process without such enforcement.

## Work records and decisions

Tracked items are WIZ-12–16 in `wizard-work.json`. Recommended order:
manual/mode and authorship clarity → local capability preflight → offline provisioning →
operator-approved runner containment if required. Do not present these recommendations as
already implemented features.

Owner decisions needed: initial manual JSON versus a manual form editor; which execution modes
to support first; whether existing agency sandbox/network controls are sufficient; and which
run metadata is required (current hashes versus model identity, transfer accounting or
authenticated approval). Record source-access/transfer policy separately from provider choice.

## Evidence limits

This was static inspection by coordinator and a read-only audit agent. The prior dashboard
test run exercised local fake wrappers, actual rendering and UI interactions, not a live model
provider or an air-gapped environment. No network or secret inspection was performed for this
assessment. No sandbox policy or setup behavior was changed by this document.
