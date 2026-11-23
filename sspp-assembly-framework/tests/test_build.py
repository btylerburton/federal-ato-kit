"""Exercise real package outputs, portability, omission failures and owned-output cleanup."""

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("builder", ROOT / "tools/build.py")
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="sspp-composition-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.project = self.root / "project"
        shutil.copytree(ROOT / "examples/minimal", self.project)
        self.manifest = self.project / "manifest.json"
        self.output = self.root / "output"

    def edit(self, function):
        manifest = json.loads(self.manifest.read_text())
        function(manifest)
        self.manifest.write_text(json.dumps(manifest))

    def snapshot(self, path):
        return {p.relative_to(path).as_posix(): p.read_bytes()
                for p in path.rglob("*") if p.is_file()}

    def test_fresh_repeat_and_relocated_builds_are_identical(self):
        builder.build(self.manifest, self.output)
        first = self.snapshot(self.output)
        self.assertEqual(set(first), {"document.md", "inventory.json", "assets/boundary-diagram.svg",
                                     "attachments/test-evidence.txt"})
        builder.build(self.manifest, self.output)
        self.assertEqual(self.snapshot(self.output), first)
        copied = self.root / "relocated"
        shutil.copytree(self.project, copied)
        builder.build(copied / "manifest.json", self.root / "fresh")
        self.assertEqual(self.snapshot(self.root / "fresh"), first)
        inventory = json.loads(first["inventory.json"])
        self.assertEqual(len(inventory["modules"]), 6)
        for name, expected in inventory["outputs"].items():
            self.assertEqual(builder.sha(first[name]), expected)
        self.assertEqual(first["attachments/test-evidence.txt"],
                         (self.project / "evidence/test-record.txt").read_bytes())

    def test_removed_module_removes_only_unchanged_owned_output(self):
        builder.build(self.manifest, self.output)
        self.edit(lambda m: m["modules"].pop(3))
        (self.project / "chapters/system.md").write_text("Fictional replacement chapter.\n")
        builder.build(self.manifest, self.output)
        self.assertFalse((self.output / "attachments/test-evidence.txt").exists())
        self.assertTrue((self.output / "assets/boundary-diagram.svg").exists())

    def test_missing_attachment_fails_before_modifying_previous_build(self):
        builder.build(self.manifest, self.output)
        before = self.snapshot(self.output)
        (self.project / "evidence/test-record.txt").unlink()
        with self.assertRaisesRegex(ValueError, "Missing or escaping"):
            builder.build(self.manifest, self.output)
        self.assertEqual(self.snapshot(self.output), before)

    def test_modified_output_and_untracked_file_are_preserved(self):
        builder.build(self.manifest, self.output)
        (self.output / "document.md").write_text("User edits\n")
        with self.assertRaisesRegex(ValueError, "modified output"):
            builder.build(self.manifest, self.output)
        self.assertEqual((self.output / "document.md").read_text(), "User edits\n")
        (self.output / "personal.txt").write_text("User work\n")
        with self.assertRaisesRegex(ValueError, "untracked files"):
            builder.build(self.manifest, self.output)
        self.assertTrue((self.output / "personal.txt").exists())

    def test_duplicate_id_and_duplicate_json_key_fail(self):
        self.edit(lambda m: m["modules"].append(dict(m["modules"][0])))
        with self.assertRaisesRegex(ValueError, "duplicate module ID"):
            builder.compose(self.manifest)
        self.manifest.write_text('{"schema_version": 1, "schema_version": 2}')
        with self.assertRaisesRegex(ValueError, "Duplicate JSON key"):
            builder.compose(self.manifest)

    def test_hash_mismatch_rejected(self):
        self.edit(lambda m: m["modules"][0].update(sha256="0" * 64))
        with self.assertRaisesRegex(ValueError, "Input hash mismatch"):
            builder.compose(self.manifest)

    def test_path_escape_and_symlink_escape_rejected(self):
        self.edit(lambda m: m["modules"][0].update(path="../outside.md"))
        with self.assertRaisesRegex(ValueError, "stay within project"):
            builder.compose(self.manifest)
        outside = self.root / "outside.md"
        outside.write_text("not a project input")
        (self.project / "escape.md").symlink_to(outside)
        self.edit(lambda m: m["modules"][0].update(path="escape.md"))
        with self.assertRaisesRegex(ValueError, "escaping project file"):
            builder.compose(self.manifest)

    def test_publication_gap_and_unregistered_reference_fail(self):
        self.edit(lambda m: m["document"].update(edition="publication"))
        with self.assertRaisesRegex(ValueError, "Publication has unresolved gap"):
            builder.compose(self.manifest)
        self.edit(lambda m: m["document"].update(edition="review"))
        (self.project / "chapters/system.md").write_text("[Lost attachment](module:unknown)")
        with self.assertRaisesRegex(ValueError, "Unknown module link"):
            builder.compose(self.manifest)

    def test_source_image_definition_cannot_silently_disappear(self):
        (self.project / "chapters/system.md").write_text("![Figure][image2]\n\n[image2]: data:image/png;base64,abc\n")
        with self.assertRaisesRegex(ValueError, "reference-style"):
            builder.compose(self.manifest)

    def test_fenced_parameter_json_remains_literal(self):
        literal = '```json\n{"label": "[AU-2a.](#au-2_smt.a)"}\n```'
        (self.project / "chapters/system.md").write_text(literal)
        files = builder.compose(self.manifest)
        self.assertIn(literal, files["document.md"].decode())

    def test_cli_runs_outside_framework_and_reports_failure(self):
        command = [sys.executable, str(ROOT / "tools/build.py"), str(self.manifest),
                   "--output", str(self.output)]
        result = subprocess.run(command, cwd=self.root, text=True, capture_output=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.output / "document.md").is_file())
        self.manifest.write_text("invalid json")
        failed = subprocess.run(command, cwd=self.root, text=True, capture_output=True, timeout=15)
        self.assertEqual(failed.returncode, 1)
        self.assertIn("Assembly refused", failed.stderr)


if __name__ == "__main__":
    unittest.main()
