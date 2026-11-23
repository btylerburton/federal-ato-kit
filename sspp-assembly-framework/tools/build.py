#!/usr/bin/env python3
"""Compose a local, manifest-driven SSPP Markdown package. No network or dependencies."""

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ID = re.compile(r"^[a-z][a-z0-9-]{0,79}$")
HASH = re.compile(r"^[0-9a-f]{64}$")
KINDS = {"inline", "asset", "attachment", "reference", "gap", "diagram"}
INVENTORY = "inventory.json"
FORMAT = "sspp-assembly-prototype-v1"


def sha(content):
    return hashlib.sha256(content).hexdigest()


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def text(value, label):
    if not isinstance(value, str) or not value.strip() or "\n" in value or "\r" in value:
        raise ValueError(f"{label} must be a nonempty single-line string")
    return value


def literal(value):
    return re.sub(r"([\\`*{}\[\]<>_!|])", r"\\\1", value)


def https_url(value):
    text(value, "URL")
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("References must use HTTPS URLs without credentials")
    if any(char.isspace() for char in value) or any(char in value for char in "<>"):
        raise ValueError("Reference URL contains unsupported whitespace or delimiters")
    return value


def local_path(root, value):
    text(value, "Path")
    relative = Path(value)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"Path must stay within project: {value}")
    path = (root / relative).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise ValueError(f"Missing or escaping project file: {value}")
    return path


def validate(manifest):
    if not isinstance(manifest, dict) or manifest.get("schema_version") != 1:
        raise ValueError("Expected manifest schema_version 1")
    document = manifest.get("document")
    if not isinstance(document, dict):
        raise ValueError("Missing document object")
    for field in ("title", "revision", "date", "edition"):
        text(document.get(field), f"document.{field}")
    if document["edition"] not in {"review", "publication"}:
        raise ValueError("Edition must be review or publication")
    modules = manifest.get("modules")
    if not isinstance(modules, list) or not modules:
        raise ValueError("At least one module is required")
    seen = set()
    for module in modules:
        if not isinstance(module, dict):
            raise ValueError("Module must be an object")
        key = text(module.get("id"), "module.id")
        if not ID.fullmatch(key) or key in seen:
            raise ValueError(f"Invalid or duplicate module ID: {key}")
        seen.add(key)
        for field in ("title", "kind", "source"):
            text(module.get(field), f"{key}.{field}")
        if module["kind"] not in KINDS:
            raise ValueError(f"Unknown module kind: {key}")
        if "sha256" in module and not HASH.fullmatch(str(module["sha256"])):
            raise ValueError(f"Invalid SHA-256: {key}")
        if module["kind"] == "reference":
            https_url(module.get("url"))
            if module.get("verification") not in {"not-reviewed", "reviewed"}:
                raise ValueError(f"Reference verification state required: {key}")
        if module["kind"] == "asset":
            text(module.get("alt"), f"{key}.alt")
        if module["kind"] == "diagram":
            from diagrams import validate as validate_diagram
            validate_diagram(module)
            if document["edition"] == "publication" and module["review_status"] != "approved":
                raise ValueError(f"Publication diagram lacks owner approval: {key}")
        if module["kind"] == "gap":
            for field in ("tracking", "owner", "reason"):
                text(module.get(field), f"{key}.{field}")
            if document["edition"] == "publication":
                raise ValueError(f"Publication has unresolved gap: {key}")
    return document, modules


def read_inputs(root, modules, plantuml_jar=None):
    inputs, targets, files = {}, {}, {}
    for module in modules:
        key, kind = module["id"], module["kind"]
        targets[key] = "#" + key
        if kind not in {"inline", "asset", "attachment", "diagram"}:
            continue
        path = local_path(root, module.get("path"))
        content = path.read_bytes()
        if "sha256" in module and sha(content) != module["sha256"]:
            raise ValueError(f"Input hash mismatch: {key}")
        inputs[key] = content
        if kind == "diagram":
            from diagrams import render
            for extension, rendered in render(content, module, plantuml_jar).items():
                files[f"assets/{key}.{extension}"] = rendered
            targets[key] = f"assets/{key}.png"
            continue
        if kind != "inline":
            suffix = path.suffix.lower()
            if not re.fullmatch(r"\.[a-z0-9]{1,12}", suffix):
                raise ValueError(f"File needs a simple extension: {key}")
            target = ("assets/" if kind == "asset" else "attachments/") + key + suffix
            targets[key], files[target] = target, content
    return inputs, targets, files


def markdown(content, targets):
    source = content.decode("utf-8")
    if source.startswith("---\n"):
        parts = source.split("\n---\n", 1)
        if len(parts) != 2:
            raise ValueError("Unterminated module frontmatter")
        source = parts[1]
    # Fenced catalog JSON and code examples are literal text, not resource references.
    chunks = re.split(r"(^```[^\n]*\n.*?^```[ \t]*$)", source, flags=re.M | re.S)
    active = "\n".join(chunks[::2])
    # Illustrative responses in HTML comments must not enter assembled documents.
    for index in range(0, len(chunks), 2):
        chunks[index] = re.sub(r"<!--.*?-->", "", chunks[index], flags=re.S)
    active = "\n".join(chunks[::2])
    if re.search(r"!?\[[^\n]*\]\[|^\s*\[[^\]]+\]:", active, re.M):
        raise ValueError("Convert reference-style links/images to registered module targets")
    if re.search(r"<\s*(?:img|script|iframe)\b", active, re.I):
        raise ValueError("Register images as assets; active HTML is not supported")

    def replace(match):
        prefix, label, destination = match.groups()
        if destination.startswith("module:"):
            key = destination.removeprefix("module:")
            if key not in targets:
                raise ValueError(f"Unknown module link: {key}")
            if prefix and not targets[key].startswith("assets/"):
                raise ValueError(f"Image must target a registered asset: {key}")
            return f"{prefix}[{label}]({targets[key]})"
        if prefix:
            raise ValueError("Images must target registered local assets")
        if destination.startswith("https://"):
            https_url(destination)
            return match.group(0)
        raise ValueError(f"Use module:<id> for local links: {destination}")

    for index in range(0, len(chunks), 2):
        chunks[index] = re.sub(r"(!?)\[([^\]\n]*)\]\(([^)\n]+)\)", replace, chunks[index])
    return "".join(chunks).strip()


