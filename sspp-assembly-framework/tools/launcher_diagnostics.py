"""Private startup diagnostics without argument, answer or environment-value capture."""
import argparse
import logging
import os
import sys
from pathlib import Path

LOGGER = logging.getLogger('ato-wizard')


def configure(root, argv):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('--log', type=Path)
    options, _ = parser.parse_known_args(argv)
    path = (options.log or root / 'tmp/ato-wizard.log').expanduser().absolute()
    if any(p.is_symlink() for p in (path, *path.parents)):
        raise ValueError('Diagnostic log path must not use symlinks')
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND | getattr(os, 'O_NOFOLLOW', 0), 0o600)
    stream = os.fdopen(descriptor, 'a', encoding='utf-8')
    for handler in list(LOGGER.handlers):
        LOGGER.removeHandler(handler)
        handler.close()
    handler = logging.StreamHandler(stream)
    formatter = logging.Formatter('%(asctime)sZ pid=%(process)d %(levelname)s %(message)s')
    import time
    formatter.converter = time.gmtime
    handler.setFormatter(formatter)
    LOGGER.addHandler(handler)
    LOGGER.setLevel(logging.DEBUG if options.verbose else logging.INFO)
    LOGGER.propagate = False
    if options.verbose:
        print(f'ato-wizard: startup diagnostics: {path}', file=sys.stderr, flush=True)
    return options.verbose, path


def stage(message, verbose=0):
    LOGGER.info(message)
    if verbose:
        print(f'ato-wizard: {message}', file=sys.stderr, flush=True)


def failure(error):
    # Avoid raw exception messages: a downstream error may quote source or user answers.
    LOGGER.error('Startup/workflow failed: %s', type(error).__name__)
    trace = error.__traceback__
    while trace:
        LOGGER.error('  %s:%d in %s', Path(trace.tb_frame.f_code.co_filename).name,
                     trace.tb_lineno, trace.tb_frame.f_code.co_name)
        trace = trace.tb_next
