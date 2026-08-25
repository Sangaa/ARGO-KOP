# MUT-2026-08-25-KRS001 — Session Closure & Currentness Gate

Status: CONTROLLED / EXECUTED
Authority: GOV-013 / BOOTSTRAP-001

## Objective
Make the new currentness-first reconciliation workflow and deterministic session closure path explicit before structural migration.

## Required Outcomes
- Every HERMUZ session starts from current repository evidence.
- Legacy/canonical artifacts are not treated as current evidence without currentness checks.
- Historical truth remains preserved during structural migration.
- Every session closes with an exact checkpoint and mandatory next target.

## KEEP
GOV-013 remains the operating contract. BOOTSTRAP-001 remains mandatory authority. Existing production safety boundaries and evidence classifications remain unchanged.

## DO NOT
- rewrite the whole repository;
- mark legacy content current without reconciliation;
- treat canonical status as proof of current validity;
- promote synthetic seams to production evidence;
- create a new model merely to avoid reconciling the existing one.

## Verification Gate
After write, re-read the new plan and this matrix from the current repository, confirm their current commit/ref, then use them to drive the next session. No mass migration is authorized by this matrix.
