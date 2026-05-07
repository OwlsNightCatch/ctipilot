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
         │   └ CHANGELOG.md          ├ deep_dive_history.json       │
         │                           └ run_log.json                 │
         │                          sources/                        │
         │  briefs/                  └ sources.json                 │
         │   ├ YYYY-MM-DD.md                                        │
         │   └ weekly/YYYY-Www.md   docs/                           │
         │                          ├ workflow.md                   │
         │                          ├ verification.md               │
         │                          ├ routine-setup.md              │
         │                          ├ architecture.md (this file)   │
         │                          └ improvements.md               │
         └──────────────┬─────────────────────────────────┬─────────┘
                        │                                 │
        push to claude/**│ (fallback)              push to main │
                        ▼                                 ▼
                 ┌──────────────┐                ┌──────────────────┐
                 │ auto-merge   │ ff-merges      │ deploy-site.yml  │
                 │ workflow     │───────────────▶│ runs build.py    │
                 └──────────────┘  to main       │ uploads to Pages │
                                                 └────────┬─────────┘
                                                          │
                                                          ▼
                                              GitHub Pages reader
                                              (site/index.html SPA)
```

## Components

### `prompts/` — the agent's instructions

Two prompts. Each is the *entire* runtime contract for a routine; the routine
is invoked with a one-line wrapper ("Read this prompt and execute it").

- [`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md) — the daily
  brief. Phases 0–7 (preflight → parallel research → verification → deep dive
  → compose → state update → commit/push → output). Spawns four parallel
  research sub-agents.
- [`prompts/weekly-summary.md`](../prompts/weekly-summary.md) — the weekly
  consolidating summary. Reads the past 7 days of dailies, plus two
  long-horizon sub-agents.
- [`prompts/CHANGELOG.md`](../prompts/CHANGELOG.md) — the version history of
  the prompt itself. Treat as the audit trail for editorial-policy changes.

### `briefs/` — the canonical output

One Markdown file per day at `briefs/YYYY-MM-DD.md`, one per ISO week at
`briefs/weekly/YYYY-Www.md`. Sections 0–9 per the structure pinned in
[`briefs/README.md`](../briefs/README.md). These files are immutable once
committed — corrections happen in the *next* brief, not by editing past ones.

### `state/` — rolling memory across runs

The agent re-reads these every run before writing.

- [`state/covered_items.json`](../state/covered_items.json) — full coverage
  records for every CVE / actor / campaign / incident / tool / annual report
  ever referenced. Each item has an `appearances[]` array — the SPA uses this
  to render the "story timeline" view.
- [`state/cves_seen.json`](../state/cves_seen.json) — flat fast-lookup CVE
  index for sub-agent dedup. A subset of `covered_items.json` (CVEs only)
  with a tighter schema.
- `state/deep_dive_history.json` — rolling 30-day list of `{date, topic, category}`
  entries used by Phase 3 to apply the deep-dive category-rotation rule.
- `state/run_log.json` — rolling 90-day per-run record: model, sub-agent
  source allocation (`sources_attempted` / `sources_used` / `items_returned`
  per S1–S4), `fetch_failures`, `items_published`, `deep_dive`. Surfaced
  by the SPA's `#/ops` view.

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
  the agent's default UA. Read-only by design: no auth, no JS execution,
  no third-party deps, host allow-list enforced. Surfaced to the agent
  in the daily prompt's Phase 1 research-methodology section as the
  documented fallback whenever a `WebFetch` comes back blocked.

### `docs/` — operator-facing documentation

- [`docs/workflow.md`](workflow.md) — phase-by-phase execution of both
  routines.
- [`docs/verification.md`](verification.md) — the editorial / fake-news
  defence policy. The agent's quality gates are derived from this.
- [`docs/routine-setup.md`](routine-setup.md) — one-time GitHub App / Pages
  / branch-permission setup.
- [`docs/architecture.md`](architecture.md) — this file.
- [`docs/improvements.md`](improvements.md) — recommended improvements to
  the agentic workflow and the site, with rationale.

### `.github/workflows/` — CI

- [`auto-merge-claude.yml`](../.github/workflows/auto-merge-claude.yml) —
  triggers on push to `claude/**`. Fast-forwards `main` from the feature
  branch and deletes the branch. **Belongs to the agent's publish chain;
  do not edit unless you understand the publishing fallback in
  [`docs/routine-setup.md`](routine-setup.md).**
- [`deploy-site.yml`](../.github/workflows/deploy-site.yml) — triggers on
  push to `main` whenever the site inputs change. Runs `site/build.py`,
  uploads the bundle to GitHub Pages.

The two workflows are independent. The site is a *consumer* of the agent's
output and never writes back.

### `site/` — the public reader

A static SPA, served from GitHub Pages. See [`site/README.md`](../site/README.md)
for the internal layout. The site is read-only with respect to the rest of
the repo:

- It only **reads** `briefs/`, `state/`, `sources/`, `README.md`,
  `docs/*.md`, and `prompts/CHANGELOG.md` (rendered on the About page).
- It writes nothing back — its build artifact lives entirely under
  `site/_site/` (gitignored locally; uploaded as a Pages artifact in CI).
- It generates an RSS feed at `_site/feed.xml` (the recent 30 briefs) and
  a section-level search index (every H3 inside every brief is its own
  search entry, jumping straight to the matching paragraph).
- It mirrors `state/run_log.json` to `_site/data/run_log.json` so the
  `#/ops` view can render the run history client-side.

## Data flow per routine run

```
 ┌──────────────┐  preflight   ┌──────────────────────────────┐
 │  routine     │─────────────▶│  load sources.json (active)  │
 │  fires       │              │  load past 7 days of briefs  │
 │  (06:30 CET) │              │  load covered_items.json     │
 └──────┬───────┘              │  load cves_seen.json         │
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
 │ Update state/covered_items.json, state/cves_seen.json,       │
 │ state/deep_dive_history.json, state/run_log.json,            │
 │ sources/sources.json (last-seen, demotions, candidates)      │
 └──────────┬───────────────────────────────────────────────────┘
            ▼
 ┌──────────────────────────────┐
 │ Phase 5.5 — self-check gate  │  ─ JSON parses
 │                              │  ─ every brief CVE is in cves_seen
 │                              │  ─ every § 1–4 item has appearance
 │                              │    today in covered_items
 │  drift → abort commit;       │
 │  brief stays on disk; next   │
 │  run rebuilds state from it  │
 └──────────┬───────────────────┘
            ▼
 ┌──────────────────────────────┐  one of:
 │ git commit + push            │  ① push origin HEAD:main
 │                              │  ② push claude/<name>; CI ff
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
reasoning in [`docs/improvements.md`](improvements.md) before making the
change. The agent's prompts are the load-bearing part of the system; small
contract changes are easy to ship by accident and hard to roll back.
