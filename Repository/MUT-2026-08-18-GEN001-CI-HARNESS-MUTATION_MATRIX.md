# GEN-001 Candidate-001 CI Harness Mutation Matrix

Transaction ID: `MUT-2026-08-18-GEN001-CI-HARNESS-001`
Protocol: `GOV-014 v1.0.1`
Scope: Add deterministic Candidate-001 reuse regression to existing Full-Stack CI only.

## Source

Target: `.github/workflows/full-stack-audit.yml`
Source Blob SHA: `73cce0c89da71668215f39860af9fbf8eb076532`

## Intended Changes

| Change ID | Target | Action | Expected State | Applied | Verified |
|---|---|---|---|:---:|:---:|
| GEN001-CI-001 | Full-Stack workflow | ADD | One deterministic step invoking `Quality/Integration/test_gen001_candidate001_reuse.py` after semantic regression and before current-change enforcement | N | N |

## KEEP / Preservation

All other workflow content is `KEEP`.

Required conditions:

- Trigger configuration unchanged.
- Existing P4 gates unchanged.
- Existing Mutation Matrix presence/semantic regression unchanged.
- Existing three real Matrix variants unchanged.
- Existing audit, runtime evidence and artifact upload steps unchanged.
- No new workflow file.
- Unexpected changes = 0 except the single approved step addition.

## Boundary

This mutation only wires an already-versioned deterministic regression into the existing Full-Stack CI. It does not alter Candidate-001 semantics, authority, runtime behavior, or relationship promotion.

## Post-Commit

Re-read the workflow and inspect the resulting CI job steps. Candidate-001 becomes CI-verified only if the new step completes successfully inside an authoritative workflow run.

---

End of Matrix
