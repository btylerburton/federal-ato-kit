"""Exercise the real executable wrapper against missing and mismatched environments."""
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


@unittest.skipIf(os.name == 'nt', 'POSIX interpreter-wrapper fixtures')
class BootstrapTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='ato-bootstrap-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copy2(ROOT / 'ato-wizard', self.root / 'ato-wizard')
        tools = self.root / 'sspp-assembly-framework/tools'
        tools.mkdir(parents=True)
        shutil.copy2(ROOT / 'sspp-assembly-framework/tools/launcher.py', tools / 'launcher.py')
        shutil.copy2(ROOT / 'sspp-assembly-framework/tools/launcher_diagnostics.py', tools / 'launcher_diagnostics.py')
        self.python = self.root / '.venv-tui/bin/python'
        self.python.parent.mkdir(parents=True)

    def run_wrapper(self, *args):
        env = dict(os.environ)
        env.pop('ATO_WIZARD_BOOTSTRAP', None)
        return subprocess.run([sys.executable, str(self.root / 'ato-wizard'), *args],
                              env=env, text=True, capture_output=True, timeout=3)

    def test_help_does_not_execute_broken_prepared_python(self):
        self.python.write_text('#!/bin/sh\nexit 91\n')
        self.python.chmod(0o755)
        result = self.run_wrapper('--help')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('--workspace', result.stdout)

    def test_prefix_mismatch_fails_once_instead_of_looping(self):
        # -S avoids venv discovery on older Python as well; executable is outside fixture venv.
        self.python.write_text('#!/bin/sh\nexec ' + shlex.quote(sys.executable) + ' -S "$@"\n')
        self.python.chmod(0o755)
        result = self.run_wrapper('/example/repository')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Stopped instead of restarting repeatedly', result.stderr)
        self.assertNotIn('Traceback', result.stderr)

    def test_verbose_log_records_restart_and_failure_without_arguments(self):
        self.python.write_text('#!/bin/sh\nexec ' + shlex.quote(sys.executable) + ' -S "$@"\n')
        self.python.chmod(0o755)
        log = self.root / 'diagnostics.log'
        result = self.run_wrapper('-v', '--log', str(log), '/private-argument-sentinel')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('startup diagnostics', result.stderr)
        text = log.read_text()
        self.assertIn('Switching once', text)
        self.assertIn('prefix mismatch', text)
        self.assertNotIn('private-argument-sentinel', text)

    def test_reexec_clears_interpreter_overrides_and_uses_isolated_mode(self):
        marker = self.root / 'switch.json'
        script = self.root / 'probe.py'
        script.write_text('import json,os,sys\nfrom pathlib import Path\n'
                          f'Path({str(marker)!r}).write_text(json.dumps({{"isolated":sys.flags.isolated,"overrides":'
                          '[k for k in ("__PYVENV_LAUNCHER__","PYTHONHOME","PYTHONPATH","PYTHONUSERBASE") if k in os.environ]}))\n')
        self.python.write_text('#!/bin/sh\nexec ' + shlex.quote(sys.executable) + ' -I ' + shlex.quote(str(script)) + '\n')
        self.python.chmod(0o755)
        # Inject after base Python startup so the test itself can start with a deliberately bad PYTHONHOME.
        program = ('import os,runpy,sys\n'
                   'os.environ.update({k:"bad-interpreter-hint" for k in '
                   '("__PYVENV_LAUNCHER__","PYTHONHOME","PYTHONPATH","PYTHONUSERBASE")})\n'
                   f'sys.argv=[{str(self.root / "ato-wizard")!r},"example"]\n'
                   f'runpy.run_path({str(self.root / "ato-wizard")!r},run_name="__main__")')
        result = subprocess.run([sys.executable, '-c', program], capture_output=True, text=True, timeout=3)
        self.assertEqual(result.returncode, 0, result.stderr)
        import json
        self.assertEqual(json.loads(marker.read_text()), {'isolated': 1, 'overrides': []})


if __name__ == '__main__':
    unittest.main()
