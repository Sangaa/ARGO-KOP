# MUTATION MATRIX — P7 CORE-KERNEL → RUN-009 VALIDATION — N

Transaction: `MUT-2026-09-01-P7-CORE-KERNEL-RUN009-VALIDATION-N`
Work Lease: `HERMUZ-P7-N-CORE-KERNEL-RUN009-20260901`
Priority: `7 — Core cross-layer validation`
State: `PRE-WRITE / LEASE ACTIVE / VALIDATION-FIRST`
Entry HEAD: `6c22cc9d9d04f8d62f1b44e2f6cbac3175b12cea`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Boot-proof record

- Repository: `Sangaa/ARGO-KOP`
- Branch/ref: `main`
- Live HEAD independently rediscovered twice before first write: `6c22cc9d9d04f8d62f1b44e2f6cbac3175b12cea`
- `PROJECT_BOOTSTRAP.md`: loaded from live HEAD.
- Current control surfaces re-read: REP-001, REP-002, REP-011, REP-014, REP-016, REP-020 current manifest, Core folder status.
- Current checkpoint: Transaction M closed/resume-safe at live HEAD.
- Exact-head CI state: four required workflows present and successful for live Entry HEAD.
- Global queue: Phase 1 OPEN; Priority 7 Core OPEN; global integrity HOLD.
- Current Core status: `CROSS-LAYER VALIDATION OPEN`; Folder Certification pending.
- Mutation scope: bounded validation evidence only; no source-authority or relationship-registry mutation in N.

## Reconstructed highest-value legal action

Current direct evidence shows:

1. `Core/ARGO_KERNEL.md` explicitly says recovery follows the applicable governed recovery flow.
2. The same canonical Kernel artifact lists `Runtime/RUN-009_RECOVERY.md` under `Related Authority`.
3. The Kernel dependency boundary explicitly warns that a name appearing in the document does not establish dependency merely by being listed.
4. `Runtime/RUN-009_RECOVERY.md` defines the governed Runtime recovery mechanism and does not directly identify `CORE-KERNEL` as a dependency, consumer, implementation or reverse authority.
5. `REP-014` v1.2.12 registers `CORE-KERNEL → RUN-001 = REFERENCES` but contains no `CORE-KERNEL → RUN-009` relationship.
6. Current Core status requires continued material dependency/consumer validation before certification review.

Therefore N validates the bounded candidate only:

`CORE-KERNEL → RUN-009 = REFERENCES / INTENTIONAL ONE-WAY / RECOVERY-HANDOFF-ALIGNED / NON-DEPENDENCY`

N does not register the relationship.

## Prior-learning retrieval and classification

- Transaction E `CORE-KERNEL → RUN-001 = REFERENCES` — `DIRECTLY APPLICABLE`: same source artifact, same explicit Related Authority pattern, same non-dependency warning, same one-way restraint.
- Transaction L validation-first authority seam — `DIRECTLY APPLICABLE`: prove direct current source semantics before registry mutation.
- Transaction M registry reconciliation and R1 recovery — `TRANSFERABLE`: preserve proven source assertions and do not rewrite evidence merely to satisfy tests.
- Transaction J/K one-way documentary discipline — `TRANSFERABLE`.
- Historical broad runtime coupling assumptions — `HISTORICAL / SUPERSEDED` for this bounded seam unless rebound to current source evidence.

## Authorized material change set

Exactly three paths in one material commit after this pre-write Matrix:

1. `Quality/Integrity/test_core_kernel_run009_recovery_boundary.py` — create focused validation-first regression.
2. `Repository/P7_CORE_KERNEL_RUN009_RECOVERY_SEAM_2026-09-01_N.md` — create execution/evidence record.
3. This Matrix — rebind to the exact material candidate and post-write state in the same material commit.

## Required assertions

The focused test must verify current direct source evidence:

- Kernel identity and recovery-handoff language.
- `Runtime/RUN-009_RECOVERY.md` present in Kernel `Related Authority`.
- Kernel dependency-boundary warning that textual/name appearance does not itself establish dependency.
- RUN-009 canonical recovery identity and safe-resume semantics.
- REP-014 intentionally has no N relationship row yet.
- No reverse `RUN-009 → CORE-KERNEL` relationship is manufactured.
- No `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES` or `GOVERNS` promotion between this pair.
- Core remains `CROSS-LAYER VALIDATION OPEN`; Folder Certification pending.

## KEEP / non-authority

- No mutation to `Core/ARGO_KERNEL.md`.
- No mutation to `Runtime/RUN-009_RECOVERY.md`.
- No mutation to `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`.
- No mutation to REP-020 current manifest or Core folder status in validation-only N.
- No dependency, executable reachability, consumer, implementation or reverse relationship claim.
- No Core/Runtime certification.
- No Phase-1 closure, Connected Baseline closure, repository-wide graph closure or Global PASS.

## Verification contract

`PRE-WRITE MATRIX → ONE ATOMIC 3-PATH MATERIAL COMMIT → EXACT-HEAD READ-BACK → DIFF-SCOPE CHECK → REQUIRED 4-WORKFLOW CI → LEARNING ASSESSMENT → LEASE CLOSE → CLOSURE-HEAD CI`

Any source contradiction, unexpected path expansion, main movement, failed required gate or evidence ambiguity stops N and is preserved under GOV-016.
