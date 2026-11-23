#!/usr/bin/env python3
"""Invoke federal-ato-kit entrypoints without copying their implementations."""
import argparse
import os
import subprocess
import sys
from pathlib import Path

COMMANDS = ["check", "verify", "environment_report", "heartbeat"]
DEFAULT_KIT = Path(__file__).resolve().parents[2]


def kit_entrypoint(root, name):
    if not root.is_absolute():
        raise ValueError("FEDERAL_ATO_KIT must be an absolute directory")
    if name not in COMMANDS:
        raise ValueError("Unsupported kit command")
    path = root / "tools/ato" / (name + ".py")
    if not path.is_file() or not (root / "tools/ato/registry.json").is_file():
        raise ValueError("Configured federal-ato-kit is unavailable: " + str(root))
    return path


def kit_root(environ, default=DEFAULT_KIT):
    """An explicit override (even an empty one) is never replaced by the default."""
    if "FEDERAL_ATO_KIT" in environ:
        return Path(environ["FEDERAL_ATO_KIT"]).expanduser()
    return default


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=COMMANDS)
    parser.add_argument("arguments", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    try:
        path = kit_entrypoint(kit_root(os.environ), args.command)
    except ValueError as error:
        parser.error(str(error))
    result = subprocess.run([sys.executable, str(path), *args.arguments], check=False)
    raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
