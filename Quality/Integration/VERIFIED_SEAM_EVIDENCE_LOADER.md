# Verified Seam Evidence Loader

The loader is the bridge from the repository itself into the Verified Seam Evidence Registry.

It accepts a candidate only when all three referenced local artifacts exist:

```text
Contract + Test + Trace
        ↓
Registry
        ↓
CONNECTED
```

Missing artifacts are not synthesized. The loader simply excludes the incomplete candidate.

## Boundary

The loader checks artifact existence only. It does not claim that the artifacts are semantically correct; that remains the responsibility of the integration audit and human/architectural review.
