# EJR-158 — Active Architecture Baseline Drift

**Date:** 2026-08-13
**HEAD reviewed:** `61831c315c10615df1a0c75717ca96981caf1439`
**Status:** OPEN — ACTIVE DRIFT CONFIRMED

## Authority

`Release/VERSION.md` is the authoritative version reference and currently declares Development Baseline `3.2.1` and Latest Official Release `1.0.0`.

## Folder-level evidence

Direct reads of active Architecture artifacts show that the following documents still declare Development Baseline `3.3.0`:

- `Architecture/ARC-006_DEPENDENCY_MODEL.md`
- `Architecture/ARC-007_INTEGRATION_MODEL.md`
- `Architecture/ARC-009_ARCHITECTURE_DECISIONS.md`
- `Architecture/ARC-010_EVOLUTION_MODEL.md`
- `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md`

Other active Architecture artifacts inspected (`ARC-002`, `ARC-003`, `ARC-004`, `ARC-005`, `ARC-008`) already declare `3.2.1`.

## Classification

This is now a confirmed **active metadata drift** inside the Architecture domain, not merely a historical occurrence. These five documents are active architecture controls and their baseline field is intended to describe the current development baseline.

The finding is distinct from historical `3.3.0` occurrences elsewhere in the repository; those remain subject to the EJR-157 classification process and must not be mass-rewritten.

## Repair plan

1. Update only the five active Architecture artifacts listed above from `3.3.0` to `3.2.1`.
2. Refresh their audit date to the current audit date when the content is revalidated.
3. Add a regression gate that compares active Architecture baseline metadata to `Release/VERSION.md`.
4. Run Architecture/Integration CI.
5. Re-read all five artifacts after the write.
6. Re-run the repository-wide audit and independently verify any resulting negative findings.

## Safety rule

No version-history, journal, template, model, runtime, or archived occurrence of `3.3.0` will be changed by this repair unless its own authority and active-consumer status are independently established.

## Session checkpoint

The next session may resume at the five-file targeted repair above. Architecture remains `INTEGRITY HOLD` until the repaired files, folder status, map, repository index and cross-layer references pass validation.
