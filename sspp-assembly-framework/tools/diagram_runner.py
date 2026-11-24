"""Explicit operator-configured agent runner, invoked only by a dashboard action."""
import os
import signal
import subprocess
import time
import uuid
from pathlib import Path

from build import load_json, json_bytes, sha

TOKENS = {'{repository}', '{request}', '{proposal}', '{revision}'}


def load_runner(path, repository):
    if path.is_symlink() or path.resolve().is_relative_to(repository):
        raise ValueError('Runner configuration must be operator-owned outside the application checkout')
    config = load_json(path)
    if not isinstance(config, dict) or config.get('schema_version') != 1:
        raise ValueError('Runner needs schema_version 1')
    argv = config.get('argv')
    if not isinstance(argv, list) or not argv or any(not isinstance(v, str) or not v or '\x00' in v for v in argv):
        raise ValueError('Runner argv must be a nonempty argument array; shell command strings are not supported')
    executable = Path(argv[0])
    if not executable.is_absolute() or not executable.is_file() or not os.access(executable, os.X_OK):
        raise ValueError('Runner executable must be an absolute executable file path')
    if executable.resolve().is_relative_to(repository):
        raise ValueError('Do not execute agent runners from the application checkout')
    if not {'{request}', '{proposal}'} <= set(argv):
        raise ValueError('Runner argv must include standalone {request} and {proposal} arguments')
    for value in argv[1:]:
        if ('{' in value or '}' in value) and value not in TOKENS:
            raise ValueError('Runner placeholders must be standalone supported tokens')
    timeout = config.get('timeout_seconds', 600)
    if type(timeout) is not int or not 1 <= timeout <= 1800:
        raise ValueError('Runner timeout_seconds must be 1..1800')
    return argv, timeout


def run_agent(config_path, repository, root, request, proposal, revision):
    argv, timeout = load_runner(config_path, repository)
    replacements = {'{repository}': str(repository), '{request}': str(request),
                    '{proposal}': str(proposal), '{revision}': revision}
    command = [replacements.get(value, value) for value in argv]
    before = sha((root / 'session.json').read_bytes())
    started = time.time()
    record = {'format': 'diagram-agent-run-v1', 'config_sha256': sha(config_path.read_bytes()),
              'started_at_unix': started, 'repository_revision': revision, 'status': 'failed'}
    root.joinpath('runs').mkdir(exist_ok=True)
    receipt = root / 'runs' / (uuid.uuid4().hex + '.json')
    # The configured wrapper owns model credentials and provider policy. Never persist stdout,
    # stderr, argv or environment values here: an agent may print sensitive source or tokens.
    try:
        process = subprocess.Popen(command, cwd=root, stdin=subprocess.DEVNULL,
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                   start_new_session=True)
        try:
            code = process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait()
            record['status'] = 'timeout'
            raise ValueError('Agent runner timed out. Its partial output is preserved; inspect before retrying.')
        record['exit_code'] = code
        if before != sha((root / 'session.json').read_bytes()):
            raise ValueError('Runner changed review session unexpectedly. Inspect state before continuing.')
        if code:
            raise ValueError(f'Agent runner exited {code}. No analysis pass is claimed; inspect the configured runner.')
        if proposal.is_symlink() or not proposal.is_file():
            raise ValueError('Agent exited successfully but did not write a regular proposal.json. Analysis remains incomplete.')
        record['status'] = 'proposal-written-awaiting-validation'
        record['proposal_sha256'] = sha(proposal.read_bytes())
    finally:
        if record['status'] != 'proposal-written-awaiting-validation' and proposal.exists():
            quarantined = root / 'runs' / (receipt.stem + '-unaccepted-proposal.json')
            proposal.rename(quarantined)
            record['unaccepted_output'] = str(quarantined.relative_to(root))
        record['duration_seconds'] = round(time.time() - started, 3)
        receipt.write_bytes(json_bytes(record))
