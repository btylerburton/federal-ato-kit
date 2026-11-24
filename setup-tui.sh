#!/usr/bin/env bash
# Optional hash-locked terminal UI; installs only into this repository's local environment.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ "${1:-}" == "--help" ]]; then
  echo "Usage: bash setup-tui.sh (Python 3.11+; downloads pinned wheels into .venv-tui)"
  exit 0
fi
if [[ $# -ne 0 ]]; then
  echo "Usage: bash setup-tui.sh" >&2
  exit 2
fi
python3 -m venv "$ROOT/.venv-tui"
"$ROOT/.venv-tui/bin/python" -m pip install --require-hashes --only-binary=:all: -r "$ROOT/sspp-assembly-framework/requirements-tui.txt"
echo "Ready: .venv-tui/bin/python sspp-assembly-framework/tools/wizard.py tui --repository /path/to/repo --workspace /path/to/repo-ato"
