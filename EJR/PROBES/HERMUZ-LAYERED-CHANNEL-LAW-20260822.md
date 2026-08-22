# HERMUZ Layered Channel Law Probe

Diagnostic-only probe. Not production evidence.

Marker: HERMUZ-LAYERED-CHANNEL-LAW-20260822-THETA

Experiment layers:
1. Connectivity: read known canonical file.
2. Write: create this marker on isolated branch.
3. Direct observation: read marker from exact branch/ref.
4. Blind repository search: search for marker and related distinctive terms.
5. Change surface: observe commit and PR.
6. Execution surface: observe workflow/run evidence available from the same change.
7. Side-effect analysis: inventory every newly observed surface and trace it back to the operation that produced it.
8. Cleanup: remove marker only after observations complete.

Hypothesis: a single operation may create observable effects across multiple surfaces; each surface must be classified by causal relation rather than assumed to be incidental.
