# P9 Architecture — ARC-006 / ARC-007 / ARC-011 Dependency-Integration Alignment — Transaction H

Transaction ID: `MUT-2026-09-03-P9-ARC006-ARC007-ARC011-DEPENDENCY-INTEGRATION-H`
Priority: `9 — Architecture`
State: `PRE-WRITE / TARGET MUTATIONS NOT YET APPLIED`
Entry HEAD: `938cc599daf48a80dfdaa1d95aa4abd4657ffe18`
Protocol: `GOV-013 / GOV-014 / GOV-014A / GOV-015 / GOV-016`

| Target | Action | Expected change | KEEP / preservation | Pre-write | Post-write |
|---|---|---|---|---|---|
| `Architecture/ARC-006_DEPENDENCY_MODEL.md` | bounded canonical dependency alignment | Explicitly bind dependency direction to ARC-011; add ARC-011 Related Document; minimal version/audit refresh | Exact dependency hierarchy, allowed/prohibited dependencies, integration/authority boundaries | PASS | PENDING |
| `Architecture/ARC-007_INTEGRATION_MODEL.md` | bounded canonical integration alignment | Explicitly bind responsibility/dependency flow to ARC-011 while retaining ARC-006 operational dependency contract; add ARC-011 Related Document; minimal version/audit refresh | Integration requirements, external/repository/memory/runtime/project boundaries, validation gate | PASS | PENDING |

Evidence boundary:
- Architecture status names ARC-011 current canonical authority for structural boundaries and dependency direction.
- ARC-006 and ARC-007 mirror that direction but leave canonical authority implicit.
- The two targets form one bounded dependency/integration boundary; no layer, dependency, interface, authorization, or lifecycle semantic is added/removed/reordered.
- No Architecture partition closure, Global Connected Baseline closure, or Global Integrity PASS is claimed.

Validation plan:
`immutable read-back of both targets → exact matrix-head/final-material compare → exact-head required CI → close or preserve failure`.
