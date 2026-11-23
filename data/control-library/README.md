---
title: "Pinned control-library inputs"
description: "NIST source revisions and reference baseline selection provenance"
status: draft
tier: 2
last_updated: "2026-11-23"
---

# Pinned inputs

`provenance.json` records immutable upstream URLs, Git revision and SHA-256 for every downloaded
input. The NIST catalog is Rev. 5.2.0 with assessment procedures; the official security profiles
select 149 Low, 287 Moderate and 370 High control/enhancement IDs. The complete catalog has
1,196 entries, including withdrawn controls.

`lato-reference.json` is the user-approved 58-control reference selection. It contains control
IDs only, not source-system narratives or inherited parameter assignments. It is not a universal
LATO standard or an agency-approved applicability determination for another system.

The normal build is offline and checks each input hash. The current baseline selector supports
the explicit-ID form used by these pinned profiles; profiles containing more complex selection
or tailoring must be resolved by Trestle instead of silently approximated. Security baseline
selection does not settle additional privacy-control or agency-overlay obligations.

Official public publication references used by the library:

- https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
- https://csrc.nist.gov/pubs/sp/800/53/a/r5/final
- https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final
- https://pages.nist.gov/OSCAL/

Input retrieval from the NIST GitHub repository succeeded. Attempts to verify the publication
pages on November 23 failed TLS certificate verification in the execution environment; no
certificate checks were disabled. Link reachability remains unverified, not falsely reported
as a passing link check. These public government publications are source references, not a
license determination for this repository's original code.
