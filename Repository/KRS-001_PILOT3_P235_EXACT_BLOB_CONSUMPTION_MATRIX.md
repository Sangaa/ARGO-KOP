# KRS-001 Pilot 3 — P235 Exact Blob Consumption Matrix

Status: `PRE-WRITE / OPEN`
Branch: `hermuz/p234-safe-gate`
Source contract blob: `37a78805de9f26c66bf84e080c14db83b5ebc544`

| Gate | Requirement | Result |
|---|---|---|
| Source identity | Consumer must bind to the exact contract blob | PENDING |
| Consumer path | Existing harness must demonstrate actual artifact consumption | FAIL — current harness accepts payload directly |
| Side effects | No external I/O | PASS by source inspection |
| Evidence | Execution result must identify consumed blob | PENDING |

## Decision
Do not execute the current harness as an exact-SHA test. It cannot prove artifact consumption. Any implementation change requires a separately justified mutation and post-write closure.

## Non-Goals
No schema change, no production integration, no main mutation, no fabricated runtime evidence.
