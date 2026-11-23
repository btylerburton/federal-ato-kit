"""Optional real Trestle/Pandoc test using synthetic inputs and a relocated framework."""
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class IntegrationTests(unittest.TestCase):
    def test_kit_rejects_invalid_explicit_location(self):
        result = subprocess.run([sys.executable, str(ROOT / "tools/kit.py"), "check"],
                                env={**os.environ, "FEDERAL_ATO_KIT": "relative-path"},
                                capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 2)
        self.assertIn("must be an absolute", result.stderr)

    @unittest.skipUnless(os.environ.get("TRESTLE_TEST_BIN") and os.environ.get("PANDOC_TEST_BIN"),
                         "Set TRESTLE_TEST_BIN and PANDOC_TEST_BIN for real integration")
    def test_relocated_engine_assembles_synthetic_project(self):
        with tempfile.TemporaryDirectory(prefix="sspp-extraction-") as directory:
            base = Path(directory)
            framework = base / "framework"
            shutil.copytree(ROOT / "tools", framework / "tools")
            project = base / "project"
            project.mkdir()
            metadata = {"title": "Synthetic catalog", "last-modified": "2026-01-01T00:00:00Z",
                        "version": "1", "oscal-version": "1.2.1"}
            catalog = {"catalog": {"uuid": "d7cb7344-3b96-4a16-9dfd-0bc4b4fbc177", "metadata": metadata,
                       "controls": [{"id": "ac-1", "title": "Synthetic control", "parts": [
                           {"id": "ac-1_smt", "name": "statement", "prose": "Review synthetic accounts."}]}]}}
            (project / "catalog.json").write_text(json.dumps(catalog))
            profile = {"profile": {"uuid": "9a6a359d-7c04-4c22-a693-f59f6a138596", "metadata": metadata,
                       "imports": [{"href": "trestle://catalogs/nist/catalog.json",
                                    "include-controls": [{"with-ids": ["ac-1"]}]}]}}
            (project / "profile.json").write_text(json.dumps(profile))
            (project / "source.md").write_text("Synthetic source.\n")
            (project / "controls").mkdir()
            (project / "controls/ac-1.md").write_text("Synthetic input marker.\n")
            (project / "adapter.py").write_text('''
def load_controls(root, config):
    return [{"id": "ac-1", "path": root / "controls/ac-1.md",
             "meta": {"x-migration-status-selections": [], "x-migration-source": "source.md",
                      "x-migration-source-lines": "1"},
             "narrative": "### This System\\n\\nSynthetic team reviews access quarterly.",
             "assessment": "No execution evidence supplied; NOT_ASSESSED."}]
def supplement(root, config):
    return "Synthetic supporting review."
def sharing_links(text):
    return text
def build_full(controls, root, config, frontmatter):
    return frontmatter("Synthetic full draft") + "# System description\\n\\nSynthetic service.\\n\\n" + controls.split("---", 2)[2], []
def verify_document(text):
    if "Synthetic team reviews access quarterly." not in text:
        raise ValueError("Synthetic response lost")
''')
            config = {"schema_version": 1, "project_root": ".", "area": "output", "source": "source.md",
                      "adapter": "adapter.py", "controls": "controls", "catalog": "catalog.json", "profile": "profile.json",
                      "catalog_sha256": hashlib.sha256((project / "catalog.json").read_bytes()).hexdigest(),
                      "trestle": os.environ["TRESTLE_TEST_BIN"], "pandoc": os.environ["PANDOC_TEST_BIN"],
                      "application_revision": "synthetic-1", "date": "2026-01-01T00:00:00Z", "assessment_date": "2026-01-01",
                      "system_name": "Synthetic service", "model_name": "synthetic-review", "export_model": "synthetic-export",
                      "controls_output": "synthetic-controls", "full_output": "synthetic-full"}
            path = project / "project.json"
            path.write_text(json.dumps(config))
            command = [sys.executable, str(framework / "tools/assemble_review.py"), "--project", str(path)]
            result = subprocess.run(command, cwd=base, capture_output=True, text=True, timeout=150)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            report = json.loads((project / "output/result.json").read_text())
            self.assertEqual(report["controls"], 1)
            self.assertEqual(report["responses_verified"], 1)
            self.assertTrue(report["repeat_assembly_equal"])
            self.assertTrue((project / "output/exports/synthetic-full.docx").is_file())
            config["adapter"] = "../outside.py"
            path.write_text(json.dumps(config))
            refused = subprocess.run(command, cwd=base, capture_output=True, text=True, timeout=15)
            self.assertNotEqual(refused.returncode, 0)
            self.assertIn("escapes root", refused.stderr)


if __name__ == "__main__":
    unittest.main()
