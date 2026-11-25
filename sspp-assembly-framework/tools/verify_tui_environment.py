"""Fail before pip can install outside the intended isolated UI environment."""
import argparse
import importlib.util
import site
import sys
from pathlib import Path


def verify(expected, check_textual=False):
    expected = expected.resolve()
    if Path(sys.prefix).resolve() != expected or sys.prefix == sys.base_prefix:
        raise ValueError(f'Python is not running in the intended virtual environment: {expected}. '
                         'No installation should proceed. Check the interpreter links and pyvenv.cfg; '
                         'rename the broken .venv-tui directory and rerun setup.')
    if site.ENABLE_USER_SITE:
        raise ValueError('User site-packages are enabled; refusing a nonisolated UI environment')
    config = expected / 'pyvenv.cfg'
    entries = dict(line.split('=', 1) for line in config.read_text().splitlines() if '=' in line)
    if {k.strip(): v.strip().lower() for k, v in entries.items()}.get('include-system-site-packages') != 'false':
        raise ValueError('Virtual environment exposes system site-packages; recreate it before installing')
    if check_textual:
        spec = importlib.util.find_spec('textual')
        if spec is None or not spec.origin or not Path(spec.origin).resolve().is_relative_to(expected):
            raise ValueError('Textual must be installed inside the intended virtual environment')
    return expected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('environment', type=Path)
    parser.add_argument('--check-textual', action='store_true')
    args = parser.parse_args()
    try:
        path = verify(args.environment, args.check_textual)
    except (ValueError, OSError) as error:
        parser.exit(1, f'Environment verification failed: {error}\n')
    print(f'PASS: isolated UI environment verified: {path}')


if __name__ == '__main__':
    main()
