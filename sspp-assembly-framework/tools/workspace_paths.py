"""Explicit ownership for wizard workspaces; existing documentation is never adopted blindly."""
import json
import re
import time
from pathlib import Path

MARKER = '.ato-workspace.json'
FORMAT = 'ato-workspace-v1'
NAME = re.compile(r'docs(?:-\d+(?:-\d+)?)?')


def clean_path(path):
    path = Path(path).expanduser().absolute()
    if any(p.is_symlink() for p in (path, *path.parents)):
        raise ValueError('Workspace path must not use symlinks')
    return path.resolve()


def marker_matches(path, repository):
    marker = path / MARKER
    if marker.is_symlink() or not marker.is_file():
        return False
    try:
        value = json.loads(marker.read_text())
    except (ValueError, OSError):
        return False
    return isinstance(value, dict) and value.get('format') == FORMAT and value.get('repository') == str(repository)


def validate_workspace(repository, workspace):
    repository = Path(repository).resolve()
    workspace = clean_path(workspace)
    if repository.is_relative_to(workspace):
        raise ValueError('Workspace cannot replace the application checkout or its parent; choose an owned docs directory or a workspace outside the application checkout')
    if workspace.is_relative_to(repository):
        if workspace.parent != repository or not NAME.fullmatch(workspace.name) or not marker_matches(workspace, repository):
            raise ValueError('In-repository output must use an explicitly claimed docs or docs-timestamp workspace; otherwise use a workspace outside the application checkout')
        if (workspace / '.git').exists():
            raise ValueError('Workspace must not be a nested Git checkout')
    else:
        for parent in (workspace, *workspace.parents):
            if (parent / '.git').exists():
                raise ValueError('External workspace must be outside every Git checkout')
    if workspace.exists() and not workspace.is_dir():
        raise ValueError('Workspace path is not a directory')
    return workspace


def claim_workspace(repository, workspace):
    repository = Path(repository).resolve()
    workspace = clean_path(workspace)
    if marker_matches(workspace, repository):
        return validate_workspace(repository, workspace)
    if workspace.is_relative_to(repository):
        if workspace.parent != repository or not NAME.fullmatch(workspace.name):
            raise ValueError('Choose docs or docs-<unix-timestamp> directly inside the repository')
    else:
        validate_workspace(repository, workspace)
    if repository.is_relative_to(workspace):
        raise ValueError('Workspace cannot contain the application checkout')
    if workspace.exists() and (not workspace.is_dir() or any(workspace.iterdir())):
        raise ValueError('Existing directory contains unrelated work; choose a new workspace')
    workspace.mkdir(parents=True, exist_ok=True)
    with (workspace / MARKER).open('x') as stream:
        json.dump({'format': FORMAT, 'repository': str(repository)}, stream, indent=2)
        stream.write('\n')
    return validate_workspace(repository, workspace)


def discover_workspaces(repository):
    repository = Path(repository).resolve()
    candidates = [p for p in repository.iterdir() if NAME.fullmatch(p.name) and p.is_dir() and not p.is_symlink()
                  and marker_matches(p, repository)]
    # docs first, then numeric creation timestamp/suffix newest-first, with deterministic order.
    def priority(path):
        return (1, 0, 0) if path.name == 'docs' else (0, *([int(x) for x in path.name.split('-')[1:]] + [0])[:2])
    return sorted(candidates, key=priority, reverse=True)


def suggest_workspace(repository, now=None):
    repository = Path(repository).resolve()
    # Respect case-insensitive filesystems as well as an existing lowercase docs directory.
    occupied = {p.name.lower() for p in repository.iterdir()}
    if 'docs' not in occupied:
        return repository / 'docs'
    name = f'docs-{int(time.time() if now is None else now)}'
    candidate, count = name, 1
    while candidate.lower() in occupied:
        candidate = f'{name}-{count}'
        count += 1
    return repository / candidate


def validate_output(repository, output, role):
    """Application-relative writes only at fixed children of a claimed workspace."""
    output = clean_path(output)
    repository = Path(repository).resolve()
    if repository.is_relative_to(output):
        raise ValueError('Output cannot contain the application checkout; choose outside the application or a claimed docs workspace')
    if output.is_relative_to(repository):
        workspace = output.parent
        if output.name != role:
            raise ValueError(f'In-repository output must be <claimed-workspace>/{role}; otherwise use a path outside the application checkout')
        validate_workspace(repository, workspace)
        if (output / '.git').exists():
            raise ValueError('Output must not be a nested Git checkout')
    return output


def excluded_workspaces(repository):
    """Never rediscover the tool's generated documentation as application architecture."""
    excluded = set()
    for path in Path(repository).iterdir():
        if not NAME.fullmatch(path.name) or not path.is_dir() or path.is_symlink():
            continue
        marker = path / MARKER
        if marker.is_symlink() or not marker.is_file():
            continue
        try:
            value = json.loads(marker.read_text())
        except (ValueError, OSError):
            continue
        # A moved checkout is not authorized for writes by its old marker, but its
        # generated documentation still must not become application evidence.
        if isinstance(value, dict) and value.get('format') == FORMAT:
            excluded.add(path.name)
    return excluded
