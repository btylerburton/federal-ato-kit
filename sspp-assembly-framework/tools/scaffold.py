#!/usr/bin/env python3
"""Create non-destructive team SSPP shells from a hash-pinned OSCAL catalog."""

import argparse
import json
import re
import uuid
from pathlib import Path

from build import json_bytes, load_json, sha

FORMAT = "sspp-team-scaffold-v1"
CONTROL_ID = re.compile(r"^[a-z][a-z0-9-]*(?:\.[a-z0-9-]+)*$")
CHAPTERS = [
    ("cover", "Cover and document preparation"),
    ("revision-history", "Revision history"),
    ("guidance", "Document guidance"),
    ("approvals", "Approvals and signature references"),
    ("system-name", "1 Information system name"),
    ("categorization", "2 Categorization and digital identity acceptance"),
    ("owners", "3 System owner"),
    ("authorizing-official", "4 Authorizing official"),
    ("security-responsibilities", "5 Security responsibilities"),
    ("contacts", "6 Other designated contacts"),
    ("operational-status", "7 Operational status"),
    ("system-type", "8 System type and providing systems"),
    ("boundary", "9 System description and authorization boundary"),
    ("environment", "10 Environment, assets, software and data flows"),
    ("interconnections", "11 Interconnections and agreements"),
    ("laws", "12 Applicable laws and regulations"),
    ("control-introduction", "13 Minimum controls and acceptance criteria"),
]
APPENDICES = [("references", "References"), ("attachments", "Attachment index"),
              ("assessment-notes", "Assessment notes and open work")]


def markdown_file(title, description, content):
    # JSON strings are valid YAML scalars; no dependency is needed to write frontmatter.
    return (f"---\ntitle: {json.dumps(title)}\ndescription: {json.dumps(description)}\n"
            f"status: draft\ntier: 3\n---\n\n{content.rstrip()}\n").encode()


def pinned(path, expected):
    if not re.fullmatch(r"[0-9a-f]{64}", expected or ""):
        raise ValueError("Supply a lowercase SHA-256 pin for each catalog")
    content = path.read_bytes()
    if sha(content) != expected:
        raise ValueError(f"Catalog hash mismatch: {path.name}")
    value = load_json(path)
    if not isinstance(value, dict) or not isinstance(value.get("catalog"), dict):
        raise ValueError("Expected an OSCAL catalog; resolve profiles with Trestle first")
    return content, value["catalog"]


def collect_controls(catalog):
    result = {}

    def walk(container):
        for control in container.get("controls", []):
            key = control.get("id", "")
            if not isinstance(key, str) or not CONTROL_ID.fullmatch(key) or key in result:
                raise ValueError(f"Unsafe or duplicate control ID: {key}")
            if not isinstance(control.get("title"), str) or not control["title"].strip():
                raise ValueError(f"Control has no title: {key}")
            result[key] = control
            walk(control)
        for group in container.get("groups", []):
            walk(group)

    walk(catalog)
    if not result:
        raise ValueError("Catalog contains no controls")
    slugs = [key.replace(".", "-") for key in result]
    if len(set(slugs)) != len(slugs):
        raise ValueError("Control IDs collide as document anchors")
    return result


def parts_for(control):
    result = []

    def walk(parts, statement=False):
        for part in parts:
            relevant = statement or part.get("name") == "statement"
            if relevant:
                key = part.get("id")
                if not isinstance(key, str) or not CONTROL_ID.fullmatch(key.replace("_", "-")):
                    raise ValueError("Statement part needs a safe stable ID")
                result.append((key, part))
            walk(part.get("parts", []), relevant)

    walk(control.get("parts", []))
    if len({key for key, _ in result}) != len(result):
        raise ValueError("Duplicate statement part ID")
    return result


