# MUTATION MATRIX — EJR-232 → EJR-412 IDENTITY REPAIR 262

Status: FUNCTIONAL MUTATION APPLIED / VERIFICATION PENDING
Transaction ID: MUT-2026-08-31-P2-EJR-232-TO-412-IDENTITY-REPAIR-262
Opening main: `4eb1b97036677797eca9002ac75f4b8d4d84d4f2`
Pre-write matrix commit: `e0b592dfbe16496a34cd2febb376cc705637ee34`
Execution lease commit: `6ea9da1edf70025e986bfe480435a54146bfaa47`
Source disposition: `MUT-2026-08-31-P2-EJR-232-DISPOSITION-AUTHORIZATION-260.md`
Vacancy authority: `MUT-2026-08-31-P2-EJR-412-REPLACEMENT-VACANCY-PROOF-261.md`

## Pre-write evidence retained

- Lease260 retained the earlier Memory EJR-232 and classified the later root EJR-232 displaced.
- Lease261 is CLOSED / EXECUTION-VERIFIED and proves EJR-412 historically vacant across complete reachable history; EJR-412 is reserved for exactly one bounded replacement allocation.
- Immediately before the functional mutation, main remained `6ea9da1edf70025e986bfe480435a54146bfaa47`; the old root source re-read at blob `207b1450767460145a4a5ce6840582479e1dc2dc`, and the exact successor path returned 404.
- Prior Repair257 is DIRECTLY APPLICABLE: preserve the semantic body/date/chronology, mutate only the displaced root record path and H1 identity, preserve the current census baseline inside the repair lease, and handle deterministic cohort-count drift in a separate successor lease.
- Current exact old-member path search established only the historical Lease260 disposition reference; it remains unchanged as provenance evidence.
- Direct executable/operational consumer obligations established for the displaced root member: zero.

## Functional mutation reconciliation

| Surface | Before | Applied Lease262 state |
|---|---|---|
| Memory EJR-232 | retained valid earlier allocation | unchanged / retained |
| Root old path | `EJR/EJR-232_2026-08-17_GOV-015_EXECUTION_DOCUMENTATION_KNOWLEDGE_TRANSFER.md` | removed in the atomic repair tree |
| Root successor path | absent / vacancy-proven | created as `EJR/EJR-412_2026-08-17_GOV-015_EXECUTION_DOCUMENTATION_KNOWLEDGE_TRANSFER.md` |
| Root H1 | `# EJR-232 — ...` | changed to `# EJR-412 — ...` |
| Root semantic body/date/chronology | source blob `207b1450767460145a4a5ce6840582479e1dc2dc` | preserved byte-for-byte except H1 identity |
| Historical disposition/path references | provenance evidence | unchanged |
| Direct executable consumers | zero established | zero rewrites |
| MEMORY_TO_ROOT expected baseline | 25 | unchanged at 25 inside Repair262 |
| Classifier/audit logic | current | unchanged |
| Global integrity | HOLD | HOLD |

## Preservation boundary

Lease262 did not modify the retained Memory EJR-232, historical Lease260/261 evidence, GOV-015 governance/index semantics, census classifier logic/tests, any unrelated identity, or Global Integrity state.

The root source footer/body, including historical text `End of EJR-232`, remains preserved under the execution-verified Repair257 precedent; only path and H1 record identity changed.

## Expected repair-head validation behavior

The repair resolves one MEMORY_TO_ROOT ambiguity while Lease262 intentionally preserves baseline 25. Therefore an Internal-ID/census channel may legitimately report deterministic cohort-count drift `expected=25 / observed=24` at the exact repair head. Such a result is acceptable only if identity/chronology/provenance stages are otherwise clean and the sole incompleteness is cohort-count drift. Baseline correction belongs to a separate successor lease.

## Verification pending

Functional completion now requires:
1. exact post-write read-back of old path absence, successor path/H1/body, and retained Memory EJR-232;
2. exact commit diff confirmation;
3. post-mutation CI and audit evidence;
4. classification of any expected cohort-count drift before opening a separate baseline-sync successor lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
