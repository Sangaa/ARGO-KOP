# MUTATION MATRIX — P2 EJR PROVENANCE CENSUS 192

Transaction ID: `MUT-2026-08-30-P2-EJR-PROVENANCE-CENSUS-192`
Protocol: GOV-014 v1.0.1
Lease: `R71-20260830-P2-EJR-PROVENANCE-CENSUS-192`
State: `CLOSED / ANALYTICAL EVIDENCE PERSISTED / FUNCTIONAL TREE NOT APPLIED`
Entry head: `ed4036c86a0e5c2e3900776106eedfbaf7a47793`
Prewrite head: `595ebd23e393bc7eb57de6930d60ce7211a66e9a`
Analytical evidence commit: `d1c071cb386814e97de67e4d462d267e86fa99d0`

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| 192-001 | Lease 192 record | UPDATE | persist exact six-group census, chronology, root cause and continuation gate | Y | Y |
| 192-002 | separate census functional artifact | CREATE | exact six-group census artifact | N | N — `create_tree` blocked before repository mutation; evidence persisted in Lease instead |
| 192-003 | all existing EJR artifacts | KEEP | no EJR identity/content/path mutation | Y | Y |
| 192-004 | detector semantics | KEEP | no suppression or ambiguity-membership reduction | Y | Y |

## Proven analytical result

Lease-191 artifact `9731526902` contains 144 ambiguous groups, 121 EJR groups and exactly six EJR groups containing at least one `DOCUMENT_ID_FIELD`: EJR-003, EJR-026, EJR-180, EJR-181, EJR-182, EJR-183.

Chronology proves a historical allocation/discovery defect for at least EJR-026, EJR-181 and EJR-183: later repair/migration commits selected replacement IDs already occupied by earlier H1 identity claims.

EJR-003 is an early explicit claim followed by later distinct reuse. EJR-180 and EJR-182 remain unresolved multi-claim groups; metadata strength alone is not promoted to ownership.

## Tool-policy boundary

Prepared blobs for a separate census artifact and Matrix candidate were not attached because `create_tree` was blocked twice by the tool-policy layer. Both blocks occurred before creation of a functional tree or movement of `main` beyond the prewrite head.

No partial EJR mutation occurred.

## Required continuation

Next gate: `P2 EJR COLLISION-SAFE ALLOCATION GATE`.

Candidate replacement IDs must prove vacancy across:

`metadata → H1 → filename → Git history`

before allocation.

Priority 2 remains OPEN. Global and phase-wide holds remain unchanged.
