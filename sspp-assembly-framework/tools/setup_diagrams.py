#!/usr/bin/env python3
"""Install checksum-pinned PlantUML locally after explicit download approval."""
import argparse
import hashlib
from pathlib import Path
from urllib.request import urlopen
from diagrams import SHA256, URL, VERSION


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()
    if args.destination.exists():
        if hashlib.sha256(args.destination.read_bytes()).hexdigest() != SHA256:
            parser.error("Existing destination differs; choose a new path")
    else:
        with urlopen(URL, timeout=120) as response:
            content = response.read()
        if hashlib.sha256(content).hexdigest() != SHA256:
            parser.error("Downloaded JAR failed SHA-256 verification")
        args.destination.parent.mkdir(parents=True, exist_ok=True)
        args.destination.write_bytes(content)
    print(f"PASS: PlantUML {VERSION} verified at {args.destination}")


if __name__ == "__main__":
    main()
