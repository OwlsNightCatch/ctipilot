# Architecture

A single, end-to-end map of every component in the repository: what it is,
what it reads, what it writes, and how it talks to the others. If you are
debugging an unexpected commit or onboarding a new operator, start here.

## One picture

```
                                 ┌──────────────────────────┐
                                 │  Claude Code routine     │
                                 │  (cloud, scheduled)      │
                                 │  prompt: "Read           │
                                 │   prompts/daily-cti-     │
                                 │   brief.md and execute"  │
                                 └─────────────┬────────────┘
                                               │ git push
                                               ▼
   reads ┌──────────────────────────────────────────────────────────┐
 ──────► │                       repository                         │
         │                                                          │
         │  prompts/                state/                          │
         │   ├ daily-cti-brief.md    ├ covered_items.json           │
         │   ├ weekly-summary.md     ├ cves_seen.json               │
         │   ├ CHANGELOG.md          ├ deep_dive_history.json       │
         │   ├ verification.md       └ run_log.json                 │
         │   ├ brief-template.md    sources/                        │
         │   └ check-brief-fixes.md  └ sources.json                 │
         │                          tools/                          │
         │  briefs/                  ├ check_brief.py (Phase 5.5)   │
         │   ├ YYYY-MM-DD.md         └ fetch_source.py              │
         │   └ weekly/YYYY-Www.md   docs/                           │
         │                          ├ architecture.md (this file)   │
         │  .claude/agents/         ├ operating.md                  │
         │   ├ cti-research.md      └ analytics.md                  │
         │   └ cti-verification.md                                  │
         └──────────────────────────────┬───────────────────────────┘
                                        │
                                        │ git push (claude/** branches only)
                                        ▼
                           ┌────────────────────────────┐
                           │ auto-merge-claude.yml      │
                           │  ff-merges (or merges with │
                           │  state/* → ours,           │
                           │  sources.json → theirs)    │
                           └────────────┬───────────────┘
                                        ▼
                                      main
                                        │
                                        ▼ workflow_run (success only)
                           ┌────────────────────────────┐
                           │ deploy-site.yml            │
                           │  runs site/build.py        │
                           │  force-pushes to gh-pages  │
                           └────────────┬───────────────┘
                                        ▼
                              GitHub Pages reader
                              (real HTML pages emitted
                              by site/build.py — no SPA)
```

## Components

### `prompts/` — everything the routine loads at runtime

The two master prompts plus the runtime-policy / template / debug docs they reference. Each master prompt is the *entire* runtime contract for a routine; the routine is invoked with a one-line wrapper ("Read this prompt and execute it"). The supporting files are also under `prompts/` because the master prompts `Read` them at runtime — they are part of the prompt machinery, not operator-facing documentation.

