"""The dispatcher preserves conventional command-line path semantics."""
import os
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import launcher


class LauncherCliTests(unittest.TestCase):
    def test_relative_arguments_resolve_against_invocation_directory(self):
        captured=[]
        class App:
            def __init__(self,*args):captured.append(args)
            def run(self):return None
        modules={'launcher_tui':types.SimpleNamespace(LauncherApp=App),
                 'wizard_tui':types.SimpleNamespace(launch=lambda *args:None),
                 'diagram_tui':types.SimpleNamespace(launch=lambda *args:None)}
        with tempfile.TemporaryDirectory() as directory:
            previous=Path.cwd()
            try:
                os.chdir(directory)
                with patch.dict(sys.modules,modules), patch.object(sys,'argv',['ato-wizard','app','--workspace','existing-ato']), \
                     patch.object(sys.stdin,'isatty',return_value=True), patch.object(sys.stdout,'isatty',return_value=True):
                    launcher.main()
            finally:
                os.chdir(previous)
            self.assertEqual(captured[0][0],Path(directory)/'app')
            self.assertEqual(captured[0][1],Path(directory)/'existing-ato')


if __name__ == '__main__':
    unittest.main()
