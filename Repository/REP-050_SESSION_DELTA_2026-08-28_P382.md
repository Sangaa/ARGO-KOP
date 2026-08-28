# P382 — Pull-Request Execution Observation Probe

Date: 2026-08-28
Status: `CLOSED / VERIFIED / ISOLATED / NO RUN / NO CANONICAL MUTATION / NO PROMOTION`
Protocol: `GOV-013`

## RE-ENTRY
Resumed from P381. P381 established `NO RUN` for a controlled push-trigger stimulus even though the repository workflow declares push and pull_request coverage.

## ANALYSIS
The repository already contains a pull_request trigger covering the relevant Runtime/Execution and Quality/Integration paths. Historical repository probes also show that pull_request execution has previously been used as an observation channel. Therefore a fresh, isolated PR is the next justified diagnostic boundary rather than another documentation-only push.

## CONTROLLED ACTION
Created isolated PR #64 from:
`hermuz/p375-rel009-minimal-b07-b08-20260828`

to:
`main`

PR head SHA:
`2a0a0bd12cf21d1c59a8260d2e4d6b37fabd2ba2`

Base SHA at PR creation:
`09b216e403fe99a6f1a4a35e3c3038831398f6a3`

The PR is open, non-draft, and explicitly scoped as an execution-observation probe. No merge was performed.

## OBSERVATION
The exact PR head SHA was queried through the available PR-triggered workflow observation channel.

Result:
`workflow_runs = []`

Therefore PR creation itself did not yield an observable workflow run for the exact head through this channel.

This remains `NO RUN`, not `FAIL`.

## RECONCILIATION
The workflow definition is present on both main and the isolated branch and declares `pull_request` coverage. The absence of a run therefore remains an operational observation gap. The evidence does not identify whether the cause is repository Actions policy, event activation, connector observation limitations, or another platform condition.

No cause is promoted to fact.

## DECISION
- Keep PR #64 open as an isolated observation surface.
- Do not merge it.
- Do not change workflow configuration merely to manufacture a run.
- Do not classify B07 as PASS or FAIL.
- Do not proceed to B08 as though B07 execution were proven.
- Preserve the exact head SHA as the evidence boundary.

## EVIDENCE STATE
- Pull-request creation capability: `PROVEN`
- Exact PR head identity: `PROVEN`
- Workflow pull_request declaration: `PROVEN BY INSPECTION`
- PR-triggered workflow run for exact head: `NO RUN / NOT OBSERVED`
- B07 behavioral execution: `UNPROVEN`
- B07 failure: `NOT ESTABLISHED`
- B08 runtime dispatch: `UNPROVEN`
- Canonical mutation: `NONE`
- Promotion: `NOT JUSTIFIED`

## KNOWLEDGE DELTA
**KD-066 — A successfully created PR is a GitHub lifecycle observation, not evidence that Actions execution occurred.**

**KD-067 — When both push and pull_request stimuli produce no observable run for exact isolated heads, the execution-channel boundary itself becomes the primary diagnostic object; application code should not be modified solely to compensate for missing execution evidence.**

## CHECKPOINT
`P382 → preserve PR #64 as isolated execution surface → independently obtain/restore observable Actions execution → bind run to exact head 2a0a0bd... → execute B07 matrix → inspect jobs/logs → classify → repair only observed defects → B07 closure → B08 controlled observation.`

## CLOSE
`CLOSED / VERIFIED / ISOLATED / NO RUN / NO CANONICAL MUTATION / NO AUTHORITY PROMOTION`
