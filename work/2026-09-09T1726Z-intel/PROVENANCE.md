# Findings provenance

The S1–S4 findings YAMLs in this directory were produced by the sub-agents of
the stood-down fire `2026-09-09T0410Z-intel` (Sonnet 5, ~04:13–04:23Z today),
which ran Phase 1 research but never reached Phase 6 (no run record on
origin/main; newest published run at session start was 2026-09-08T0411Z-intel).
The operator handed the sub-agent returns to this fire (`2026-09-09T1726Z-intel`)
to complete. This fire re-fetched every WILL-PUBLISH primary in its own Phase 4
deep read (guard #9 exception), re-ran the mechanical KEV sweep for its own 39 h
window (result: identical two uncovered Windows zero-days), dedup'd against the
14-day prior-coverage index, and put every candidate through the full gate +
Phase 5.7 verifier before publishing. No Phase 1 sub-agents were re-spawned:
the 04:10Z research is ~13 h old, the KEV sweep confirmed no newer strong signal,
and the dominant items (Sept 8 Patch Tuesday, WeWorm, NovoCure attribution) are
all fully captured in the handed returns.
