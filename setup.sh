#!/usr/bin/env bash
# Optional setup entrypoint. The offline check (python3 check.py) needs no setup.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

usage() {
  cat <<'USAGE'
Usage: bash setup.sh [--help]

Creates the kit-local .venv-ato from the hash-locked tools/ato/requirements.txt by
running tools/ato/setup.sh. This DOWNLOADS packages from PyPI: run it only after
approving dependency downloads. It never installs system-wide.

Optional renderers are separate, explicit steps and are not run by this script:
  Pandoc + catalog  python3 sspp-assembly-framework/tools/setup_assembly.py --project /abs/project.json
                    (Linux ARM64/AMD64; downloads pinned assets named in the project provenance)
  PlantUML jar      python3 sspp-assembly-framework/tools/setup_diagrams.py --destination /abs/plantuml.jar
                    (also needs a Java runtime that you install yourself)
Live tests then take TRESTLE_TEST_BIN, PANDOC_TEST_BIN and PLANTUML_TEST_JAR; see README.md.
USAGE
}

case "${1:-}" in
  -h|--help) usage; exit 0 ;;
  "") ;;
  *) usage >&2; exit 2 ;;
esac

bash "${ROOT}/tools/ato/setup.sh"
echo "PASS: locked dependencies installed in ${ROOT}/.venv-ato"
echo "Optional renderers are not installed; run 'bash setup.sh --help' for instructions."
