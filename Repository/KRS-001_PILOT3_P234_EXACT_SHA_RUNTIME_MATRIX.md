# KRS-001 Pilot 3 — P234 Exact-SHA Runtime Matrix

Status: `PRE-WRITE / OPEN`
Protocol: `GOV-013 / GOV-014`
Base SHA: `7762e434149956482f0e0c85efd19db97c4e60b4`
Selected contract blob: `37a78805de9f26c66bf84e080c14db83b5ebc544`

## Gate
The selected contract is `Runtime/Prototype/PROTOTYPE_INTEGRATION_CONTRACT.md`. Existing generic harness execution cannot establish runtime evidence for this exact source identity.

## Controlled Action
Use one isolated HERMUZ branch only for the evidence-producing test. Do not mutate `main` during the test. The test must consume the selected contract at its exact blob identity and emit traceable evidence tied to that identity.

## Acceptance
- exact source blob recorded;
- executable consumer recorded;
- execution result recorded;
- trace/artifact identity recorded;
- no external side effect;
- no production promotion.

## Failure / Hold
If exact-SHA consumption cannot be established, classify `RUNTIME-EVIDENCE-ABSENT / NOT ESTABLISHED`; do not infer from generic test success.

## Closure
Read back this matrix after write. Record the execution branch/resulting SHA in the subsequent closure before any merge or production claim.
