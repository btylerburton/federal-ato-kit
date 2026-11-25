#!/usr/bin/env python3
"""One-command offline verification of the evidence toolkit and SSPP assembly framework."""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OPTIONAL = ["TRESTLE_TEST_BIN", "PANDOC_TEST_BIN", "PLANTUML_TEST_JAR"]


def suites(root=ROOT):
    return [
        ("evidence toolkit", [sys.executable, str(root / "tools/ato/check.py")], root),
        ("sspp-assembly-framework", [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
         root / "sspp-assembly-framework"),
    ]


def main(selected=None):
    codes = []
    with tempfile.TemporaryDirectory(prefix="portable-ato-kit-") as temporary:
        # macOS temp roots can contain system symlinks; pass physical paths to fixtures.
        env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(Path(temporary).resolve())}
        for name, command, cwd in (selected if selected is not None else suites()):
            print("== " + name, flush=True)
            code = subprocess.run(command, cwd=cwd, env=env, check=False).returncode
            print(f"{'PASS' if code == 0 else 'FAIL'}: {name} (exit {code})", flush=True)
            codes.append(code)
    missing = [name for name in OPTIONAL if not os.environ.get(name)]
    if missing:
        print("NOT RUN: live renderer/Trestle integration tests are skipped without " + ", ".join(missing))
    print("Offline stdlib check only; it does not assess any project's controls.")
    return next((code for code in codes if code), 0)


if __name__ == "__main__":
    sys.exit(main())
