"""Verify the full pinned inventory and the separation of samples from claims."""

import copy
import hashlib
import json
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import control_library as library


class ControlLibraryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = library.load_catalog()
        cls.records = library.control_records(cls.catalog)
        cls.output = library.ROOT / "examples/control-library"

    def test_full_inventory_and_on_disk_hashes(self):
        index = json.loads((self.output / "index.json").read_text())
        self.assertEqual(len(self.records), 1196)
        self.assertEqual(len(index["controls"]), 1196)
        self.assertEqual({r["id"] for r in index["controls"]}, set(self.records))
        self.assertEqual({p.stem for p in self.output.glob("*.md") if p.name != "README.md"},
                         set(self.records))
        self.assertEqual(sum(r["status"] == "withdrawn" for r in index["controls"]), 182)
        for record in index["controls"]:
            data = (self.output / record["path"]).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), record["sha256"])
            self.assertTrue(data.startswith(b"---\ntitle:"))

    def test_every_active_requirement_parameter_and_assessment_is_present(self):
        for key, record in self.records.items():
            if library.withdrawn(record):
                continue
            with self.subTest(control=key):
                text = (self.output / (key + ".md")).read_text()
                self.assertIn("doi.org/10.6028/NIST.SP.800-53Ar5", text)
                questions = text.split("### Questions to complete the real response", 1)[1]
                for part in library.statements(record):
                    self.assertIn(part["id"], text)
                    if part.get("prose"):
                        self.assertIn(library.prose(part["prose"]), questions)
                for param in library.parameters(record, self.catalog):
                    self.assertIn(f"`{param}`", questions)
                for part in library.parts(record):
                    if part.get("prose") and part["name"] in {"guidance", "assessment-objective", "assessment-objects"}:
                        for paragraph in part["prose"].split("\n\n"):
                            if paragraph.strip():
                                self.assertIn(library.prose(paragraph), text)

    def test_all_samples_are_commented_and_not_rendered_claims(self):
        for key, record in self.records.items():
            text = (self.output / (key + ".md")).read_text()
            visible = re.sub(r"<!--.*?-->", "", text, flags=re.S)
            self.assertNotIn("[RESPONSIBLE ROLE] uses", visible)
            if not library.withdrawn(record):
                self.assertEqual(text.count("<!--"), 1)
                self.assertEqual(text.count("-->"), 1)
                self.assertIn("ILLUSTRATIVE TEMPLATE ONLY", text)
                self.assertIn("### Questions to complete the real response", visible)
                self.assertIn("### Catalog assessment objectives and evidence", visible)

    def test_all_withdrawals_preserve_disposition_without_active_response(self):
        for key, record in self.records.items():
            if not library.withdrawn(record):
                continue
            text = (self.output / (key + ".md")).read_text()
            self.assertIn("### Withdrawn disposition", text)
            self.assertNotIn("Illustrative parameterized response", text)
            self.assertNotIn("<!--", text)
            for link in record.get("links", []):
                self.assertIn(link["href"].lstrip("#"), text)
        self.assertIn("Addressed through tailoring.", (self.output / "cp-10.3.md").read_text())
        self.assertIn("incorporated-into: `ac-6`", (self.output / "ac-3.1.md").read_text())

    def test_generation_is_byte_deterministic_and_fixture_is_untouched(self):
        def snapshot(root):
            return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in root.rglob("*") if p.is_file()}

        fixture = library.ROOT / "examples/package"
        before = snapshot(fixture)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "data/control-library").mkdir(parents=True)
            for name in ("catalog.json", "provenance.json"):
                shutil.copyfile(library.ROOT / "data/control-library" / name,
                                root / "data/control-library" / name)
            library.generate(root)
            first = snapshot(root / "examples/control-library")
            self.assertEqual(first, snapshot(self.output))
            library.generate(root)
            self.assertEqual(first, snapshot(root / "examples/control-library"))
        self.assertEqual(before, snapshot(fixture))

    def test_parent_and_sibling_parameters_and_scaffold_api(self):
        self.assertIn("ia-13_odp.01", library.parameters(self.records["ia-13.3"], self.catalog))
        self.assertIn("sc-42.01_odp", library.parameters(self.records["sc-42.2"], self.catalog))
        self.assertEqual(library.guidance_markdown(self.records["ac-2.1"]),
                         library.guidance_markdown(self.records["ac-2.1"], self.catalog["catalog"]))
        import scaffold
        response = scaffold.response_document(self.records["ac-2.1"], ["ac-2.1_smt"]).decode()
        self.assertIn("Implementation status: UNFILLED", response)
        self.assertIn(library.guidance_markdown(self.records["ac-2.1"]).strip(), response)

    def test_duplicate_unsafe_ids_and_bad_pin_are_rejected(self):
        record = {"id": "ac-1", "title": "Example"}
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            library.control_records({"controls": [record, record]})
        with self.assertRaisesRegex(ValueError, "Invalid"):
            library.control_records({"controls": [{"id": "../escape"}]})
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            data = root / "data/control-library"
            data.mkdir(parents=True)
            (data / "catalog.json").write_text('{}')
            (data / "provenance.json").write_text(json.dumps({"catalog": {"sha256": "0" * 64}}))
            with self.assertRaisesRegex(ValueError, "hash mismatch"):
                library.generate(root)
            self.assertFalse((root / "examples/control-library").exists())

    def test_catalog_text_cannot_end_illustrative_comment(self):
        control = copy.deepcopy(self.records["ac-2.1"])
        control["parts"][0]["prose"] = "Sample --> text <!-- continued"
        comment = library.illustrative_response(control, self.catalog)
        self.assertEqual(comment.count("<!--"), 1)
        self.assertEqual(comment.count("-->"), 1)

    def test_catalog_fragment_links_are_not_package_local_links(self):
        linked = next(record for record in self.records.values()
                      if any("](#au-2)" in part.get("prose", "") for part in library.parts(record)))
        text = library.guidance_markdown(linked, self.catalog)
        self.assertIn("catalog reference: `#au-2`", text)
        self.assertNotIn("](#au-2)", text)
        self.assertEqual(text.count("<!--"), 1)
        self.assertEqual(text.count("-->"), 1)
        for record in self.records.values():
            text = library.guidance_markdown(record, self.catalog)
            self.assertNotRegex(text, r"\]\(\s*<?#")
        self.assertEqual(library.prose("See [control](#au-2) and [NIST](https://doi.org/example)."),
                         "See control (catalog reference: `#au-2`) and [NIST](https://doi.org/example).")


if __name__ == "__main__":
    unittest.main()
