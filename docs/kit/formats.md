---
title: "Package and evidence input contracts"
description: "Supported migration-index layout, excerpt marker and claim fields"
status: draft
tier: 2
last_updated: "2026-11-12"
---

# Supported inputs

## Package adapter

`verify.py package --package PATH` expects:

```text
PATH/
  migration-index.json
  control-statements/<family>/<control-id>.md
  component-definitions/<component>/component-definition.json   (optional)
  profiles/... and catalogs/...                               (when referenced)
```

The index has a nonempty `controls` array. Each record requires `control_id`
(lowercase, such as `ac-2` or `ac-2.1`), `path` relative to the package,
`source_sha256` and `source_status_selections` (a list of source selections).
Each Markdown control has exactly one `## Original SSP export excerpt` heading,
followed by a blank line and its excerpt. The digest covers UTF-8 excerpt bytes
after stripping trailing newlines; it does not cover preceding authored prose.
All Markdown files immediately under `control-statements/<family>/` must be indexed.

Paths must remain within the package, including after resolving symlinks.
Local `trestle://` targets must exist; this check does not resolve remote catalogs.
Component JSON is parsed, not schema-validated by this command. Multiple/absent
source status selections return BLOCKED. These conventions are an explicit adapter
format, not a universal OSCAL or agency document requirement.

## Claims and evidence

`verify.py claims --manifest FILE --evidence-root PATH` expects `schema_version: 1`,
a nonempty `claims` array and an `evidence` array. Each claim requires:

- `id`, `statement`, `environment`, `source_revision`.
- `controls`: uppercase IDs, for example `AC-2` or `AC-2(1)`.
- `required_kind`: `source-review`, `offline-test`, `live-test`, or `provider-attestation`.
- `evidence_ids`: references to evidence, or an empty list for NOT_ASSESSED.

Each evidence record requires `id`, `kind`, `environment`, `source_revision`,
`observed_at`, `expires_at`, `artifact`, `sha256`, `method`, `result`, `observation`.
Times must include timezones and a valid observation/expiry interval. Artifacts
must resolve inside the evidence root. Results are PASS, FAIL, BLOCKED or NOT_ASSESSED.
Duplicate JSON keys/IDs, path escapes and unsupported kinds are rejected.

Passing checks establish integrity/readiness only. A matching hash cannot prove
an observation true, and an offline test cannot establish a live claim.

## Timer state

The optional `heartbeat.py` takes explicit `--state` and `--log` paths. State uses
`iteration`, `status` and optional `last_agent_reflection`. Supported statuses are
`in_progress`, `blocked`, `complete`, `cancelled`; complete/cancelled stop the timer.
The timer writes snapshots, not AI reflections, and does not start automatically.
