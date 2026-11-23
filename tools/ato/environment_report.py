#!/usr/bin/env python3
"""Inventory the current environment and test a supplied package's Trestle models offline."""

import argparse
import json
from datetime import datetime, timezone
from importlib.metadata import distributions, version
from pathlib import Path

from pydantic import ValidationError
from trestle.oscal.component import ComponentDefinition


def licenses():
    records = []
    for distribution in sorted(distributions(), key=lambda d: d.metadata["Name"].lower()):
        metadata = distribution.metadata
        records.append({
            "name": metadata["Name"], "version": distribution.version,
            "license_expression": metadata.get("License-Expression"),
            "license_classifiers": [c for c in metadata.get_all("Classifier", [])
                                    if c.startswith("License ::")],
            "license_metadata": (metadata.get("License") or "").splitlines()[:1],
        })
    return records


def components(root):
    checks = []
    paths = sorted(root.glob("component-definitions/*/component-definition.json"))
    if not paths:
        raise ValueError("No component definitions found")
    for path in paths:
        document = json.loads(path.read_text())["component-definition"]
        try:
            model = ComponentDefinition.model_validate(document)
            ComponentDefinition.model_validate_json(model.model_dump_json(by_alias=True))
            status = "PASS"
        except ValidationError:
            status = "FAIL"
        invalid = dict(document)
        invalid.pop("uuid", None)
        try:
            ComponentDefinition.model_validate(invalid)
            negative = "FAIL"
        except ValidationError:
            negative = "PASS"
        checks.append({"artifact": str(path.relative_to(root)), "model_roundtrip": status,
                       "missing_uuid_rejected": negative,
                       "declared_oscal_version": document["metadata"]["oscal-version"]})
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", type=Path, required=True)
    args = parser.parse_args()
    checks = components(args.package)
    print(json.dumps({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "trestle_version": version("compliance-trestle"),
        "scope": "Installed metadata and Trestle object-model validation; no remote resolution",
        "licenses": licenses(), "components": checks,
        "not_assessed": ["Exact historical OSCAL schema conformance", "Profile resolution",
                         "SSP assembly", "Provider inheritance", "Operational effectiveness"],
    }, indent=2))
    return int(any(c["model_roundtrip"] != "PASS" or c["missing_uuid_rejected"] != "PASS"
                   for c in checks))


if __name__ == "__main__":
    raise SystemExit(main())
