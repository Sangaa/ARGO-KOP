# Full Stack Audit — Gap Classification

The repository-wide audit produces candidates, not automatic architectural verdicts.

| Gap | Meaning | Default severity |
|---|---|---|
| ORPHAN_CANDIDATE | Implementation has no discovered incoming local reference | REVIEW |
| UNTESTED_CANDIDATE | Runtime source area has no discovered sibling test | HIGH |
| BROKEN_REFERENCE | Reference points to a missing local target | CRITICAL |
| UNREACHABLE_PATH | Component exists but cannot be traced into the connected spine | HIGH |

## Rule

A candidate must be reviewed against architecture and intent before remediation.

The audit is a discovery instrument, not an autonomous deletion or refactoring engine.
