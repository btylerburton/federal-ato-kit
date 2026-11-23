---
title: "Portable verification commands"
description: "Offline core and optional isolated-environment entrypoints"
status: draft
tier: 2
last_updated: "2026-11-12"
---

# Tools

Run `python3 tools/ato/check.py` from the kit, or invoke it by absolute path from
any directory. It verifies synthetic fixtures, Python syntax, documentation and
registry wiring without project files or installed third-party dependencies.

`verify.py` accepts explicit package/manifest/evidence paths; see
[formats](../../docs/kit/formats.md). It prints JSON and uses exit 0 for PASS,
1 for failure, and 2 for blocked/unassessed work without failure.

Optional commands after `bash tools/ato/setup.sh`:

```sh
.venv-ato/bin/python tools/ato/environment_report.py --package /path/to/project/docs/compliance
.venv-ato/bin/python -m pytest tools/ato/properties_check.py tools/ato/authoring_check.py -q -p no:cacheprovider
.venv-ato/bin/python -m bandit -r tools/ato -f json
.venv-ato/bin/python -m pip_audit --format json
```

The last command accesses advisory services and requires network approval. Save
results outside the shared kit, with the assessed project/environment. Installation
and past scans are not inferred from the dependency lock. Setup is kit-local;
it neither installs system-wide packages nor configures an agent globally.
