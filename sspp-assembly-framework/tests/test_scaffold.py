"""Real scaffold regeneration, preservation and selection tests."""
import copy
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))
import scaffold
import build


class ScaffoldTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="sspp-shells-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.output = self.root / "team"
        self.catalog = self.root / "catalog.json"
        self.data = {"catalog": {"groups": [{"id": "ac", "controls": [
            {"id": "ac-1", "title": "Policy", "parts": [{"id": "ac-1_smt", "name": "statement", "prose": "Maintain policy.",
                 "parts": [{"id": "ac-1_smt.a", "name": "item", "prose": "Review policy."}]}],
             "controls": [{"id": "ac-1.1", "title": "Enhancement", "parts": []}]}]}]}}

    def run_scaffold(self, selected=None):
        self.catalog.write_text(json.dumps(self.data))
        pin = build.sha(self.catalog.read_bytes())
        selection = self.root / "selected.json"
        if selected is not None:
            selection.write_text(json.dumps({"catalog": {"controls": selected}}))
        return scaffold.scaffold(self.catalog, pin, self.output, "Fictional team", "2026-11-16",
                                 selection if selected is not None else None,
                                 build.sha(selection.read_bytes()) if selected is not None else None)

    def snapshot(self):
        return {p.relative_to(self.output).as_posix(): p.read_bytes() for p in self.output.rglob("*") if p.is_file()}

    def test_all_nested_controls_and_parts_created_idempotently(self):
        report, count = self.run_scaffold()
        self.assertEqual((report["total_controls"], count), (2, 2))
        first = self.snapshot()
        self.assertEqual(self.run_scaffold()[1], 0)
        self.assertEqual(first, self.snapshot())
        index = build.load_json(self.output / "control-index.json")
        self.assertEqual(set(index["controls"][0]["statement_parts"]), {"ac-1_smt", "ac-1_smt.a"})
        manifest = build.load_json(self.output / "manifest.json")
        self.assertEqual({m["view"] for m in manifest["modules"] if m["kind"] == "diagram"},
                         {"context", "boundary", "architecture", "data-flow"})
        # A diagram build must not silently omit figures when no renderer is configured.
        with self.assertRaisesRegex(ValueError, "plantuml-jar"):
            build.build(self.output / "manifest.json", self.root / "export")

    def test_team_edits_and_identity_preserved_when_catalog_adds_parts(self):
        self.run_scaffold()
        response = self.output / "controls/ac/ac-1.response.md"
        response.write_text("Team-owned implementation.\n")
        identities = build.load_json(self.output / "scaffold-state.json")["identities"]
        self.data["catalog"]["groups"][0]["controls"][0]["parts"][0]["parts"].append(
            {"id": "ac-1_smt.b", "name": "item", "prose": "New requirement."})
        report, _ = self.run_scaffold()
        self.assertEqual(response.read_text(), "Team-owned implementation.\n")
        self.assertIn("ac-1_smt.b", report["response_parts_requiring_review"]["ac-1"])
        after = build.load_json(self.output / "scaffold-state.json")["identities"]
        self.assertTrue(all(after[k] == v for k, v in identities.items()))

    def test_selection_does_not_remove_unselected_shells(self):
        self.run_scaffold([{"id": "ac-1.1", "title": "Enhancement"}])
        manifest = build.load_json(self.output / "manifest.json")
        paths = [m.get("path", "") for m in manifest["modules"]]
        self.assertIn("controls/ac/ac-1.1.response.md", paths)
        self.assertNotIn("controls/ac/ac-1.response.md", paths)
        self.assertTrue((self.output / "controls/ac/ac-1.response.md").exists())

    def test_modified_generated_file_refused_without_overwriting_response(self):
        self.run_scaffold()
        path = self.output / "controls/ac/ac-1.requirement.md"
        path.write_text("Manual requirement edit\n")
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "Generated scaffold file modified"):
            self.run_scaffold()
        self.assertEqual(before, self.snapshot())

    def test_invalid_pin_and_unknown_selection_refused(self):
        self.catalog.write_text(json.dumps(self.data))
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            scaffold.scaffold(self.catalog, "0" * 64, self.output, "Team", "date")
        with self.assertRaisesRegex(ValueError, "absent from the full"):
            self.run_scaffold([{"id": "zz-1", "title": "Missing"}])
        self.assertFalse(self.output.exists())

    def test_duplicate_catalog_ids_refused(self):
        self.data["catalog"]["groups"][0]["controls"].append({"id": "ac-1", "title": "Duplicate"})
        with self.assertRaisesRegex(ValueError, "duplicate control ID"):
            self.run_scaffold()

    def test_missing_authored_file_not_silently_recreated(self):
        self.run_scaffold()
        (self.output / "chapters/cover.md").unlink()
        with self.assertRaisesRegex(ValueError, "Team-authored file missing"):
            self.run_scaffold()


if __name__ == "__main__":
    unittest.main()
