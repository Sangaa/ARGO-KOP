# P10 Runtime — Knowledge Correction Evidence Gate — Transaction H

Transaction ID: `MUT-3-P10-RUNTIME-KNOWLEDGE-CORRECTION-H`
Priority: `10 — Runtime`
Gate: `12 — Runtime ↔ Knowledge / Memory`
State: `PRE-WRITE / OPEN`
Entry HEAD: `406cc2a1349467a4d26bf2fe871e3de50e38c15a`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / GOV-014A / GOV-016 / REP-011 / REP-016`

## Preserved failure finding

The tracked Runtime context pipeline delegates contradiction handling to `Knowledge/Learning/knowledge_correction.py`. Current implementation can emit `DEMOTION_REVIEW_REQUIRED` when:

- evidence is empty or malformed;
- the record has no stable task identity;
- the record is not in `PROMOTED` state;
- the contradiction flag is a truthy non-boolean value.

This does not directly mutate Knowledge, but it opens a governed state-change review without the minimum evidence/identity/state proof required by the Knowledge lifecycle and Evidence Feedback Loop.

Classification: `REAL TRACKED RUNTIME→KNOWLEDGE FAIL-CLOSED REVIEW-GATE GAP`.

## Authorized mutation

| Change ID | Target | Action | Expected change | KEEP / preservation | Pre-write | Post-write |
|---|---|---|---|---|:---:|:---:|
| P10-H-01 | `Knowledge/Learning/EVIDENCE_FEEDBACK_LOOP.md` | UPDATE | define explicit evidence, promoted-state, identity and boolean contradiction minimums | no silent overwrite; review-only boundary | PASS | PENDING |
| P10-H-02 | `Knowledge/Learning/knowledge_correction.py` | UPDATE | fail closed before demotion review when state, identity, evidence or contradiction signal is invalid | NO_CHANGE behavior and no mutation | PASS | PENDING |
| P10-H-03 | `Knowledge/Learning/test_knowledge_correction.py` | UPDATE | add negative evidence/state/identity/signal coverage | existing positive cases | PASS | PENDING |
| P10-H-04 | `Runtime/Context/test_runtime_context_pipeline.py` | UPDATE | prove Runtime consumer receives HOLD instead of unsupported review | existing retrieval/correction flow | PASS | PENDING |
| P10-H-05 | `Quality/Integrity/test_runtime_p10_knowledge_correction_boundary.py` | CREATE | bind Runtime consumer, Knowledge gate and immutable promoted record behavior | no demotion execution/authority | PASS | PENDING |
| P10-H-06 | `Repository/REP-011_PRIORITY10_RUNTIME_KNOWLEDGE_CORRECTION_ADDENDUM_2026-09-03_H.md` | CREATE | record failure, repair and independent holds | historical records unchanged | PASS | PENDING |
| P10-H-07 | this Matrix | UPDATE IN MATERIAL CHANGE SET | bind pre-write/material evidence | scope and non-claims | PASS | PENDING |

## Non-claims

- `DEMOTION_REVIEW_REQUIRED` remains a proposal for review, not a demotion mutation.
- The repair does not grant Runtime authority over Knowledge.
- This transaction repairs one Runtime→Knowledge consumer; Gate 12 and Priority 10 remain OPEN.
- Gate 13, executable-promotion hold, Phase 1, repository-wide graph, Global Connected Baseline and Global Integrity remain open/hold.

Validation:
`pre-write matrix → atomic contract/code/test/addendum/matrix repair → local read-back → exact-head four-family CI → close or HOLD`.
