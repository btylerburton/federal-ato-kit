"""Validate diagrams and exercise actual offline rendering and DOCX inclusion."""
import copy
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import build
import diagrams
import pipeline
from diagram_starters import starters


class DiagramTests(unittest.TestCase):
    def test_unknown_nodes_and_missing_data_rejected(self):
        _, modules = starters()
        bad = copy.deepcopy(modules[0])
        bad["flows"][0]["to"] = "missing"
        with self.assertRaisesRegex(ValueError, "unknown node"):
            diagrams.validate(bad)
        bad = copy.deepcopy(modules[0])
        del bad["flows"][0]["authentication"]
        with self.assertRaisesRegex(ValueError, "authentication"):
            diagrams.validate(bad)

    def test_includes_and_inventory_drift_rejected(self):
        files, modules = starters()
        source = files[modules[0]["path"]]
        with self.assertRaisesRegex(ValueError, "self-contained"):
            diagrams.check_source(source.replace(b"@enduml", b"!include elsewhere\n@enduml"), modules[0])
        with self.assertRaisesRegex(ValueError, "aliases differ"):
            diagrams.check_source(source.replace(b"as viewer", b"as stranger"), modules[0])
        with self.assertRaisesRegex(ValueError, "arrows differ"):
            diagrams.check_source(source.replace(b"viewer --> service", b"service --> viewer"), modules[0])

    @unittest.skipUnless(os.environ.get("PLANTUML_TEST_JAR") and os.environ.get("PANDOC_TEST_BIN"),
                         "Set diagram tool variables for actual renderer tests")
    def test_render_repeat_docx_and_failed_build_preserves_output(self):
        with tempfile.TemporaryDirectory(prefix="sspp-diagrams-") as directory:
            root = Path(directory)
            files, modules = starters()
            for name, content in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
            manifest = root / "manifest.json"
            manifest.write_text(json.dumps({"schema_version": 1, "document": {
                "title": "Synthetic diagrams", "revision": "1", "date": "2026-11-19", "edition": "review"}, "modules": modules}))
            jar = Path(os.environ["PLANTUML_TEST_JAR"])
            first = build.compose(manifest, jar)
            self.assertEqual(first, build.compose(manifest, jar))
            self.assertEqual(len([n for n in first if n.endswith('.png')]), 4)
            self.assertEqual(len([n for n in first if n.endswith('.svg')]), 4)
            output = root / "output"
            pipeline.pipeline(manifest, output, jar, Path(os.environ["PANDOC_TEST_BIN"]))
            report = json.loads((output / "verification.json").read_text())
            self.assertEqual(report["figures_verified"], 4)
            self.assertTrue(report["toc_present"])
            before = (output / "document.docx").read_bytes()
            (root / modules[0]["path"]).write_text("@startuml\ninvalid syntax here ?\n@enduml\n")
            with self.assertRaises(ValueError):
                pipeline.pipeline(manifest, output, jar, Path(os.environ["PANDOC_TEST_BIN"]))
            self.assertEqual((output / "document.docx").read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
