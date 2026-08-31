# MUTATION MATRIX — EJR-232 → EJR-412 IDENTITY REPAIR 262

Status: PREWRITE / REPAIR-PENDING
Transaction ID: MUT-2026-08-31-P2-EJR-232-TO-412-IDENTITY-REPAIR-262
Opening main: `4eb1b97036677797eca9002ac75f4b8d4d84d4f2`
Source disposition: `MUT-2026-08-31-P2-EJR-232-DISPOSITION-AUTHORIZATION-260.md`
Vacancy authority: `MUT-2026-08-31-P2-EJR-412-REPLACEMENT-VACANCY-PROOF-261.md`

## Pre-write evidence

- Lease260 retained the earlier Memory EJR-232 and classified the later root EJR-232 displaced.
- Lease261 is CLOSED / EXECUTION-VERIFIED and proves EJR-412 historically vacant across complete reachable history; EJR-412 is reserved for exactly one bounded replacement allocation.
- Current root source was re-read from main at blob `207b1450767460145a4a5ce6840582479e1dc2dc`.
- Prior Repair257 is DIRECTLY APPLICABLE: preserve the semantic body/date/chronology, mutate only the displaced root record path and H1 identity, preserve the current census baseline inside the repair lease, and handle deterministic cohort-count drift in a separate successor lease.
- Current exact old-member path search finds only `Repository/MUT-2026-08-31-P2-EJR-232-DISPOSITION-AUTHORIZATION-260.md`; that reference is historical disposition/provenance evidence and MUST remain unchanged.
- Broader GOV-015 semantic search finds governance/index material about GOV-015, but no direct executable/operational consumer that requires the old root EJR-232 identity.
- Direct executable/operational consumer obligations established for the displaced root member: zero.

## Functional mutation specification

| Surface | Before | Authorized Lease262 change | Expected repair-head state |
|---|---|---|---|
| Memory EJR-232 | retained valid earlier allocation | NONE | unchanged |
| Root old path | `EJR/EJR-232_2026-08-17_GOV-015_EXECUTION_DOCUMENTATION_KNOWLEDGE_TRANSFER.md` | REMOVE as part of one atomic tree mutation | absent |
| Root successor path | absent | CREATE `EJR/EJR-412_2026-08-17_GOV-015_EXECUTION_DOCUMENTATION_KNOWLEDGE_TRANSFER.md` | present |
| Root H1 | `# EJR-232 — ...` | change H1 identity only to `# EJR-412 — ...` | EJR-412 |
| Root semantic body/date/chronology | current source body | PRESERVE byte-for-byte except H1 identity | preserved |
| Historical disposition/path references | provenance evidence | NONE | unchanged |
| Direct executable consumers | zero established | NONE | zero rewrites |
| MEMORY_TO_ROOT expected baseline | 25 | NONE in Lease262 | remains 25 |
| Classifier/audit logic | current | NONE | unchanged |
| Global integrity | HOLD | NONE | HOLD |

## Preservation boundary

Lease262 MUST NOT:
- modify the retained Memory EJR-232;
- rewrite historical Lease260/261 evidence;
- alter GOV-015 governance content or indexes merely because they discuss the same semantic subject;
- change `EXPECTED_GROUP_COUNT` inside this repair lease;
- modify census classifier logic/tests;
- allocate any identity other than the already-proven EJR-412;
- promote Priority 2, Phase 1, or Global Integrity.

The root source footer/body, including historical text such as `End of EJR-232`, is semantic body and remains preserved under the execution-verified Repair257 precedent; only path and H1 record identity are mutated.

## Expected validation behavior

Because the repair resolves one MEMORY_TO_ROOT ambiguity while Lease262 intentionally preserves baseline 25, an Internal-ID/census channel may legitimately report deterministic cohort-count drift `expected=25 / observed=24` at the exact repair head. Such a failure, if and only if all identity/chronology/provenance stages pass and the sole incompleteness is cohort-count drift, is repair evidence rather than permission to alter the repair transaction. Baseline correction belongs to a separate successor lease.

## Pre-write decision

`PREWRITE GATE = PASS`

Next: re-read this matrix from current main and require applicable push CI success. Then open the Lease262 execution record before performing the single atomic root path/H1 identity mutation.
