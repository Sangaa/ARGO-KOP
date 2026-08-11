# Synthetic Reuse Experiment 001

## Objective

Test whether promoted knowledge can be retrieved and used in a second task without silently expanding its scope.

## Prior Knowledge

The promoted record establishes the tested behavior of `add(a, b)`.

## Second Task

A new task asks the learner to reason about a function that accepts two inputs and returns a predictable result.

## Required Behavior

1. Retrieve only promoted knowledge.
2. Preserve the original provenance.
3. Use the retrieved record as evidence, not as an unquestionable universal rule.
4. Record the new task observation separately.

## Contradiction Test

A deliberately contradictory observation must not overwrite the promoted record. It must enter the correction/demotion review path.

## Success Criteria

The experiment succeeds if ARGO can:

- reuse the promoted knowledge;
- identify its scope;
- distinguish reuse from new evidence;
- preserve the old record;
- trigger review when contradiction is detected.
