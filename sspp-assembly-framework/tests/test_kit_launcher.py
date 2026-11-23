"""Launcher tests: co-located default, explicit override, exact exit and argument propagation."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
FAKE_VERIFY = ("import os, sys\n"
               "print(os.getcwd())\n"
               "print(repr(sys.argv[1:]))\n"
               "raise SystemExit(int(os.environ.get('FAKE_EXIT', '0')))\n")


def make_fake_kit(base):
    kit = Path(base) / "kit"
    (kit / "tools/ato").mkdir(parents=True)
    (kit / "tools/ato/registry.json").write_text("{}\n")
    (kit / "tools/ato/verify.py").write_text(FAKE_VERIFY)
    return kit


def run_launcher(launcher, *arguments, cwd, env_extra=None, unset=()):
    env = {key: value for key, value in os.environ.items() if key not in unset}
    env.update(env_extra or {})
    return subprocess.run([sys.executable, str(launcher), *arguments], cwd=cwd, env=env,
                          capture_output=True, text=True, timeout=30)


class KitLauncherTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix="kit-launcher-")
        self.addCleanup(self.directory.cleanup)
        self.base = Path(self.directory.name)

    def colocated_copy(self):
        """A relocated repository: this framework's tools beside a fake kit at the same root."""
        kit = make_fake_kit(self.base)
        shutil.copytree(ROOT / "tools", kit / "sspp-assembly-framework/tools")
        return kit, kit / "sspp-assembly-framework/tools/kit.py"

    def test_default_uses_colocated_root_when_variable_absent(self):
        kit, launcher = self.colocated_copy()
        other = self.base / "elsewhere"
        other.mkdir()
        result = run_launcher(launcher, "verify", "claims", "--flag", cwd=other,
                              env_extra={"FAKE_EXIT": "0"}, unset=("FEDERAL_ATO_KIT",))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines()[0], str(other.resolve()))
        self.assertIn("['claims', '--flag']", result.stdout)

    def test_exit_status_is_propagated_exactly(self):
        _, launcher = self.colocated_copy()
        for code in (1, 2, 7):
            with self.subTest(code=code):
                result = run_launcher(launcher, "verify", cwd=self.base,
                                      env_extra={"FAKE_EXIT": str(code)}, unset=("FEDERAL_ATO_KIT",))
                self.assertEqual(result.returncode, code)

    def test_explicit_override_wins_over_colocated_default(self):
        _, launcher = self.colocated_copy()
        other = make_fake_kit(self.base / "other")
        (other / "tools/ato/verify.py").write_text("raise SystemExit(9)\n")
        result = run_launcher(launcher, "verify", cwd=self.base,
                              env_extra={"FEDERAL_ATO_KIT": str(other), "FAKE_EXIT": "0"})
        self.assertEqual(result.returncode, 9)

    def test_invalid_override_fails_without_fallback_to_default(self):
        _, launcher = self.colocated_copy()
        missing = self.base / "does-not-exist"
        for value, text in ((str(missing), "unavailable"), ("relative-path", "must be an absolute"),
                            ("", "must be an absolute")):
            with self.subTest(value=value):
                result = run_launcher(launcher, "verify", cwd=self.base,
                                      env_extra={"FEDERAL_ATO_KIT": value, "FAKE_EXIT": "0"})
                self.assertEqual(result.returncode, 2)
                self.assertIn(text, result.stderr)
                self.assertNotIn(str(self.base / "kit"), result.stdout)

    def test_missing_default_reports_unavailable(self):
        framework = self.base / "lonely/sspp-assembly-framework"
        shutil.copytree(ROOT / "tools", framework / "tools")
        result = run_launcher(framework / "tools/kit.py", "check", cwd=self.base,
                              unset=("FEDERAL_ATO_KIT",))
        self.assertEqual(result.returncode, 2)
        self.assertIn("unavailable", result.stderr)

    def test_unknown_command_is_rejected(self):
        result = run_launcher(ROOT / "tools/kit.py", "setup", cwd=self.base, unset=("FEDERAL_ATO_KIT",))
        self.assertEqual(result.returncode, 2)

    def test_real_repository_default_propagates_not_assessed_exit_from_unrelated_cwd(self):
        result = run_launcher(ROOT / "tools/kit.py", "verify", "claims", "--manifest",
                              str(REPO / "examples/claims.json"), "--evidence-root",
                              str(REPO / "examples"), cwd=self.base, unset=("FEDERAL_ATO_KIT",))
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn('"NOT_ASSESSED": 2', result.stdout)


if __name__ == "__main__":
    unittest.main()
