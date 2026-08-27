# MI-IGT INDEPENDENCE ATTESTATION v1.0

Status: `GOVERNED / EXECUTION-READY / NOT-AUTHORITY`

## Purpose
Prevent false independent-validation claims when multiple sessions or instances share repository state, prompts, conclusions, or artifacts.

## Independence Is Multi-Dimensional
A run MUST establish, where applicable:

1. **Execution independence** — distinct execution context/instance.
2. **Information independence** — source conclusion is not disclosed before prediction.
3. **State independence** — transformed/novel case is not merely a renamed source case.
4. **Temporal independence** — the run occurs after the source evidence and records its own baseline.
5. **Mutation independence** — no untracked prior mutation is silently attributed to the current run.

A different window alone is insufficient.

## Attestation Fields
- Source evidence ID:
- Run ID:
- Execution context:
- Baseline ref/SHA:
- Novel transformation:
- Source conclusion withheld: `YES / NO`
- Prior mutation detected: `YES / NO / UNKNOWN`
- Independent context justified: `YES / NO`
- Independence result: `PASS / FAIL / INCONCLUSIVE`
- Evidence locations:

## Decision Rule
If any critical dimension is `NO` or `UNKNOWN`, independence is not established. The IGT outcome must be `INCONCLUSIVE` for promotion purposes.

## Non-Claims
This attestation does not establish learning, persistence, broad generalization, model-weight change, or governance authority. It only establishes whether the run qualifies as an independent evidence event.

`AUTHORITY = NONE`