def requirement_document(control):
    rows = [f"# {control['id'].upper()} — {control['title']}",
            "Generated catalog requirements. Edit the neighboring response file, not this file."]
    if control.get("props"):
        rows += ["## Catalog properties", "```json\n" + json.dumps(control["props"], indent=2) + "\n```"]

    def walk(parts, depth=2):
        for part in parts:
            rows.append("#" * min(depth, 6) + " " + part.get("name", "part") + " — " + part.get("id", "unidentified"))
            if part.get("prose"):
                # Catalog links are evidence text here; no arbitrary local links enter the build.
                prose = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (catalog reference: `\2`)", part["prose"])
                rows.append(prose)
            walk(part.get("parts", []), depth + 1)

    walk(control.get("parts", []))
    rows.append("## Parameter definitions\n\n```json\n" + json.dumps(control.get("params", []), indent=2) + "\n```")
    return markdown_file(control["title"], "Generated pinned OSCAL control requirements", "\n\n".join(rows))


def response_document(control, part_ids):
    rows = [f"# {control['id'].upper()} — Team response",
            "## Ownership and status\n\n- Responsible owner: UNFILLED\n- Implementation status: UNFILLED\n"
            "- Applicability/tailoring decision: UNFILLED\n- Evidence review state: NOT_ASSESSED",
            "## Parameter assignments\n\nRecord each parameter ID, chosen value, decision authority and source. UNFILLED.",
            "## System implementation\n\nUNFILLED — describe the implemented mechanism and its environment.",
            "## Provider responsibilities\n\nUNFILLED — identify each provider, responsibility and authoritative CRM reference."]
    for key in part_ids:
        rows.append(f"## Response for {key}\n\n- Implementation narrative: UNFILLED\n"
                    "- Responsible component/provider: UNFILLED\n- Evidence references: UNFILLED")
    rows += ["## Evidence references\n\nUNFILLED — register local attachments or external references in supporting.json.",
             "## Current assessment\n\nNOT_ASSESSED — record date, method, observations and limitations.",
             "## Open work\n\nUNFILLED — record tracked item, owner and trigger."]
    return markdown_file(control["title"] + " response", "Team-owned control response; preserved on regeneration", "\n\n".join(rows))


def previous_state(output):
    if output.is_symlink():
        raise ValueError("Scaffold output cannot be a symlink")
    path = output / "scaffold-state.json"
    if not output.exists() or not any(output.iterdir()):
        return {"format": FORMAT, "generated": {}, "identities": {}, "authored": []}
    if not path.is_file() or path.is_symlink():
        raise ValueError("Refusing an existing directory without scaffold ownership state")
    if any(p.is_symlink() for p in output.rglob("*")):
        raise ValueError("Scaffold tree contains a symlink")
    state = load_json(path)
    if state.get("format") != FORMAT:
        raise ValueError("Unsupported scaffold state")
    for name, expected in state["generated"].items():
        target = (output / name).resolve()
        if not target.is_relative_to(output.resolve()) or not target.is_file() or sha(target.read_bytes()) != expected:
            raise ValueError(f"Generated scaffold file modified or missing: {name}")
    return state


def stable_id(identities, key):
    if key not in identities:
        identities[key] = str(uuid.uuid4())
    # Existing values must be well-formed UUIDv4; never silently replace a team's identities.
    value = uuid.UUID(identities[key])
    if value.version != 4:
        raise ValueError(f"Expected UUIDv4 identity: {key}")
    return str(value)


def module(key, title, path, source):
    return {"id": key, "title": title, "kind": "inline", "path": path, "source": source}


