# Branch Disposition — hermuz/evolution-guard-p277

Date: 2026-08-29
Lease: `R71-20260829-BRANCH-HYGIENE-048`
Authority: `OPERATIONAL CLASSIFICATION ONLY`

## Evidence

Compared against `main@c94540c2c2bd17053f7fdfaf525590520487bb95`:
- status: diverged;
- ahead_by: 1;
- behind_by: 271;
- merge base: `75e838e5e02d7c1db72ad75a9a4c1029d76a013b`.

Branch-only content consists of:
- `EJR/EJR-333_EVOLUTION_GUARD_ANTI_FREEZE_DECISION.md`;
- `Governance/GOV-018_EVOLUTION_GUARD.md`.

The branch Governance artifact explicitly declares itself `CANDIDATE / NON-CANONICAL` and says promotion requires review. Current main already contains a different `GOV-018` identity owner: `Governance/GOV-018_EVIDENCE_REASONING_AND_CONFLICT_RESOLUTION.md`, also candidate/non-canonical but with the same Document ID. Therefore wholesale merge would reintroduce an identity collision rather than safely promote the evolution-guard idea.

## Disposition

`HISTORICAL_CANDIDATE_LEARNING / GOV018_IDENTITY_COLLISION_WITH_CURRENT_MAIN / NO_WHOLESALE_MERGE / PRESERVE_EJR_PROVENANCE / NO_DELETE_AUTHORIZED`

The anti-freeze reasoning remains useful historical learning, but its branch Governance identity is not a valid current promotion surface. Any future reuse must extract the semantic lesson under a fresh governed identity or integrate it into an already-authorized surface after review.

## Non-claims

- This does not reject the evolution-guard idea on substance.
- This does not promote the branch EJR or Governance file.
- This does not authorize deletion.
- No CI claim is made for this documentation-only classification.

## Learning

A sound candidate rule can still be unsafe to merge when its identity has been independently reassigned. Semantic value and document identity are separate dimensions; preserve the former without reviving the latter collision.
