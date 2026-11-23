---
title: "Team template generation verification"
description: "Observed full-catalog shell generation, preservation and selected-document build results"
status: draft
tier: 2
last_updated: "2026-11-17"
---

# Team template verification

> **Historical record.** Results below were observed in the source repository before consolidation into
> portable-ato-kit, with paths and tools of that environment. They do not verify this repository; live
> reruns are tracked as PKG-04 in `../docs/kit/packaging-work.json`.

OpenCode AI agent; approved FW-09 implementation. Work began November 16 and completed
November 17. The example's declared November 16 document date remains fixed for reproducibility.

## Actual catalog run

Full catalog: `docs/compliance/assembly/inputs/nist-catalog.json` in the consuming repository.
SHA-256: `64ca6b4161de51ab6af098a7d101d326f14c95e1abf721396cd8a049e8115eeb`.

Resolved selection: `docs/compliance/assembly/workspace-v2/catalogs/lato-resolved/catalog.json`.
SHA-256: `eeb3738ed8862a8e31783da048c9770e59b3ca5c17f47e87bc5bc8b9bb86a57e`.

Executed `tools/scaffold.py` with both catalog paths/pins, an explicit title/date and output
`build/team-template`. Observed exit 0:

```text
PASS: 1196 control/enhancement shells; 58 selected; 1196 new control shells
```

The output includes 20 chapter/appendix shells, generated requirement files and separate
team-owned response files. A second generation compared every output file's SHA-256 with
the first run:

```text
PASS: 2421 full-catalog scaffold files byte-identical on regeneration;
0 new shells; 1196 controls; 58 selected
```

The selected template was then built with the existing composer:

```sh
python3 tools/build.py build/team-template/manifest.json --output build/team-template-export
```

Observed exit 0: `PASS: wrote 2 deterministic package files` (document and inventory).
No real supporting attachments were supplied for this synthetic starter.

## Tests and scans

The complete framework suite was executed with the existing pinned local Trestle/Pandoc
paths supplied through `TRESTLE_TEST_BIN` and `PANDOC_TEST_BIN`, using the project Python
environment and disposable scratch under `/tmp/opencode`:

```text
Ran 20 tests in 7.113s — OK
```

Seven new scaffold tests verify nested control/enhancement coverage, part identities,
idempotent regeneration, preserved edits/UUIDs, new-part reporting, selected-only manifest
inclusion, missing authored files, modified generated-file refusal, invalid pins, unknown
selected controls and duplicate IDs. Existing composer and real relocated OSCAL-to-DOCX tests
also passed. Test temporary directories were cleaned automatically.

Bandit scanned `tools/scaffold.py` and `tools/build.py`: exit 0, no findings. No package
installation, external request or dependency change was required.

## Failure caught and corrected

The first selected-catalog document build rejected a link appearing inside a fenced JSON
parameter definition. That is literal catalog data, not an active resource link. The composer
now excludes fenced code blocks from Markdown link rewriting/validation. A regression test
checks the actual literal JSON survives composition; the real template build then passed.
One nonfunctional cleanup patch failed context matching and made no changes before correction.

## Supported guarantees and limits

- Catalog-wide shells and profile-resolved selection are implemented. Selected-catalog
  tailored prose/parameter overrides are not merged into full-catalog requirement files;
  FW-10 tracks that additional display mode.
- Response/chapter/project/supporting files are preserved; additions to catalog parts are
  surfaced for manual authoring instead of modifying existing narrative text.
- Template generation and Markdown assembly are verified. Connecting the new response-file
  format to the Trestle adapter is FW-11; an OSCAL export of filled team shells is not claimed.
- An always-visible readiness gap and UNFILLED/NOT_ASSESSED fields prevent the starter from
  representing authored or assessed implementation. Owner publication-readiness decisions
  remain outside shell generation.
- UUIDv4 values are generated on first creation and persisted in project state. Same-state
  regeneration is byte-identical; independently initialized projects have different identities.

See `team-template.md` for the reusable commands, authoring rules and project structure.
