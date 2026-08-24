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

## 2026-08-05 — the pool was NOT exhausted, and three sub-agents believed it was

A different failure from the 2026-08-02 outage, and more insidious: the pool held **7 keys, 5 live
with 37M tokens**, but the first two in spend order were exhausted. Dead-key state was
process-scoped, and every sub-agent shells out to a fresh `fetch_source.py` process — so every
single invocation re-probed both dead keys, printed a "balance exhausted" line for each, then
rotated to a live key and **succeeded**. Three of four research sub-agents read those two warnings
as a dead transport and abandoned the reader rung for the entire run. Cost: two rotation-priority
sources unswept (`prodaft`, `ccn-cert-es`), a Chrome stable-post body unread, and no recovery
attempt on a CERT-PL 403.

**Fixed in `tools/fetch_source.py`:** exhausted/revoked keys are now cached across processes
(`<JINA_CACHE_DIR>/dead-keys.json`, sha256 key ids only — never the credential) with a 6 h TTL
(`JINA_DEAD_KEY_TTL`), so a fresh invocation skips a known-dead key instead of re-probing it. The
TTL preserves recovery (a topped-up key is re-probed once the entry ages out), and if *every* key is
inside its TTL the full pool is re-probed rather than dropping to the anonymous tier — a stale cache
entry can never lock the pool out. The rotation notice now says explicitly that it is not a failure
and that the fetch continues.

**Diagnostic rule:** `jina-usage` reports the whole pool; a sub-agent's stderr reports only the keys
it happened to touch. Never conclude "the pool is exhausted" from a sub-agent's report — check
`jina-usage` first. Rotation warnings followed by content mean the ladder worked.

## 2026-08-22 — the second probe-side false `needs-demote`: byte count is not health

Same family as the `probe_url` target-mismatch fix, different mechanism. `source_health.py`
judged a bridge recipe healthy by how many bytes it printed, so `sec-edgar 8k` — which
correctly returned a well-formed JSON envelope with `count: 0` because no matching filing
existed in the window, about 120 bytes — was flagged `needs-demote`. A **valid empty result is
a working source**, and a quiet window is the normal state of a filing feed.

Fixed on `main` by the 2026-08-23 fire: when a bridge exits 0 and its output parses as JSON,
health is decided by structure rather than size — `count`/`total`/`total_count` at zero, or an
empty `hits`/`results`/`items`/`vulns` list, reports `bridge-ok` with "well-formed empty result
set" said explicitly.

**Worth knowing how this note came to be written twice.** The stalled 2026-08-22 fire
independently found the same defect from the same `sec-edgar 8k` case and wrote its own narrower
fix (`count`/`total` plus one list shape). At merge time `main` already had the better version, so
the 08-22 patch was discarded. Two fires two days apart rediscovering one probe defect is a signal
about the sweep's own reporting: an UNSOLVED row that names the *symptom* ("120 B, needs-demote")
rather than the *shape mismatch* invites each run to re-derive the diagnosis from scratch.

**Generalisation for any future probe work: a probe must assert the shape the recipe promises,
never a proxy for it.** Byte counts, non-empty output and HTTP 200 are all proxies, and each
one has produced a false demotion signal in this repo. Demoting a healthy source costs
coverage silently, which is the expensive direction of this error.
