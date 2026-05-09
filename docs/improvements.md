# Recommended improvements

A consolidated list of improvements for the agentic workflow, the editorial
policy, the operator tooling, the site, and the docs. Each open item has a
*Why* (what failure mode or pain point it addresses) and a *How* (concrete
shape of the change). They are **independent** — pick any subset.

> **Status as of 2026-05-09 (prompt v2.41).** The v2 cut-over landed in
> prompt v2.23 + the SSG rewrite of `site/`. v2.38 introduced custom
> sub-agents under `.claude/agents/`. v2.41 separated prompt-runtime
> content into `prompts/` and reworked `docs/`. The implemented items
> below have one-line hooks back to where the change lives. The
> unimplemented items are kept below in their original sections.

---

## Implemented

| ID | One-line summary | Lives in |
|----|------------------|----------|
| **A1** | Sustained 403 / 429 / 5xx no longer demotes a source — recorded as transport block, source kept in rotation. | [`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md) Phase 5 |
| **A2** | Phase 5.5 self-check gate — JSON parse, brief-CVE ↔ cves_seen, brief-item ↔ covered_items consistency, every UPDATE has an inline cite, every H3 has a v2 metadata footer, every footer value is in the taxonomy. Drift aborts the commit. | [`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md) Phase 5.5 |
| **A5** | `state/run_log.json` — per-run sub-agent allocation (90-day FIFO). | [`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md) Phase 5 + the operations dashboard at [`/ops/`](https://ctipilot.ch/ops/) |
| **A6** | Weekly summary read explicitly by name in Phase 0 — closes the Sunday-weekly / Monday-daily dedup gap. | [`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md) Phase 0 step 2 |
| **A8** | Deep-dive category-rotation memory — 30-day rolling history, demotes repeated categories. | [`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md) Phase 3 + `state/deep_dive_history.json` |
| **A9** | Distinct counters: `consecutive_quiet_periods` vs `consecutive_fetch_failures`. Demotion fires only on the content axis. | [`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md) Phase 5 |
| **A10** | Per-item metadata footer on every brief item, with controlled vocabulary in [`site/taxonomy.yaml`](../site/taxonomy.yaml). The build emits per-item / per-tag / per-region pages and a per-item RSS feed from this footer. | [`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md) Phase 4 + [`site/build.py`](../site/build.py) `parse_footer_line` |
| **A11** | Consolidated anti-crash guards in the prompt's "CRITICAL" block — always write the file; ~10 min sub-agent timebox; compose-incrementally to dodge stream timeout; persist intermediate state to `work/<run-id>/`; bounded retries; two-stage publishing chain. | [`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md) top + [`prompts/weekly-summary.md`](../prompts/weekly-summary.md) top |
| **S1** | Three RSS feeds — `/feed.xml` (daily, last 30), `/feed-weekly.xml` (weekly, last 30), `/feed-items.xml` (per-item, last 50). All use the actual git-commit timestamp as `<pubDate>`. | [`site/build.py`](../site/build.py) `build_daily_feed` / `build_weekly_feed` / `build_items_feed`. [Closes #2](https://github.com/OwlsNightCatch/ctipilot/issues/2). |
| **S2** | Print stylesheet — clean, link-annotated, hides chrome. | [`site/assets/css/styles.css`](../site/assets/css/styles.css) `@media print` |
| **S4** | Light / dark / system theme toggle, persisted in localStorage. | [`site/assets/js/theme.js`](../site/assets/js/theme.js) |
| **S5** | Topbar search autocomplete across briefs / CVEs / topics / sources. Token-prefix scoring; `/` shortcut; arrow-key navigation. | [`site/build.py`](../site/build.py) writes `data/search.json`; [`site/assets/js/search.js`](../site/assets/js/search.js) + [`site/assets/js/app.js`](../site/assets/js/app.js) `wireGlobalSearch` |
| **S6** | "Copy link" button in the brief header → clipboard, with toast. | [`site/assets/js/app.js`](../site/assets/js/app.js) `wireCopyLinkButtons` |
| **S7** | Source URL match by longest URL prefix instead of bare hostname. | [`site/build.py`](../site/build.py) `annotate_sources` |
| **S8** | Operations dashboard at `/ops/` — recent runs, fetch failures, stale active sources. | [`site/build.py`](../site/build.py) `render_ops_page` |
| **S9** | Verification-flag chip filters on the Topics page — filter by `[SINGLE-SOURCE]`, `[SINGLE-SOURCE-NATIONAL-CERT]`, `[SINGLE-SOURCE-OTHER]`. | [`site/build.py`](../site/build.py) `annotate_topics` + `render_topic_list_page` |
| **S10** | Brief-page filter UI — section toggles + tag chips + region chips, all merged into the aside-toc. Default = all selected = entire report visible; click a chip to negate. Multi-combo. | [`site/build.py`](../site/build.py) `render_brief_page` filter bar + [`site/assets/vendor/filter.min.js`](../site/assets/vendor/filter.min.js) |
| **S11** | Static-site rendering — every URL is a real HTML page rendered server-side at build time. No SPA, no client-side Markdown rendering. | [`site/build.py`](../site/build.py) `base_template` + per-page renderers |
| **D2** | `prompts/CHANGELOG.md` rendered on the About page at `/about/prompts/changelog/`, with the prompts index at `/about/prompts/` listing recent version headings inline. | [`site/build.py`](../site/build.py) `render_static_doc` + the about-page emission block |
| **D3** | Per-brief prompt-version badge linking to the matching CHANGELOG entry. | [`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md) compose template + [`site/build.py`](../site/build.py) `parse_brief` |
| **D4** | Repo-relative links in `README.md`, `docs/*.md`, and `prompts/*.md` rewritten to `/about/docs/<name>/` and `/about/prompts/<name>/` (or to GitHub blob URLs for non-rendered files) when emitted on About pages. Fragment identifiers preserved. | [`site/build.py`](../site/build.py) `_rewrite_about_links` |
| **D5** | About page split into a Documentation section (operator-facing system docs) and a Prompts section (everything the routine `Read`s at runtime, plus the version-history changelog). | [`site/build.py`](../site/build.py) about-page emission block |
| **SR4** | Sub-agent capability ceiling explicitly documented. | [`docs/operating.md`](operating.md#sub-agent-capability-ceiling) |
| **SR5** | Build-side Markdown sanitisation — fixed tag + URI-scheme allowlist, no client-side renderer to bypass. Vendored marked.js + DOMPurify kept for reference but not wired into the runtime. | [`site/build.py`](../site/build.py) `render_markdown` + `render_inline` + `render_static_doc` |
| **SR9** | Routine credential rotation cadence documented (90 days). | [`docs/operating.md`](operating.md#rotation-cadence-credentials) |
| **SR10** | One new candidate source per run, maximum. Overflow goes to § 8. | [`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md) Phase 5 |

---

## Open — workflow & infra (need additional pipelines, not landed)

### A3 — Bound the size of `state/covered_items.json`

**Why.** The file currently has ~50 items; it gains roughly 5–15 per daily run. After a year, this file is in the multi-megabyte range and becomes slower for the agent to load *and* parse in Phase 0 — which is on the critical path for every run.

**How.** Add a quarterly archival job (a tiny standalone routine, or a step in the weekly summary):

```
state/covered_items.json                   # last 180 days, hot path
state/archive/covered_items_2026Q1.json    # frozen, read-only
state/archive/covered_items_2026Q2.json
```

The agent's Phase 0 only reads the hot file. The site's `build.py` reads both and merges for the topics view. Archival is reversible — moving an older item back to hot if it becomes relevant again is a single-file edit.

**Why not yet:** Needs a separate routine cadence; the current state file is still small enough to be a non-issue.

### A4 — Continuous CVE-validity check against NVD

**Why.** The verification policy mandates "every CVE cited resolves on NVD/MITRE". The check happens in-context during the run. A CVE that *was* real but later got rejected (rare but happens) would sit in `cves_seen.json` undetected.

**How.** Add a small standalone routine: walk `state/cves_seen.json`, query `https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={id}` for each, and flag any that returns 404 or `vulnStatus: REJECTED`. Append flags as a `status: REJECTED — flagged YYYY-MM-DD` notes line; do *not* delete (audit trail). The site can surface a "rejected CVEs" badge on the CVE list. NVD rate-limits to 5 req / 30 s without a key, 50 req / 30 s with one — a key in repo secrets makes the whole list scannable in under a minute.

**Why not yet:** Separate routine + NVD API key management.

### A7 — Editorial-invariant tests in CI

**Why.** Prompt changes can silently regress editorial discipline. "No IOCs", "every claim has a link", "no vanity metrics" are all auditable from the Markdown alone. Catching a regression at PR review is far cheaper than catching it after a routine has published.

**How.** Add `.github/workflows/check-brief.yml` and `tests/check_brief.py`:

```python
def test_no_md5_sha_hashes(text):     # 32/40/64-hex
    assert not re.search(r'\b[0-9a-f]{32,64}\b', text, re.I)
def test_no_ipv4_in_running_text(text):
    ...
def test_every_claim_has_inline_link(brief):
    ...
def test_cve_format(text):
    for m in re.finditer(r'\bCVE-\S+', text):
        assert re.fullmatch(r'CVE-\d{4}-\d{4,7}', m.group(0)), m.group(0)
```

Run on every push that touches `briefs/`. A failure opens an issue tagged `editorial-regression`. *Status: deliberately deferred — the model is allowed to apply judgement here, and Phase 5.5 already catches the structural drift modes.*

### S3 — Code-block syntax highlighting

**Why.** Briefs deep-dives sometimes include shell or YAML snippets. Plain text in monospace is fine for now; a real highlighter is a small quality bump.

**How.** Vendor `highlight.js` core + only the languages used (bash, yaml, python, json, c). Wire in the marked `code` renderer. Adds ~30KB.

**Why not yet:** Low value vs. the bytes.

### S7b — Pages-site analytics (separate pipeline, opt-in)

**Why.** The repository previously pulled the GitHub Repo Traffic API into `state/engagement.json`. That API exposes **github.com repo traffic only, not GitHub Pages site traffic**, so the metric was misleading for our deployment shape — it has been removed. The site no longer collects any aggregate visit data. If real per-brief reader analytics is wanted, this is what it would look like; none of the options below are enabled by default.

**How — three options, in order of operator effort:**

1. **Cloudflare Web Analytics** — privacy-respecting, no cookies, free up to 10M req/mo. Single `<script>` tag insertion. Adds a third-party trust decision but the data stays only on Cloudflare's servers, not in this repo. Aggregate dashboards via Cloudflare UI; no API into `state/engagement.json` (so the agent's Phase 0 can't consume it).
2. **GoatCounter** (open-source) or **Plausible** — both privacy-by-design, GDPR-friendly, GoatCounter has a free hosted tier and an API. A small extension to a `sync-engagement.yml` workflow would query GoatCounter's `/api/v0/stats/hits` and merge into a state file. Integrates cleanly with the existing pipeline and gives the agent a true Pages-traffic signal.
3. **Cloudflare Worker / Vercel function** with a beacon endpoint — the SPA POSTs `{brief, dwell}` events; the worker aggregates by day in KV. A daily GitHub Action pulls the aggregates into the repo. Highest effort, highest control.

For now the github.com repo-blob views are the only available signal.

---

## Open — security & autonomy hardening (need external CI, not landed)

These are the autonomy / self-evolution hardening items. The realistic landing path for most of them is a single editorial-invariant CI workflow.

### SR1 — Editorial-invariant CI workflow (T1, T2)

**Why.** The single highest-leverage external control. Catches IOCs, hallucinated CVEs, suspicious patterns, and multi-day [SINGLE-SOURCE] floods before a regression is established.

**How.** New workflow `.github/workflows/editorial-invariants.yml` runs on every push to `main` that touches `briefs/`. Runs `tests/check_brief.py` (also new). Failures open an issue tagged `editorial-regression`. *Status: deferred. Phase 5.5 covers the most common failure modes inside the run; the CI workflow is the next step when external CI is added.*

### SR2 — Prompt-drift alerting (T2)

**Why.** Even with the in-prompt self-check, the operator wants visibility into what the agent is changing in `prompts/*.md`.

**How.** New workflow `.github/workflows/prompt-drift-alert.yml` triggers on push to `main` touching `prompts/`. Posts a comment on a pinned issue (or sends to a webhook secret) with the diff. Human-readable, no decisions taken.

### SR3 — State-file size budget (T3)

**Why.** Slow poisoning is the failure mode that's least visible. A budget catches sudden growth.

**How.** A check in the editorial-invariants workflow: `state/cves_seen.json` and `state/covered_items.json` cannot grow more than 25% in a single commit. SR10 already caps `sources/sources.json` growth in-prompt.

### SR6 — Auto-merge gated on quality CI (T6)

**Why.** The auto-merge currently fast-forwards anything pushed to `claude/*`. Gating on the editorial-invariant CI binds even a credential-compromise scenario to passing the editorial check.

**How.** Edit [`.github/workflows/auto-merge-claude.yml`](../.github/workflows/auto-merge-claude.yml) to wait for the `editorial-invariants` workflow conclusion via `gh run watch` before fast-forwarding. If the gate fails, comment on the open issue and exit cleanly.

### SR7 — Engagement outlier suppression (T7)

**Why.** Bot-driven view spikes shouldn't influence editorial weight.

**How.** Moot until aggregate engagement data is collected again (see S7b). Documented in case the pipeline is restored.

### SR8 — Out-of-band hash provenance for vendored libs (T8)

**Why.** A coordinated attacker who flips both the binary and `HASHES` defeats the build's integrity check. An external provenance log makes this single-commit attack impossible.

**How.** Sign the `site/assets/vendor/HASHES` file with a key the agent doesn't have access to (operator-held), and verify the signature in CI. Or publish hashes via sigstore Rekor and verify in CI. Both require external infra.

---

## Open — documentation

### D1 — A "first run" walkthrough

**Why.** [`docs/operating.md`](operating.md) covers steps; a narrative walkthrough with screenshots of the routine UI would be faster to follow for a first-time operator.

**How.** Add `docs/first-run.md` and link from the README.

---

## Quick-fix shortlist (still open)

If only an afternoon is available:

1. **SR1** — editorial-invariant CI (90 min). Highest-leverage external single change.
2. **SR2** — prompt-drift alert workflow (30 min).
3. **SR3** — state-file size budget (30 min, in the same CI as SR1).
4. **A3** — `covered_items.json` archival as a small standalone routine (60 min).

Together with the in-prompt controls already in place (Phase 5.5, A1/A8/A9, SR10), these turn the system from "self-evolving with no observability" into "self-evolving with detect-and-correct in place".
