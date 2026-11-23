---
title: "Federal standards and playbook provenance"
description: "Context-derived guidance with authority and revision boundaries"
status: draft
tier: 2
last_updated: "2026-11-06"
---

# Standards map

The agentic-coding-playbook is informational guidance, not official GSA policy.
The following synthesis comes from the universal `AGENTS.md` contract version
1.0.0 (document dated 2026-07-06), `docs/CODING_PRACTICES.md` (2026-06-22), and
the loaded `code-review`, `federal-decision-records`, and `paseo-first-mate`
skills. Their local installation paths are not portable source references.
Record the actual playbook repository revision when supplied. Its claimed dates
and framework revisions have not all been checked against current publications.

| Authority/family | Role in review | Evidence needed |
| --- | --- | --- |
| FIPS 199; FIPS 200; NIST SP 800-60 | Categorization, minimum requirements, information types | Owner-approved impact and type rationale |
| NIST SP 800-37 Rev. 2 | RMF lifecycle: prepare, categorize, select, implement, assess, authorize, monitor | Agency-specific workflow and accountable decisions |
| NIST SP 800-53 Rev. 5 and applicable updates | Security/privacy control catalog | Exact catalog revision, selected controls, tailoring and parameters |
| NIST SP 800-53B | Control baselines | Approved baseline and tailoring rationale |
| NIST SP 800-53A Rev. 5 | Assessment procedures | Objectives, examination/interview/test methods, assessor observations |
| NIST SP 800-18 and agency SSPP template | Plan organization | Applicable publication/template revision confirmed by agency |
| NIST SP 800-63 series | Digital identity | Applicable revision, IAL/AAL/FAL rationale and flow evidence |
| FIPS 140-3 / applicable cryptographic validation requirements | Cryptographic modules | Actual module/certificate, mode, platform and use; algorithm name alone is insufficient |
| NIST SP 800-218 and 800-218A | Secure development and AI-related development practices | Change provenance, review, testing and supply-chain evidence |
| NIST AI RMF 1.0 and AI 600-1 | AI risk management | Model/provider inventory, evaluations, monitoring, data handling |
| OSCAL | Machine-readable compliance models | Model version, valid structure/references and source provenance |
| Agency policy, privacy law, agreements, OMB direction | Applicable organizational/legal obligations | Current applicability determination; owner/legal review where needed |
| OWASP LLM/agentic guidance | Supplemental threat modeling | Versioned guidance and mapped risks, not a federal control baseline |

Authoritative discovery entry points: https://csrc.nist.gov/publications and
https://pages.nist.gov/OSCAL/ . These are references, not evidence that a particular
revision has been retrieved or is applicable. Track current-source refresh in the
consuming project's work register with an owner and trigger.

## Control-oriented review lenses

- AC/IA: privilege, account lifecycle, session handling, authentication and identity.
- AU: events, log content/redaction, access, retention and audit integrity.
- CA/RA/SA: assessment, monitoring, testing, vulnerability treatment and suppliers.
- CM: configuration provenance, environment differences, inventory and change review.
- SC/SI: boundary, transmission/storage protection, validation and failure handling.
- PT/PL: processing purpose, notice/consent where applicable, plan and architecture.
- CP/IR/MP: recovery, incident handling, media retention/deletion and evidence.

Control mappings identify review relevance, not satisfaction. Provider
authorization, commercial certifications, and a passing scanner do not substitute
for the system's selected assessment objectives or authorizing official decision.
