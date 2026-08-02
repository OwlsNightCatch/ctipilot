---
name: Reader-credential outage — what breaks and what to do
description: The blast radius when every jina key is exhausted, and the correct source-lifecycle response
type: project
---

# Reader-credential outage — what breaks and what to do

Observed 2026-08-02: `python3 tools/fetch_source.py jina-usage` reported **all four pooled keys `exhausted` with large negative balances**. The last-resort rung of the fetch ladder was down for an entire run.

## Blast radius (8 sources lost in one run)

Two classes go dark:
- **Sources pinned `fetch_method: jina`** because their listing is JS-hydrated or WAF-blocked — `ico-uk`, `ccn-cert-es`, `prodaft`.
- **Sources whose bridge recipe silently falls back to the reader** — `cisa-advisories`, `cisa-directives`, `cisa-news` (Akamai 403s every direct UA), plus `sysdig` and `trellix` (unrendered SPA shells).

The one that matters most: **the CISA advisories and directives listings have no other transport.** CISA KEV is safe — it has its own `cisa-kev` api subcommand that does not touch the reader — so exploited-vulnerability ground truth survives, but the general advisory channel is fully dark.

## Correct response

- **Never demote for this.** An exhausted credential is a transport/billing failure, not source death, exactly like a 403. Record the diagnosis in the source's `notes` and leave it in rotation.
- **Probe direct alternatives before writing it off**, and record what you tried. On this run: ICO returns HTTP 200 to a browser UA but exposes no dated enforcement hrefs (the hydration problem that caused the pin), and `/rss` paths 404; the FBI alerts pages 403 direct. Neither has a live alternative while the reader is down.
- **This needs the operator.** No in-pipeline fix restores credit. Surface it in the run record's coverage notes *and* push a notification — it silently degrades every subsequent run until topped up.

## Related: probe-target mismatches masquerading as recipe breaks

`source_health.py` probes `url`. When a publisher blocks its *directory index* while the documented per-item recipe works, the sweep reports a `needs-demote` that does not exist. Fixed 2026-08-02 by adding an optional **`probe_url`** field that overrides the probe target (`source_health.py` honours it; `check_run.py` requires fields rather than rejecting extras, so adding one is safe). Worked example: `siemens-productcert-csaf` — the CSAF directory and all four CSAF discovery files (`changes.csv`, `index.txt`, `.well-known/csaf/provider-metadata.json`, the ROLIE feed) 403 every UA, while `url .../csaf/ssa-NNNNNN.json` returns the full document. Pointing `probe_url` at a stable per-advisory document turned a recurring false flag into `bridge-ok`.
