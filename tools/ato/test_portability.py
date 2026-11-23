"""Real CLI tests using only synthetic kit inputs from a different working directory."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class PortabilityTests(unittest.TestCase):
    def run_cli(self, *arguments):
        with tempfile.TemporaryDirectory(prefix="kit-unrelated-cwd-") as temporary:
            result = subprocess.run(
                [sys.executable, str(ROOT / "tools/ato/verify.py"), *arguments],
                cwd=temporary, capture_output=True, text=True, timeout=30)
        return result.returncode, json.loads(result.stdout)

    def test_synthetic_package_from_unrelated_directory(self):
        code, result = self.run_cli("package", "--package", str(ROOT / "examples/package"))
        self.assertEqual(code, 2)
        self.assertEqual(result["counts"], {"PASS": 2, "FAIL": 0, "BLOCKED": 0, "NOT_ASSESSED": 2})

    def test_synthetic_claims_from_unrelated_directory(self):
        code, result = self.run_cli("claims", "--manifest", str(ROOT / "examples/claims.json"),
                                    "--evidence-root", str(ROOT / "examples"))
        self.assertEqual(code, 2)
        self.assertEqual(result["counts"]["NOT_ASSESSED"], 2)


if __name__ == "__main__":
    unittest.main()
