"""Read-only Git path inventory; do not execute repository code or read secret contents."""
import subprocess
from pathlib import Path

SKIP_PARTS = {'.git', 'node_modules', '.venv', '.venv-ato', 'vendor', 'dist', 'build', '__pycache__'}


def checkout_root(repository):
    result = subprocess.run(['git', '-C', str(repository.resolve()), 'rev-parse', '--show-toplevel'],
                            capture_output=True, text=True, timeout=30, check=False)
    if result.returncode:
        raise ValueError('Repository must be inside a Git checkout')
    return Path(result.stdout.strip()).resolve()


def inspect(repository):
    repository = checkout_root(repository)
    def git(*args):
        result = subprocess.run(['git', '-C', str(repository), *args], capture_output=True,
                                timeout=30, check=False)
        if result.returncode:
            raise ValueError('Repository inspection requires a readable Git checkout with a commit')
        return result.stdout
    revision = git('rev-parse', 'HEAD').decode().strip()
    paths = git('ls-files', '-z').decode('utf-8').split('\0')
    safe = []
    for name in filter(None, paths):
        p = Path(name)
        if p.is_absolute() or '..' in p.parts or any(part in SKIP_PARTS for part in p.parts):
            continue
        if p.name.startswith(('.env', '.dev.vars')) or p.suffix.lower() in {'.pem', '.key', '.p12', '.pfx'}:
            continue
        if not (repository / p).resolve().is_relative_to(repository) or (repository / p).is_symlink():
            continue
        safe.append(name)
    groups = {
        'dependency_manifests': [p for p in safe if Path(p).name in {'package.json', 'pyproject.toml', 'Cargo.toml', 'go.mod', 'Gemfile'}],
        'deployment_files': [p for p in safe if Path(p).name in {'Dockerfile', 'wrangler.jsonc', 'wrangler.toml', 'manifest.yml'} or p.endswith('.tf')],
        'workflow_files': [p for p in safe if p.startswith('.github/workflows/')],
        'test_files': [p for p in safe if Path(p).name.startswith('test_') or '.test.' in p or '.spec.' in p],
        'documentation': [p for p in safe if p.lower().endswith('.md')],
    }
    return {'repository_revision': revision, 'working_tree_dirty': bool(git('status', '--porcelain', '-uno')),
            'method': 'tracked-path inventory only; no repository file contents executed or assessed',
            'tracked_paths_considered': len(safe),
            'signals': {k: {'count': len(v), 'sample_paths': v[:25], 'status': 'observed-paths-not-effectiveness'} for k, v in groups.items()},
            'limits': ['No runtime, provider, code-semantic or deployment verification.',
                       'A listed test/workflow is not evidence it passed.', 'Categorization and boundary cannot be inferred from paths.']}


def questions():
    from inheritance import QUESTIONS
    return [
        {'id': 'system_name', 'question': 'What system and mission does this repository support?'},
        {'id': 'mode', 'question': 'Generate a LATO reference draft or full ATO baseline draft?', 'choices': ['lato', 'ato']},
        {'id': 'baseline', 'question': 'For full ATO, which owner-selected impact baseline applies?', 'choices': ['low', 'moderate', 'high'], 'when': 'mode=ato'},
        {'id': 'scope_confirmed', 'question': 'Has the owner confirmed this selection is appropriate for this draft?', 'type': 'boolean'},
        {'id': 'system_owner', 'question': 'Who owns the system and unresolved decisions?'},
        {'id': 'environment', 'question': 'Which environment and release are in scope?'},
        {'id': 'date', 'question': 'What fixed document date should this draft use (YYYY-MM-DD)?'},
        {'id': 'data_categories', 'question': 'What data is processed, including PII, authenticator and agency records?', 'type': 'string-list'},
        {'id': 'boundary_summary', 'question': 'What components and external services are inside/outside the proposed boundary?'},
        {'id': 'topology', 'question': 'Supply nodes (id/title/boundary) and flows (from/to/data/protocol/authentication/storage) for proposed diagrams.', 'type': 'object'},
    ] + [dict(q, section='inheritance') for q in QUESTIONS]
