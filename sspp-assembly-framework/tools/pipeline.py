#!/usr/bin/env python3
"""Render diagrams, compose Markdown, export DOCX and verify embedded figure bytes."""
import argparse
import json
import subprocess
import tempfile
import zipfile
from pathlib import Path
from build import compose, json_bytes, publish, sha


def pipeline(manifest, output, jar, pandoc):
    files = compose(manifest, jar)
    pandoc = pandoc.resolve()
    version = subprocess.run([str(pandoc), "--version"], capture_output=True, text=True, timeout=15, check=True)
    if version.stdout.splitlines()[0] != "pandoc 3.8.2":
        raise ValueError("Pipeline requires Pandoc 3.8.2")
    with tempfile.TemporaryDirectory(prefix="sspp-render-") as scratch:
        stage = Path(scratch)
        for name, content in files.items():
            path = stage / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        result = subprocess.run([str(pandoc), "document.md", "--from=markdown-smart", "--to=docx",
                                 "--standalone", "--toc", "-o", "document.docx"], cwd=stage,
                                capture_output=True, text=True, timeout=120, check=False)
        if result.returncode or result.stderr.strip():
            raise ValueError(f"DOCX rendering failed or warned: {result.stderr}")
        docx = stage / "document.docx"
        with zipfile.ZipFile(docx) as archive:
            media = {sha(archive.read(name)) for name in archive.namelist() if name.startswith("word/media/")}
            document_xml = archive.read("word/document.xml")
        inventory = json.loads(files["inventory.json"])
        figures = [m for m in inventory["modules"] if m["kind"] in {"diagram", "asset"}]
        for figure in figures:
            if sha(files[figure["target"]]) not in media:
                raise ValueError(f"DOCX lost or changed figure: {figure['id']}")
        files["document.docx"] = docx.read_bytes()
    files["verification.json"] = json_bytes({"figures_verified": len(figures), "embedded_media": len(media),
        "toc_present": b"TOC" in document_xml, "pandoc": "3.8.2",
        "layout_review": "NOT_ASSESSED", "diagram_owner_approval": "Not inferred from rendering"})
    inventory["outputs"] = {name: sha(value) for name, value in files.items() if name != "inventory.json"}
    files["inventory.json"] = json_bytes(inventory)
    return publish(manifest, output, files)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--plantuml-jar", type=Path, required=True)
    parser.add_argument("--pandoc", type=Path, required=True)
    args = parser.parse_args()
    try:
        count = pipeline(args.manifest, args.output, args.plantuml_jar, args.pandoc)
    except (ValueError, OSError, subprocess.SubprocessError) as error:
        parser.exit(1, f"Pipeline refused: {error}\n")
    print(f"PASS: {count} package files; diagram bytes verified in DOCX")


if __name__ == "__main__":
    main()
