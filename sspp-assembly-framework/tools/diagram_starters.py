"""Synthetic editable architecture starter modules, not real system claims."""
import json


def starters():
    files, modules = {}, []
    views = [("context", "System context"), ("boundary", "Authorization boundary"),
             ("architecture", "Application architecture"), ("data-flow", "Data flow")]
    for view, title in views:
        nodes = [{"id": "viewer", "boundary": "outside"}, {"id": "service", "boundary": "inside"}]
        flows = [{"from": "viewer", "to": "service", "data": "UNFILLED request category",
                  "protocol": "UNFILLED", "authentication": "UNFILLED", "storage": "UNFILLED"}]
        source = ('@startuml\ntitle ' + title + ' — SYNTHETIC STARTER / NOT APPROVED\n'
                  'actor "External viewer" as viewer\nrectangle "Proposed boundary — review required" {\n'
                  '  rectangle "Service — UNFILLED" as service\n}\n'
                  'viewer --> service : UNFILLED request / protocol / auth\n')
        if view == "architecture":
            nodes.append({"id": "store", "boundary": "inside"})
            flows.append({"from": "service", "to": "store", "data": "UNFILLED records",
                          "protocol": "UNFILLED", "authentication": "UNFILLED", "storage": "UNFILLED retention"})
            source = source.replace('}\nviewer', '  database "Store — UNFILLED" as store\n}\nviewer')
            source += 'service --> store : UNFILLED read/write\n'
        if view == "data-flow":
            source += 'note right of service\nData: UNFILLED\nProtocol: UNFILLED\nAuthentication: UNFILLED\nStorage/retention: UNFILLED\nend note\n'
        source += '@enduml\n'
        path = f"diagrams/{view}.puml"
        files[path] = source.encode()
        modules.append({"id": "diagram-" + view, "title": title, "kind": "diagram", "path": path,
                        "source": "Synthetic editable starter", "view": view, "environment": "UNFILLED",
                        "revision": "starter-1", "review_status": "draft", "caption": title + " — owner review required",
                        "alt": title + ": fictional viewer and service; replace with actual components",
                        "nodes": nodes, "flows": flows})
    files["diagrams.json"] = (json.dumps({"modules": modules}, indent=2) + "\n").encode()
    return files, modules
