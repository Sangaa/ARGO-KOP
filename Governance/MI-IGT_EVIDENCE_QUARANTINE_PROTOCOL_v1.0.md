# MI-IGT EVIDENCE QUARANTINE PROTOCOL v1.0

Status: `GOVERNED / EXECUTION-READY / NOT-AUTHORITY`

## Purpose
Prevent contaminated, stale, or ambiguously independent IGT observations from entering the learning evidence pool.

## Evidence States
- `UNSEEN` — no run evidence.
- `CAPTURED` — raw run record exists but qualification is incomplete.
- `QUALIFIED` — independence and leakage gates pass.
- `QUARANTINED` — evidence exists but cannot support promotion.
- `INVALIDATED` — evidence is contradicted, contaminated, or baseline-invalid.

## Automatic Quarantine Triggers
1. Critical independence dimension is `UNKNOWN` or `NO`.
2. Source conclusion was exposed before prediction.
3. Baseline SHA cannot be established.
4. Shared mutation occurred without re-baselining.
5. Relationship validation is missing after an affected mutation.
6. Run outcome depends on an unverified session-memory claim.
7. The novel transformation is only a renamed source case.

## Invalidation Rule
A later-discovered contamination can retroactively invalidate a previously captured result. The original record MUST remain; invalidation is appended, never silently erased.

## Promotion Rule
Only `QUALIFIED` evidence may enter promotion analysis. Multiple `CAPTURED` or `QUARANTINED` runs do not accumulate into independent evidence.

## Preservation
Quarantined/invalidated evidence remains searchable for learning about failure modes. It must not be counted as positive transfer evidence.

`AUTHORITY = NONE`
