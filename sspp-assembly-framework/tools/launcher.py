"""Single optional UI launcher, with explicit workspace selection and no provider guessing."""
import argparse
import sys
from pathlib import Path
from launcher_diagnostics import configure, stage, failure, LOGGER


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repository', nargs='?', type=Path, default=Path.cwd())
    parser.add_argument('--workspace', type=Path, help='Resume a specific existing external or wizard-owned workspace')
    parser.add_argument('--runner', type=Path, help='Explicit operator-owned source/diagram agent configuration')
    parser.add_argument('--plantuml-jar', type=Path)
    parser.add_argument('--pandoc', type=Path)
    parser.add_argument('-v', '--verbose', action='count', default=0, help='Show startup stages and enable detailed local diagnostics')
    parser.add_argument('--log', type=Path, help='Diagnostic log (default: kit/tmp/ato-wizard.log)')
    args = parser.parse_args()
    configure(Path(__file__).resolve().parents[2], sys.argv[1:])
    stage('Loading terminal UI modules', args.verbose)
    try:
        from launcher_tui import LauncherApp
        from wizard_tui import launch as text_launch
        from diagram_tui import launch as diagram_launch
        from source_review_tui import launch as source_launch
    except ModuleNotFoundError as error:
        if error.name not in {'textual', 'rich'}:
            raise
        parser.exit(1, 'Optional UI not installed. From the kit directory run: bash setup-tui.sh\n'
                       'Then rerun ./ato-wizard /path/to/repository. Nothing was downloaded automatically.\n')
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        stage('Interactive terminal check failed', args.verbose)
        parser.exit(1, 'ato-wizard requires an interactive terminal. For automation use wizard.py or diagram_flow.py CLI commands.\n')
    repository = args.repository.expanduser().absolute()
    workspace = args.workspace.expanduser().absolute() if args.workspace is not None else None
    while True:
        stage('Starting workspace chooser', args.verbose)
        result = LauncherApp(repository, workspace, args.runner, args.plantuml_jar, args.pandoc).run()
        if not result:
            stage('Launcher exited normally', args.verbose)
            return
        repository, workspace = result['repository'], result['workspace']
        try:
            LOGGER.info('Opening workflow: %s', result['workflow'])
            if result['workflow'] == 'text':
                if source_launch(repository, workspace, args.runner):
                    text_launch(repository, workspace)
            elif result['workflow'] == 'source':
                source_launch(repository, workspace, args.runner)
            else:
                diagram_launch(repository, workspace, args.runner, args.plantuml_jar, args.pandoc)
        except (ValueError, OSError) as error:
            failure(error)
            print(f'Workflow could not open: {error}', file=sys.stderr)
            input('Press Enter to return to the workspace chooser. ')


if __name__ == '__main__':
    main()
