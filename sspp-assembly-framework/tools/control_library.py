#!/usr/bin/env python3
"""Generate illustrative control guidance from the pinned NIST OSCAL catalog."""

import argparse
import hashlib
import json
import re
from functools import lru_cache
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PARAM = re.compile(r"\{\{\s*insert:\s*param,\s*([^}\s]+)\s*\}\}")


def control_records(catalog):
    """Return every control and enhancement, including withdrawn records, by ID."""
    records = {}

    def visit(node):
        for control in node.get("controls", []):
            if not re.fullmatch(r"[a-z]+-[0-9]+(?:\.[0-9]+)?", control["id"]):
                raise ValueError("Invalid control ID")
            if control["id"] in records:
                raise ValueError(f"Duplicate control ID: {control['id']}")
            records[control["id"]] = control
            visit(control)
        for group in node.get("groups", []):
            visit(group)

    visit(catalog.get("catalog", catalog))
    return records


@lru_cache(maxsize=4)
def load_catalog(root=ROOT):
    """Read the locally pinned catalog without network access."""
    root = Path(root)
    data = (root / "data/control-library/catalog.json").read_bytes()
    provenance = json.loads((root / "data/control-library/provenance.json").read_text())
    if hashlib.sha256(data).hexdigest() != provenance["catalog"]["sha256"]:
        raise ValueError("Pinned control catalog hash mismatch")
    return json.loads(data)


def parts(node):
    """Walk parts without accidentally including child enhancement requirements."""
    for part in node.get("parts", []):
        yield part
        yield from parts(part)


def withdrawn(control):
    return any(p["name"] == "status" and p["value"] == "withdrawn"
               for p in control.get("props", []))


def prose(text):
    text = PARAM.sub(lambda match: f"[PARAM {match[1]}]", text)
    # OSCAL fragment targets belong to the source catalog, not the SSPP document.
    text = re.sub(r"\[([^\]]+)\]\(\s*<?(#[^\s)>]+)>?\s*\)",
                  r"\1 (catalog reference: `\2`)", text)
    text = re.sub(r"\[([^\]]+)\]\((mailto:[^)]+)\)",
                  r"\1 (catalog contact: `\2`)", text)
    return "\n".join(line.rstrip() for line in text.splitlines()).strip()


def statements(control):
    for part in control.get("parts", []):
        if part["name"] == "statement":
            yield part
            yield from parts(part)


def parameters(control, catalog):
    """Include referenced parameters, including parent and sibling definitions."""
    result = {p["id"]: p for p in control.get("params", [])}
    available = {p["id"]: p for record in control_records(catalog).values()
                 for p in record.get("params", [])}
    available.update(result)
    texts = [p.get("prose", "") for p in parts(control)]
    while texts:
        for key in PARAM.findall(texts.pop()):
            if key not in result:
                if key not in available:
                    raise ValueError(f"Undefined parameter {key} in {control['id']}")
                result[key] = available[key]
                texts.extend(available[key].get("select", {}).get("choice", []))
    return result


def parameter_questions(control, catalog):
    rows = ["### Parameter decisions"]
    for key, param in parameters(control, catalog).items():
        selection = param.get("select")
        definition = prose(param.get("label", "selection"))
        if selection:
            definition += (f"; choose {selection.get('how-many', 'one')} from: "
                           + "; ".join(prose(c) for c in selection["choice"]))
        rows.append(f"- `{key}` — What approved value applies to **{definition}**? "
                    "Record the value, scope, approving authority, and decision source.")
        rows.extend(f"  - Catalog context: {prose(g['prose'])}"
                    for g in param.get("guidelines", []))
    if len(rows) == 1:
        rows.append("The catalog defines no organization-assigned parameters for this control.")
    return rows


