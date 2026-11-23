---
title: "Modular assembly draft verification"
description: "Observed results for the semantic comparison and portable Markdown package prototype"
status: draft
tier: 2
last_updated: "2026-11-16"
---

# Verification

OpenCode AI agent. Mode: user-authorized draft/scoped prototype, delivered in small disk-backed
increments. Scope: semantic comparison, reusable framework design/README/work register and
offline Markdown composition prototype. Actual session tools record command executions.

## Executed checks

From `tmp/sspp-assembly-framework/`:

```sh
TMPDIR=/tmp/opencode PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
PYTHONDONTWRITEBYTECODE=1 python3 tools/build.py examples/minimal/manifest.json --output build/minimal
```

Observed exit **0** for both:

```text
Ran 10 tests in 0.170s
OK
PASS: wrote 4 deterministic package files to build/minimal
```

The tests cover real CLI success/failure, duplicate IDs/JSON keys, input hash mismatch,
missing attachments, path/symlink escape, publication gaps, unknown links, dropped image
definitions, user-modified/untracked outputs and removal of unchanged stale outputs.
Fresh, repeated and relocated builds are compared byte-for-byte, including the inventory.
Output attachment bytes are compared against source bytes and all inventory output hashes
are recomputed. Tests use disposable temporary directories, cleaned on completion.

From the parent repository:

```sh
PYTHONDONTWRITEBYTECODE=1 .venv-ato/bin/python -m bandit -q tmp/sspp-assembly-framework/tools/build.py
git diff --check
```

Observed exit **0**, no findings/output. Additional local validation confirmed five authored
Markdown frontmatters, related-file paths, JSON records, 13 unique ICG findings and matching
comparison snapshot hashes. The generated example document was read to check section order,
figure/attachment links, source labels and the explicit gap.

## Delivered files

- `docs/compliance/assessment/import-construct-gap.md` in the consuming repository:
  section-level meaning/readiness comparison, 13 material findings and owners/triggers.
- `README.md`, `design.md`, `work-items.json`: portable design and handoff draft.
- `tools/build.py`, `examples/minimal/`, `tests/test_build.py`: executable initial scaffold.
- `build/minimal/`: ignored demonstration output, retained for inspection.
- `progress.json`, `heartbeat.jsonl`: local task status and timer audit, not release content.

## Limits and next delivery

The demonstrated idempotence is for the synthetic Markdown/resource package. The prototype
accepts a deliberately restricted Markdown link subset; it is not a general Markdown parser
or an HTML sanitizer. Reference-style links/images must be ingested into registered module
targets. Do not treat this as a renderer for arbitrary untrusted active HTML.

America.gov source ingestion, complete original-document restoration, portable Trestle
integration, DOCX/PDF determinism and Google Docs layout acceptance are **planned** under
FW-03–06, not claimed complete. FW-03 is the next concrete implementation step: map the import's
front matter, chapters, control preamble, references, six attachment links and images into
the manifest. FW-07 tracks future repository extraction and release documentation; FW-08
tracks owner reconciliation of substantive narrative conflicts.

The existing `federal-ato-kit` and full America.gov assembly remain separate project artifacts.
No dependencies, external downloads or remote repository creation were needed for this draft.
No document snapshot or previous audit log was deleted. The five-minute heartbeat records
progress; it does not execute agent work or restart interrupted sessions.