def plan(output, full, selected, document, state):
    identities = dict(state["identities"])
    generated, authored, modules, index = {}, {}, [], []
    for key, title in CHAPTERS + APPENDICES:
        path = f"chapters/{key}.md"
        authored[path] = markdown_file(title, "Team-owned SSPP chapter", f"# {title}\n\nUNFILLED — owner, content, source and review date required.")
    authored["supporting.json"] = json_bytes({"modules": []})
    authored["project.json"] = json_bytes(document)
    authored["README.md"] = team_readme()
    from diagram_starters import starters
    diagram_files, default_diagrams = starters()
    authored.update(diagram_files)
    diagram_config = load_json(output / "diagrams.json") if (output / "diagrams.json").exists() else {"modules": default_diagrams}
    if not isinstance(diagram_config, dict) or not isinstance(diagram_config.get("modules"), list):
        raise ValueError("diagrams.json must contain a modules array")
    required_views = {"context", "boundary", "architecture", "data-flow"}
    if not required_views <= {m.get("view") for m in diagram_config["modules"]}:
        raise ValueError("Team template needs context, boundary, architecture and data-flow views")
    for key, title in CHAPTERS:
        modules.append(module(key, title, f"chapters/{key}.md", "Team-authored chapter"))
        if key == "boundary":
            modules.extend(diagram_config["modules"])
    for key, control in full.items():
        folder = key.split("-")[0]
        requirement = f"controls/{folder}/{key}.requirement.md"
        response = f"controls/{folder}/{key}.response.md"
        part_ids = [part_id for part_id, _ in parts_for(control)]
        generated[requirement] = requirement_document(control)
        authored[response] = response_document(control, part_ids)
        record = {"id": key, "title": control["title"], "selected": key in selected,
                  "uuid": stable_id(identities, key), "requirement": requirement, "response": response,
                  "statement_parts": {p: stable_id(identities, key + "/" + p) for p in part_ids}}
        index.append(record)
        if key in selected:
            slug = key.replace(".", "-")
            modules += [module("requirement-" + slug, key.upper() + " Requirement", requirement, "Pinned catalog"),
                        module("response-" + slug, key.upper() + " Response", response, "Team-authored response")]
    for key, title in APPENDICES:
        modules.append(module(key, title, f"chapters/{key}.md", "Team-authored appendix"))
    supporting = load_json(output / "supporting.json") if (output / "supporting.json").exists() else {"modules": []}
    if not isinstance(supporting, dict) or not isinstance(supporting.get("modules"), list):
        raise ValueError("supporting.json must contain a modules array")
    modules.extend(supporting["modules"])
    modules.append({"id": "template-readiness", "title": "Template readiness", "kind": "gap",
                    "tracking": "TEAM-READY-01", "owner": "System owner and ISSO",
                    "reason": "Generated shells are unfilled until the team supplies and reviews implementation evidence.",
                    "source": "Template work register"})
    manifest = {"schema_version": 1, "document": document, "modules": modules}
    from build import validate
    validate(manifest)
    generated["manifest.json"] = json_bytes(manifest)
    generated["control-index.json"] = json_bytes({"controls": index, "total": len(index), "selected": len(selected)})
    # Never delete removed controls: retained responses and identity history appear in the report.
    additions = [key for key in full if key not in state.get("control_ids", [])]
    return generated, authored, identities, additions


def team_readme():
    return markdown_file("Team SSPP project", "Generated team workspace authoring guide", """# Team SSPP project

1. Edit `project.json` for document title/revision/date. Keep edition `review` while shells are unfilled.
2. Fill team-owned `chapters/*.md` and `controls/*/*.response.md`. Generated requirement files are read-only.
3. Edit `diagrams/*.puml` and their metadata in `diagrams.json`; register attachments and HTTPS references in `supporting.json`.
4. Regenerate with the same pinned catalog and optional profile-resolved catalog to update `manifest.json`.
5. Assemble with `python3 /path/to/framework/tools/build.py manifest.json --output build/review --plantuml-jar /path/to/pinned/plantuml.jar`.

Four draft diagram views are provided: system context, authorization boundary, architecture,
and data flow. Replace synthetic components, boundaries and UNFILLED flow metadata before
requesting owner review. SVG and PNG are generated locally; PNG is used for document embedding.

Every catalog control and enhancement gets a shell. `control-index.json` marks the selected
subset used in the document. Passing a profile directly is rejected: resolve it with Trestle
against the pinned catalog, then supply the resolved catalog and its SHA-256 to the scaffolder.

Regeneration preserves existing response/chapter/supporting/project files and UUIDv4 identities.
New controls get new response files. Requirements refresh only when the previous generated file
is unchanged. Removed controls remain on disk for review, and selection changes only export inclusion.
New statement-part IDs are recorded in the index; update the preserved response manually when
the catalog changes. The generation report identifies parts lacking response headings.

UNFILLED is not an implementation status. NOT_ASSESSED is not a failed control. The readiness
gap is deliberately emitted in every generated review manifest. A publication workflow with
owner-approved status/evidence validation is separate work; deleting placeholders is not approval.

Framework-required inputs are versioned catalog files and SHA-256 pins. `scaffold-state.json`
owns generated files and stable IDs; retain it in version control. Generated package output
belongs in `build/`, not among authoring sources. This workspace is not itself an approved SSPP.
""")


