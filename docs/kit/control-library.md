---
title: "Full catalog control response library"
description: "Regenerate and use catalog-grounded illustrative response templates"
status: draft
tier: 2
---

# Full catalog control response library

The [library index](../../examples/control-library/README.md) covers all **1,196**
controls and enhancements in the pinned NIST SP 800-53/800-53A 5.2.0 OSCAL catalog:
**1,014 active records and 182 withdrawn records**. It helps authors translate exact
requirements into evidence-backed responses without presenting sample text as an
implemented or assessed system.

Each active Markdown file includes the catalog's control-specific guidance,
requirements with stable statement-part IDs, an HTML-commented parameterized
response, questions keyed to each requirement and parameter, assessment objectives,
EXAMINE/INTERVIEW/TEST objects where supplied, and authoritative publication links.
Parameter placeholders retain exact OSCAL IDs. Cross-control references include
parent and sibling parameter definitions; selection choices and parameter guidelines
are retained. Catalog wording is preserved, including upstream inconsistencies;
the library does not reinterpret assessment objectives or invent parameter values.

Withdrawn records document their catalog disposition, including moved-to and
incorporated-into relationships or tailoring statements. They have no illustrative
active implementation response. Inclusion in this library is not baseline selection.

## Using a sample

Read the guidance and exact requirements, then answer the questions using verified
facts for the system boundary. Inspect the Markdown source to see the commented
response template. Replace placeholders with the actual owner, mechanism, scope,
trigger, approved parameter values, and evidence references. Record gaps as tracked
work. A parameterized example is neither evidence nor an assessment result.

The generator owns these examples. Put real system responses in the team's scaffold
response files rather than editing generated library files.

## Offline regeneration and verification

From the repository root:

```sh
python3 sspp-assembly-framework/tools/control_library.py
python3 -m unittest discover -s sspp-assembly-framework/tests -p 'test_control_library.py' -v
```

Generation verifies the catalog SHA-256 against
`data/control-library/provenance.json`, requires no network or additional packages,
and writes one `examples/control-library/<catalog-id>.md` file per record plus
`README.md` and `index.json`. The index includes source revision, source URL, catalog
hash, per-file hashes, and catalog status. Output order follows the pinned catalog;
no timestamps, random identifiers, or machine paths enter the output.

Tests cover the entire inventory, content coverage, comment visibility, withdrawals,
inherited parameters, invalid IDs and pins, byte-for-byte regeneration, scaffold
integration, and preservation of `examples/package`.

## Python integration

`sspp-assembly-framework/tools/control_library.py` exposes:

- `control_records(catalog)`: ID-to-record dictionary, including nested enhancements
  and withdrawn controls; accepts an OSCAL wrapper or its catalog object.
- `guidance_markdown(control, catalog=None)`: appendable Markdown string with no
  frontmatter. An omitted catalog uses the hash-verified local catalog. Pass a
  catalog when resolving parameters and source resources from another catalog.
- `generate(root)`: writes the library under the repository root and returns its
  machine-readable index. Existing generated examples are regenerated in place.

The scaffold appends guidance while retaining `UNFILLED` and `NOT_ASSESSED` status.
AI-assisted generator changes and resulting templates require human review before
use in an authorization package.
