# EJR-297 — HERMUZ Blind Law Prediction Test

Date: 2026-08-22
Status: CLOSED / DIAGNOSTIC LEARNING CAPTURED
Classification: Architectural Learning / Observation-Surface Law
Production impact: NONE (probe marker cleaned)

## Prior-learning gate
Reviewed EJR-293, EJR-294, EJR-295, EJR-296, Issue #11, and Issue #21 before experimentation.

## Hypothesis
If a repository phenomenon is created by a write, different observation surfaces should expose different parts of its state. In particular, direct content read may succeed even when repository search does not immediately expose the same marker.

## Controlled experiment
A unique marker `HERMUZ-BLIND-LAW-PROBE-20260822-Ω17` was written as a temporary repository file. The write returned commit `876b5480e2e7fed1527005f8799052155e41a0e4`.

Prediction before observation:
1. direct repository read should be able to retrieve the marker;
2. repository search may or may not expose it immediately because search indexing is a distinct observation surface;
3. the write should create a commit trace;
4. cleanup should be possible by deleting the marker.

## Observations

- Direct `fetch_file` immediately returned the exact marker and blob SHA `0f389040b753ee6e373b195fc1cfbf9ca5f6aeaa`.
- Repository `search` for the exact unique marker returned no result.
- The file was therefore observable through direct contents retrieval but not through the search surface at that moment.
- The marker was deleted successfully, producing cleanup commit `dbc0fe5dde8b3a64b9ce050b10091965074494da`.

## Learning

The hypothesis was partially confirmed and refined. Observation surfaces have different semantics and timing. A failed search result is not equivalent to absence of the object. Direct retrieval is stronger evidence of current existence than a negative search result when search indexing freshness is unknown.

Revised rule:

`Negative search result -> UNKNOWN / INDEXING-BOUNDARY until corroborated by an authoritative direct observation.`

And more generally:

`Observation result = function(world state, surface semantics, indexing/visibility, identifier knowledge, timing)`

## Failure learning

The probe was created on the default branch rather than an isolated probe branch. This was an execution-discipline defect in the experiment setup. It was immediately cleaned up and caused no production semantic change. Future probes must create the isolated branch first unless the protocol explicitly requires a main-branch observation.

## Architectural implication

ARGO should distinguish at minimum:
- authoritative direct object observation;
- search/index observation;
- historical/derived documentation;
- execution evidence;
- connector capability/exposure.

A negative result from one surface must not suppress investigation through another surface.

## P6 impact
No P6 logic, relationship, runtime evidence, or governance state was promoted.

## Closure
Experiment closed after direct read verification and cleanup. The result is reusable as a self-diagnostic law for future repository investigations.

End of EJR-297
