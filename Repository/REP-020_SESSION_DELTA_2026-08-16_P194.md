# REP-020 — SESSION DELTA P194

Platform: ARGO KOP
Checkpoint: P194
Status: Active / Integrity Hold
Predecessor: P193

## Objective
Correct the consolidated audit so it consumes the repository's actual materialized verified-registry records instead of assuming a single top-level registry JSON file.

## Discovery

The repository uses materialized per-seam registry records under:

`Quality/Integration/evidence/runtime/*_verified_registry.json`

Records exist in two compatible shapes: a single seam record and a mapping keyed by seam. The existing verified loader already validates these records against local Contract/Test/Trace artifacts.

The previous consolidated audit incorrectly looked only for:

`Quality/Integration/verified_seam_evidence_registry.json`

which is not the repository's actual registry storage model. This was a real audit-integrity defect: the consolidated report could undercount verified evidence even when the loader/audit boundary had valid materialized records.

## Safe Mutation

Updated:

- `Quality/Integration/canonical_spine_consolidated_audit.py`
- `Quality/Integration/test_consolidated_canonical_spine_audit.py`

The consolidated audit now:

1. discovers only materialized `*_verified_registry.json` records under the governed runtime-evidence directory;
2. normalizes both supported registry shapes;
3. passes the records through the existing `verified_seam_evidence_loader`;
4. passes the loader result into the existing conservative canonical audit;
5. reports the number of verified registry records actually loaded;
6. keeps `Learning Pipeline -> Verified Registry` outside the 11-seam Canonical Spine;
7. preserves `Authorization -> Execution` as governed unless independently evidenced.

## Verification

Updated audit commit:
`f54b948589377eaaa7e3111ac999950cc6179fe8`

Updated regression test commit:
`6b712e31336d0133ba23ac30e5ca616c0de19d47`

Both files were re-read after mutation. CI workflow runs are not yet observable for the new commits, so no CI PASS is claimed.

## Decision

This is a correction of the audit's evidence ingestion path, not a promotion of any seam. It reduces false negatives without weakening the verification boundary.

## Next Priority

Run/reconcile the corrected consolidated audit once CI evidence is available, then build only the highest-value genuine remaining gap. Do not add another evidence wrapper if the corrected audit already establishes the required state.

## Classification

`AUDIT_EVIDENCE_INGESTION_CORRECTED / CI_PENDING`
