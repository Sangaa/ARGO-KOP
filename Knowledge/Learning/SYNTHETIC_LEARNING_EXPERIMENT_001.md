# Synthetic Learning Experiment 001 — Executable Function

## Objective

Turn the first synthetic programming fixture into observable practical evidence.

## Source Concepts Under Test

- reusable function;
- parameters as inputs;
- returned value;
- clear responsibility;
- predictable behavior.

## Experiment

Implement a deliberately small function:

```python
def add(a, b):
    return a + b
```

## Observations

Expected observations:

- `add(2, 3)` returns `5`;
- changing the inputs changes the result predictably;
- the function has one clear responsibility.

## Validation

The experiment must include both a passing and a deliberately failing expectation so that predictable behavior is demonstrated rather than assumed.

## Learning Boundary

This experiment validates the source concepts. It does not establish that every function should be small, pure, or single-purpose; those would require broader evidence.

## Promotion Input

The resulting evidence may be submitted to the Learning Promotion Gate as a candidate. It is not canonical knowledge by itself.
