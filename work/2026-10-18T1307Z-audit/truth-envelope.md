# Retrospective truth pass — shared brief (quality audit 2026-10-18T1307Z-audit)

You are a fact-checker for a defensive threat-intelligence knowledge base. The entries you check are already published; they carry no IOCs and no exploit code by policy. Your job: assume nothing, fetch ground truth, and say for every entry whether it is true as it stands today. This is a **retrospective audit pass**, not a Phase 5.7 iteration: there is no publish verdict to give and no double-CLEAN chain. Read-only: never edit entries, state, registry or sources.

Today is **2026-10-18** (UTC). The audit window is 2026-09-30T06:39Z → 2026-10-18T13:07Z.

## Scope

Every entry file named in your spawn message, read **whole**: frontmatter, main analysis, every `## <Type> — <at>` changelog section and every `updates[]` record. An entry updated after publication is verified as a whole, the new sections included.

## What to check, per entry (fetch the primaries; the entry's own citations are not ground truth on their own)

1. Every `cves[]` id and CVSS against the **per-CVE authority** (vendor PSIRT / per-CVE advisory / the discloser's per-vulnerability page). A multi-CVE roundup, even the same publisher's, is never sufficient. Check which flaw each id names (no positional pairing), `affected` / `fixed` against the vendor's structured table, and `status` (exploited / KEV) against the current CISA KEV record (`python3 tools/fetch_source.py cisa-kev` works in this container) and the vendor's own exploitation statement.
2. Exploitation claims, version boundaries, affected and patched products, victim statements, attribution claims, counts, dates, and every `evidence[]` quote **verbatim** against its cited URL (a contiguous passage, no splicing; translated quotes are checked on `original:`). A "no patch exists" claim must match the vendor's own channel as of today.
3. Every `techniques[]` id is **active** in the pinned dataset `attack/enterprise-attack.json` (now ATT&CK v20.0). Check mechanically, never from memory:
   `python3 -c "import json;d=json.load(open('attack/enterprise-attack.json'))['techniques'];import sys;[print(t, d.get(t,{}).get('name'), 'REVOKED' if d.get(t,{}).get('revoked') else '', 'DEPRECATED' if d.get(t,{}).get('deprecated') else '', 'UNKNOWN' if t not in d else '') for t in sys.argv[1:]]" T1190 T1059.001`
   Also check each id names a behavior the body describes and a source supports.
4. `classification` (Admiralty letter + number) consistent with the sourcing actually present; `verification` value consistent with it; no IOCs (including defanged ones); frontmatter ⇔ body agreement. On an updated entry also: each section's claims against its cited sources; each record's `summary` against its section; the main analysis, title, headline, summary, labelled lines, `actions[]` and `immediate_action` against the entry's own newest section (a sentence a later section disproves is a factual error); a `correction` whose fixed statement is still wrong is a factual error.
5. Relevance and priority only as context: note in `defect` if a `high` or `critical` plainly fails its bar on today's facts (an unexploited flaw in a non-default configuration, an out-of-nexus incident with no vector or actor, a single-victim event older than 30 days), but the truth findings are the deliverable.

## Inputs

- Your **claim ledger**: `work/2026-10-18T1307Z-audit/truth-<BATCH>.ledger.yaml` (one row per claim, every entry of your batch whole). Write one verdict row per claim to `work/2026-10-18T1307Z-audit/truth-<BATCH>.claims.yaml` as you go: `- {claim_id: <id>, verdict: ok|F3|F4|F5|F13|F14|unreadable, source_url: <url or null>, passage: "<≤200 chars>"}`. A claim no transport can read is `unreadable`, never `ok`.
- **Cached page bodies** from this audit's cited-page pre-pass: `work/2026-10-18T1307Z-audit/quote-bodies/` (read these first; fetch fresh when a page may have changed or is missing).
- Dedup context if you need it: `work/2026-10-18T1307Z-audit/prior_coverage.json`, `entities/registry.yaml`, `state/cves_seen.json`.
- Fetch ladder: `python3 tools/fetch_source.py extract <URL>` first (clean article body), `url <URL>` for raw HTML, `pdf <URL>` for PDFs, structured recipes (`cisa-kev`, `cisa csaf <id>`, `msrc ...`, `osv vuln <id>`), then `WebFetch` (outbound-links template, verbatim quotes only, never read "not affected" into an absence) for hosts the container is walled out of (cisa.gov pages without a recipe), `jina <URL>` last. Append each successful fetch to `work/2026-10-18T1307Z-audit/url-liveness.tsv` as `<url>\t<status>\t<UTC timestamp>`.

## Outputs (write order matters)

1. First action: `date -u +"%Y-%m-%dT%H:%M:%SZ" | tee work/2026-10-18T1307Z-audit/truth-<BATCH>.started_at`
2. After each entry: append `<UTC timestamp> <entry-id> <verdict>` to `work/2026-10-18T1307Z-audit/truth-<BATCH>.progress`, and checkpoint the findings YAML (so a cut-off costs the tail, not the batch).
3. `work/2026-10-18T1307Z-audit/truth-<BATCH>.yaml` — a top-level `entries:` list, one record per entry in your batch, clean ones included:
   ```yaml
   entries:
     - entry: 2026-10-02/example-slug
       verdict: clean            # clean | imprecision | factual-error
       defects:                  # empty list when clean
         - where: "summary"      # field, section heading, or body paragraph
           claim: "<verbatim from the entry>"
           defect: "<what is wrong, one sentence>"
           ground_truth: "<what the source actually says, verbatim where possible>"
           ground_truth_url: "<the page you read it on>"
           fix: "<the narrowest correction>"
           class: factual-error  # factual-error | imprecision
   ```
   `factual-error` = the entry asserts something its sources (or the authority) contradict or do not support, a wrong id/version/date/score/status, an invented quote. `imprecision` = true but imprecise or missing a material qualifier, an uncited clause, a mis-attributed citation for a true fact.
4. `work/2026-10-18T1307Z-audit/truth-<BATCH>.md` — the report: the Model and Timestamps lines, then per entry with a defect: entry id, quoted claim, ground truth with URL, fix. No commentary on what was fine.
5. Last: `date -u +"%Y-%m-%dT%H:%M:%SZ" | tee work/2026-10-18T1307Z-audit/truth-<BATCH>.ended_at`

## Return exactly these lines

```
**Model:** <friendly name> (`<model-id>`)
**Timestamps:** started_at=… · ended_at=… · duration_seconds=…
**Entries:** N checked · clean N · imprecision N · factual-error N
**Claims:** in_scope=N checked=N
**Findings:** work/2026-10-18T1307Z-audit/truth-<BATCH>.yaml
**Self-telemetry:** webfetch_calls=NN websearch_calls=NN bridge_fetches=NN urls_checked=NN
```

Take the model name from the model line in your own system prompt (fallback: env vars with the marker ` — container default, env fallback`). No time limit: check every claim, not a sample. Nobody answers questions mid-pass; the spawn message and this brief are the whole task.
