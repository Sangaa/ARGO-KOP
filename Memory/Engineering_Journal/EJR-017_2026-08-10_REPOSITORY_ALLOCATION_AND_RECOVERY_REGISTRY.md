# EJR-017 — Repository Allocation & Recovery Registry

Date: 2026-08-10
Status: Active / Learning Evidence

## Trigger

During Phase 1 review it became clear that review traceability alone was not enough. ARGO needed a technical mechanism that could answer where an artifact belongs, what repository state was last reviewed, whether it became dirty, and how a future session can resume or recover without repeating completed work.

## Decision Implemented

Created `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` as the canonical specification for:

- logical repository partitions;
- artifact allocation/state;
- current vs last-reviewed identity comparison;
- dirty/revalidation detection;
- checkpoint classification;
- file/domain/session/repository recovery;
- build-session resume;
- mutation-to-checkpoint flow;
- explicit Phase 1 closure control.

Updated `REP-011` to make the review ledger and allocation/recovery registry complementary rather than overlapping.

## Important Boundary

REP-012 is currently a **partial registry specification**, not a claim that every repository artifact has already been allocated and checkpointed.

Initial deployment status remains:

`PARTIAL REGISTRY / RECONSTRUCTION REQUIRED`

Existing files must be populated incrementally during Phase 1 review.

## Learning

The repository now separates three questions that were previously easy to mix:

1. **Where is the artifact and what state is it in?** — REP-012
2. **What review evidence exists and what was actually checked?** — REP-011
3. **What does the artifact mean and who has semantic authority?** — Domain-specific canonical authorities

This separation is intended to prevent both duplicated effort and accidental authority inflation.

## Recovery Principle

A commit proves that a repository state existed. It does not prove semantic correctness.

A recovery checkpoint therefore preserves both the state and its uncertainty classification.

## Phase 1

No folder or domain is closed by this entry. Remaining content remains open until explicit `CLOSED_FOR_PHASE_1` evidence exists.

---

End of Entry