def illustrative_response(control, catalog):
    rows = ["ILLUSTRATIVE TEMPLATE ONLY — NOT AN IMPLEMENTATION OR ASSESSMENT RESULT.",
            "Replace every placeholder with verified system facts before using a response.",
            "System: [SYSTEM]. Owner: [ACCOUNTABLE ROLE]. Scope: [BOUNDARY/COMPONENTS].",
            "Responsibility: [SYSTEM/PROVIDER/SHARED; cite responsibility matrix]."]
    for part in statements(control):
        if part.get("prose"):
            rows.append(f"\nResponse for {part['id']} — {prose(part['prose'])}\n"
                        "[RESPONSIBLE ROLE] uses [IMPLEMENTED MECHANISM/PROCEDURE] in "
                        "[COMPONENT/SCOPE] to satisfy this requirement by [CONCRETE ACTIONS]. "
                        "Operation is triggered by [EVENT/FREQUENCY]. "
                        "[EVIDENCE ID AND LOCATION] records [OBSERVATION, DATE, AND RESULT]. "
                        "[EXCEPTIONS/GAPS AND TRACKED WORK] describes any unmet requirement.")
    for key in parameters(control, catalog):
        rows.append(f"Parameter {key}: [APPROVED VALUE]; authority/source: [DECISION REFERENCE].")
    # Catalog prose must never terminate the illustrative HTML comment.
    body = "\n\n".join(rows).replace("--", "&#45;&#45;")
    return "### Illustrative parameterized response\n\n" + "<!--\n" + body + "\n-->"


def assessment_guidance(control):
    rows = ["### Catalog assessment objectives and evidence",
            "These are catalog assessment targets, not collected evidence or passing results. "
            "Select applicable objects, register actual evidence, and record dated observations."]
    for part in control.get("parts", []):
        if part["name"] == "assessment-objective":
            for objective in [part, *parts(part)]:
                if objective.get("prose"):
                    targets = ", ".join(link["href"].lstrip("#")
                                        for link in objective.get("links", [])
                                        if link.get("rel") == "assessment-for")
                    rows.append(f"- `{objective['id']}` ({targets or 'control objective'}): "
                                + prose(objective["prose"]))
        elif part["name"] == "assessment-method":
            method = next(p["value"] for p in part["props"] if p["name"] == "method")
            rows.append(f"#### {method} — `{part['id']}`")
            for obj in parts(part):
                if obj.get("prose"):
                    rows.extend("- " + prose(item) for item in obj["prose"].split("\n\n") if item.strip())
    return rows


def source_links(control, catalog):
    rows = ["### Authoritative sources",
            "- [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5)",
            "- [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5)",
            f"- Pinned OSCAL catalog version: {catalog.get('metadata', {}).get('version', 'unspecified')}; "
            f"record ID: `{control['id']}`. The library index records the exact source revision and hash."]
    resources = {r["uuid"]: r for r in catalog.get("back-matter", {}).get("resources", [])}
    for link in control.get("links", []):
        target = link["href"].lstrip("#")
        resource = resources.get(target)
        if resource:
            for rlink in resource.get("rlinks", []):
                if rlink["href"].startswith(("https://", "http://")):
                    rows.append(f"- [{resource.get('title', target)}]({rlink['href']})")
        elif link["href"].startswith("#"):
            rows.append(f"- Catalog relationship **{link.get('rel', 'reference')}**: `{target}`.")
    return rows


