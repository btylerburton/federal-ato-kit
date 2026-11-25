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
# Local to this script: do not change the user's shell or global pyenv configuration.
unset __PYVENV_LAUNCHER__ PYTHONHOME PYTHONPATH PYTHONUSERBASE
unset PIP_TARGET PIP_PREFIX PIP_USER
export PIP_CONFIG_FILE=/dev/null
python3 -I -m venv "$ROOT/.venv-tui"
"$ROOT/.venv-tui/bin/python" -I "$ROOT/sspp-assembly-framework/tools/verify_tui_environment.py" "$ROOT/.venv-tui"
"$ROOT/.venv-tui/bin/python" -I -m pip --isolated install --require-hashes --only-binary=:all: -r "$ROOT/sspp-assembly-framework/requirements-tui.txt"
"$ROOT/.venv-tui/bin/python" -I "$ROOT/sspp-assembly-framework/tools/verify_tui_environment.py" "$ROOT/.venv-tui" --check-textual
echo "Ready: ./ato-wizard /path/to/repository"