def compose(manifest_path, plantuml_jar=None):
    manifest_path = manifest_path.resolve()
    manifest = load_json(manifest_path)
    document, modules = validate(manifest)
    inputs, targets, files = read_inputs(manifest_path.parent, modules, plantuml_jar)
    body = [f"# {literal(document['title'])}",
            f"Revision: {literal(document['revision'])} | Date: {literal(document['date'])} | "
            f"Edition: {document['edition']}", "Generated with AI-assisted assembly tooling."]
    records = []
    for module in modules:
        key, kind = module["id"], module["kind"]
        body += [f"## {literal(module['title'])} {{#{key}}}", f"Source: {literal(module['source'])}"]
        if kind == "inline":
            body.append(markdown(inputs[key], targets))
        elif kind in {"asset", "diagram"}:
            body.append(f"![{literal(module['alt'])}]({targets[key]})")
            if kind == "diagram":
                body.append(f"Figure: {literal(module['caption'])}. Environment: {literal(module['environment'])}; "
                            f"revision: {literal(module['revision'])}; review: {module['review_status']}.")
                body.append("| From | To | Data | Protocol | Authentication | Storage |\n"
                            "| --- | --- | --- | --- | --- | --- |\n" + "\n".join(
                                "| " + " | ".join(literal(flow[k]) for k in
                                ("from", "to", "data", "protocol", "authentication", "storage")) + " |"
                                for flow in module["flows"]))
        elif kind == "attachment":
            body.append(f"[Packaged attachment: {literal(module['title'])}]({targets[key]})\n\n"
                        f"SHA-256: `{sha(inputs[key])}`")
        elif kind == "reference":
            body.append(f"[External reference](<{module['url']}>)\n\n"
                        f"Recorded review state: {module['verification']}. Not fetched by this build.")
        else:
            body.append(f"**GAP — {literal(module['tracking'])}**: {literal(module['reason'])}\n\n"
                        f"Owner: {literal(module['owner'])}")
        record = dict(module, target=targets[key])
        if key in inputs:
            record["input_sha256"] = sha(inputs[key])
        if kind == "diagram":
            from diagrams import SHA256, VERSION
            record["renderer"] = {"name": "PlantUML", "version": VERSION, "sha256": SHA256}
        records.append(record)
    files["document.md"] = ("\n\n".join(body) + "\n").encode()
    inventory = {"format": FORMAT, "document": document, "modules": records,
                 "manifest_sha256": sha(manifest_path.read_bytes()),
                 "outputs": {name: sha(value) for name, value in sorted(files.items())}}
    files[INVENTORY] = json_bytes(inventory)
    return files


def owned_outputs(output):
    """Refuse to overwrite user work or follow output symlinks."""
    if output.is_symlink():
        raise ValueError("Output directory may not be a symlink")
    if not output.exists():
        return set()
    if any(path.is_symlink() for path in output.rglob("*")):
        raise ValueError("Output tree contains a symlink")
    existing = {p.relative_to(output).as_posix() for p in output.rglob("*") if p.is_file()}
    if not existing:
        return set()
    if INVENTORY not in existing:
        raise ValueError("Refusing untracked output directory")
    inventory = load_json(output / INVENTORY)
    if inventory.get("format") != FORMAT or not isinstance(inventory.get("outputs"), dict):
        raise ValueError("Invalid output ownership inventory")
    owned = set(inventory["outputs"]) | {INVENTORY}
    if existing != owned:
        raise ValueError("Output directory has missing or untracked files")
    for name, expected in inventory["outputs"].items():
        if sha(local_path(output.resolve(), name).read_bytes()) != expected:
            raise ValueError(f"Refusing modified output: {name}")
    return owned


def build(manifest, output, plantuml_jar=None):
    files = compose(manifest, plantuml_jar)
    return publish(manifest, output, files)


def publish(manifest, output, files):
    """Publish only after all rendering and validation have completed."""
    output = output.absolute()
    # Output cannot replace the manifest directory or an ancestor of its inputs.
    source_root = manifest.resolve().parent
    if source_root.is_relative_to(output.resolve()):
        raise ValueError("Output cannot contain the source project")
    owned = owned_outputs(output)
    output.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        destination = output / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
    for name in owned - files.keys():
        (output / name).unlink()
    return len(files)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--plantuml-jar", type=Path)
    args = parser.parse_args()
    try:
        count = build(args.manifest, args.output, args.plantuml_jar)
    except (ValueError, OSError, UnicodeError, KeyError, TypeError) as error:
        parser.exit(1, f"Assembly refused: {error}\n")
    print(f"PASS: wrote {count} deterministic package files to {args.output}")


if __name__ == "__main__":
    main()
