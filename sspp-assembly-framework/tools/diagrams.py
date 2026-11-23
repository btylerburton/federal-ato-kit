"""Pinned offline PlantUML rendering and structural diagram metadata validation."""
import hashlib
import re
import struct
import subprocess
from pathlib import Path
from xml.parsers import expat

VERSION = "1.2026.2"
SHA256 = "3cdce52133c424dea22425b947ae9d47f2167b0866dfcf99e714d4ea1689975c"
URL = "https://github.com/plantuml/plantuml/releases/download/v1.2026.2/plantuml.jar"
VIEWS = {"context", "boundary", "architecture", "data-flow", "sequence"}


def validate(module):
    for field in ("view", "environment", "revision", "review_status", "caption", "alt"):
        value = module.get(field)
        if not isinstance(value, str) or not value.strip() or "\n" in value:
            raise ValueError(f"Diagram {module.get('id')} needs {field}")
    if module["view"] not in VIEWS or module["review_status"] not in {"draft", "reviewed", "approved"}:
        raise ValueError("Invalid diagram view or review status")
    nodes = module.get("nodes")
    edges = module.get("flows")
    if not isinstance(nodes, list) or not nodes or not isinstance(edges, list):
        raise ValueError("Diagram needs nodes and flows inventories")
    ids = set()
    for node in nodes:
        if not isinstance(node, dict) or not re.fullmatch(r"[a-z][a-z0-9_]*", node.get("id", "")):
            raise ValueError("Invalid diagram node ID")
        if node["id"] in ids or node.get("boundary") not in {"inside", "outside"}:
            raise ValueError("Duplicate node or missing inside/outside boundary")
        ids.add(node["id"])
    for flow in edges:
        if not isinstance(flow, dict) or flow.get("from") not in ids or flow.get("to") not in ids:
            raise ValueError("Flow references an unknown node")
        for field in ("data", "protocol", "authentication", "storage"):
            if not isinstance(flow.get(field), str) or not flow[field].strip():
                raise ValueError(f"Flow needs {field}")
    if module["view"] == "data-flow" and not edges:
        raise ValueError("Data-flow view needs at least one flow")


def check_source(content, module):
    source = content.decode("utf-8")
    if len(content) > 256 * 1024:
        raise ValueError("Diagram source exceeds 256 KiB")
    if len(re.findall(r"^@startuml(?:\s.*)?$", source, re.M)) != 1 or len(re.findall(r"^@enduml\s*$", source, re.M)) != 1:
        raise ValueError("Expected exactly one PlantUML diagram")
    # The portable subset is self-contained. No preprocessing, file includes, URLs or sprites.
    if re.search(r"^\s*!|https?://|file:|\[\[|<img|%[a-zA-Z_]+\(", source, re.M | re.I):
        raise ValueError("Diagram source must be self-contained without includes, links or preprocessing")
    declarations = set(re.findall(r"\bas\s+([a-z][a-z0-9_]*)\b", source))
    if declarations != {n["id"] for n in module["nodes"]}:
        raise ValueError("Source node aliases differ from diagram inventory")
    arrows = set(re.findall(r"^\s*([a-z][a-z0-9_]*)\s*-+>\s*([a-z][a-z0-9_]*)\s*:", source, re.M))
    if arrows != {(flow["from"], flow["to"]) for flow in module["flows"]}:
        raise ValueError("Source directed arrows differ from flow inventory; use 'from --> to : label'")
    return source


def svg_size(content):
    parser = expat.ParserCreate()
    root = []
    def start(name, attrs):
        if not root:
            root.append((name, attrs))
    def reject(*args):
        raise ValueError("SVG entity/DTD declarations are not allowed")
    parser.StartElementHandler = start
    parser.StartDoctypeDeclHandler = reject
    parser.EntityDeclHandler = reject
    parser.Parse(content, True)
    if not root or root[0][0] != "svg":
        raise ValueError("Renderer did not produce SVG")
    return root[0][1].get("width"), root[0][1].get("height")


def render(content, module, jar):
    validate(module)
    check_source(content, module)
    if jar is None or not Path(jar).is_file():
        raise ValueError("Diagram rendering requires --plantuml-jar with the pinned local JAR")
    jar = Path(jar).resolve()
    if hashlib.sha256(jar.read_bytes()).hexdigest() != SHA256:
        raise ValueError("PlantUML JAR hash does not match pinned version")
    outputs = {}
    for kind in ("svg", "png"):
        # Smetana is bundled in the JAR, avoiding a separate Graphviz dependency.
        result = subprocess.run(["java", "-Djava.awt.headless=true", "-DPLANTUML_SECURITY_PROFILE=SANDBOX",
                                 "-jar", str(jar), "-Playout=smetana", "-charset", "UTF-8",
                                 "-nometadata", "-failfast2", "-t" + kind, "-pipe"],
                                input=content, capture_output=True, timeout=90, check=False)
        if result.returncode:
            raise ValueError(f"PlantUML {kind} failed: {result.stderr.decode(errors='replace')[:1000]}")
        if kind == "svg":
            svg_size(result.stdout)
        elif not result.stdout.startswith(b"\x89PNG\r\n\x1a\n") or len(result.stdout) < 24:
            raise ValueError("Renderer did not produce PNG")
        elif min(struct.unpack(">II", result.stdout[16:24])) == 0:
            raise ValueError("PNG has empty dimensions")
        outputs[kind] = result.stdout
    return outputs