def scaffold(catalog, catalog_sha, output, title, date, selection=None, selection_sha=None):
    output = output.absolute()
    raw, full_catalog = pinned(catalog, catalog_sha)
    full = collect_controls(full_catalog)
    selection_raw = None
    selected = full
    if selection:
        selection_raw, resolved = pinned(selection, selection_sha)
        selected = collect_controls(resolved)
        if not set(selected) <= set(full):
            raise ValueError("Selected catalog contains controls absent from the full catalog")
    for source in [catalog, *([selection] if selection else [])]:
        if source.resolve().is_relative_to(output.resolve()):
            raise ValueError("Catalog inputs must be outside the scaffold output")
    state = previous_state(output)
    document = load_json(output / "project.json") if (output / "project.json").exists() else {
        "title": title, "date": date, "revision": "draft-1", "edition": "review"}
    generated, authored, identities, additions = plan(output, full, selected, document, state)
    generated["inputs/catalog.json"] = raw
    if selection_raw:
        generated["inputs/selected-catalog.json"] = selection_raw
    missing = {}
    for key, control in full.items():
        path = f"controls/{key.split('-')[0]}/{key}.response.md"
        response = (output / path).read_text() if (output / path).exists() else authored[path].decode()
        absent = [p for p, _ in parts_for(control) if f"## Response for {p}\n" not in response]
        if absent:
            missing[key] = absent
    # Validate every collision before any artifact mutation.
    for name in generated:
        if (output / name).exists() and name not in state["generated"]:
            raise ValueError(f"Refusing unowned generated-file collision: {name}")
    for name in authored:
        if (output / name).exists() and name not in state["authored"]:
            raise ValueError(f"Refusing unowned authored-file collision: {name}")
        if name in state["authored"] and not (output / name).is_file():
            raise ValueError(f"Team-authored file missing; restore explicitly: {name}")
    old_generated = dict(state["generated"])
    for name, content in generated.items():
        old_generated[name] = sha(content)
    new_state = {"format": FORMAT, "generated": old_generated, "identities": identities,
                 "authored": sorted(set(state["authored"]) | authored.keys()), "control_ids": list(full)}
    # Report deterministically describes current state; additions belong to CLI output only.
    report = {"catalog_sha256": catalog_sha, "selection_sha256": selection_sha,
              "total_controls": len(full), "selected_controls": len(selected),
              "retained_controls_outside_catalog": sorted(set(identities) - set(full) - {k for k in identities if "/" in k}),
              "response_parts_requiring_review": missing, "readiness": "UNFILLED_REVIEW_TEMPLATE"}
    for name, content in {**generated, **{k: v for k, v in authored.items() if not (output / k).exists()}}.items():
        target = output / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    (output / "scaffold-state.json").write_bytes(json_bytes(new_state))
    (output / "generation-report.json").write_bytes(json_bytes(report))
    return report, len(additions)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--catalog-sha256", required=True)
    parser.add_argument("--selected-catalog", type=Path)
    parser.add_argument("--selected-sha256")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--date", required=True)
    args = parser.parse_args()
    try:
        report, added = scaffold(args.catalog, args.catalog_sha256, args.output, args.title, args.date,
                                 args.selected_catalog, args.selected_sha256)
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f"Scaffold refused: {error}\n")
    print(f"PASS: {report['total_controls']} control/enhancement shells; "
          f"{report['selected_controls']} selected; {added} new control shells")


if __name__ == "__main__":
    main()
