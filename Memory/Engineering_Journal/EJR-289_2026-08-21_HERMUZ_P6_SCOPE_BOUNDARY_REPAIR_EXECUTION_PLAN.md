# EJR-289 — HERMUZ P6 Scope Boundary Repair — Execution Plan

## Status
OPEN — EXECUTION IN PROGRESS / PLAN PRESERVED

## Trigger
User explicitly requested that the complete P6 Scope Boundary Repair procedure be preserved in the repository so the repair cannot be lost across sessions, and instructed HERMUZ to continue execution under GOV-013.

## Problem Being Repaired
The P6 correlator currently conflates two independent questions:

1. whether a changed path can be correlated to canonical repository evidence;
2. whether that path is actually within P6 correlation scope.

This produced `EJR/** → UNMAPPED → PARTIAL` even though the repository had not established an authoritative EJR scope policy. EJR-284 and EJR-285 established this as a governance-policy gap rather than proof of a missing relationship. Issue #15 remains open for the eventual governance decision.

## Canonical Repair Design
P6 is to be separated into three ordered layers:

`Changed Path → Scope / Eligibility → Correlation → Execution Evidence → Evidence Classification`

### Layer 1 — Scope / Eligibility
Canonical artifact:
`Repository/P6_SCOPE_ELIGIBILITY_REGISTRY.md`

Allowed states:
- `IN_SCOPE`
- `OUT_OF_SCOPE`
- `UNRESOLVED`

Current EJR policy state:
`UNRESOLVED`

The correlator must emit `POLICY_UNRESOLVED` for an unresolved path and must never reinterpret it as `UNMAPPED`, `MAPPED`, `PARTIAL`, `OUT_OF_SCOPE`, or a relationship state.

### Layer 2 — Correlation
The correlator must perform mapping only after eligibility is resolved:
- `IN_SCOPE + mapping` → `MAPPED`
- `IN_SCOPE + no mapping` → `UNMAPPED`
- `OUT_OF_SCOPE` → `NOT_APPLICABLE`
- `UNRESOLVED` → `POLICY_UNRESOLVED`

The correlator must not invent governance policy from missing evidence.

### Layer 3 — Execution / Semantic Evidence
The following remain independent:
- `EXECUTION_VERIFIED`
- `CANONICAL_MAPPING_VERIFIED`
- `RELATIONSHIP_VERIFIED`

CI/runtime/synthetic evidence cannot silently promote one class into another.

Evidence maturity remains bounded:
`UNIT → CONTROLLED_SYNTHETIC → CANONICAL_REPOSITORY → INTEGRATION → RUNTIME`

## Required Implementation Sequence

1. **Materialize scope contract** — completed as Step 01.
2. **Modify `Quality/Integration/ci_impact_correlation.py`** to load the canonical scope registry and evaluate eligibility before correlation.
3. **Add/extend regression tests** for `IN_SCOPE`, `OUT_OF_SCOPE`, and `UNRESOLVED`, including a hard regression preventing `UNRESOLVED → MAPPED/PROMOTED`.
4. **Add canonical repository integration tests** that read the real `P6_SCOPE_ELIGIBILITY_REGISTRY.md`, `REP-020`, and `REP-014`, rather than relying only on synthetic fixtures.
5. **Verify execution evidence boundaries** so execution PASS cannot become mapping or relationship verification.
6. **Run the affected regression/integration suite**, then the applicable full-stack audit/workflow when available.
7. **Re-read all changed artifacts and validate affected indexes/relationships.**
8. **Document learning and checkpoint evidence.**
9. **Only after the repair is verified, return to Issue #15 for the governance decision on EJR scope.**
10. **Do not modify REP-020 merely to suppress the former PARTIAL result.**

## Explicit Non-Goals
This repair must NOT:
- decide whether EJR is ultimately in-scope or out-of-scope;
- add speculative REP-020 mappings;
- promote relationships;
- change runtime semantics;
- treat synthetic evidence as canonical evidence;
- infer CI success as relationship verification;
- rewrite P6 wholesale when a bounded mutation is sufficient.

## GOV-013 Execution Discipline
Every material mutation follows:
`Pre-check → Change → Re-read → Relationship/Index Validation → Integration/Regression Validation → Checkpoint Evidence`

Negative findings must be independently rechecked before being treated as repository defects. Repository reality outranks conversation memory.

After each coherent command/work group, record the result and closure/checkpoint evidence. Do not create artificial progress or claim PASS from commit creation alone.

## Current Evidence
- `EJR-284`: documented the original policy gap and prohibited unsafe mapping/classifier fixes.
- `EJR-285`: converted the gap into governance Issue #15 and kept implementation blocked pending policy resolution.
- `EJR-288`: materialized `P6_SCOPE_ELIGIBILITY_REGISTRY.md` with EJR=`UNRESOLVED`.
- Current correlator inspection confirms it still performs direct mapping before scope evaluation and currently has no scope-registry consumption.
- Issue #15 remains open; no governance decision has been inferred.

## Current Checkpoint
Step 01 contract materialization is complete. The next safe mutation is the correlator implementation, followed immediately by canonical regression coverage.

## Learning Candidate
`Correlation absence is not policy absence.`
A correlation engine must not infer eligibility from missing mappings. Scope must be evaluated first, and unresolved policy must remain a first-class result.

This is recorded as candidate learning until the repair is validated and the learning-promotion gate is satisfied.

---

End of EJR-289
