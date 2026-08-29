# ROOM71 DOCS AUTHORITY BOUNDARY — LEASE 140

Date: 2026-08-29
Role: HERMUZ via Room71
Baseline: `a2a2919a8210f32ee7122083c8aed8f90ebabe83`
Authority: bounded current-repository evidence only

## Current Tree

The exact current recursive `Docs/` tree is non-truncated and contains:
- `PROJECT_OVERVIEW.md` (`DOC-001`)
- `ARCHITECTURE_OVERVIEW.md` (`DOC-002`)
- `COGNITIVE_MODEL.md` (`DOC-003`)
- `FAQ.md`
- `GLOSSARY.md` (`DOC-005`)
- `Examples.MD`
- `External_Review/EXT-001_EXTERNAL_REVIEW_PROTOCOL.md`

## Authority Review

### DOC-001 — Project Overview

The artifact declares Category `Documentation` and explicitly provides a high-level project introduction. It is explanatory and does not establish higher platform authority over Core, Governance, Architecture or Repository control surfaces.

### DOC-002 — Architecture Overview

The artifact explicitly states that it is a simplified overview and "summarizes the architectural layers without replacing the detailed architecture documentation."

Therefore:

`DOC002_ARCHITECTURE_AUTHORITY = EXPLANATORY_ONLY / DOES_NOT_REPLACE_ARCHITECTURE`

### DOC-003 — Cognitive Model

DOC-003 is an Approved documentation explanation of the cognitive model.

Current Core owns a later governed cognitive surface:
`Core/CORE-005_COGNITIVE_MODEL.md` declares Document ID `CORE-005`, Version `3.2.0`, Status `Validated / Integrity Hold / Revalidated`, Category `Core`, Canonical `Yes`.

Therefore:

`DOC003_COGNITIVE_AUTHORITY = EXPLANATORY_DOCUMENTATION`

`CORE005 = CURRENT GOVERNED CORE COGNITIVE MODEL WITHIN ITS DECLARED SCOPE`

### DOC-005 — Glossary

Lease 135 already established:

`CORE-000A_PLATFORM_GLOSSARY = CURRENT GOVERNED CORE TERMINOLOGY REFERENCE`

`DOC005 = DOCUMENTATION / LEGACY EXPLANATORY SURFACE / NO COMPETING CORE AUTHORITY`

### EXT-001 — External Review Protocol

EXT-001 declares `Candidate / Integrity Hold` and explicitly states that external review is evidence, not authority. It therefore cannot become governance authority merely by living under Docs.

## Bounded Disposition

For the current inspected tree:

`DOCS_DOMAIN_DEFAULT_ROLE = EXPLANATORY / NAVIGATIONAL / REVIEW-SUPPORT`

`DOCS_CONTENT != AUTOMATIC CORE_GOVERNANCE_ARCHITECTURE_AUTHORITY`

Where a Docs artifact overlaps a governed Core/Architecture/Governance semantic surface, the higher/current governed artifact controls according to its declared scope and authority; Docs remains explanatory unless separately promoted through governance.

## Why No Bulk Rewrite

The current Docs artifacts remain useful as human-facing explanations and external-review support. Authority ambiguity can be closed without deleting them. Future content reconciliation may add explicit pointers to current governed sources after consumer/navigation review.

## Learning

`APPROVED DOCUMENTATION != CANONICAL DOMAIN AUTHORITY`

`OVERVIEW != SOURCE OF ARCHITECTURAL TRUTH`

`EXPLANATORY DUPLICATION CAN REMAIN USEFUL IF AUTHORITY BOUNDARY IS EXPLICIT`

## Close State

`DOCS_CURRENT_TREE_AUTHORITY_AMBIGUITY = CLOSED / EXPLANATORY_BY_DEFAULT_WITH_EXPLICIT_HIGHER_AUTHORITY_OVERRIDES`

`DOCS_CONTENT_REFRESH_AND_LINK_MIGRATION = OPEN / NON_BLOCKING`

`CONNECTED_BASELINE_GLOBAL = NOT CLOSED BY THIS LEASE`
