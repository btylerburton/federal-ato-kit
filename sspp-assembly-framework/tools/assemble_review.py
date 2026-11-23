#!/usr/bin/env python3
"""Build review exports through real Trestle assembly, retaining evidence boundaries."""

import argparse
import copy
import hashlib
import html
import json
import re
import subprocess
import uuid
import zipfile
import importlib.util
from defusedxml import ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

import yaml

CONFIG = {}


def configure(path):
    global CONFIG, ROOT, AREA, TRESTLE, PANDOC, SOURCE, CATALOG_SHA, REVISION, DATE, ADAPTER
    path = path.resolve()
    CONFIG = json.loads(path.read_text())
    if CONFIG.get("schema_version") != 1:
        raise ValueError("Expected project schema_version 1")
    required = {"project_root", "area", "source", "trestle", "pandoc", "adapter", "controls",
                "catalog", "profile", "catalog_sha256", "application_revision", "date",
                "assessment_date", "system_name", "model_name", "export_model", "controls_output", "full_output"}
    if any(not isinstance(CONFIG.get(key), str) or not CONFIG[key] for key in required):
        raise ValueError("Missing or invalid project configuration fields")
    for key in ("model_name", "export_model", "controls_output", "full_output"):
        if not re.fullmatch(r"[a-z][a-z0-9-]{0,79}", CONFIG[key]):
            raise ValueError(f"Invalid output identifier: {key}")
    if not re.fullmatch(r"[0-9a-f]{64}", CONFIG["catalog_sha256"]):
        raise ValueError("Invalid catalog SHA-256")
    ROOT = (path.parent / CONFIG["project_root"]).resolve()
    def local(key):
        result = (ROOT / CONFIG[key]).resolve()
        if not result.is_relative_to(ROOT):
            raise ValueError(f"Project path escapes root: {key}")
        return result
    AREA, SOURCE = local("area"), local("source")
    for key in ("controls", "catalog", "profile"):
        local(key)
    # Tool paths are explicit trusted configuration and may point to a shared environment.
    TRESTLE, PANDOC = [(ROOT / CONFIG[key]).resolve() for key in ("trestle", "pandoc")]
    if any(not tool.is_file() for tool in (TRESTLE, PANDOC)):
        raise ValueError("Configured Trestle or Pandoc executable is unavailable")
    CATALOG_SHA, REVISION, DATE = CONFIG["catalog_sha256"], CONFIG["application_revision"], CONFIG["date"]
    spec = importlib.util.spec_from_file_location("project_import_adapter", local("adapter"))
    ADAPTER = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ADAPTER)
    for name in ("load_controls", "supplement", "sharing_links", "build_full", "verify_document"):
        if not callable(getattr(ADAPTER, name, None)):
            raise ValueError(f"Import adapter is missing {name}")


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path, value):
    write(path, json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def identity(name):
    path = AREA / "identities.json"
    identities = json.loads(path.read_text()) if path.exists() else {}
    if name not in identities:
        identities[name] = str(uuid.uuid4())
        write_json(path, identities)
    return identities[name]


def run(command, workspace, log):
    if command[0] not in {str(TRESTLE), str(PANDOC)}:
        raise ValueError("Only pinned local Trestle and Pandoc executables are allowed")
    result = subprocess.run(command, cwd=workspace, text=True, capture_output=True, timeout=180)
    entry = {"at": datetime.now(timezone.utc).isoformat(), "command": list(map(str, command)),
             "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
    log.append(entry)
    write_json(AREA / "commands.json", log)
    if result.returncode:
        raise RuntimeError(f"Command failed ({result.returncode}): {command}\n{result.stderr}\n{result.stdout}")
    return result.stdout


def trestle(workspace, log, *args):
    return run([str(TRESTLE), *args, "--trestle-root", str(workspace)], workspace, log)


def metadata(title):
    return {"title": title, "last-modified": DATE, "version": "assembly-test-1",
            "oscal-version": "1.2.1"}


def load_controls():
    return ADAPTER.load_controls(ROOT, CONFIG)


def prepare(workspace, controls, log):
    existing = {p.stem for p in (workspace / "controls").glob("*.md")}
    expected = {c["id"] for c in controls}
    if len(expected) != len(controls) or not expected:
        raise ValueError("Control adapter returned an empty or duplicate inventory")
    if existing - expected:
        raise ValueError("Workspace contains stale controls; use a fresh --workspace")
    catalog = ROOT / CONFIG["catalog"]
    if digest(catalog) != CATALOG_SHA:
        raise ValueError("Pinned catalog hash mismatch")
    if not (workspace / ".trestle").exists():
        trestle(workspace, log, "init", "--local")
    write(workspace / "catalogs/nist/catalog.json", catalog.read_text())
    profile = json.loads((ROOT / CONFIG["profile"]).read_text())
    selected = profile["profile"]["imports"][0]["include-controls"][0]["with-ids"]
    if set(selected) != {c["id"] for c in controls}:
        raise ValueError("Template profile and controls differ")
    profile["profile"]["imports"][0]["href"] = "trestle://catalogs/nist/catalog.json"
    # OSCAL minItems disallows empty alters; omitting an empty optional list preserves meaning.
    if profile["profile"].get("modify", {}).get("alters") == []:
        del profile["profile"]["modify"]["alters"]
    write_json(workspace / "profiles/lato/profile.json", profile)
    titles = sorted({title for c in controls for title in
                     re.findall(r"^### (.+)$", c["narrative"], re.M) if title != "This System"})
    components = []
    for title in titles:
        requirements = [{"uuid": identity(f"{title}/{c['id']}"), "control-id": c["id"],
                         "description": "Imported attribution only; consult the per-part source prose."}
                        for c in controls if f"### {title}\n" in c["narrative"]]
        components.append({"uuid": identity(title), "type": "service", "title": title,
                           "description": "Attribution of imported SSP prose only; no provider attestation.",
                           "purpose": "Assembly test of attributed source responsibilities.",
                           "control-implementations": [{"uuid": identity(title + "/controls"),
                               "source": "trestle://profiles/lato/profile.json",
                               "description": "Assembly attribution, not provider implementation evidence.",
                               "implemented-requirements": requirements}]})
    if components:
        write_json(workspace / "component-definitions/source-attribution/component-definition.json",
                   {"component-definition": {"uuid": identity("source-attribution"),
                                             "metadata": metadata("Source attribution for assembly test"),
                                             "components": components}})
    for control in controls:
        header = {"x-trestle-global": {"profile": {"title": profile["profile"]["metadata"]["title"],
                                                   "href": "trestle://profiles/lato/profile.json"}}}
        if "x-trestle-set-params" in control["meta"]:
            header["x-trestle-set-params"] = control["meta"]["x-trestle-set-params"]
        content = "---\n" + yaml.safe_dump(header, sort_keys=False) + "---\n\n"
        content += f"# {control['id']}\n\n## What is the solution and how is it implemented?\n\n"
        content += control["narrative"] + "\n"
        write(workspace / "controls" / f"{control['id']}.md", content)
    trestle(workspace, log, "author", "profile-resolve", "-n", "lato", "-o", "lato-resolved")


def assemble(workspace, log):
    args = ["author", "ssp-assemble", "-m", "controls", "-o", CONFIG["model_name"]]
    if (workspace / "component-definitions/source-attribution/component-definition.json").exists():
        args += ["-cd", "source-attribution"]
    trestle(workspace, log, *args)
    path = workspace / "system-security-plans" / CONFIG["model_name"] / "system-security-plan.json"
    first = json.loads(path.read_text())
    trestle(workspace, log, *args)
    second = json.loads(path.read_text())
    if first != second:
        raise ValueError("Unchanged repeated SSP assembly differs")
    trestle(workspace, log, "validate", "--all")
    return second


def responses(control):
    """Map every source component response to its control/part location."""
    result = {}
    part = ""
    component = None
    lines = []

    def flush():
        if component is not None:
            value = "\n".join(lines).strip()
            if value:
                result[(part.strip("()."), component)] = value

    for line in control["narrative"].splitlines():
        heading = re.match(r"## Implementation for part (.+)", line)
        comp = re.match(r"### (.+)", line)
        if heading or comp:
            flush()
            lines = []
            if heading:
                part, component = heading.group(1), None
            else:
                component = comp.group(1)
        else:
            lines.append(line)
    flush()
    return result


def verify_responses(ssp, controls):
    model = ssp["system-security-plan"]
    names = {c["uuid"]: c["title"] for c in model["system-implementation"]["components"]}
    requirements = {c["control-id"]: c for c in model["control-implementation"]["implemented-requirements"]}
    if set(requirements) != {c["id"] for c in controls}:
        raise ValueError("Assembled control inventory differs")
    count = 0
    for control in controls:
        req = requirements[control["id"]]
        actual = {( "", names[c["component-uuid"]]): c["description"] for c in req.get("by-components", [])}
        for statement in req.get("statements", []):
            part = statement["statement-id"].removeprefix(control["id"] + "_smt.")
            for comp in statement.get("by-components", []):
                actual[(part, names[comp["component-uuid"]])] = comp["description"]
        for key, expected in responses(control).items():
            if actual.get(key, "").strip() != expected:
                raise ValueError(f"Response lost or moved: {control['id']} {key}")
            count += 1
    return count


def review_model(ssp, controls):
    """Keep raw assembler output; publish a review model without invented status claims."""
    result = copy.deepcopy(ssp)
    model = result["system-security-plan"]
    model["metadata"] = metadata(CONFIG.get("system_name", "System") + " — assembly test, not approved SSPP")
    characteristics = model["system-characteristics"]
    characteristics["system-name"] = CONFIG.get("system_name", "System")
    characteristics["system-name-short"] = CONFIG.get("system_name", "System")
    characteristics["system-ids"] = [{"id": "assembly-test-not-fisma-id"}]
    characteristics["description"] = "Draft assembled from attributed source narratives and current review material."
    characteristics["authorization-boundary"]["description"] = "Pending owner approval; see the full-document gap report."
    characteristics["status"] = {"state": "other", "remarks": "Assembly test; operational status not determined by tooling."}
    characteristics["system-information"]["information-types"] = [{
        "title": "Pending owner-confirmed categorization", "description": "See imported chapter 2; not approved by this assembly test."}]
    sources = {c["id"]: c for c in controls}
    for req in model["control-implementation"]["implemented-requirements"]:
        control = sources[req["control-id"]]
        names = {c["uuid"]: c["title"] for c in model["system-implementation"]["components"]}
        expected = responses(control)
        # Component-definition seed descriptions are scaffolding, not source responses.
        if "by-components" in req:
            req["by-components"] = [c for c in req["by-components"]
                                    if ("", names[c["component-uuid"]]) in expected]
            if not req["by-components"]:
                del req["by-components"]
        req["remarks"] = f"Current assessment — {CONFIG.get('assessment_date', '')}\n\n" + control["assessment"]
        req["props"] = [{"name": "source-status-selection", "value": value} for value in
                        control["meta"]["x-migration-status-selections"]] or [
                            {"name": "source-status-selection", "value": "UNSELECTED"}]
        for holder in [req, *req.get("statements", [])]:
            for comp in holder.get("by-components", []):
                comp.pop("implementation-status", None)
    return result


def sharing_links(text):
    return ADAPTER.sharing_links(text)


def frontmatter(title):
    return "---\n" + yaml.safe_dump({"title": title, "description": "Draft assembly test",
        "status": "draft", "tier": 2, "author": "OpenCode AI agent", "date": CONFIG["assessment_date"]}, sort_keys=False) + "---\n\n"


def controls_template(workspace, controls):
    text = frontmatter(CONFIG["system_name"] + " — Security and Privacy Controls — Review Draft")
    text += (f"# Review scope\n\nAssembly test from {len(controls)} controls. Imported implementation narratives and provider "
             "responsibilities remain attributed claims; current assessments follow each control. "
             "Source checkboxes are not effectiveness determinations. Baseline parameters require owner review.\n\n"
             f"Application source: `{REVISION}`. Prepared with AI assistance.\n\n# 13 Minimum Security Controls\n\n")
    for control in controls:
        cid = control["id"]
        text += f"{{{{ ssp_md_writer.get_control_statement('{cid}', 1) }}}}\n\n"
        text += f"### {cid.upper()} Source status and provenance\n\n"
        selected = ", ".join(control["meta"]["x-migration-status-selections"]) or "UNSELECTED"
        text += f"Imported selections: **{selected}**. Effectiveness: **NOT_ASSESSED**.\n\n"
        text += f"Source: `{control['meta']['x-migration-source']}`, lines {control['meta']['x-migration-source-lines']}.\n\n"
        text += "### Attributed implementation and provider responsibilities\n\n"
        text += f"{{{{ ssp_md_writer.get_control_response('{cid}', 3, false, true, false, false) }}}}\n\n"
        review = sharing_links(control["assessment"])
        write(workspace / "reviews" / f"{cid}.md", review + "\n")
        text += f"### {cid.upper()} Current assessment — {CONFIG['assessment_date']}\n\n"
        text += "{% md_clean_include 'reviews/" + cid + ".md' %}\n\n"
    supplement = ADAPTER.supplement(ROOT, CONFIG)
    write(workspace / "reviews/supplement.md", sharing_links(supplement).strip() + "\n")
    text += "# Source review supplement\n\nAppendix A — Current source review.\n\n"
    text += "{% md_clean_include 'reviews/supplement.md' %}\n"
    write(workspace / "controls.jinja", text)


def build_full(controls_md):
    return ADAPTER.build_full(controls_md, ROOT, CONFIG, frontmatter)


def docx_text(path):
    with zipfile.ZipFile(path) as archive:
        tree = ET.fromstring(archive.read("word/document.xml"))
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    text = "\n".join("".join(p.itertext()) for p in tree.findall(".//w:p", ns))
    return text, len(tree.findall(".//w:tbl", ns)), len(tree.findall(".//w:pStyle", ns))


def export(workspace, ssp, controls, log):
    controls_template(workspace, controls)
    review = review_model(ssp, controls)
    verify_responses(review, controls)
    write_json(AREA / "exports" / (CONFIG["model_name"] + ".oscal.json"), review)
    write_json(workspace / "system-security-plans" / CONFIG["export_model"] / "system-security-plan.json", review)
    trestle(workspace, log, "validate", "--all")
    trestle(workspace, log, "author", "jinja", "-i", "controls.jinja", "-o", "controls.md",
            "-ssp", CONFIG["export_model"], "-p", "lato")
    controls_md = sharing_links(html.unescape((workspace / "controls.md").read_text()))
    write(AREA / "exports" / (CONFIG["controls_output"] + ".md"), controls_md)
    full, chapters = build_full(controls_md)
    write(AREA / "exports" / (CONFIG["full_output"] + ".md"), full)
    reports = {}
    # Compare rendered prose from every input block with actual DOCX text, not just file size.
    blocks = [sharing_links(value) for c in controls for value in responses(c).values()]
    blocks += [sharing_links(c["assessment"]) for c in controls]
    separator = "ASSEMBLY_BLOCK_SEPARATOR_7391"
    write(workspace / "expected.md", (f"\n\n{separator}\n\n").join(blocks))
    run([str(PANDOC), str(workspace / "expected.md"), "--from=markdown-smart", "--to=plain", "--wrap=none",
         "-o", str(workspace / "expected.txt")], ROOT, log)
    plain = (workspace / "expected.txt").read_text()
    normalize = lambda value: re.sub(r"\s+", "", value).replace("\\", "")
    expected = [normalize(block) for block in plain.split(separator)]
    for name in [CONFIG["controls_output"], CONFIG["full_output"]]:
        path = AREA / "exports" / name
        run([str(PANDOC), str(path.with_suffix(".md")), "--from=markdown-smart", "--to=docx",
             "--standalone", "--toc", "--toc-depth=3", "--resource-path", str(ROOT),
             "-o", str(path.with_suffix(".docx"))], ROOT, log)
        text, tables, styles = docx_text(path.with_suffix(".docx"))
        actual = normalize(text)
        for index, block in enumerate(expected):
            if block not in actual:
                raise ValueError(f"DOCX lost source block {index}: {name}")
        for control in controls:
            if f"{control['id'].upper()} Current assessment" not in text:
                raise ValueError(f"DOCX lost assessment: {name} {control['id']}")
        ADAPTER.verify_document(text)
        reports[name] = {"tables": tables, "styled_paragraphs": styles,
                         "source_blocks_verified": len(expected),
                         "docx_sha256": digest(path.with_suffix(".docx")),
                         "markdown_sha256": digest(path.with_suffix(".md"))}
    return reports, chapters


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path)
    parser.add_argument("--workspace", type=Path)
    args = parser.parse_args()
    if args.project:
        configure(args.project.resolve())
    if not CONFIG:
        parser.error("--project is required")
    workspace = (args.workspace or AREA / "workspace-v2").resolve()
    workspace.mkdir(parents=True, exist_ok=True)
    log_path = AREA / "commands.json"
    log = json.loads(log_path.read_text()) if log_path.exists() else []
    controls = load_controls()
    prepare(workspace, controls, log)
    ssp = assemble(workspace, log)
    response_count = verify_responses(ssp, controls)
    reports, chapters = export(workspace, ssp, controls, log)
    write_json(AREA / "result.json", {"controls": len(controls), "responses_verified": response_count,
        "repeat_assembly_equal": True, "exports": reports, "chapter_sources": chapters,
        "source_hashes": {str(c['path'].relative_to(ROOT)): digest(c['path']) for c in controls}})
    print(f"PASS: {len(controls)} controls, {response_count} exact part/component responses, two DOCX exports")


if __name__ == "__main__":
    main()
