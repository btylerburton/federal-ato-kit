"""Portable offline Trestle CLI compatibility test; synthetic data, never an agency baseline."""

import json
import subprocess
import sys
import uuid
from pathlib import Path

import pytest


@pytest.mark.parametrize("nested", [False, True])
def test_synthetic_authoring_roundtrip(tmp_path, nested):
    executable = Path(sys.executable).parent / "trestle"
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    metadata = {
        "title": "Synthetic authoring fixture - not an approved baseline",
        "last-modified": "2026-11-06T00:00:00Z", "version": "1", "oscal-version": "1.2.1",
    }
    catalog = {"catalog": {
        "uuid": str(uuid.uuid4()), "metadata": metadata,
        "controls": [{"id": "ac-1", "title": "Synthetic control", "parts": [
            {"id": "ac-1_smt", "name": "statement", "prose": "Synthetic requirement."},
        ]}],
    }}
    if nested:
        catalog["catalog"]["controls"][0]["parts"][0]["parts"] = [{
            "id": "ac-1_smt.a", "name": "item", "prose": "Synthetic nested requirement.",
            "props": [{"name": "label", "value": "a."}],
        }]
    profile = {"profile": {
        "uuid": str(uuid.uuid4()), "metadata": metadata,
        "imports": [{"href": "trestle://catalogs/fixture/catalog.json", "include-all": {}}],
    }}
    for name, content in [("catalog", catalog), ("profile", profile)]:
        (tmp_path / f"{name}.json").write_text(json.dumps(content))

    def run(*args):
        completed = subprocess.run(
            [str(executable), *args, "--trestle-root", str(workspace)],
            capture_output=True, text=True, timeout=30, check=False,
        )
        assert completed.returncode == 0, completed.stdout + completed.stderr

    run("init", "--local")
    for name in ["catalog", "profile"]:
        run("import", "-f", str(tmp_path / f"{name}.json"), "-o", "fixture")
    run("author", "ssp-generate", "-p", "fixture", "-o", "markdown", "--include-all-parts")
    markdown = workspace / "markdown/ac-1.md"
    sentinel = "Synthetic implementation: designated staff review accounts every week."
    text = markdown.read_text()
    heading = "### This System"
    assert text.count(heading) == (2 if nested else 1)
    historical = "SYNTHETIC-HISTORICAL-CLAIM-NOT-CURRENT"
    before, after = text.rsplit(heading, 1)
    markdown.write_text(before + heading + "\n\n" + sentinel + after
                        + "\n## Original SSP export excerpt\n\n" + historical + "\n")
    run("author", "ssp-assemble", "-m", "markdown", "--output", "fixture-ssp")
    output = workspace / "system-security-plans/fixture-ssp/system-security-plan.json"
    first = json.loads(output.read_text())

    def strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for child in value.values():
                yield from strings(child)
        elif isinstance(value, list):
            for child in value:
                yield from strings(child)

    implementation = first["system-security-plan"]["control-implementation"]
    assert any(sentinel in value for value in strings(implementation))
    if nested:
        requirements = implementation["implemented-requirements"]
        assert len(requirements) == 1
        statements = requirements[0]["statements"]
        matching = [s for s in statements if s["statement-id"] == "ac-1_smt.a"]
        assert len(matching) == 1
        assert any(sentinel in value for value in strings(matching[0]))
    assert not any(historical in value for value in strings(first))
    run("author", "ssp-assemble", "-m", "markdown", "--output", "fixture-ssp")
    assert json.loads(output.read_text()) == first
    revised = "Synthetic implementation: designated staff review accounts every day."
    markdown.write_text(markdown.read_text().replace(sentinel, revised))
    run("author", "ssp-assemble", "-m", "markdown", "--output", "fixture-ssp")
    changed = json.loads(output.read_text())["system-security-plan"]["control-implementation"]
    assert any(revised in value for value in strings(changed))
    assert not any(sentinel in value for value in strings(changed))
    run("validate", "--all")
