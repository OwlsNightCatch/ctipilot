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
  consolidating summary. Reads the past 7 days of dailies, plus two
  long-horizon sub-agents (W1 long-running campaigns + annual reports;
  W2 policy + regulatory).
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

### `.claude/agents/` — custom sub-agent definitions

- [`cti-research.md`](../.claude/agents/cti-research.md) — isolated context,
  per-role model bound by the agent definition's YAML frontmatter (operator
  rebindable). Phase 1 (daily) / Phase 2 (weekly) parallel research workers;
  also reused for verification follow-ups (max 3 per iteration). Embeds the
  `WebFetch` outbound-links template, the `tools/fetch_source.py` contract
  for known-403 hosts, the discovery-trace return format, and the mandatory
  `**Model:**` self-identification line.
- [`cti-verification.md`](../.claude/agents/cti-verification.md) — read-only,
  isolated context, per-role model bound by the agent definition's frontmatter.
  Phase 4.5 (daily) / Phase 3.5 (weekly) cold-reader verifier, looped
  iteratively (cap 3, fresh spawn each time, no shared memory). Same
  self-identification contract.

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
- `state/run_log.json` — rolling 90-day per-run record: model, sub-agent
  source allocation (`sources_attempted` / `sources_used` / `items_returned`
  per S1–S4), `fetch_failures`, `items_published`, `deep_dive`. Surfaced
  on the operations dashboard at `/ops/`.

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
  bridge that re-issues HTTP requests with a stable desktop-Chrome
  User-Agent. Solves the recurring 403 / 302-to-login that the routine
  container hits on a handful of high-signal publishers (CISA pages, the
  Swiss NCSC Cyber Security Hub) where the upstream WAF is filtering
  the agent's default UA. **Mandatory every run for CISA + NCSC.ch** —
  do not even attempt `WebFetch` on those hosts; go straight to the
  bridge. Read-only by design: no auth, no JS execution, no third-party
  deps, host allow-list enforced.
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
  the agent's self-evolution authority.

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

The two workflows are independent. The site is a *consumer* of the agent's
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
- It emits **three RSS feeds**: `/feed.xml` (daily, last 30), `/feed-weekly.xml`
  (weekly, last 30), `/feed-items.xml` (per-item granular, last 50). All
  three use the actual git-commit timestamp of the underlying brief as
  `<pubDate>` (not midnight-of-brief-date).
- The unified search index at `_site/data/search.json` covers briefs,
  entities (every type), and sources.
- The operations dashboard at `/ops/` is rendered server-side from
  `state/run_log.json` at build time. The same SVG chart primitives
  (`_ops_svg_sparkline` / `_ops_svg_bars` / `_ops_svg_donut` /
  `_ops_svg_heatmap` / `_ops_kpi_tile`) power the entity pages and
  the CVE / topic / entity overview KPI strips.

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
 ┌──────────────────────────────┐         │
 │ Phase 4.5 — verification     │         │
 │ sub-agent loop (≤3 iters):   │         │
 │  truth gate                  │         │
 │   ─ every URL fetched        │         │
 │   ─ every claim grounded     │         │
 │  editorial-quality gate      │         │
 │   ─ relevance to CH/EU SOC   │         │
 │   ─ vendor advisory ≻ NVD/   │         │
 │     CERT as primary          │         │
 │   ─ drop low-relevance       │         │
 │   ─ deepen unclear items     │         │
 │     (≤3 follow-up subagents) │         │
 │   ─ surface contradictions   │         │
 │   ─ pursue missed angles     │         │
 │ ship at iter cap; residuals  │         │
 │ logged in § Verification     │         │
 └──────────┬───────────────────┘         │
            ▼                             │
 ┌──────────────────────────────────────────────────────────────┐
 │ Update state/covered_items.json, state/cves_seen.json,       │
 │ state/deep_dive_history.json, state/run_log.json (full       │
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
 │  exit != 0 → abort commit;   │
 │  brief stays on disk; next   │
 │  run rebuilds state from it  │
 └──────────┬───────────────────┘
            ▼
 ┌──────────────────────────────┐
 │ git commit + push            │ push to claude/<name> branch only;
 │                              │ auto-merge-claude.yml promotes to main;
 │                              │ deploy-site.yml rebuilds gh-pages.
 └──────────────────────────────┘
```

The agent never bypasses any of these phases — Phase 0 is a hard prerequisite
for Phase 1, Phase 5 (state update) is a hard prerequisite for Phase 6
(commit). If a phase fails, the prompt instructs the agent to stop and
surface the error rather than silently continuing.

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
