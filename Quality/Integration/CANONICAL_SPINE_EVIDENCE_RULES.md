# Canonical Spine Evidence Rules

## Purpose

Provide a conservative bridge between repository evidence and the Canonical Spine Gap Map.

## Rule

The scanner may infer only:

- `PARTIAL` when evidence for both endpoint concepts exists;
- `MISSING` when one or both endpoint concepts are not discovered.

It must **never** infer `CONNECTED` from keyword presence.

## Why

A repository containing files named `Decision` and `Execution` does not prove that Decision output is actually consumed by Execution.

`CONNECTED` requires the stronger evidence contract already defined by the Canonical Spine Coverage Map:

1. source;
2. destination;
3. data/state contract;
4. executable or synthetic test evidence;
5. traceability evidence.

## Status

This scanner is evidence discovery, not architectural validation.
