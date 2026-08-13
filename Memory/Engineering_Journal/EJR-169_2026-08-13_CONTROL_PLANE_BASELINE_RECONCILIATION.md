# EJR-169 — Control-Plane Baseline Reconciliation Finding

**Date:** 2026-08-13  
**Repository:** `Sangaa/ARGO-KOP`  
**Branch:** `main`  
**Status:** Finding Confirmed / Repair Pending  
**Authoritative Development Baseline:** 3.2.1

## Finding

The current authoritative version source `Release/VERSION.md` declares Development Baseline `3.2.1`.

The active control-plane contains at least one additional stale/higher baseline declaration: `REP-012` currently declares `3.3.0`, while `REP-016` also declares `3.3.0`.

This confirms the previously identified `REP-016` drift is not isolated to a single control-plane artifact. The discrepancy must be reconciled across the complete `REP-011..016` control-plane set before any baseline-sensitive closure claim.

## Evidence

- `Release/VERSION.md` — authoritative current development baseline: `3.2.1`.
- `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` — current header declares `3.3.0`.
- `Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md` — current header declares `3.3.0`.
- `REP-011` defines cross-registry consistency and current-fitness requirements for the control plane.
- `REP-016` requires reconciliation of `REP-011 ↕ REP-012 ↕ REP-013 ↕ REP-014 ↕ REP-015 ↕ REP-016` before closure review.

## Interpretation

A higher version number in a control-plane document does not establish authority. The designated version authority remains `Release/VERSION.md` until a governed release/development-baseline transition explicitly supersedes it.

Therefore `3.3.0` in REP-012/REP-016 is currently treated as **stale or unexplained baseline evidence**, not as the current repository baseline.

## Action

No blind mass rewrite was performed.

The next controlled repair must:

1. inspect the complete `REP-011..016` set;
2. determine which baseline declarations are stale versus intentionally historical;
3. update only those proven inconsistent with current authority;
4. commit one material change at a time;
5. re-read after each mutation;
6. reconcile the control-plane after the repairs;
7. preserve historical evidence where required.

## Impact

This finding directly affects session recovery, control-plane freshness, and the proposed Master Relationship Matrix seed. The matrix must record baseline authority as a relationship/evidence property rather than trusting a file's local version header.

## Engineering Learning

> **Baseline is a relationship property, not merely a local metadata field.**

A file can be structurally valid and internally consistent while still being stale relative to the authoritative repository baseline. Future matrix validation should therefore resolve `artifact → version authority → current baseline → last-reviewed baseline` as an explicit chain.

## Integrity Decision

`INTEGRITY HOLD` remains active.

---

End of Document