- [`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md) — the daily
  brief. Phases 0–6 + a 5.5 self-check gate (preflight → parallel research →
  verification → deep dive → compose → state update → self-check →
  commit/push). Spawns four parallel research sub-agents.
- [`prompts/weekly-summary.md`](../prompts/weekly-summary.md) — the weekly
  consolidating summary (12 sections, 0–11). Reads the past 7 days of
  dailies, runs a Phase 2.5 verification & triage pass, then composes via
  two horizon sub-agents (W1 long-running campaigns + threat-actor
  developments + research findings + annual reports; W2 policy +
  regulatory). Same procedure as the daily (gold standard); the lens
  differs — broader threat picture, multi-day chains, research / actor
  developments, annual reports, long-horizon "looking ahead". The weekly
  may repeat a daily item with a new lens; the daily never repeats the
  weekly and carries no long-horizon synthesis.
- [`prompts/CHANGELOG.md`](../prompts/CHANGELOG.md) — the version history of
  the prompts. Treat as the audit trail for editorial-policy changes.
- [`prompts/verification.md`](../prompts/verification.md) — the editorial /
  fake-news verification policy. The agent's quality gates are derived from
  this; the prompt's Phase 2 references it by name.
- [`prompts/brief-template.md`](../prompts/brief-template.md) — the canonical
  Markdown skeleton for the rendered brief / weekly. The prompt's Phase 4
  `Read`s it before composing.
- [`prompts/check-brief-fixes.md`](../prompts/check-brief-fixes.md) — fix
  recipes for common `tools/check_brief.py` FAILs. The prompt's Phase 5.5
  references it for remediation.

### `config/org-profile.yaml` + `tools/compose_prompts.py` — organization parameterization

The deployment's organization-specific values live in one config file:
organization (name, short name, sector, additional sectors, region focus,
home region, description, audience), watchlists (products with
vendor/exposure/criticality, suppliers with relationship/criticality,
standing free-text interests), and the vulnerability-triage scheme
(categories with id/name/criteria/response + a default). The defaults
reproduce the historical Swiss-federal-SOC deployment; watchlists and
triage ship empty/disabled, which makes every profile-driven behaviour a
no-op.

`tools/compose_prompts.py` (stdlib-only; `--check` / `--write` / `--dump` /
`--selftest`) renders the profile into `ORG-PROFILE:BEGIN/END` managed
marker blocks inside five files: both master prompts (mission + audience
paragraphs, plus the § Organization profile & watchlists data block), the
`cti-research` definition (mission, audience, watchlist values — so every
research spawn sees the same org context without spawn-message bloat), and
both verifier definitions (§ Organization context — so the relevance check
judges against the *configured* organization). The static policy text
around the blocks (anti-overshoot rules, sweep ownership, org-triage line
spec) lives in the prompts and follows the normal versioning rule; the
generated blocks carry values only and are exempt from version bumps.

Enforcement is three-layered: the `compose-profile` workflow (below)
composes or fail-louds on push; `tools/check_brief.py` carries a
`profile-sync` WARN so a routine run surfaces stale composition; and
CLAUDE.md forbids hand-editing the generated blocks.

The `deployment:` section (`visibility: public|private`, `site_url`)
drives the TLP ceiling on closed-source citations and the publish-phase
site poll (`compose_prompts.py --get deployment.site_url`); see
[`docs/private-deployment.md`](private-deployment.md).

### `intel/` — closed-source drop folder

Operator-owned feed scripts commit dated folders (`intel/<YYYY-MM-DD>/`)
of front-mattered text documents; the routines detect in-window content in
Phase 0 and spawn a conditional intake sub-agent (S5 daily / W3 weekly)
that extracts items with `closed_source` source records, mandatory verbatim
evidence quotes, and public-corroboration pivots. Briefs cite the documents
by reference (`Closed-source:` footer field — parsed by `site/build.py`,
rendered unlinked), never by URL. `check_brief.py` gates TLP against the
deployment visibility (`closed-source-tlp` FAIL) and traces citations back
to drop files; the verifier `Read`s the files as ground truth. Contract:
[`intel/README.md`](../intel/README.md). Empty/absent `intel/` — the normal
state — costs nothing.

### `.claude/agents/` — custom sub-agent definitions

- [`cti-research.md`](../.claude/agents/cti-research.md) — isolated context,
  per-role model bound by the agent definition's YAML frontmatter (operator
  rebindable). Phase 1 (daily) / Phase 2 (weekly) parallel research workers;
  also reused for verification follow-ups (max 3 per iteration). Embeds the
  `WebFetch` outbound-links template, the `tools/fetch_source.py` contract
  for known-403 hosts, the discovery-trace return format, the mandatory
  `**Model:**` self-identification line. Also covers: env-var
  self-identification (reads `CLAUDE_FRIENDLY_NAME` / `CLAUDE_MODEL_ID`
  set by the harness, falls back to runtime-context reasoning), prior-
  coverage dedup at fetch time (reads `work/<run-id>/prior_coverage.json`
  before fetching to avoid spending wall-clock on already-covered items),
  URL-liveness ledger append (one TSV line per successful Source fetch
  to `work/<run-id>/url-liveness.tsv` so `tools/check_brief.py` can skip
  redundant HEAD/GET).
- [`cti-verification.md`](../.claude/agents/cti-verification.md) — read-only,
  isolated context, per-role model bound by the agent definition's frontmatter
  (Opus by default — gatekeeper of the publish gate).
  Phase 5.7 (daily) / Phase 4.7 (weekly) cold-reader verifier, runs AFTER
  `tools/check_brief.py` exits 0 (cheap mechanical gate first), looped
  iteratively (cap 5, fresh spawn each time, no shared memory; each iteration
  re-runs `check_brief.py` between fix and re-spawn). Same self-identification
  contract. Also covers: the F12 single-source-flag finding category;
  an iteration-rotation note (don't assume same model as prior
  iteration); env-var self-identification.
- [`cti-verification-alt.md`](../.claude/agents/cti-verification-alt.md) —
  Sonnet-pinned variant of `cti-verification`. Byte-identical operational system
  prompt; only the YAML `model:` frontmatter differs (`sonnet` vs `opus`).
  The Phase 5.7 / Phase 4.7 main-agent loop spawns this on **even iterations**
  (iter 2, iter 4) so model-specific blind spots are caught when the next
  iteration runs on a different model. The two verifier definitions move
  in lockstep — when you edit one, edit the other.

### `briefs/` — the canonical output

One Markdown file per day at `briefs/YYYY-MM-DD.md`, one per ISO week at
`briefs/weekly/YYYY-Www.md`. Sections 0–8 per the structure pinned in
[`briefs/README.md`](../briefs/README.md):
0 TL;DR · 1 Immediate Actions (often absent) · 2 Active Threats / Trending
Actors / Notable Incidents & Disclosures · 3 Trending Vulnerabilities ·
4 Research & Investigative Reporting · 5 Updates to Prior Coverage ·
6 Deep Dive · 7 Action Items · 8 Verification Notes. Each individual H3
item carries a structured metadata footer (`— *Source: … · Tags: … ·
Region: … [· CVE: …] [· CVSS: …] [· Vector: …] [· Auth: …] [· Status: …]*`)
parseable by the build. These files are immutable once committed —
corrections happen in the *next* brief, not by editing past ones.

### `state/` — rolling memory across runs

The agent re-reads these every run before writing.

- [`state/covered_items.json`](../state/covered_items.json) — full coverage
  records for every CVE / actor / campaign / incident / tool / annual report
  ever referenced. Each item has a structured `appearances[]` array
  (`{date, section, brief_path, delta_summary}`) — the site uses this
  to render the **Story timeline** on each `/entities/<key>/` page.
  CVE-only entries (in `cves_seen.json` but not yet promoted to a topic)
  synthesise a stub timeline from their flat brief-name list so every
  entity has a coverage timeline regardless of which state file
  carries it.
- [`state/cves_seen.json`](../state/cves_seen.json) — flat fast-lookup CVE
  index for sub-agent dedup. A subset of `covered_items.json` (CVEs only)
  with a tighter schema.
- `state/deep_dive_history.json` — rolling 30-day list of `{date, topic, category}`
  entries used by Phase 3 to apply the deep-dive category-rotation rule.
- `state/run_log.json` — rolling 90-day per-run record: `run_id`
  (deterministic `<YYYY-MM-DD>-<sha8 of brief_path|started_minute>` —
  idempotent retry), model, sub-agent source allocation (`sources_attempted`
  / `sources_used` / `items_returned` per S1–S4), `fetch_failures`,
  `items_published`, `deep_dive`, `verification.iterations[]` (per-iteration
  model + verdict + truth/editorial/advisory finding counts),
  `verification_iterations`, `verification_residual_count` (derived
  from final-iteration `truth + editorial` when verdict is NEEDS_FIXES;
  `0` when CLEAN — the cap-breach signal builds on this), and
  `sources_changed` (one `{id, change, from, to, reason}` per
  `sources/sources.json` edit the run made: status transitions, new
  candidates, and fetch-method / category / reliability / url corrections).
  Surfaced on the operations dashboard at `/ops/`.
- `state/source_health.json` — written by [`tools/source_health.py`](../tools/source_health.py)
  on a weekly GitHub Actions cron. Bounded history (12 runs ≈ 3 months
  at weekly cadence) of `(id, status_code, latency_ms, fetched_at, class)`
  per active source. Lets the daily routine's source-demotion logic key off
  a stable failing pattern instead of the day-of-week luck of its single
  fire. Rendered on `/ops/` (the "Sources" cluster's
  health-snapshot panel — class breakdown + any non-ok source).

### `sources/` — the curated source list

[`sources/sources.json`](../sources/sources.json) — ~80 entries spanning
national CERTs, vendor TI, journalism, breach trackers. Schema:

```jsonc
{
  "id": "stable-id-never-changes",        // referenced from covered_items.json
  "publisher": "Display name",
  "url": "https://...",
  "category": ["ch-eu", "vulns", ...],
  "reliability": "HIGH | MEDIUM | LOW",
  "language": ["en", "de", ...],
  "status": "active | candidate | demoted",
  "last_successful_fetch": "YYYY-MM-DD | null",
  "consecutive_failures": 0,
  "notes": "history of changes, dated"
}
```

The agent maintains this file autonomously per the lifecycle in the top-level
[README](../README.md#source-lifecycle-all-transitions-autonomous).

### `tools/` — small operator-shipped helpers

- [`tools/fetch_source.py`](../tools/fetch_source.py) — stdlib-only Python
  bridge that re-issues HTTP requests with a current desktop-Chrome
  User-Agent (Chrome 138 + the matching `Sec-CH-UA` client-hint
  headers a real Chrome sends, so WAFs that cross-check UA ↔ client-hints
  stop filtering it — the UA bump recovered `databreaches.net` and
  `prodaft.com` in the 2026-06-20 audit). Solves the recurring 403 /
  302-to-login that the routine container hits on high-signal publishers
  (CISA pages, the Swiss NCSC Cyber Security Hub) where the upstream WAF
  filters the agent's default UA. **Mandatory every run for CISA + NCSC.ch** —
  do not even attempt `WebFetch` on those hosts; go straight to the
  bridge. Structured subcommands (`cisa-kev`, `ncsc-csh`, `enisa-euvd`,
  `bsi-rss/csaf`, `ncsc-nl`, `cert-eu`, `cert-fr`, `ico-uk`, `sec-edgar`,
  `feed`, `msrc`) wrap the publishers whose listing pages are
  JS-rendered SPAs. Read-only by design: no auth, no JS execution, no
  third-party deps; an earlier host allow-list was removed in favour of
  the layer-3 SSRF defences (https-only, resolved-IP deny list, redirect
  re-validation, body-size cap).
- [`tools/check_brief.py`](../tools/check_brief.py) — the institutionalised
  Phase 5.5 self-check gate. Stdlib-only Python script that bundles every
  pre-commit consistency check (state JSON parses, CVE sync, H3 footer
  presence and field completeness, taxonomy validation, UPDATE
  citations, multi-CVE / multi-source / primary-source-quality checks,
  `tools/fetch_source.py`-for-CISA/NCSC.ch enforcement,
  `covered_items.json` appearance heuristic, `run_log.json`
  Ops-dashboard population, `sources.json` last-fetched bookkeeping,
  IOC heuristic scan with version-string suppression) **plus** runs the
  build-side smoke tests in `site/test_build.py`. Imports the footer
  parser + taxonomy loader from `site/build.py` so script and build agree
  on parsing rules. Read-only — the agent fixes drift, the script
  reports it. Non-zero exit aborts the commit. Maintained as part of
  the agent's self-evolution authority. Also covers: `cap-breach`
  WARN (final-iteration `NEEDS_FIXES`); `verification_residual_count`
  derived from final iteration's `truth + editorial`; deterministic
  `run_id` field required + idempotent (no duplicate runs[] entries);
  `tldr-deadline-lead` WARN (PD-13 enforcement at the bullet level);
  `aggregator-only-sourcing` WARN (≥2 Sources all from news aggregators);
  `single-source-flag` WARN (single Source missing `[SINGLE-SOURCE]`);
  URL-liveness cache (skip live HEAD/GET on URLs the sub-agents already
  verified live in `work/<run-id>/url-liveness.tsv`).
- [`tools/source_candidates.py`](../tools/source_candidates.py) —
  walks last 30 days of briefs, counts every outbound-link host, subtracts
  hosts already in `sources.json` and the news-aggregator allowlist, outputs
  the top-N missing-but-cited domains with citation counts and brief samples.
  Operator runs manually to spot publishers worth promoting to
  `status: candidate`. Pure post-hoc analytics; no runtime cost.
- [`tools/source_health.py`](../tools/source_health.py) — periodic
  accessibility probe of **every** source (active + candidate +
  demoted), now probed via its *actual recipe*: `feed` (with common-path
  discovery) for RSS sources, the documented `tools/fetch_source.py`
  subcommand for `api`/`bridge` sources (so the bridge recipes themselves are
  verified), and a browser-UA HEAD→GET (Chrome-138 UA, GET-retry-after-403)
  for `webfetch`. Records `(id, status, fetch_method, status_code, class,
  action, action_reason, fetched_at)` to `state/source_health.json`
  (schema_version 2, 12-run bounded history). The derived `action` ∈
  `none | needs-bridge | needs-demote` is what the Ops dashboard Health panel
  floats — only the unsolved problems. Run by the
  [`source-health.yml`](../.github/workflows/source-health.yml) GitHub Action
  on Sundays at 04:30 UTC, on `workflow_dispatch`, **and at the end of every
  daily / weekly routine run** (Phase 5 / Phase 4) so the snapshot is fresh
  every fire.

### `docs/` — operator-facing documentation

System reference for operators, contributors, and curious readers. Pure docs — nothing here is loaded by the prompt at runtime (that material lives under `prompts/`).

- [`docs/architecture.md`](architecture.md) — this file. End-to-end map of every component.
- [`docs/operating.md`](operating.md) — operator runbook: GitHub App setup, Pages enablement, ops dashboard, sub-agent capability ceiling, troubleshooting.
- [`docs/analytics.md`](analytics.md) — public-facing privacy disclosure (what we measure, what we don't).

### `.github/workflows/` — CI

- [`auto-merge-claude.yml`](../.github/workflows/auto-merge-claude.yml) —
  triggers on push to `claude/**`. The **only** path commits land on `main`;
  fast-forwards when the feature branch is a strict descendant, falls back
  to a regular merge with auto-resolution for `state/*.json` (`--ours`) and
  `sources/sources.json` (`--theirs`) on a true divergence. Deletes the
  feature branch on success. **Belongs to the publishing chain; do not edit
  unless you understand the resolution rules in
  [`docs/operating.md`](operating.md#publishing-chain-feature-branch-only).**
- [`deploy-site.yml`](../.github/workflows/deploy-site.yml) — triggers on
  push to `main` whenever the site inputs change. Runs `site/build.py`,
  uploads the bundle to GitHub Pages.
- [`source-health.yml`](../.github/workflows/source-health.yml) — weekly
  cron (Sundays 04:30 UTC) + `workflow_dispatch`. Runs
  [`tools/source_health.py`](../tools/source_health.py) HEAD-only against
  every active source, commits `state/source_health.json` directly to
  `main` (state/* sits in the auto-merge auto-resolution allowlist, so a
  concurrent claude/* push won't race). Independent of the daily routine.
- [`compose-profile.yml`](../.github/workflows/compose-profile.yml) —
  triggers on push touching `config/org-profile.yaml`, the
  compose script, or any composed target. Selftests the compose script,
  then: on operator branches with drift, runs `--write` and commits the
  composed prompts back to the branch; on `main` and `claude/**`, is
  check-only and fails loud (`::error::`) — auto-committing on `claude/**`
  would race `auto-merge-claude.yml` (same push event; the branch can be
  merged + deleted mid-run, and a GITHUB_TOKEN push would not re-trigger
  the merge), so the Claude session that edits the config is required to
  compose in the same commit instead.

The four workflows are independent. The site is a *consumer* of the agent's
output and never writes back.

### `site/` — the public reader

A stdlib-only Python static-site generator (`site/build.py`) emits a real
HTML page for every URL — home, every brief, every per-item block, every
**entity** page (CVE, actor, campaign, incident, tool, advisory, annual
report, research, technique — all rendered through one `render_entity_page`
function), every source page, every tag and region index, the operations
dashboard, the about pages. JavaScript only enhances (topbar search
autocomplete via `data/search.json`, GitHub-stars badge, brief-page filter
chips, theme cycle, copy-link, SPA-redirect bootstrap on `/`). With JS
disabled the site is fully readable. See [`site/README.md`](../site/README.md)
for the internal layout. The site is read-only with respect to the rest
of the repo:

- It only **reads** `briefs/`, `state/`, `sources/`, `README.md`,
  `docs/*.md`, `prompts/*.md` (including `CHANGELOG.md`), and `site/taxonomy.yaml`.
- It writes nothing back — its build artifact lives entirely under
  `site/_site/` (gitignored locally; force-pushed to the `gh-pages` branch
  by the CI workflow).
- Every entity is canonical at `/entities/<key>/`. The legacy
  `/cves/<id>/` and `/topics/<key>/` URLs are HTML meta-refresh
  redirect stubs — they still resolve, search engines see the
  canonical, and internal links (CVE pills, brief-page reference
  blocks, search results) point at the canonical directly without a
  redirect hop. Type-filtered overviews live at `/cves/` (type=cve)
  and `/topics/` (type≠cve); the unified overview at `/entities/`
  has the same Ops-style KPI strip + type-distribution donut +
  recent-coverage sparkline as every entity page.
- It emits **eleven RSS feeds**: three main feeds (`/feed.xml`, daily,
  last 30; `/feed-weekly.xml`, weekly, last 30; `/feed-items.xml`,
  per-item granular, last 50) plus **eight sector slices**:
  `/feed-public-sector.xml`, `/feed-healthcare.xml`, `/feed-finance.xml`,
  `/feed-energy.xml`, `/feed-ot-ics.xml`, `/feed-defense.xml`,
  `/feed-telco.xml`, `/feed-education.xml`. Each slice is the per-item
  feed filtered by the relevant Sector / Tags so subscribers can subscribe
  to the slice they care about. All eleven use the actual git-commit
  timestamp of the underlying brief as `<pubDate>` (not midnight-of-brief-date).
  All eleven listed on `/feeds/`.
- The unified search index at `_site/data/search.json` covers briefs,
  entities (every type), and sources.
- The operations dashboard at `/ops/` is rendered server-side from
  `state/run_log.json` at build time. The same SVG chart primitives
  (`_ops_svg_sparkline` / `_ops_svg_bars` / `_ops_svg_donut` /
  `_ops_svg_heatmap` / `_ops_kpi_tile`) power the entity pages and
  the CVE / topic / entity overview KPI strips.
- `/trends/` cross-brief threat-class trend dashboard
  (8 cohort sparklines bucketed by ISO week — ransomware, actively-
  exploited vulnerabilities, public-sector, OT/ICS, supply-chain,
  AI-abuse, Switzerland+Europe, nation-state); `/feeds/` single
  discovery page for all 11 RSS feeds; per-item delta `<details>` block
  inside each brief item whose CVE / topic key has more than one
  appearance in `covered_items.json`; "Editorial choices" `<details>`
  block at the bottom of each daily brief surfacing items dropped from
  § 7 Verification Notes; horizontal actor-timeline strip on entity
  pages of type actor / campaign / incident / tool / annual-report.
- `data/site.json.github.{url,stars}` populated at build time
  via best-effort GitHub API fetch; the topbar's `wireGithubBadge()` in
  `assets/js/app.js` consumes it to render a live star count next to
  the GitHub icon. Build never fails on the fetch (silently degrades to
  icon-only when unreachable / rate-limited).

[`site/taxonomy.yaml`](../site/taxonomy.yaml) is the controlled vocabulary
for every metadata-footer value (themes / sectors / regions / nexus /
cve_types / cve_vectors / cve_auth / cve_status / sections). The build
refuses any post-cut-over item using a value not in this file.

## Data flow per routine run

```
 ┌──────────────┐  preflight   ┌──────────────────────────────┐
 │  routine     │─────────────▶│  load sources.json (active)  │
 │  fires       │              │  load past 7 days of briefs  │
 │  (operator-  │              │  load covered_items.json     │
 │  scheduled)  │              │  load cves_seen.json         │
        │                      └──────────┬───────────────────┘
        │                                 │
        ▼  spawn 4 sub-agents in parallel │
 ┌──────────────────────────────┐         │
 │ S1 active threats / vulns    │         │
 │ S2 CH/EU & public sector     │         │
 │ S3 research & journalism     │         │
 │ S4 incidents & disclosures   │         │
 └──────────┬───────────────────┘         │
            │ flexible Markdown returns   │
            ▼                             │
 ┌──────────────────────────────┐         │
 │ verify (two-source / CERT)   │         │
 │ dedup vs preflight context   │         │
 │ rank, apply deep-dive        │         │
 │   category-rotation rule     │         │
 └──────────┬───────────────────┘         │
            ▼                             │
 ┌──────────────────────────────┐         │
 │ Write briefs/YYYY-MM-DD.md   │         │
 │ (with prompt-version badge)  │         │
 └──────────┬───────────────────┘         │
            ▼                             │
 ┌──────────────────────────────────────────────────────────────┐
 │ Phase 5 — Update state/covered_items.json, state/cves_seen.  │
 │ json, state/deep_dive_history.json, state/run_log.json (full │
 │ sub-agent allocation + fetch_failures + verification_         │
 │ iterations + verification_residual_count — Ops dashboard      │
 │ depends on this), sources/sources.json (last-seen, demotions, │
 │ candidates)                                                  │
 └──────────┬───────────────────────────────────────────────────┘
            ▼
 ┌──────────────────────────────┐
 │ Phase 5.5 — self-check gate  │  python3 tools/check_brief.py
 │ (institutionalised script):  │   ─ state JSON parses
 │                              │   ─ every brief CVE in cves_seen
 │                              │   ─ core sections vs covered appear-
 │                              │     ances heuristic                  
 │                              │   ─ every UPDATE has inline cite     
 │                              │   ─ every H3 has a v2 footer         
 │                              │     (Source ≥1 link + Tags + Region) 
 │                              │   ─ CVE entries carry CVE / Vector / 
 │                              │     Auth / Status                    
 │                              │   ─ multi-CVE: shared CVSS or per-   
 │                              │     CVE breakdown                    
 │                              │   ─ primary-source quality (NVD /    
 │                              │     CERT as sole primary → WARN)     
 │                              │   ─ tools/fetch_source.py used for   
 │                              │     CISA + NCSC.ch when 403 hit      
 │                              │   ─ run_log.json today fully         
 │                              │     populated (Ops dashboard)        
 │                              │   ─ ≥1 source fetched today          
 │                              │   ─ heuristic IOC scan               
 │                              │   ─ taxonomy validation              
 │                              │   ─ site/test_build.py passes        
 │  exit != 0 → abort the rest  │
 │  of the run; brief stays on  │
 │  disk; next run rebuilds     │
 └──────────┬───────────────────┘
            ▼
 ┌──────────────────────────────┐
 │ Phase 5.7 — verification     │  cti-verification (Opus) loop
 │ sub-agent loop (≤5 iters):   │  ─ runs only after Phase 5.5 = 0
 │  truth gate                  │  ─ each iteration: receive report,
 │   ─ every URL fetched        │    apply fixes, re-update state,
 │   ─ every claim grounded     │    re-run check_brief.py, then
 │  editorial-quality gate      │    re-spawn fresh verifier
 │   ─ relevance to CH/EU SOC   │  ─ CLEAN verdict ⇒ proceed to commit
 │   ─ vendor advisory ≻ NVD/   │  ─ iteration 5 NEEDS_FIXES ⇒
 │     CERT as primary          │    fail-open, residuals logged
 │   ─ drop low-relevance       │
 │   ─ deepen unclear items     │
 │     (≤3 follow-up subagents) │
 │   ─ surface contradictions   │
 │   ─ pursue missed angles     │
 │ gate to publish; cap is      │
 │ safety valve, not goal       │
 └──────────┬───────────────────┘
            ▼
 ┌──────────────────────────────┐
 │ git commit + push            │ push to claude/<name> branch only;
 │                              │ auto-merge-claude.yml promotes to main;
 │                              │ deploy-site.yml rebuilds gh-pages.
 └──────────────────────────────┘
```

The agent never bypasses any of these phases — Phase 0 is a hard prerequisite
for Phase 1, Phase 5 (state update) is a hard prerequisite for Phase 5.5
(self-check gate), which is a hard prerequisite for Phase 5.7 (verification
sub-agent), which is a hard prerequisite for Phase 6 (commit). If a phase
fails, the prompt instructs the agent to stop and surface the error rather
than silently continuing.

## Adding a new component

A safe pattern for extending the system without affecting the agent:

1. **Site-only feature** (new view, new search facet). Edit `site/`. The
   agent's run is untouched.
2. **New data field** (e.g. add a `severity` to `covered_items.json`).
   Update the prompt's Phase 5 instructions, then re-flow the new field
   through `site/build.py` and the renderers. Old briefs stay valid because
   the field is optional.
3. **New source category**. Edit `sources/sources.json` (add the entry) and
   the category list in `prompts/daily-cti-brief.md` Phase 1 (so a
   sub-agent picks it up). The site's category filter picks it up on the
   next build automatically.
4. **New routine** (e.g. monthly horizon scan). Add a prompt in `prompts/`,
   create a new Claude Code routine pointing at it, and add a parallel
   workflow in `.github/workflows/` if you want CI to react to its output.

Anything more invasive (new state file, new repo layout) — write down the
reasoning in the commit message and bump the prompt version with a
CHANGELOG entry explaining the *why* before making the change. The agent's
prompts are the load-bearing part of the system; small contract changes
are easy to ship by accident and hard to roll back.
