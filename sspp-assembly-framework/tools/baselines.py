"""Offline baseline selection using pinned NIST profiles and labeled LATO reference IDs."""
import copy
from pathlib import Path
from build import load_json, sha, json_bytes
from scaffold import collect_controls

KIT = Path(__file__).resolve().parents[2]


def load_inputs(root=KIT):
    pins = load_json(root / 'data/control-library/provenance.json')
    values = {}
    for name, record in pins.items():
        path = (root / record['path']).resolve()
        if not path.is_relative_to(root.resolve()) or sha(path.read_bytes()) != record['sha256']:
            raise ValueError(f'Pinned input mismatch: {name}')
        values[name] = load_json(path)
    return values, pins


def selected_catalog(mode, baseline, root=KIT):
    values, pins = load_inputs(root)
    if mode == 'lato':
        ids = values['lato-reference']['control_ids']
        selection = 'lato-reference'
    elif mode == 'ato' and baseline in {'low', 'moderate', 'high'}:
        selection = baseline
        profile = values[baseline]['profile']
        # These pinned profiles select explicit IDs only; refuse unsupported tailoring semantics.
        if len(profile['imports']) != 1 or 'modify' in profile:
            raise ValueError('Profile needs full OSCAL resolution before use')
        imported = profile['imports'][0]
        if set(imported) != {'href', 'include-controls'} or len(imported['include-controls']) != 1:
            raise ValueError('Unsupported baseline selection expression')
        include = imported['include-controls'][0]
        if set(include) != {'with-ids'}:
            raise ValueError('Unsupported baseline include expression')
        ids = include['with-ids']
    else:
        raise ValueError('Select lato or ato with low/moderate/high baseline')
    full = collect_controls(values['catalog']['catalog'])
    if len(set(ids)) != len(ids) or not set(ids) <= set(full):
        raise ValueError('Invalid baseline control inventory')
    controls = []
    for key in ids:
        control = copy.deepcopy(full[key])
        control.pop('controls', None)  # Enhancements are independently selected, never implied.
        controls.append(control)
    catalog = {'catalog': {'uuid': values['catalog']['catalog']['uuid'],
        'metadata': dict(values['catalog']['catalog']['metadata'], title=f'Draft selection: {selection}'),
        'controls': controls}}
    return catalog, {'selection': selection, 'count': len(ids), 'source_sha256': pins[selection]['sha256'],
                     'catalog_sha256': pins['catalog']['sha256'], 'tailoring': 'Owner confirmation required'}
