# Execution Trace Contract

## Purpose

Define the canonical record created after an experimental execution run.

## Required Identity

- `trace_id`
- `task_id`
- `session_id`
- `recorded_at`
- `record_type`

## Required Outcome

- `final_status`
- `side_effect`
- ordered `stages`

## Memory Boundary

Execution traces are historical observations. They must not be treated as active state, current knowledge, authorization, or pending action unless a later governed process explicitly promotes information from the trace.

## Safety

A trace records whether a side effect occurred; it does not create permission to perform one.
