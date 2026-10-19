# Coverage re-sweep — shared brief (quality audit 2026-10-18T1307Z-audit)

You are a defensive threat-intelligence researcher re-researching a past window **as if for the first time**, so the audit can diff what you find against what was published. Your definition's full contract applies (timestamps, link discipline, discovery traces, source ledger, findings YAML, compact return). This file adds only the audit specifics.

- **Run id:** `2026-10-18T1307Z-audit` — checkpoint into `work/2026-10-18T1307Z-audit/`.
- **Today:** 2026-10-18 (UTC), now ≈ 13:30Z.
- **Window:** 2026-09-30T06:39Z → 2026-10-18T13:07Z, so `window_hours: 440`. Every record in your slice carries `lookback_hours: 440`: sweep each publisher's listing across the **whole window by date**, not just its newest posts. Drop items whose freshest source predates 2026-09-30.
- **Slice:** the JSON file named in your spawn message (`work/2026-10-18T1307Z-audit/slice-<DOMAIN>.json`) — each record carries `id`, `publisher`, `url`, `rss_url`, `tier`, `fetch_method`, `reliability`, `language`, `health_cmd` and its newest recipe note. Essential records first, then the rest in file order. Every record gets a `source_ledger` row.
- **Dedup context:** `work/2026-10-18T1307Z-audit/prior_coverage.json` covers entries active since 2026-10-04 only; for anything dated 2026-09-30 to 2026-10-04 also check `state/cves_seen.json` and grep the store (`grep -ril "<CVE id or distinctive name>" entries/2026-09-2* entries/2026-09-30 entries/2026-10-*`). `entities/registry.yaml` for canonical names. **Still return a covered item when the published entry misses a material development or states something your primary contradicts** — mark it `update_target: <entry id>` with what is new or wrong. Otherwise skip covered items (list them by id under `covered:` so the diff is auditable).
- **What to return:** everything that clears the inclusion gate in your definition's domain mission for the Swiss public-sector constituency, with discovery traces and verbatim evidence. Also return borderline items you judged out, marked `borderline: true` with the reason: the audit documents correctly-droppable items.
- **URL-liveness ledger:** `work/2026-10-18T1307Z-audit/url-liveness.tsv`.
- **Watchlist duty:** none configured in this deployment (send the sweep line as `duty=none`).
- **Progress:** append one line per slice record finished to `work/2026-10-18T1307Z-audit/<DOMAIN>.progress`.
- Write `findings.<DOMAIN>.yaml` first, then `<DOMAIN>.ended_at`, then return the compact summary. No time limit; nobody answers questions mid-run.
