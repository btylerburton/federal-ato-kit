---
title: "Treat provider inheritance as source assertions plus applicability decisions"
description: "Draft decision for importing reference components into wizard responsibility mapping"
status: draft
tier: 2
date: "2026-11-23"
decision_status: proposed
decision_makers: ["Repository owner"]
category: "Deployment and Infrastructure"
nist_controls: ["PL-2", "PL-8", "CM-8", "SA-5"]
ato_relevance: yes-internal
---

# Candidate inheritance mapping

## Context and drivers

The user requested four common-control component definitions in the reusable kit and wizard
questions to select relevant providers/practices. The supplied files mix provider/common/hybrid
assertions, customer prerequisites and historical OSCAL versions. Provider presence is not
sufficient to establish applicability or application compliance.

## Options and decision

Options: copy provider status to system status; ignore provider material; or retain exact
source assertions with separate declarations and unresolved decisions. Use the third option.
Import bytes unchanged with version/hash provenance. Ask service-specific yes/no/unknown
questions. Match exact selected control and part IDs; expose rule descriptions and customer
actions. Keep inheritance decisions UNRESOLVED and evidence NOT_ASSESSED until supplied.

## Consequences

The review document gains an actionable responsibility inventory while retaining provenance.
Historical claims are not silently upgraded to current provider attestations. The supplied
cloud.gov PaaS definition does not establish Pages inheritance. SHA pinning is a dependency
practice rather than automatic eligibility for GSA Common Controls. Real provider examples
are an explicitly requested exception to the kit's otherwise synthetic system examples.

Formal OSCAL incorporation and architectural boundary decisions remain separate tracked
work. This increment adds no dependency, changes no authentication flow and performs no live
provider verification. Source schema labels remain as supplied; exact-schema validation is
not claimed from a JSON parse.
