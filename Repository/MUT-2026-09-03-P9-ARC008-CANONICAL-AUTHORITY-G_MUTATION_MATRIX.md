# P9 Architecture — ARC-008 Canonical Authority Correction — Transaction G

Transaction ID: `MUT-2026-09-03-P9-ARC008-CANONICAL-AUTHORITY-G`
Priority: `9 — Architecture`
State: `PRE-WRITE / TARGET MUTATION NOT YET APPLIED`
Entry HEAD: `15c924a3384ca5bc111f0e5fe47986394ca4acd3`
Protocol: `GOV-013 / GOV-014 / GOV-014A / GOV-015 / GOV-016`

| Target | Action | Expected change | KEEP / preservation | Pre-write | Post-write |
|---|---|---|---|---|---|
| `Architecture/ARC-008_REPOSITORY_LAYOUT.md` | bounded stale-authority correction | Replace stale statement that active architecture is represented by ARC-001 with current canonical ARC-011 authority; retain ARC-001 as platform architecture surface; add ARC-011 Related Document; refresh audit/version minimally | Repository-layout principles, physical-vs-logical distinction, nine-layer model, Repository authority, connected-baseline hold | PASS | PENDING |

Evidence boundary:
- Architecture folder status explicitly states ARC-011 is the current canonical Architecture Model for structural boundaries and dependency direction.
- ARC-008 currently states `The active architecture is represented by ARC-001`, creating a stale competing authority interpretation.
- ARC-001 remains a valid platform architecture document and is not deprecated or removed.
- No layer/dependency/repository structure is changed; no partition/global closure is claimed.

Validation plan:
`immutable target read-back → exact parent compare → exact-head required CI → close or preserve failure`.
