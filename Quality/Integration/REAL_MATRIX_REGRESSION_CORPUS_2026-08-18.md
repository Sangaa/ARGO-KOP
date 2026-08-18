# Real Mutation Matrix Regression Corpus — 2026-08-18

Status: `PROTOTYPE / DATA-DRIVEN / INTEGRITY HOLD`
Authority: `GOV-014 + GOV-015 + GOV-016`

## Purpose

Run semantic Mutation Matrix validation against several real repository matrices without encoding the matrix set as workflow YAML logic.

## Initial Corpus

1. `Repository/MUT-2026-08-17-REP001-001_MUTATION_MATRIX.md`
2. `Repository/MUT-2026-08-17-REP001-002_MUTATION_MATRIX.md`
3. `Repository/MUT-2026-08-17-AUDIT-RECON-001_MUTATION_MATRIX.md`
4. `Repository/MUTATION_MATRIX_AUDIT_2026-08-17.md` as reconciliation evidence, not as a mutation matrix input.

Historical audit evidence confirms that REP-001-001 and REP-001-002 were closed with authoritative Git and Matrix evidence, while REL-003 was separately remediated through a dedicated retrospective Matrix. fileciteturn960file0L2-L6

## Execution Design

The runner must:

- load a declared list of real Matrix paths from versioned data;
- validate each Matrix independently;
- report per-Matrix result and failure classification;
- aggregate results without hiding individual failures;
- remain independent of workflow YAML matrix semantics;
- reuse the existing semantic validator without granting mutation authority.

## Current Boundary

This corpus is a test asset only. It must not perform canonical writes or interpret semantic completeness as proof that the underlying mutation decision was correct.

## Promotion Path

`Prototype Corpus → Multi-Variant Verified Corpus → Reusable Regression Asset → Default CI Dataset`

Promotion requires successful validation over multiple real variants and failure-learning analysis for every exception.

---

End of Document
