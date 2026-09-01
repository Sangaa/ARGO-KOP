# MUT-2026-09-01-P7-CORE011-ARC005-CHARTER-RULES-SEAM-H — Mutation Matrix

Transaction ID: `MUT-2026-09-01-P7-CORE011-ARC005-CHARTER-RULES-SEAM-H`
Protocol: `GOV-013 / GOV-014A`
Status: `PREWRITE-AUTHORIZED / P7-OPEN`
Date: 2026-09-01
Entry HEAD: `0940c7b3f9d0d81b96e2cdfd4e80a5d65c1d0c83`

## Problem definition

Priority-7 Core cross-layer validation remains open after Transactions E/F/G. Recomputed live evidence identifies a directly evidenced Core→Architecture seam that is absent from REP-014: `Architecture/ARC-005_ARCHITECTURE_RULES.md` explicitly lists `Core/CORE-011_PLATFORM_CHARTER.md` under Related Documents, while CORE-011 defines platform responsibility/authority boundaries and does not directly name ARC-005. Current REP-014 v1.2.9 has no CORE-011 relationship row.

Classification: `MATERIAL CORE→ARCHITECTURE DOCUMENTARY RELATIONSHIP GAP / NO SOURCE SEMANTIC DEFECT FOUND`.

## Prior-learning retrieval

- `GOV-013`: repository-first re-entry, prior-learning gate, Three-Search Rule, smallest sufficient mutation, integration verification — DIRECTLY APPLICABLE.
- `GOV-014A`: prewrite Matrix and same-change-set binding required for protected mutation — DIRECTLY APPLICABLE.
- Transaction E / REL-062: a direct one-way documentary reference must not be promoted to dependency or receive a reverse edge for symmetry — DIRECTLY APPLICABLE.
- Transaction F: bidirectional registry state is allowed only when both directions are independently evidenced — DIRECTLY APPLICABLE.
- Transaction G / REL-065: unchanged source artifacts may support a bounded registry-only relationship reconciliation — DIRECTLY APPLICABLE.
- `ARC-006`: Core depends on none at the architectural layer level; Architecture may depend on Core/Governance; textual reference alone is not architectural dependency — DIRECTLY APPLICABLE.

## Three-path verification

1. Direct source: ARC-005 current content explicitly lists `Core/CORE-011_PLATFORM_CHARTER.md` under Related Documents.
2. Direct target: CORE-011 defines platform scope/responsibility/authority boundaries, explicitly states it does not override Canonical Architecture, and does not directly name ARC-005.
3. Independent repository search: CORE-011 appears in Architecture only through ARC-005; REP-014 contains no CORE-011 row; no current evidence establishes a reverse `CORE-011 → ARC-005` relationship or a stronger `DEPENDS_ON`/`GOVERNS`/`IMPLEMENTS`/`CONSUMES` relationship.

## Planned protected change set

| ID | Target | Intended change |
|---|---|---|
| H-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | v1.2.9 → v1.2.10; add one `ARC-005 → CORE-011 = REFERENCES` row only |
| H-02 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | refresh REP-014 row to v1.2.10 and bind exact H candidate; preserve all Phase-1/global holds |
| H-03 | `Core/_FOLDER_STATUS.md` | v1.3.5 → v1.3.6; record fourth bounded seam; certification remains pending |
| H-04 | `Quality/Integrity/test_core011_arc005_charter_rules_boundary.py` | focused one-way/non-dependency regression |
| H-05 | `Repository/P7_CORE011_ARC005_CHARTER_RULES_SEAM_2026-09-01_H.md` | evidence/progress record |
| H-06 | this Matrix | same-change-set binding/candidate evidence, then closure evidence after CI |

No mutation of CORE-011 or ARC-005 source content is authorized because current evidence does not establish a source semantic defect.

## Relationship decision authorized for candidate

```text
ARC-005 → CORE-011 = REFERENCES
```

Candidate state label:

`INTENTIONAL ONE-WAY / CHARTER-BOUNDARY-ALIGNED / NON-DEPENDENCY`

No reverse edge is authorized without direct evidence. No architectural dependency is authorized merely because ARC-005 names CORE-011.

## KEEP / HOLD boundaries

- CORE-011 remains unchanged and does not acquire Architecture authority.
- ARC-005 remains unchanged and does not acquire Core authority.
- `ARC-006` dependency direction remains intact.
- Core remains `INTEGRITY HOLD / CROSS-LAYER VALIDATION OPEN`; Folder Certification remains pending.
- Architecture remains under its own Integrity Hold / re-audit; this transaction does not certify Architecture.
- Phase 1 remains OPEN; repository-wide graph / Connected Baseline remains OPEN; Global integrity remains HOLD; Global PASS is NOT CLAIMED.

## Execution rule

After this prewrite authorization is committed, re-read live main. If unchanged except for this Matrix, create the protected candidate as one atomic Git-object commit containing H-01 through H-06. Any required CI failure triggers `GOV-013 §9B HARD HOLD` before further construction.
