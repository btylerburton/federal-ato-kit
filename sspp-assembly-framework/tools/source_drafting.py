"""Render human-selected source findings as attributed, unassessed draft text."""
from build import json_bytes, literal, sha
from scaffold import collect_controls, markdown_file, parts_for, response_document


def finding_text(finding, record):
    refs = '; '.join(f'{e["path"]}:{e["lines"][0]}-{e["lines"][1]}' for e in finding['evidence'])
    decision = record['decisions'][finding['id']]
    return ('### Source finding: ' + literal(finding['id']) + '\n\n'
            + '\n'.join('> ' + literal(line) for line in finding['text'].splitlines()) + '\n\n'
            + f'- Basis: {finding["status"]}; method: {record["method"]}; author: {literal(record["author"])}\n'
            + f'- Source revision: {record["repository_revision"]}\n'
            + f'- Citations: {literal(refs) or "None — hypothesis"}\n'
            + f'- Included for drafting by: {literal(decision["reviewer"])}\n'
            + '- Assessment: NOT_ASSESSED; source support and operational applicability require review.\n')


def draft_files(record, catalog, output, managed):
    """Seed only pristine or unchanged managed responses; report edited/out-of-selection targets."""
    if record is None:
        return {}, [], ''
    controls = collect_controls(catalog['catalog'])
    desired, preserved, summary = {}, [], []
    context = []
    grouped = {}
    for finding in record['findings']:
        rendered = finding_text(finding, record)
        summary.append(rendered)
        if finding['section'] == 'control':
            grouped.setdefault(finding['control_id'], []).append((finding, rendered))
        else:
            context.append(rendered)
    # A later exclusion removes only unchanged generated suggestions, never team edits.
    for key in controls:
        if f'controls/{key.split("-")[0]}/{key}.response.md' in managed:
            grouped.setdefault(key, [])
    for key, findings in grouped.items():
        if key not in controls:
            summary.append(f'Control {key} is outside this selected baseline; retained here for tailoring review.')
            continue
        name = f'controls/{key.split("-")[0]}/{key}.response.md'
        control = controls[key]
        original = response_document(control, [p for p, _ in parts_for(control)])
        existing = (output / name).read_bytes()
        if existing != original and sha(existing) != managed.get(name):
            preserved.append(name)
            continue
        candidates = ['\n\n## Source-assisted candidate implementation narratives\n\n'
                      'Human-selected drafting suggestions. Existing UNFILLED/NOT_ASSESSED status remains.\n']
        for finding, rendered in findings:
            candidates.append('Target: ' + literal(finding.get('part_id') or key) + '\n\n' + rendered)
        desired[name] = original + ('\n\n'.join(candidates).encode() if findings else b'')
    report = ('# Reviewed source findings for drafting\n\n'
              f'Findings file SHA-256: {record["findings_sha256"]}\n\n'
              f'{record["omitted_count"]} findings excluded or pending. '
              'Inclusion is permission to draft, not evidence of effective controls.\n\n' + '\n\n'.join(summary))
    desired['source-review/findings.md'] = markdown_file('Source review', 'Human-selected candidate source findings', report)
    desired['source-review/provenance.json'] = json_bytes(record)
    return desired, preserved, '\n\n'.join(context)
