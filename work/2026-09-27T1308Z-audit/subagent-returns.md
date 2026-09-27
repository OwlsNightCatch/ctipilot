# Sub-agent return telemetry and reported dispositions — 2026-09-27T1308Z-audit

The run record's `sub_agents:` blocks are populated **verbatim from each sub-agent's return**
(`prompts/cti-run.md` Phase 5 § Run-record telemetry). Some values a sub-agent reports in its
return are not repeated inside its own findings YAML, so this file records them where a later
reader can check what the run record was built from. Where a sub-agent gave an approximate
figure, it is reproduced as approximate here and should be read that way in the run record too.

## Research re-sweeps

| Agent | webfetch | websearch | bridge | sources attempted / used | items |
|---|---|---|---|---|---|
| G1 | 0 | 10 | ~28 | 22 / 8 | 5 |
| G2 | 1 | 27 | 28 | 14 / 3 | 4 |
| G3 | 0 | 7 | ~55 | 32 / 16 | 18 |

G1 and G2 also carry a `self_telemetry` block inside their own `gap-G*.yaml`. **`gap-G3.yaml`
does not**, so G3's `websearch_calls` and `bridge_fetches` in the run record come from its return
message alone and its `bridge_fetches` was reported as approximate ("~55"). Its
`sources_attempted: 32`, `sources_used: 16` and `items_returned: 18` are independently
reproducible from that file's own `publisher_reachability` block (32 publishers, 16 with
in-window posts) and `items` list (18).

## Items G2 reported reaching and gating below the inclusion bar

These were named in G2's return rather than written into `gap-G2.yaml`, which carries only the
items it returned as candidate gaps. They are recorded here so the audit report's
"correctly droppable" line has a checkable basis:

- **heise-sec** (feed plus two drill-downs fetched): an AusweisApp certificate revocation, and a
  German phone-fraud takedown. Both judged below the relevance bar.
- **cert-pl** (RSS fetched): one Poland toll-fraud research post inside the window, judged
  outside G2's incident-and-region domain.
- **sec-disclosures-edgar** (EDGAR full-text search for Item 1.05 8-K filings in the window):
  one hit, Astrana Health, judged below the bar as a US healthcare incident with no Swiss or EU
  public-sector nexus and no novel technique.

## Truth passes

| Batch | webfetch | websearch | bridge | urls checked | entries |
|---|---|---|---|---|---|
| truth-A | 0 | 0 | ~8 | ~40 | 14 |
| truth-B | 0 | 0 | unreported | unreported | 16 |
| truth-C | 0 | 0 | ~3 | ~30 | 14 |
| truth-D | 0 | 0 | 17 | 17 | 10 |

truth-B reported no transport counts; the run record records them as `unknown` rather than
inventing a figure.
