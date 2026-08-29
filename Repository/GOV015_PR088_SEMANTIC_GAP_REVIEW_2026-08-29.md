# GOV-015 / PR #88 — Semantic Gap Review

Date: 2026-08-29  
Source: closed unmerged PR #88 candidate `Governance/GOV-015_EXECUTION_DOCUMENTATION_AND_KNOWLEDGE_TRANSFER_PROTOCOL.md`  
State: `REVIEWED / NO WHOLE-DOCUMENT ADOPTION / RESIDUAL TAXONOMY DEFERRED`

## Purpose

Evaluate the **content** of the richer PR #88 GOV-015 candidate against current canonical main without treating branch age, detail, or repeated wording as authority.

## Current canonical surfaces

- `Governance/GOV-015_EXECUTION_DOCUMENTATION_AND_KNOWLEDGE_TRANSFER.md` already governs execution record, knowledge-transfer chain, promotion levels, evidence separation, closure and model independence.
- `Governance/GOV-021_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION.md` already governs repository-first activation, parallel scope declaration, serialized files, HERMUZ/HORUS/MAAT boundaries, work leases, handoffs, collision prevention, and reconstruction.
- `Governance/GOV-027_PROVENANCE_PRESERVATION_AND_SESSION_RECONSTRUCTION_AMENDMENT.md` already governs cross-identity provenance, evidence/authority separation and canonical verification states `HORUS-REPORTED / HERMUZ-VERIFIED / INDEPENDENTLY-VALIDATED`.

## Candidate-content disposition

| Candidate concept from PR #88 | Current-main finding | Disposition |
|---|---|---|
| deterministic activation/re-entry | GOV-021 already stronger and effective | `NO GAP / DO NOT DUPLICATE` |
| base SHA / scope / allowed mutation boundary | GOV-021 parallel-work contract already requires baseline and mutation boundary | `NO GAP / DO NOT DUPLICATE` |
| Work Lease | GOV-021 has canonical lease fields and state model | `NO GAP / DO NOT DUPLICATE` |
| HERMUZ / HORUS / MAAT boundaries | GOV-021 already canonical and more tightly separated | `NO GAP / DO NOT DUPLICATE` |
| Room71 role | GOV-021 already defines Human Control Room boundary | `NO GAP / DO NOT DUPLICATE` |
| handoff capsule | GOV-021 canonical handoff contract is semantically equivalent and already effective | `NO GAP / DO NOT DUPLICATE` |
| evidence-class separation | GOV-015 + GOV-027 already establish separation without promotion | `NO GAP / DO NOT DUPLICATE` |
| `INDEPENDENTLY_VALIDATED` idea | GOV-027 already owns canonical `INDEPENDENTLY-VALIDATED` verification state | `USE CURRENT CANONICAL VOCABULARY` |
| PR labels `SELF_REVIEWED_NOT_INDEPENDENT`, `CROSS_ROLE_REVIEW_NOT_PROVEN_INDEPENDENT`, `EXTERNAL_VALIDATION_UNVERIFIED` | useful descriptive candidate labels, but no demonstrated recurring failure requires canonical promotion yet | `DEFER AS CANDIDATE TAXONOMY` |
| collision classes `C1_FILE..C6_HANDOFF` | useful compact operational taxonomy; underlying protections already exist in GOV-021 | `DEFER UNTIL REPEAT EVIDENCE SHOWS TAXONOMY ADDS VALUE` |
| issue lifecycle state vocabulary | operational convenience, not proven Governance gap | `DEFER / TOOLING-SURFACE CANDIDATE` |

## Decision

Do **not** create a second GOV-015 document and do **not** copy the PR candidate wholesale into canonical GOV-015.

The candidate's core safety semantics are already covered by current canonical GOV-015/GOV-021/GOV-027. Repeating them would create overlapping authority surfaces and future drift risk.

The only residual value is compact vocabulary/taxonomy. It remains candidate knowledge until repeated operational evidence demonstrates that adding the labels/classes improves ambiguity handling beyond existing controls.

## Promotion trigger for deferred taxonomy

A future promotion may be considered only if at least one recurring ambiguity/failure is shown to be materially harder to classify under existing GOV-021/GOV-027 states, and a controlled test demonstrates that the new taxonomy improves deterministic routing without creating competing authority.

## Continuous-improvement learning

A richer document is not automatically a better canonical document. Semantic review must ask whether a proposed rule fills a real gap or merely restates controls that already exist elsewhere. **Duplicate safety rules can become a future inconsistency threat.**

## Closure

`PR88-GOV015-WHOLE-DOCUMENT-CANDIDATE = CLOSED / NOT ADOPTED`  
`PR88-GOV015-UNIQUE-TAXONOMY = DEFERRED CANDIDATE / PROMOTION TRIGGER DEFINED`

No canonical Governance mutation was required by this review.
