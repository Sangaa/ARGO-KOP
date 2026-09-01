# MUT-2026-09-01-P7-CORE012-GOV016-LEARNING-SEAM-G — Mutation Matrix

Transaction ID: `MUT-2026-09-01-P7-CORE012-GOV016-LEARNING-SEAM-G`
Protocol: `GOV-013 / GOV-014A`
Status: `PREWRITE / AUTHORIZED / P7-OPEN`
Date: 2026-09-01
Entry HEAD: `2e8d89d15b7c4874737a9440e30c8b3e7ff9dd9a`

## Problem definition

`Core/CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md` explicitly states that its failure-as-generative-training rule works together with `GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md`. The current canonical `Governance/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md` is ACTIVE / MANDATORY and governs failure classification, root-cause analysis, regression, reuse and knowledge transfer. Current REP-014 does not yet register this material Core→Governance learning-control seam.

No source-level defect requiring mutation of CORE-012 or GOV-016 was found. The gap is relationship-registry coverage only.

## Prior-learning retrieval

- `GOV-013`: prior-learning retrieval, evidence-first continuation and Three-Search Rule — DIRECTLY APPLICABLE.
- `GOV-014A`: protected mutation requires prewrite Matrix plus same-change-set binding — DIRECTLY APPLICABLE.
- Transaction E / REL-062: direct one-way reference must not be promoted to dependency or receive a reverse edge merely for symmetry — DIRECTLY APPLICABLE.
- Transaction F: two directions are registered only when both directions are independently evidenced — DIRECTLY APPLICABLE.
- `EJR-251`: CORE-012 and GOV-016 were introduced together in the same governed inventory reconciliation and historical closeout uses both as session authority — TRANSFERABLE provenance evidence, not independent reverse-edge authority.
- `EJR-253`: GOV-016 path reconciliation explicitly changed path case without changing governance semantics, Core authority, Runtime behavior or relationships — TRANSFERABLE identity evidence.

## Three-path verification

1. Direct source: CORE-012 explicitly says its Failure-as-Generative-Training rule works together with `GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md`.
2. Direct target: current `Governance/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md` is ACTIVE / MANDATORY and defines the failure→learning control chain, but does not name CORE-012 as a required source/dependency.
3. Historical/control evidence: EJR-251 records CORE-012 and GOV-016 as the paired Core/Governance additions; current repository searches reveal co-authority usage but no source evidence for a `GOV-016 → CORE-012` relationship in the target document.

## Relationship decision

```text
CORE-012 → GOV-016 = REFERENCES
```

Disposition: `INTENTIONAL ONE-WAY / FAILURE-LEARNING-ALIGNED / NON-DEPENDENCY`.

Do NOT create:
- `GOV-016 → CORE-012` merely for symmetry;
- `CORE-012 → GOV-016 = DEPENDS_ON` merely because the Core rule works together with the governance protocol;
- any authority promotion of CORE-012 over GOV-016 or GOV-016 over Core constitutional authority.

## Authorized change set

| ID | Target | Action | Expected change | Prewrite |
|---|---|---|---|---|
| G-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE | add one evidence-backed `CORE-012 → GOV-016 = REFERENCES` record; increment version minimally | AUTHORIZED |
| G-02 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | UPDATE | refresh REP-014 version after G-01; preserve Phase-1/global holds | AUTHORIZED |
| G-03 | `Core/_FOLDER_STATUS.md` | UPDATE | record third bounded P7 seam while preserving broader dependency/consumer and certification hold | AUTHORIZED |
| G-04 | `Quality/Integrity/test_core012_gov016_learning_boundary.py` | CREATE | enforce one-way reference/non-dependency/no fabricated reverse edge | AUTHORIZED |
| G-05 | `Repository/P7_CORE012_GOV016_LEARNING_SEAM_2026-09-01_G.md` | CREATE | evidence/progress/closure record | AUTHORIZED |
| G-06 | this Matrix | UPDATE | bind exact same-change-set mutation and later CI/closure evidence | AUTHORIZED |

## KEEP requirements

- CORE-012 content remains unchanged; no new semantic certification is invented.
- GOV-016 content remains unchanged; ACTIVE / MANDATORY authority is not redefined.
- No reverse relationship is added without direct source evidence.
- No stronger relationship type than REFERENCES is created.
- Core remains `INTEGRITY HOLD / CROSS-LAYER VALIDATION OPEN`.
- No Core certification, Phase-1 closure, repository-wide graph completion, Connected Baseline PASS or Global integrity PASS.
- Protected changes plus this Matrix must enter one atomic Git change set.

## Pre-write decision

`PASS / AUTHORIZED FOR BOUNDED ATOMIC MUTATION`.
