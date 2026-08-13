# EJR-157 — Architecture Folder Version Drift Review

**Date:** 2026-08-13
**HEAD reviewed:** `bb02a646666baed4d3656cb73f7e59843da12654`
**Status:** OPEN — DRIFT INVENTORY CAPTURED

## Scope

Review the Architecture domain as a folder: map, active ARC artifacts, folder status, release authority, and repository consumers. The objective is to distinguish genuine stale-version drift from historical or intentionally preserved content before editing anything.

## Evidence

- `Architecture/ARC_MAP.md` now reports Development Baseline `3.2.1`, Latest Official Release `1.0.0`, Map Version `1.3.2`, and Last Audit `2026-08-13`.
- `Architecture/_FOLDER_STATUS.md` remains `INTEGRITY HOLD` and explicitly keeps cross-reference, layer, dependency, canonical-model, and cross-layer validation open.
- Repository search for `3.3.0` still returns references in multiple domains outside Architecture, including Models, Templates, Runtime, and historical Engineering Journal material.
- Therefore the Architecture map correction must not be treated as a repository-wide version migration.

## Classification

The current evidence establishes **version drift candidates**, not blanket defects. A `3.3.0` occurrence can be:

1. active stale metadata;
2. a historical record;
3. an example/template value;
4. a superseded artifact that must remain recoverable;
5. a genuinely stale consumer of the active baseline.

## Decision

Do not mass-rewrite `3.3.0` occurrences. Each active consumer must be classified against `Release/VERSION.md` and its owning domain before modification.

## Next verification pass

Prioritize active non-journal consumers in this order:

1. Repository/registry artifacts;
2. Architecture consumers;
3. Runtime/Services/AI operational READMEs;
4. Models/Templates used to generate or validate current artifacts;
5. Historical Engineering Journal / Archive — preserve unless explicitly migrated.

Every confirmed active stale consumer will receive a targeted repair and regression coverage where executable validation exists.

## Session checkpoint

This record is the resumption point for the next pass. It intentionally leaves the Architecture domain on `INTEGRITY HOLD` until cross-layer reconciliation is complete.
