#!/usr/bin/env python3
"""Portable read-only package/evidence integrity checks, not a compliance attestation."""

import argparse
import hashlib
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

STATUSES = {"PASS", "FAIL", "BLOCKED", "NOT_ASSESSED"}
KINDS = {"source-review", "offline-test", "live-test", "provider-attestation"}
MARKER = "## Original SSP export excerpt\n\n"


def utc_now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("Duplicate JSON key")
            result[key] = value
        return result

    def invalid_number(value):
        raise ValueError("Non-finite JSON number")

    return json.loads(path.read_text(), object_pairs_hook=unique_pairs,
                      parse_constant=invalid_number)


def confined(root, relative):
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise ValueError("Expected a nonempty root-relative artifact path")
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("Artifact escapes its evidence/package root")
    return path


def result(check, status, observation):
    return {"check": check, "status": status, "observation": observation}


def package_checks(root):
    index = read_json(root / "migration-index.json")
    controls = index["controls"]
    if not isinstance(controls, list) or not controls:
        raise ValueError("Nonempty control inventory required")
    checks, seen, paths = [], set(), set()
    for record in controls:
        cid = record["control_id"]
        if not re.fullmatch(r"[a-z]{2}-\d+(?:\.\d+)?", cid) or cid in seen:
            raise ValueError("Invalid or duplicate control ID")
        seen.add(cid)
        path = confined(root, record["path"])
        if path in paths:
            raise ValueError("Duplicate control path")
        paths.add(path)
        if not path.is_file():
            checks.append(result(cid + ":excerpt", "FAIL", "Control file missing"))
            continue
        text = path.read_text()
        excerpt = text.split(MARKER, 1)[1].rstrip("\n") if text.count(MARKER) == 1 else None
        matches = excerpt is not None and digest(excerpt.encode()) == record["source_sha256"]
        checks.append(result(cid + ":excerpt", "PASS" if matches else "FAIL",
                             "Excerpt matches recorded hash" if matches else "Excerpt missing or hash mismatch"))
        selections = record["source_status_selections"]
        if len(selections) != 1:
            checks.append(result(cid + ":status", "BLOCKED", "Source status requires owner resolution"))
        for reference in set(re.findall(r"trestle://([^\s\"'<>]+)", text)):
            target = confined(root, reference)
            checks.append(result(cid + ":reference:" + reference,
                                 "PASS" if target.is_file() else "BLOCKED",
                                 "Local reference exists" if target.is_file() else "Local reference missing"))
    actual = {p.resolve() for p in (root / "control-statements").glob("*/*.md")}
    checks.append(result("control-inventory", "PASS" if actual == paths else "FAIL",
                         f"Inventory: {len(paths)}; files: {len(actual)}; unmatched: {len(actual ^ paths)}"))
    components = sorted((root / "component-definitions").glob("*/component-definition.json"))
    for path in components:
        try:
            read_json(confined(root, str(path.relative_to(root))))
            checks.append(result("json:" + str(path.relative_to(root)), "PASS", "JSON parses; schema not assessed"))
        except (ValueError, OSError):
            checks.append(result("json:" + path.name, "FAIL", "JSON unreadable or invalid"))
    checks.append(result("oscal-schema-and-resolution", "NOT_ASSESSED",
                         "Requires pinned Trestle/model validation and resolved catalog/profile"))
    checks.append(result("implementation-effectiveness", "NOT_ASSESSED",
                         "Excerpt hashes and JSON parsing do not assess implementation"))
    return checks


