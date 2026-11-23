#!/usr/bin/env bash
# Shared-kit setup; run only after approving dependency downloads; no global installation.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
python3 -m venv "${ROOT}/.venv-ato"
"${ROOT}/.venv-ato/bin/python" -m pip install --require-hashes --only-binary=:all: \
  --index-url https://pypi.org/simple -r "${ROOT}/tools/ato/requirements.txt"
"${ROOT}/.venv-ato/bin/python" -m pip check
