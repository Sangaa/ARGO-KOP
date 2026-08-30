# MUT-2026-08-30-P2-ID-AUDIT-PARSER-180

**Status:** PREWRITE / LEASE ACTIVE / HARD-HOLD REPAIR
**Baseline:** `main@9ab30264e937885833c814b850a58d21c77dd82a`
**Parent evidence:** `Repository/MUT-2026-08-30-P2-ID-AUDIT-COVERAGE-179.md`

## Gap proved before mutation

Priority-2 audit expansion 179 executed and the GitHub Actions run `33290249900`, job `99200522544`, failed only at `Run internal Document-ID audit`; M2 succeeded on the same HEAD.

Direct source inspection proves the expanded heading fallback is over-broad: `PROJECT_STATUS.md` declares `Document ID: PROJECT_STATUS`, while its human title begins `# ARGO KOP — Current Project Status`. The generic heading regex accepts the token `ARGO` as a document identity, producing an explicit-vs-heading identity conflict that is a parser false positive rather than a repository identity collision.

## Repair hypothesis

Preserve namespace independence while requiring a structural document-ID shape for H1 fallback. A heading identity candidate must contain a namespace token followed by a numeric document sequence (for example `REL-001`, `GOV-013A`, `BOOTSTRAP-001`) instead of accepting any uppercase title word. Explicit `Document ID:` remains the primary identity source.

## Allowed paths

- `Quality/Integration/internal_document_id_audit.py`
- `Quality/Integration/test_internal_document_id_audit.py`
- new bounded Repository evidence / learning / closure records for 179-180

## Forbidden paths

- `Core/**`
- `Governance/**`
- `Runtime/**`
- `Engine/**`
- `Services/**`
- `Interfaces/**`
- `Knowledge/**`
- `Release/**`
- `Repository/REP-001_*`
- `Repository/REP-002_*`
- `Repository/REP-014_*`
- `Repository/ROOM071_CURRENT_STATE.json`
- branch deletion or ref mutation

## C1-C6 collision gate

- **C1 path collision:** PASS — new transaction path is unique.
- **C2 semantic collision:** PASS — repair changes detector grammar only; no document identity is rewritten.
- **C3 authority collision:** PASS — no release/baseline/governance authority is changed.
- **C4 promotion collision:** PASS — no knowledge or domain status promotion is authorized by this lease.
- **C5 evidence collision:** PASS — diagnosis is based on direct source plus failed workflow step; no search-hit count is treated as proof.
- **C6 handoff collision:** PASS — 179 is in HARD HOLD and explicitly requires root-cause analysis plus minimal repair before further promotion.

## Verification contract

1. Add a regression test proving a human H1 such as `ARGO KOP` cannot override explicit `PROJECT_STATUS` identity.
2. Add/retain a test proving a previously unseen structural namespace can still be discovered without an allowlist.
3. Run the repository's internal Document-ID audit through CI.
4. Verify M2 on the repair HEAD.
5. Verify Full-Stack and Runtime/Integration checks where triggered/available for the repair HEAD before any broad closure claim.
6. On any failure: HARD HOLD → first meaningful failure → root cause → minimal repair only.

## Learning candidate

`GENERIC PARSING != UNCONSTRAINED PARSING`

A generic detector should generalize the *grammar of identity*, not accept arbitrary surface text as identity.
