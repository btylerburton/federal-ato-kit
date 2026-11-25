"""Environment validation must refuse base interpreters and leaked package directories."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHECK = ROOT / 'sspp-assembly-framework/tools/verify_tui_environment.py'


class EnvironmentTests(unittest.TestCase):
    def test_base_python_refuses_expected_venv(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run([sys.executable, '-I', str(CHECK), directory],
                                    capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 1)
            self.assertIn('No installation should proceed', result.stderr)

    def test_real_venv_passes_but_system_site_and_missing_textual_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            env = Path(directory) / 'venv'
            subprocess.run([sys.executable, '-I', '-m', 'venv', '--without-pip', str(env)], check=True, timeout=30)
            python = env / ('Scripts/python.exe' if sys.platform == 'win32' else 'bin/python')
            command = [str(python), '-I', str(CHECK), str(env)]
            result = subprocess.run(command, capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            result = subprocess.run([*command, '--check-textual'], capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 1)
            self.assertIn('Textual must be installed', result.stderr)
            config = env / 'pyvenv.cfg'
            config.write_text(config.read_text().replace('include-system-site-packages = false', 'include-system-site-packages = true'))
            result = subprocess.run(command, capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 1)
            self.assertIn('system site-packages', result.stderr)
