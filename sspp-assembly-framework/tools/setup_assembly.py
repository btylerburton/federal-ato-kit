#!/usr/bin/env python3
"""Install the pinned, user-approved local Pandoc tool and fetch the test catalog."""

import hashlib
import argparse
import io
import json
import platform
import tarfile
import urllib.request
from urllib.parse import urlparse
from pathlib import Path



def download(record):
    url = urlparse(record["url"])
    if url.scheme != "https" or url.hostname not in {"github.com", "raw.githubusercontent.com"}:
        raise ValueError("Downloads must use approved HTTPS upstream hosts")
    if url.username or url.password or url.port not in {None, 443}:
        raise ValueError("Download URL may not include credentials or a non-TLS port")
    request = urllib.request.Request(record["url"], headers={"User-Agent": "SSPP-Assembly/1"})
    with urllib.request.urlopen(request, timeout=120) as response:
        content = response.read()
    if hashlib.sha256(content).hexdigest() != record["sha256"]:
        raise ValueError("Downloaded asset does not match pinned SHA-256")
    return content


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True)
    args = parser.parse_args()
    config = json.loads(args.project.read_text())
    if config.get("schema_version") != 1:
        raise ValueError("Expected project schema_version 1")
    root = (args.project.resolve().parent / config["project_root"]).resolve()
    def local(key):
        path = (root / config[key]).resolve()
        if not path.is_relative_to(root):
            raise ValueError(f"Setup path escapes project: {key}")
        return path
    pins = json.loads(local("provenance").read_text())
    architecture = {"aarch64": "arm64", "arm64": "arm64", "x86_64": "amd64"}.get(platform.machine())
    if platform.system() != "Linux" or architecture is None:
        raise ValueError("Pinned setup supports Linux ARM64 and AMD64 only")
    catalog = local("catalog")
    if not catalog.exists() or hashlib.sha256(catalog.read_bytes()).hexdigest() != pins["catalog"]["sha256"]:
        catalog.write_bytes(download(pins["catalog"]))
    content = download(pins["pandoc"]["linux-" + architecture])
    destination = local("tool_destination")
    destination.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(content), mode="r:gz") as archive:
        archive.extractall(destination, filter="data")
    print(f"PASS: pinned catalog and platform-matched Pandoc {pins['pandoc']['version']} verified")


if __name__ == "__main__":
    main()