def timestamp(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("Evidence timestamps require timezone")
    return parsed


def required_strings(record, fields):
    for field in fields:
        if not isinstance(record.get(field), str) or not record[field].strip():
            raise ValueError("Required nonempty field: " + field)


def evidence_check(item, root, now):
    required_strings(item, ["id", "kind", "environment", "source_revision", "observed_at",
                            "expires_at", "artifact", "sha256", "method", "observation", "result"])
    if item["kind"] not in KINDS or item["result"] not in STATUSES:
        raise ValueError("Unsupported evidence kind or result")
    if not re.fullmatch(r"[0-9a-f]{64}", item["sha256"]):
        raise ValueError("Invalid evidence SHA-256")
    observed, expires = timestamp(item["observed_at"]), timestamp(item["expires_at"])
    if observed > now or expires <= observed:
        return "FAIL", "Invalid observation/expiry chronology"
    if expires <= now:
        return "BLOCKED", "Evidence expired"
    path = confined(root, item["artifact"])
    if not path.is_file():
        return "BLOCKED", "Evidence artifact missing"
    if digest(path.read_bytes()) != item["sha256"]:
        return "FAIL", "Evidence artifact hash mismatch"
    return item["result"], "Artifact integrity/freshness checked; recorded result: " + item["result"]


def claim_checks(manifest, root, now=None):
    now = now or datetime.now(timezone.utc)
    if manifest.get("schema_version") != 1:
        raise ValueError("Unsupported claim manifest version")
    claims, evidence = manifest["claims"], manifest["evidence"]
    if not isinstance(claims, list) or not claims or not isinstance(evidence, list):
        raise ValueError("Nonempty claims and evidence list required")
    by_id, checked = {}, {}
    for item in evidence:
        if item["id"] in by_id:
            raise ValueError("Duplicate evidence ID")
        by_id[item["id"]] = item
        checked[item["id"]] = evidence_check(item, root, now)
    checks, seen = [], set()
    for claim in claims:
        required_strings(claim, ["id", "statement", "environment", "source_revision", "required_kind"])
        if claim["id"] in seen or claim["required_kind"] not in KINDS:
            raise ValueError("Duplicate claim ID or unsupported evidence requirement")
        seen.add(claim["id"])
        if not isinstance(claim.get("controls"), list) or not claim["controls"]:
            raise ValueError("Claim needs control mappings")
        if not all(isinstance(c, str) and re.fullmatch(r"[A-Z]{2}-\d+(?:\(\d+\))?", c)
                   for c in claim["controls"]):
            raise ValueError("Invalid control mapping")
        ids = claim.get("evidence_ids")
        if not isinstance(ids, list) or not all(isinstance(i, str) for i in ids):
            raise ValueError("evidence_ids must be a list of strings")
        outcomes = []
        for eid in ids:
            item = by_id.get(eid)
            if item is None:
                outcomes.append(("BLOCKED", "Referenced evidence missing"))
            elif any(item[field] != claim[field] for field in ["environment", "source_revision"]):
                outcomes.append(("BLOCKED", "Evidence environment or revision differs"))
            elif item["kind"] != claim["required_kind"]:
                outcomes.append(("BLOCKED", "Evidence kind does not establish requested scope"))
            else:
                outcomes.append(checked[eid])
        if not outcomes:
            outcomes = [("NOT_ASSESSED", "No evidence supplied")]
        status = next(s for s in ["FAIL", "BLOCKED", "NOT_ASSESSED", "PASS"]
                      if any(outcome[0] == s for outcome in outcomes))
        checks.append(result(claim["id"], status, "; ".join(dict.fromkeys(o[1] for o in outcomes))))
    return checks


def report(checks, mode, started):
    counts = {s: sum(c["status"] == s for c in checks) for s in sorted(STATUSES)}
    return {
        "schema_version": 1, "tool": "ato-verify/0.1.0", "mode": mode,
        "timestamp": utc_now(), "duration_seconds": round(time.monotonic() - started, 3),
        "assurance": "Integrity/readiness checks only; not authorization or proof of claim truth",
        "counts": counts, "checks": checks,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="mode", required=True)
    package = sub.add_parser("package")
    package.add_argument("--package", type=Path, required=True)
    claims = sub.add_parser("claims")
    claims.add_argument("--manifest", type=Path, required=True)
    claims.add_argument("--evidence-root", type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    try:
        checks = (package_checks(args.package) if args.mode == "package" else
                  claim_checks(read_json(args.manifest), args.evidence_root))
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        # Do not echo rejected payloads or host paths in a shareable report.
        checks = [result("input", "FAIL", "Invalid/unreadable input; inspect local manifest and paths")]
    output = report(checks, args.mode, started)
    print(json.dumps(output, indent=2))
    counts = output["counts"]
    return 1 if counts["FAIL"] else 2 if counts["BLOCKED"] or counts["NOT_ASSESSED"] else 0


if __name__ == "__main__":
    sys.exit(main())
