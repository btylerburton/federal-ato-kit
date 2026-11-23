---
title: "Common-control component reference examples"
description: "User-selected provider and organization responsibility definitions with preserved provenance"
status: draft
tier: 3
last_updated: "2026-11-23"
---

# Common-control reference examples

These four user-requested component definitions are intentionally provider/organization-specific
examples in the reusable kit. Their presence does not select them for every system or attest
to current provider scope. `index.json` records each original version, date, OSCAL version and
SHA-256. Original JSON bytes were copied unchanged from the supplied template directories.

| Reference | Intended use | Applicability question |
| --- | --- | --- |
| `cloud_gov` | Cloud.gov PaaS LATO responsibility matrix | Does this particular service and authorization inherit the described scope? Pages is not automatically equivalent to PaaS. |
| `cg-egress-proxy` | Proxy software and customer prerequisites | Is the proxy actually deployed, and is direct public-network egress restricted as required? |
| `gsa_common_controls` | GSA common and hybrid controls | Is the consuming system covered by the stated GSA federal/contractor scope and current catalog? |
| `org-dependency-management` | Org-level SHA pinning, Renovate, SLA tracking and actions SAST | Is the repository actually enrolled, with the stated org preset and enforcement/evidence? |

References retain their original provider statements and statuses. Some are dated 2024/2025
and use older OSCAL schema labels. The wizard parses their responsibility mappings; it does
not silently relabel schemas, certify exact historical schema conformance or declare controls
implemented. Current provider evidence and owner applicability decisions remain necessary.

## SHA-pinning example

Moving reference:

```yaml
- uses: actions/checkout@v4
```

Illustrative immutable-reference syntax (replace the placeholder with a commit you verified
against the upstream release; the placeholder is deliberately not runnable):

```yaml
- uses: actions/checkout@<VERIFIED_40_CHARACTER_COMMIT_SHA> # reviewed release
```

Pin external actions, including reusable workflows and relevant transitive actions; review
updates rather than trusting a moving tag. Retain the upstream release/commit verification,
reviewed update PR, workflow scan results and actual enforcement settings as evidence. An org
preset and Renovate onboarding are separate prerequisites from a lockfile or a single pinned action.

SHA pinning is an implementation practice, reflected in the dependency-management example.
It is not itself inheritance from GSA Common Controls. A provider's fully-inherited rule can
apply only to its stated scope and prerequisites; application-specific parts remain separate.

Guidance: [GitHub Actions security hardening](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions),
[cloud.gov customer responsibilities](https://cloud.gov/docs/overview/customer-responsibilities/),
[Renovate configuration](https://docs.renovatebot.com/configuration-options/).
These are reference links; no live link or provider-attestation validation is asserted here.
