# EJR-173 — Current-main Revalidation Handoff

## Result

PR #5 was validated against an older merge base (`6abfd40...`) while current `main` is now `598a523...`. Its two integration failures are not Runtime regressions:

- CORE-000 assertion is a stale formatting contract.
- REP-013 assertion was executed against a stale merge snapshot; current `main` contains the expected specification path.

Therefore PR #5 must not be merged or used as the final revalidation candidate.

## Next candidate

Create the Runtime authorization-state candidate directly from current `main` `598a523...`.

Intended mutation only:
- remove unreachable `State.REJECTED`;
- retain `HOLD` for missing human authorization;
- remove unreachable `REJECTED` branch in state selection;
- do not alter Integration tests;
- do not alter CORE-000 or REP-013 to satisfy stale assertions.

## Evidence status

- PR5-CI-001: FAIL, root cause identified.
- Prototype tests: PASS.
- Integration: 78 PASS / 2 FAIL.
- Current main REP-013: canonical specification path present.
- Current main CORE-000: line-separated metadata form present.
- Integrity: HOLD.
