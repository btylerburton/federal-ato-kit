#!/usr/bin/env python3
"""Invoke federal-ato-kit entrypoints without copying their implementations."""
import argparse
import os
import subprocess
import sys
from pathlib import Path


def kit_entrypoint(root, name):
    if not root.is_absolute():
        raise ValueError("FEDERAL_ATO_KIT must be an absolute directory")
    allowed = {"check", "verify", "environment_report", "heartbeat"}
    if name not in allowed:
        raise ValueError("Unsupported kit command")
    path = root / "tools/ato" / (name + ".py")
    if not path.is_file() or not (root / "tools/ato/registry.json").is_file():
        raise ValueError("Configured federal-ato-kit is unavailable")
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["check", "verify", "environment_report", "heartbeat"])
    parser.add_argument("arguments", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    configured = os.environ.get("FEDERAL_ATO_KIT")
    if not configured:
        parser.error("Set FEDERAL_ATO_KIT to the shared kit directory")
    try:
        path = kit_entrypoint(Path(configured).expanduser(), args.command)
    except ValueError as error:
        parser.error(str(error))
    result = subprocess.run([sys.executable, str(path), *args.arguments], check=False)
    raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