def guidance_markdown(control, catalog=None):
    """Return appendable guidance; only illustrative responses are HTML-commented."""
    catalog = load_catalog() if catalog is None else catalog
    catalog = catalog.get("catalog", catalog)
    rows = ["## Catalog-grounded response guidance",
            "Template guidance only. This material does not establish implementation, "
            "applicability, inheritance, or assessment status."]
    if withdrawn(control):
        rows += ["### Withdrawn disposition",
                 "**Withdrawn in the pinned catalog.** Do not author an active implementation "
                 "response for this withdrawn record. Review the catalog disposition and "
                 "any successor controls when documenting the tailoring decision."]
        rows.extend(prose(p["prose"]) for p in parts(control) if p.get("prose"))
        dispositions = [link for link in control.get("links", [])
                        if link.get("rel") in {"incorporated-into", "moved-to"}]
        rows.extend(f"- {link['rel']}: `{link['href'].lstrip('#')}`." for link in dispositions)
        if not dispositions:
            rows.append("No successor relationship is specified in this catalog record.")
    else:
        rows.append("### Control-specific description (catalog guidance)")
        rows.extend(prose(p["prose"]) for p in control.get("parts", [])
                    if p["name"] == "guidance" and p.get("prose"))
        rows.append("### Requirements and exact statement parts")
        for part in statements(control):
            rows.append(f"- `{part['id']}`: {prose(part.get('prose', 'Statement grouping; see child parts.'))}")
        rows.append(illustrative_response(control, catalog))
        rows.append("### Questions to complete the real response")
        for part in statements(control):
            if part.get("prose"):
                rows.append(f"- `{part['id']}` — For “{prose(part['prose'])}”, "
                            "who performs the action, using which mechanism, on which components, "
                            "and on what event or schedule? Cite evidence of the actual outcome "
                            "and identify gaps. Apply the parent statement context to child parts.")
        rows.extend(parameter_questions(control, catalog))
        rows.extend(assessment_guidance(control))
    rows.extend(source_links(control, catalog))
    return "\n\n".join(rows) + "\n"


def markdown_document(title, body):
    title = title.strip()
    return (f"---\ntitle: {json.dumps(title)}\n"
            'description: "Generated catalog-grounded illustrative control guidance"\n'
            f"status: draft\ntier: 3\n---\n\n# {title}\n\n{body.rstrip()}\n\n"
            "## Toolkit documents and examples\n\n"
            "- [Project intake: establish scope, owners and baseline](../../docs/templates/project-intake.md)\n"
            "- [Verification record template: capture actual checks](../../docs/templates/verification.md)\n"
            "- [Synthetic evidence manifest example](../claims.json)\n"
            "- [Repository-to-SSPP wizard workflow](../../docs/kit/wizard.md)\n\n"
            "These help organize supporting evidence; their presence does not satisfy the control.\n")


def generate(root=ROOT):
    """Write all control samples and stable machine/human indexes under root."""
    root = Path(root)
    load_catalog.cache_clear()
    catalog = load_catalog(root)
    records = control_records(catalog)
    provenance = json.loads((root / "data/control-library/provenance.json").read_text())
    output = root / "examples/control-library"
    output.mkdir(parents=True, exist_ok=True)
    index = {"catalog": provenance["catalog"], "controls": []}
    rows = ["Generated illustrative templates, not real system implementations. "
            "Active responses are HTML-commented; withdrawn records contain disposition only.",
            f"Pinned source: [{catalog['catalog']['metadata']['title']}]({provenance['catalog']['url']}).",
            "| Control | Title | Catalog status |", "| --- | --- | --- |"]
    for key, control in records.items():
        status = "withdrawn" if withdrawn(control) else "active"
        filename = key + ".md"
        text = markdown_document(f"{key.upper()} — {control['title']}", guidance_markdown(control, catalog))
        (output / filename).write_text(text, encoding="utf-8")
        index["controls"].append({"id": key, "title": control["title"], "status": status,
                                  "path": filename, "sha256": hashlib.sha256(text.encode()).hexdigest()})
        rows.append(f"| [{key.upper()}]({filename}) | {control['title']} | {status} |")
    (output / "index.json").write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    (output / "README.md").write_text(markdown_document("Full NIST control library", "\n\n".join(rows[:2])
                                                      + "\n\n" + "\n".join(rows[2:])), encoding="utf-8")
    return index


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    result = generate(parser.parse_args().root)
    print(f"Generated {len(result['controls'])} control samples.")
