"""Single optional UI launcher, with explicit workspace selection and no provider guessing."""
import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repository', nargs='?', type=Path, default=Path.cwd())
    parser.add_argument('--workspace', type=Path, help='Resume a specific existing external or wizard-owned workspace')
    parser.add_argument('--runner', type=Path, help='Explicit operator-owned diagram agent configuration')
    parser.add_argument('--plantuml-jar', type=Path)
    parser.add_argument('--pandoc', type=Path)
    args = parser.parse_args()
    try:
        from launcher_tui import LauncherApp
        from wizard_tui import launch as text_launch
        from diagram_tui import launch as diagram_launch
    except ModuleNotFoundError as error:
        if error.name not in {'textual', 'rich'}:
            raise
        parser.exit(1, 'Optional UI not installed. From the kit directory run: bash setup-tui.sh\n'
                       'Then rerun ./ato-wizard /path/to/repository. Nothing was downloaded automatically.\n')
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        parser.exit(1, 'ato-wizard requires an interactive terminal. For automation use wizard.py or diagram_flow.py CLI commands.\n')
    repository = args.repository.expanduser().absolute()
    workspace = args.workspace.expanduser().absolute() if args.workspace is not None else None
    while True:
        result = LauncherApp(repository, workspace, args.runner, args.plantuml_jar, args.pandoc).run()
        if not result:
            return
        repository, workspace = result['repository'], result['workspace']
        try:
            if result['workflow'] == 'text':
                text_launch(repository, workspace)
            else:
                diagram_launch(repository, workspace, args.runner, args.plantuml_jar, args.pandoc)
        except (ValueError, OSError) as error:
            print(f'Workflow could not open: {error}', file=sys.stderr)
            input('Press Enter to return to the workspace chooser. ')


if __name__ == '__main__':
    main()
