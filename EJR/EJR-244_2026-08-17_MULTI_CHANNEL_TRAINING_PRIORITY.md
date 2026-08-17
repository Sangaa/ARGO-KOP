# EJR-244 — Multi-Channel / Multi-Task Training Priority

Date: 2026-08-17  
Status: `CLOSED / ARCHITECTURE-PRIORITIZED / FIRST SAFE SCOPE DEFINED`

## Scope
Evaluate the proposed training path for operating multiple logical test channels concurrently and prepare ARGO for future multi-platform / multi-user intake.

## Evidence Reviewed
- `Runtime/RUN-013_CONTROLLED_HANDOFF.md` provides a single controlled handoff boundary but does not establish multi-task or multi-user isolation.
- `Quality/Integration/GEN-001_ELEVENTH_RULE_TEST.md` establishes bounded generation testing but is single-test scoped.
- `GOV-016` requires material failures to become classified, verified, reusable learning.
- `CORE-011` establishes generative capability but does not itself provide concurrency/orchestration safety.

## Decision
The request is **valuable and should not be rejected**.

Priority: `P2 — Strategic Training Track / Medium-High`.

It should not displace current integrity blockers or verified safety gates, but it should be started early enough to build the architectural discipline required before real multi-platform inputs arrive.

## Recommended Ladder
1. `M1` One User / Multi-Task / Read-Only fixture simulation.
2. `M2` One User / Multi-Task / isolated proposal-write simulation.
3. `M3` Multi-Task controlled reconciliation and conflict handling.
4. `M4` Multi-User / Multi-Task isolation, authorization and fairness.
5. `M5` Multi-Source / Multi-Platform intake with provenance and schema separation.

## First Safe Build
Start with **2 isolated logical tasks in one session**, each using an independent fixture/report channel. No canonical writes are permitted.

The first gate should prove:
- task/channel identity isolation;
- context isolation;
- independent traces;
- failure containment;
- deterministic or explicitly recorded scheduling;
- no mutation authority.

## Why It Is Strategically Valuable
The test trains the exact boundaries required for future simultaneous feeds from several AI platforms or users:

`Parallel Work ≠ Shared Authority`

The main value is not throughput. It is proving that ARGO can work in parallel without collapsing provenance, context, authorization or evidence boundaries.

## Risks / Controls
Do not begin with real multi-user concurrency, external connectors or canonical writes. These introduce unnecessary variables before isolation has been proven.

Do not equate parallel execution with correctness. Each channel remains independently verified before reconciliation.

## Knowledge Transfer
This decision is reusable architectural guidance. It is stored in:
`Runtime/Prototype/MULTI_CHANNEL_MULTI_TASK_TRAINING_CONTRACT.md`

## Next Safe Checkpoint
Implement `M1` as a deterministic, fixture-driven harness and prove it with two simultaneous logical task channels before expanding scope.

---

End of EJR-244
