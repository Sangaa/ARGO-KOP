# MUT-2026-09-01-P7-CORE011-ARC005-CHARTER-RULES-SEAM-H — Mutation Matrix

Transaction ID: `MUT-2026-09-01-P7-CORE011-ARC005-CHARTER-RULES-SEAM-H`
Protocol: `GOV-013 / GOV-014A`
Status: `CANDIDATE / CI-PENDING / P7-OPEN`
Date: 2026-09-01
Entry HEAD: `0940c7b3f9d0d81b96e2cdfd4e80a5d65c1d0c83`
Prewrite authorization HEAD: `c9b7488732aef02fd53aa45d1fb608a24dbd019f`
Candidate parent after non-overlapping prewrite: `48e6e87a4bfaa24a0ec0f9d6cf2a0fb9f8d6aa60`

## Problem definition

Priority-7 Core cross-layer validation remains open after Transactions E/F/G. Recomputed live evidence identifies a directly evidenced Core/Architecture seam absent from REP-014: `Architecture/ARC-005_ARCHITECTURE_RULES.md` explicitly lists `Core/CORE-011_PLATFORM_CHARTER.md` under Related Documents, while CORE-011 defines platform responsibility/authority boundaries and does not directly name ARC-005. REP-014 v1.2.9 has no CORE-011 relationship row.

Classification: `MATERIAL CORE→ARCHITECTURE DOCUMENTARY RELATIONSHIP GAP / NO SOURCE SEMANTIC DEFECT FOUND`.

## Prior-learning retrieval

- `GOV-013`: repository-first re-entry, prior-learning gate, Three-Search Rule, smallest sufficient mutation, integration verification — DIRECTLY APPLICABLE.
- `GOV-014A`: prewrite Matrix and same-change-set binding required for protected mutation — DIRECTLY APPLICABLE.
- Transaction E / REL-062: direct one-way documentary reference must not be promoted to dependency or receive reverse edge for symmetry — DIRECTLY APPLICABLE.
- Transaction F: bidirectional registry state only when both directions are independently evidenced — DIRECTLY APPLICABLE.
- Transaction G / REL-065: unchanged source artifacts may support bounded registry-only relationship reconciliation — DIRECTLY APPLICABLE.
- `ARC-006`: Core depends on none at architectural layer level; Architecture may depend on Core/Governance; textual reference alone is not architectural dependency — DIRECTLY APPLICABLE.

## Three-path verification

1. ARC-005 explicitly lists `Core/CORE-011_PLATFORM_CHARTER.md` under Related Documents.
2. CORE-011 defines platform scope/responsibility/authority boundaries, states it does not override Canonical Architecture, and does not directly name ARC-005.
3. Independent repository search found no current reverse `CORE-011 → ARC-005` relationship and no stronger `DEPENDS_ON`/`GOVERNS`/`IMPLEMENTS`/`CONSUMES` evidence.

## Protected candidate change set

| ID | Target | Candidate change |
|---|---|---|
| H-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | v1.2.9 → v1.2.10; add `REL-066 ARC-005 → CORE-011 = REFERENCES` only |
| H-02 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | refresh REP-014 row to v1.2.10 and bind H candidate parent; preserve all Phase-1/global holds |
| H-03 | `Core/_FOLDER_STATUS.md` | v1.3.5 → v1.3.6; record fourth bounded seam; certification remains pending |
| H-04 | `Quality/Integrity/test_core011_arc005_charter_rules_boundary.py` | focused one-way/non-dependency regression |
| H-05 | `Repository/P7_CORE011_ARC005_CHARTER_RULES_SEAM_2026-09-01_H.md` | evidence/progress record |
| H-06 | this Matrix | same-change-set binding/candidate evidence |

CORE-011 and ARC-005 source content remain unchanged because no source semantic defect is established.

## Relationship decision

`ARC-005 → CORE-011 = REFERENCES`

State: `INTENTIONAL ONE-WAY / CHARTER-BOUNDARY-ALIGNED / NON-DEPENDENCY`.

No reverse edge or stronger relationship is authorized without direct evidence.

## Intervening-change revalidation

After H prewrite authorization, `main` advanced only by creation of `Repository/MUT-2026-09-01-P7-CORE000-CANONICAL-ARCHITECTURE-DRIFT-I_MUTATION_MATRIX.md` at `48e6e87a4bfaa24a0ec0f9d6cf2a0fb9f8d6aa60`. That commit does not touch H-01..H-05 targets. H source/target evidence was re-read at the new parent and remains unchanged. H is therefore rebound to this exact parent. Transaction I is deferred until H closure so shared control-plane surfaces are not mutated concurrently.

## KEEP / HOLD boundaries

- CORE-011 remains unchanged and does not acquire Architecture authority.
- ARC-005 remains unchanged and does not acquire Core authority.
- ARC-006 dependency direction remains intact.
- Core remains `INTEGRITY HOLD / CROSS-LAYER VALIDATION OPEN`; Folder Certification remains pending.
- Architecture remains under its own Integrity Hold; this transaction does not certify Architecture.
- Phase 1 remains OPEN; repository-wide graph / Connected Baseline remains OPEN; Global integrity remains HOLD; Global PASS is NOT CLAIMED.

## Verification rule

The candidate must be one atomic Git-object commit containing H-01 through H-06. Exact-head required CI must pass. Any required failure triggers `GOV-013 §9B HARD HOLD` before further construction.
