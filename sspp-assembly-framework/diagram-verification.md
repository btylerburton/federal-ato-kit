---
title: "Diagram pipeline verification"
description: "Executed rendering, repeatability, scaffold and DOCX-media checks"
status: draft
tier: 2
last_updated: "2026-11-19"
---

# Diagram pipeline verification

OpenCode AI agent; approved diagram integration increment. Source and generated files were
saved incrementally. The session heartbeat runs at five-minute intervals and is stopped on
completion. Temporary renderer/test directories are cleaned automatically; audit and package
outputs remain available for inspection.

## Results

| Check | Observed result |
| --- | --- |
| Full framework suite with PlantUML, Pandoc and Trestle variables supplied | PASS: 23 tests in 16.844 seconds; no skipped renderer integration |
| Actual four-view diagram render | PASS: four SVG and four PNG outputs |
| Repeated source render/Markdown inventory comparison | PASS: identical package bytes in the same Java/font environment |
| Actual Pandoc DOCX export | PASS: each expected PNG hash appears in DOCX embedded media |
| Invalid source/build after successful DOCX | PASS: failure leaves prior published DOCX unchanged |
| Node/flow validation | PASS: unknown nodes, missing authentication metadata, source-alias drift and reversed source arrows rejected |
| Includes/external dependencies | PASS: self-contained source validation rejects include directives |
| Full NIST team scaffold | PASS: 1,196 control/enhancement shells; 58 selected; four diagram modules registered |
| Full selected team-template pipeline | PASS: 12 package files, including DOCX and eight rendered image assets |
| Architecture PNG inspection | Viewer, service, store, boundary, arrows and draft/UNFILLED labels visually legible |
| `git diff --check` | PASS, no output |
| Bandit | Exit 1: six low subprocess warnings and one medium URL-open warning; disposition below |

Inspect the synthetic example output at `build/diagram-demo/document.docx`, or the complete
selected team-template export at `build/team-diagram-export/document.docx`. Both have matching
Markdown, asset files, `inventory.json` and `verification.json`. These are synthetic unfilled
review templates, not current America.gov architecture evidence.

## Commands

```sh
python3 tools/setup_diagrams.py --destination /path/to/plantuml-1.2026.2.jar

PLANTUML_TEST_JAR=/path/to/plantuml-1.2026.2.jar \
PANDOC_TEST_BIN=/path/to/pandoc TRESTLE_TEST_BIN=/path/to/trestle \
python3 -m unittest discover -s tests -v

python3 tools/pipeline.py examples/diagrams/manifest.json --output build/diagram-demo \
  --plantuml-jar /path/to/plantuml-1.2026.2.jar --pandoc /path/to/pandoc
```

The actual run used the existing project virtual environment, Java 25, pinned PlantUML
1.2026.2 and Pandoc 3.8.2. This minimal ARM64 environment also needed local font/native
libraries and explicit `LD_LIBRARY_PATH`/`FONTCONFIG_FILE`, documented in diagram-pipeline.md.

## Failures and environment repair

The first real Java invocation failed because `libharfbuzz.so.0` and related AWT font libraries
were absent. Libraries/fonts were locally extracted from checksum-verified Debian packages.
The next invocation identified missing `libatomic.so.1`; it was also locally extracted.
No package installation scripts or system-wide changes were executed. The next renderer test
passed. Thirteen package versions, URLs and hashes are recorded in
`diagram-native-provenance.json`. No failing invocation is counted as a passed render.

## Scan disposition and assurance limits

The complete unsuppressed scan is in `diagram-bandit.json`. B404/B603 flag subprocess usage:
commands use argument arrays without a shell, bounded timeouts, explicit result checks and a
checksum-verified JAR. B607 flags Java resolved through the operator's PATH; release environment
pinning is FW-14. B310 flags `urlopen` in setup, which uses one fixed HTTPS upstream release
URL, certificate validation and the pinned SHA-256 before writing the tool. The scan is not
reported as zero findings. A fresh external dependency/advisory review remains FW-14.

Structural metadata checks do not prove that drawn boundary geometry matches node declarations,
that all system interfaces are present, or that source claims are true. Owner review and Google
Docs layout acceptance remain FW-13. PNG identity in DOCX proves media inclusion, not final
pagination or accessible reading order. Cross-platform render identity and DOCX/PDF byte
determinism remain outside this increment's verified scope.
