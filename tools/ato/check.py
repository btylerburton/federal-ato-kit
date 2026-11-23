#!/usr/bin/env python3
"""One-command offline toolkit verification; no live assessment or downloads."""

import ast
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    for path in (ROOT / "tools/ato").glob("*.py"):
        ast.parse(path.read_text(), filename=str(path.relative_to(ROOT)))
    docs = list((ROOT / "docs").rglob("*.md")) + [ROOT / "README.md", ROOT / "tools/ato/README.md"]
    docs += list((ROOT / ".agents/skills").rglob("*.md"))
    for path in docs:
        text = path.read_text()
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            raise ValueError("Missing frontmatter: " + str(path.relative_to(ROOT)))
        header = text.split("---", 2)[1]
        for field in ["title:", "description:", "status:", "tier:"]:
            if not any(line.startswith(field) for line in header.splitlines()):
                raise ValueError("Missing frontmatter field: " + field)
    registry = json.loads((ROOT / "tools/ato/registry.json").read_text())
    ids = [item["id"] for item in registry["tools"]]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate tool ID")
    for item in registry["tools"]:
        if "entrypoint" in item and not (ROOT / item["entrypoint"]).is_file():
            raise ValueError("Unwired tool: " + item["id"])
    owned = list((ROOT / "tools/ato").glob("*")) + list((ROOT / "docs").rglob("*"))
    owned += list((ROOT / ".agents/skills").rglob("*.md"))
    for path in owned:
        if path.is_file() and path.suffix in {".py", ".md", ".json", ".jsonl"}:
            text = path.read_text()
            if not text.endswith("\n") or any(line.rstrip() != line for line in text.splitlines()):
                raise ValueError("Whitespace error: " + str(path.relative_to(ROOT)))
    print("PASS: Python syntax, documentation frontmatter, tool entrypoint wiring, owned-file whitespace", flush=True)
    with tempfile.TemporaryDirectory(prefix="ato-check-") as temporary:
        env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": temporary}
        tests = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tools/ato",
                                "-p", "test_*.py", "-v"], cwd=ROOT, env=env, timeout=60)
        if tests.returncode:
            return tests.returncode
    # Real CLI execution verifies expected NOT_ASSESSED is not silently reported as success.
    sample = subprocess.run([sys.executable, "tools/ato/verify.py", "claims", "--manifest",
                             "examples/claims.json", "--evidence-root", "examples"],
                            cwd=ROOT, capture_output=True, text=True, timeout=30)
    output = json.loads(sample.stdout)
    if sample.returncode != 2 or output["counts"]["NOT_ASSESSED"] != 2:
        raise ValueError("Example claims incorrectly assessed")
    print("PASS: real CLI reports both unevidenced claims NOT_ASSESSED (exit 2)")
    print("NOT RUN BY THIS COMMAND: third-party SAST/SCA, full OSCAL validation, live controls")
    print("Record environment-specific scans and project evidence in the consuming project.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
