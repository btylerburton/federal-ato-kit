---
title: "Architecture and data-flow diagram pipeline"
description: "Editable source, pinned rendering, registered figures and verified DOCX media"
status: draft
tier: 2
last_updated: "2026-11-19"
---

# Diagram pipeline

The framework now builds diagrams as document inputs rather than relying on hand-copied images.
New team scaffolds include four editable PlantUML views: **context, authorization boundary,
architecture and data flow**. Their synthetic labels and draft review state must be replaced
with project-specific content. Existing team files are preserved on scaffold regeneration.

## Build commands

Install the pinned PlantUML JAR locally after approving the download:

```sh
python3 tools/setup_diagrams.py --destination /path/to/tools/plantuml-1.2026.2.jar
```

Java with working AWT font support and installed fonts is required even in headless mode.
The bundled Smetana layout engine avoids a separate Graphviz dependency. PlantUML 1.2026.2
is checksum-pinned; Pandoc 3.8.2 is used for DOCX. Renderer artifacts and input hashes are
recorded in the output inventory. These tools run locally; builds fetch no remote diagrams.

Regenerate the team scaffold after editing `diagrams.json` to refresh its generated manifest.
Then run from the framework directory:

```sh
# Diagram rendering and Markdown/resource package.
python3 tools/build.py /path/to/team/manifest.json --output /path/to/output \
  --plantuml-jar /path/to/tools/plantuml-1.2026.2.jar

# Same stages plus DOCX export and embedded-image verification.
python3 tools/pipeline.py /path/to/team/manifest.json --output /path/to/docx-output \
  --plantuml-jar /path/to/tools/plantuml-1.2026.2.jar --pandoc /path/to/pandoc
```

## Module contract

Each `kind: diagram` entry declares `id`, `title`, `path`, `source`, `view`, `environment`,
`revision`, `review_status`, `caption`, `alt`, `nodes` and `flows`. `view` supports context,
boundary, architecture, data-flow and supplementary sequence diagrams. Review state is draft,
reviewed or approved; publication edition requires the supplied state to be approved but
does not independently prove that an owner approved it.

Nodes have stable `id` aliases and `boundary: inside|outside`. Flows reference known nodes
and specify `data`, `protocol`, `authentication`, and `storage`. All flow metadata appears
in a table next to the figure, so it survives image rendering and remains readable.

The supported self-contained PlantUML subset uses `as node_id` declarations and directed
`from --> to : label` relationships. Inventory node aliases and arrow endpoints must match
the source. Include files, preprocessor directives, external images and hyperlinks are refused.
One source file holds one diagram. No remote C4 library import is needed for the starter views.

Node/edge checks establish structural consistency, not architectural truth. Boundary geometry,
data classifications, completeness and the correctness of authentication/storage descriptions
still need owner review. A metadata `inside` label is not a machine-verified boundary drawing.

## Outputs and checks

- Every diagram produces SVG and PNG. PNG is embedded in Markdown/DOCX; SVG is retained.
- The composer records source SHA-256, renderer version/hash and generated-file hashes.
- The pipeline checks that each expected PNG's exact bytes occur among DOCX media entries;
  output size or image count alone is not accepted as proof.
- Captions, alt text, environment/revision/review status and flow tables accompany figures.
- Missing renderer, invalid source, mismatched inventories or missing DOCX images fail before
  publishing output. The existing owned-output policy protects user modifications.
- Same-source SVG/PNG/Markdown byte repeatability is tested in the same Java/font environment.
  Cross-platform layout and DOCX ZIP-byte reproducibility are not promised. Google Docs visual
  layout and pagination remain a separate acceptance step.

## Tool provenance and environment

PlantUML release: `https://github.com/plantuml/plantuml/releases/tag/v1.2026.2`.
JAR SHA-256: `3cdce52133c424dea22425b947ae9d47f2167b0866dfcf99e714d4ea1689975c`.
PlantUML is GPL-licensed and invoked as a standalone tool; existing Pandoc licensing remains
unchanged. Java/font/native libraries also affect layout; pin them in a release environment.

This session's minimal ARM64 Java lacked font dependencies. Thirteen Debian packages were
checksum-verified against the HTTPS package index and extracted into the ignored project-local
`.venv-ato/tools/diagram-native/` without package scripts or system installation. Versions and
hashes are in `diagram-native-provenance.json`; installed font/license material is retained in
that local extraction. These are environment prerequisites, not bundled framework dependencies.
No fresh CVE advisory scan was completed; digest verification is not a vulnerability result.

For this environment, prepend the local native-library directory to `LD_LIBRARY_PATH` and set
`FONTCONFIG_FILE` to its `fonts.conf`. Normal Java installations with fonts need neither setting.
The setup command downloads only the JAR; operating-system font provisioning is explicit.
