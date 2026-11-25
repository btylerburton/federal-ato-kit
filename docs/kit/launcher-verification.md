---
title: "Unified launcher verification"
description: "Observed chooser interactions, owned-workspace behavior and review corrections"
status: draft
tier: 2
last_updated: "2026-11-24"
---

# Verification

## Host virtual-environment correction

The user subsequently reported the mismatch guard firing and setup finding packages in the
base pyenv installation. This confirms that the intended virtual environment was not active;
it does not prove which host configuration caused it. The macOS `__PYVENV_LAUNCHER__` hint is
a possible contributor, not an observed host root cause.

The bootstrap now clears inherited interpreter overrides and invokes local Python with `-I`.
Setup clears those overrides and pip target/prefix/user overrides locally, verifies sys.prefix,
base-prefix separation and disabled global/user package access before pip, then checks that
Textual is imported from the intended environment. Synthetic interpreter and real temporary
venv tests verify these guards; no host shell/global settings were changed. One generated test
probe initially had a mismatched brace and was corrected before the final pass.

The setup script was syntax-checked; no fresh network installation or macOS-host run is claimed.

## Bootstrap hang guard and diagnostics

User reported a blank launch including `--help`. The exact host issue was not reproduced in
the Linux harness, but inspection found unbounded interpreter re-execution if the local
interpreter did not report the expected virtual-environment prefix. The wrapper now serves
help before switching and stops a mismatched interpreter after one restart. Synthetic executable
fixtures reproduce that mismatch and verify the actionable exit, rather than hanging.

Added `-v`/`--verbose` and `--log`, with append-only UTC startup-stage logging and error types/
stack locations. No argument/answer/environment values or raw exception messages are captured.
Ten focused launcher tests passed, including a real mismatched-interpreter subprocess, broken-
interpreter help, diagnostics without argument leakage and existing Textual chooser cases.
The current wrapper also rendered the chooser through a real pseudo-terminal in this environment;
this does not establish the cause or resolution on the user's Ghostty host.

OpenCode AI coordinator, bounded Textual implementation delegate and independent blocker
review. User requested one start/resume entrypoint and lowercase `docs` or timestamped docs
inside the repository. No consuming repository was changed during implementation; tests use
disposable committed fixtures.

## Focused observed results

- Six Textual chooser tests passed: no writes on mount/refresh/quit, new workspace claim,
  existing-docs collision, timestamp fallback, saved-workspace selection, repository subdirectory
  resolution, external paths and literal path display at 80×24.
- Seven workspace tests passed: marker/path ownership, unrelated-doc preservation, root/path/
  symlink rejection, numeric name collision, old external sessions, and actual text generation,
  diagram review and attachment under in-repo docs. Existing source and control responses survived.
- One dispatcher test passed: CLI-relative repository/workspace paths resolve from the invocation
  working directory, not the selected repository.
- Existing 14 wizard tests passed after adjusting error wording to describe both supported
  workspace locations; prohibited application paths remain rejected.
- `./ato-wizard --help` passed without entering a TUI. No automatic dependency installation occurs.

## Review corrections

Independent review reproduced two blockers: relative CLI workspace misresolution, and generated
docs rediscovered as source after a checkout move. Both were corrected and independently
rechecked with the focused workspace/dispatcher tests. Ownership for writes still requires a
matching repository; exclusion of generated docs recognizes relocated markers by format.

An early mouse assertion on Textual's resume Select hit a child widget rather than the Select
itself. The test now exercises keyboard focus/open/select/confirm and verifies the selected path
and unchanged files. The actual choice updates, not only the widget text, are asserted.

The first full check had three failures due to legacy tests expecting the old external-only
error wording. The rejection behavior was correct; errors now explicitly name the allowed owned
docs or external options. No tests or checks were disabled to obtain a pass.

## Static checks and limits

Bandit reported two low warnings: B606 for execv into the fixed kit-local TUI interpreter, and
B404 for importing subprocess exception types in the chooser. No shell command is assembled,
no source-repository executable is launched by choosing a workspace, and no warnings were
suppressed. The scanner invocation also emitted a Python venv prefix warning for a relative
interpreter path; later execution uses explicit prepared interpreter paths.

An ownership marker is not authenticated authorization, and filesystem race isolation against
other hostile processes is not claimed. Markers and documents can be versioned deliberately;
the launcher does not change Git ignore rules. Existing external sessions are not migrated
automatically into the repository. Local tools/provider paths still require explicit setup.

Final root `check.py` run in the pinned TUI environment passed 12 toolkit tests and completed
126 framework tests successfully in 47.089 seconds, with four optional renderer/Trestle cases
explicitly skipped. No skipped test is represented as a fresh rendering pass. All chooser,
workspace, dispatcher and actual local generation/attachment cases ran. `git diff --check`
passed after documentation updates.
