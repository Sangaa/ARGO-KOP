# MUTATION MATRIX — EJR-212 → EJR-415 IDENTITY REPAIR 273

Status: PREWRITE / EXECUTION NOT AUTHORIZED YET
Transaction ID: MUT-2026-08-31-P2-EJR-212-TO-415-IDENTITY-REPAIR-273
Opening main: `a23c7cf7702125978a7991b8db5dbe642e12e311`
Execution role: HERMUZ

## Authority

Lease272 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE and established:
- earlier Memory EJR-212 allocation is RETAINED;
- later root EJR-212 relationship-graph record is DISPLACED but legitimate;
- EJR-415 is VACANT across complete reachable history and reserved solely for this displaced root allocation.

Vacancy evidence: run `33381701808`, artifact `9753986473`, digest `sha256:84cadea292e357fee6e8b490d7e19cfd585d54ee6ab5f9214579444ee825616c`, history_complete=true, current_claims=[], historical_claims=[], decision=VACANT.

## Fresh prewrite hard-gate evidence

At opening main:
- source `EJR/EJR-212_P2_CURRENT_RELATIONSHIP_GRAPH_RECONCILIATION_2026-08-17.md` exists with blob `13ab0b94c8530498fcf86e5bcdf818a1167e1675`;
- retained `Memory/Engineering_Journal/EJR-212_2026-08-14_P29_SESSION_CLOSURE.md` exists with blob `e0c49458311fc277eb1022ed29b2511882f468ff`;
- target `EJR/EJR-415_P2_CURRENT_RELATIONSHIP_GRAPH_RECONCILIATION_2026-08-17.md` is absent (404);
- exact old member-path search returns zero consumers;
- current exact-ID search shows only historical/census references and the later EJR-400 narrative reference; no executable or governed consumer requires synchronous rewrite.

## Authorized functional mutation

Exactly one identity-bearing root record may be repaired:
1. retain Memory EJR-212 byte-for-byte;
2. remove old root EJR-212 path;
3. create `EJR/EJR-415_P2_CURRENT_RELATIONSHIP_GRAPH_RECONCILIATION_2026-08-17.md`;
4. change only first H1 identity `# EJR-212 — ...` → `# EJR-415 — ...`;
5. preserve all remaining body/date/status/relationship evidence byte-for-byte;
6. perform zero consumer rewrites unless a fresh executable/governed exact-path consumer appears immediately before mutation.

## Expected census effect

Current deterministic MEMORY_TO_ROOT baseline is 22. Resolving this one ambiguity is expected to reduce observed cohort membership 22→21 while the baseline remains 22 at the repair head. If the repair-head Internal Document-ID audit is otherwise clean and the sole incompleteness is `__COHORT_COUNT_DRIFT__`, normalize baseline 22→21 only in a separate successor lease. Any other incompleteness blocks normalization.

## Exclusions

No mutation to retained Memory EJR-212, EJR-400 narrative history, classifier logic, tests/workflows, GOV/REP authority, unrelated EJR, or Global Integrity. Historical narrative text is not rewritten merely to cosmetically replace old IDs.

## Verification contract

Before functional mutation, rediscover live main and repeat source blob / Memory blob / target absence / consumer checks. After mutation:
- exact compare must show only the EJR rename/H1 replacement plus this Matrix update;
- old root path absent, new root path present, retained Memory blob unchanged;
- Full-Stack and Internal Document-ID exact-head evidence must be inspected;
- baseline normalization, if justified, must be a separate successor lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
