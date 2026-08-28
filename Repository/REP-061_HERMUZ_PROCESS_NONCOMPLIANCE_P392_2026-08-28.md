# REP-061 — HERMUZ Process Non-Compliance Review — P392

Date: 2026-08-28
Status: `CLOSED / VERIFIED / DOCUMENTED / NO CANONICAL MUTATION / NO AUTHORITY PROMOTION`
Protocol: `GOV-013`

## PURPOSE
Record and correct a process-compliance deviation identified during review of P391 → P392. This is not a new architectural learning; the relevant prior learning already existed and was not enforced as the mutation gate.

## CLASSIFICATION
`PRIOR-LEARNING APPLICATION FAILURE`

The deviation was not caused by missing knowledge. P391 already recorded:
- `CI absence = NO RUN`, not PASS or FAIL;
- exact-head evidence is mandatory;
- candidate gaps must not become mutations automatically;
- documentation cannot upgrade evidence authority;
- the next checkpoint was to obtain observable CI on exact HEAD before repair.

## DEVIATION
After P391 reported `NO RUN / UNOBSERVED` for exact mutation `99f35c0...`, HERMUZ inferred that the governed execution channel itself was the bottleneck and mutated `.github/workflows/full-stack-audit.yml` before fully exhausting non-mutating observation options.

The resulting mutation was technically bounded and isolated, but the decision gate was premature.

## ROOT CAUSE
1. Pattern anchoring on earlier CI-channel bottlenecks.
2. Correct technical diagnosis was promoted to an immediate mutation without first proving that observation-only paths were exhausted.
3. Prior learning was recognized but not converted into a hard pre-mutation gate.
4. The distinction between `execution-channel diagnosis` and `authorized mutation condition` was not maintained tightly enough.

## CORRECTIVE RULE
Before any mutation whose stated purpose is to resolve `NO RUN` / missing execution evidence:

`NO RUN → enumerate observation-only paths → execute/verify those paths → prove insufficiency → define mutation → mutate → exact-head observation`

`NO RUN` alone never authorizes mutation.

## CURRENT EVIDENCE
The subsequent governed PR execution on merge ref `fa4c646...` completed successfully. The P391 focused regression executed with `4 passed`, and the Full-Stack Repository Audit plus Runtime Prototype/Integration workflow completed successfully.

However, the execution ref is the generated PR merge ref, not a standalone direct execution of PR head `e3f6426...`. Therefore the evidence must remain attribution-aware until reconciled under GOV-013.

## BOUNDARY STATE
- Main: unchanged
- Canonical authority: unchanged
- Governance authority: unchanged
- Runtime production semantics: unchanged
- B07: execution evidence obtained, final attribution reconciliation pending
- B08: unproven
- REL-009 promotion: not justified
- PR #64: open / unmerged

## LEARNING DISPOSITION
No new KD is claimed for the root deviation. The corrective action is an application correction to existing knowledge.

The new factual observation that the governed PR merge-ref path now executes P391 is recorded as evidence, not elevated to architectural learning until attribution reconciliation is complete.

## CLOSE
`CLOSED / VERIFIED / PRIOR-LEARNING APPLICATION FAILURE RECORDED / CORRECTIVE RULE ESTABLISHED / NO CANONICAL MUTATION / NO AUTHORITY PROMOTION`

## NEXT CHECKPOINT
`Reconcile PR merge-ref execution identity with PR-head evidence → close B07 only if GOV-013 attribution criteria are satisfied → then design the minimum controlled B08 observation.`
