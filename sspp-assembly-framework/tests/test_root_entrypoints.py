"""Root check/setup entrypoints: both suites run, failures propagate, setup never downloads on --help."""
import contextlib
import importlib.util
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("root_check", REPO / "check.py")
root_check = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(root_check)


def run_main(selected):
    with contextlib.redirect_stdout(io.StringIO()) as output:
        code = root_check.main(selected)
    return code, output.getvalue()


def exit_with(code):
    return [sys.executable, "-c", f"raise SystemExit({code})"]


class RootCheckTests(unittest.TestCase):
    def test_default_suites_cover_toolkit_and_framework(self):
        names = [name for name, _, _ in root_check.suites()]
        self.assertEqual(names, ["evidence toolkit", "sspp-assembly-framework"])
        for _, command, cwd in root_check.suites():
            self.assertTrue(cwd.is_dir())
        self.assertTrue((REPO / "tools/ato/check.py").is_file())

    def test_failure_in_either_suite_is_reported_and_other_suite_still_runs(self):
        here = Path.cwd()
        for failing_first in (True, False):
            with self.subTest(failing_first=failing_first):
                selected = [("a", exit_with(3 if failing_first else 0), here),
                            ("b", exit_with(0 if failing_first else 5), here)]
                code, output = run_main(selected)
                self.assertEqual(code, 3 if failing_first else 5)
                self.assertIn("exit 0", output)

    def test_all_passing_returns_zero(self):
        code, output = run_main([("a", exit_with(0), Path.cwd())])
        self.assertEqual(code, 0)
        self.assertIn("PASS: a", output)

    def test_setup_help_and_bad_argument_do_not_install(self):
        helped = subprocess.run(["bash", str(REPO / "setup.sh"), "--help"], capture_output=True,
                                text=True, timeout=15, cwd=tempfile.gettempdir())
        self.assertEqual(helped.returncode, 0, helped.stderr)
        for text in ("downloads packages", "setup_assembly.py", "setup_diagrams.py"):
            self.assertIn(text.lower(), helped.stdout.lower())
        bad = subprocess.run(["bash", str(REPO / "setup.sh"), "--bogus"], capture_output=True,
                             text=True, timeout=15, cwd=tempfile.gettempdir())
        self.assertEqual(bad.returncode, 2)
        self.assertNotIn("PASS", bad.stdout)

    def test_setup_delegates_to_existing_lock_setup(self):
        text = (REPO / "setup.sh").read_text()
        self.assertIn('bash "${ROOT}/tools/ato/setup.sh"', text)
        self.assertNotIn("pip install", text)


if __name__ == "__main__":
    unittest.main()
