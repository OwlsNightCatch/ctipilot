# ctipilot.ch — Continuous CTI Intelligence Pipeline

> **AI-generated content notice.** Every intelligence entry in this repository is produced autonomously by an LLM running as a [Claude Code routine](https://docs.claude.com/en/docs/claude-code/routines) on Anthropic-managed cloud infrastructure. The exact models vary based on the routine's runtime configuration; every producing run identifies its main-agent, research and verifier models in its run record under `runs/`. The agent fetches public sources, applies the verification rules in [`prompts/verification.md`](prompts/verification.md), and writes the entry files you see in `entries/`. Every claim in an entry is linked inline to its source. No human reviews entries before publication. Verify any operationally critical claim against the linked primary source before acting on it. The entries are not professional advice and may contain errors.

A **continuous Cyber Threat Intelligence pipeline** covering cyber threats targeting Switzerland and Europe with a public-sector focus (national/cantonal/federal administration, regulators, critical infrastructure, healthcare, education, public-sector technology suppliers). Audience: Tier 2/3 incident responders, threat hunters, detection engineers. Output is **always in English**.

The intel run fires **on whatever cadence the operator sets** (several times a day or once a day are equally first-class); each fire publishes only the *new* verified signal since the previous fire, as individual entry files under `entries/YYYY-MM-DD/`, and appends dated updates or corrections to the entries it already published — **one living entry per finding**, with a changelog. A quality-audit routine re-verifies and improves the store. **There is no brief file — the brief is a query**: [`/live/`](https://ctipilot.ch/live/) renders the entry store over a reader-chosen time window (default: the last 24 hours), and the rolling 24 h reads as one coherent brief regardless of how many runs produced it — every entry held to a constant, strict relevance bar. Its volume follows the window's genuine signal (no fixed count); more runs mean lower latency, never more content.

The repository is the single source of truth for the workflow: prompts, source list, the entry store, the entity registry, per-run records, and every policy document are version-controlled. The normative data model is [`docs/pipeline.md`](docs/pipeline.md).

## Where to read

- **The brief:** [https://ctipilot.ch/live/](https://ctipilot.ch/live/) — the current intelligence window, assembled from the per-finding entries. Pick a wider window (6 / 12 / 24 / 48 / 72 h chips) or a start date; the default 24 h window is server-rendered and fully readable without JavaScript. The live timeline orders findings by **activity** — a finding that received an update or correction floats back to the top under the run that changed it, flagged `UPD`, so a reader notices developments on stories they already read. Day pages use the classic brief structure: TL;DR (+ Immediate-Action callout when one exists) → Active Threats → Trending Vulnerabilities → Research, Reports & Policy → Updates to Prior Coverage → Deep Dive → Action Items → Verification Notes.
- **Day archives:** `https://ctipilot.ch/daily/YYYY-MM-DD/` — one static page per completed UTC day, the browsable historical record.
- **Everything else:** per-entry permalinks (`/entries/<date>/<slug>/`), entity pages (`/entities/<key>/` — actors, campaigns, malware, tools, incidents, reports, plus every CVE), source catalogue (`/sources/`), tag/region indexes, the `/trends/` dashboard and the `/ops/` run-telemetry dashboard.
- **GitHub:** the entries are Markdown files under [`entries/`](entries/) — frontmatter metadata + analysis body, each readable natively on GitHub. Run records live under [`runs/`](runs/).

The site deploys automatically on every push to `main` that touches the content store. See [`site/README.md`](site/README.md) for internals and [`docs/operating.md`](docs/operating.md#3-enable-github-pages) for one-time enablement.

## RSS — ten feeds

[`/feeds/`](https://ctipilot.ch/feeds/) is the single discovery page; every page advertises the two main feeds via `<link rel="alternate" type="application/rss+xml">` autodiscovery.

| URL | Contents | Truncation |
|-----|----------|------------|
| [`/feed.xml`](https://ctipilot.ch/feed.xml) | One item per day page | last 30 |
| [`/feed-items.xml`](https://ctipilot.ch/feed-items.xml) | One item per published entry **plus one item per update / correction** | last 50 |
| [`/feed-public-sector.xml`](https://ctipilot.ch/feed-public-sector.xml) | Per-entry slice — sector: public-sector | last 50 |
| [`/feed-healthcare.xml`](https://ctipilot.ch/feed-healthcare.xml) | Per-entry slice — sector: healthcare | last 50 |
| [`/feed-finance.xml`](https://ctipilot.ch/feed-finance.xml) | Per-entry slice — sector: finance | last 50 |
| [`/feed-energy.xml`](https://ctipilot.ch/feed-energy.xml) | Per-entry slice — sector: energy | last 50 |
| [`/feed-ot-ics.xml`](https://ctipilot.ch/feed-ot-ics.xml) | Per-entry slice — energy / water / manufacturing / transport / `ot-ics` tag | last 50 |
| [`/feed-defense.xml`](https://ctipilot.ch/feed-defense.xml) | Per-entry slice — sector: defense | last 50 |
| [`/feed-telco.xml`](https://ctipilot.ch/feed-telco.xml) | Per-entry slice — sector: telco | last 50 |
| [`/feed-education.xml`](https://ctipilot.ch/feed-education.xml) | Per-entry slice — sector: education | last 50 |

`<pubDate>` derives from each entry's `discovered_at` — the moment the pipeline first verified the finding, not a publish schedule or commit time — and, for the per-update items (`guid` = `<entry url>#update-<at>`), from the changelog record's own timestamp. Subscribing to `feed-items.xml` therefore delivers findings *and their later developments* at true discovery latency. `<content:encoded>` carries full HTML. No UTM parameters, no per-source variants — every link is plain canonical.

## Reader features

- **The dynamic brief.** `/live/` is a rendering over the entry store: default last-24 h window server-rendered (view source and you can read it), client-side re-windowing from `data/briefbook.json` (the last ~35 days of entries) when you pick a different window or a since-date.
- **Per-entry permalinks.** Every finding is a first-class page at `/entries/<date>/<slug>/` with its full metadata badges, its revision history, and a link to the run record that produced it.
- **Notification surface.** `data/alerts.json` carries the last 7 days (by activity moment) of `critical`/`high` entries with headline, summary, immediate-action block, entities, CVEs, `updated_at` and a compact changelog — machine-readable input for paging hooks and chat integrations, including on an update to an already-alerted entry. A `priority: critical` entry always carries a structured `immediate_action` block; the bar for `critical` is deliberately extreme — reserved for genuine stop-and-act items, so criticals stay rare by construction, not by a count cap.
- **Entity registry pages.** Every actor, campaign, malware family, tool, incident and report the pipeline tracks is canonical in [`entities/registry.yaml`](entities/registry.yaml) and rendered at `/entities/<key>/` with coverage timeline, KPI tiles and co-occurrence links; aliases resolve to one page ("UNC6240" and "ShinyHunters" are the same entity, mechanically).
- **One living entry per finding, with a changelog.** Developments, corrections and improvements are appended to the finding's own entry as timestamped `updates[]` records with matching `## Update / Correction / Improvement — <timestamp>` sections; the frontmatter always reflects the current state, the changelog shows how it got there, and `discovered_at` / `updated_at` carry first publication and latest change. The permalink of the original *is* the story's whole evolution.
- **Static HTML.** Every page contains its full content on first paint. JavaScript only enhances: window re-rendering on `/live/`, search autocomplete, filter chips, theme cycle, copy-link.
- **Topbar search** across day pages, entries, entities (every type) and sources — press `/` anywhere. CVE ids match as a single token.
- **Verification badges.** Single-source entries carry their `verification` value (`single-source`, `single-source-national-cert`, `single-source-victim`, `contradicted`) as reader-visible badges, auditable across the site.
- **Operations dashboard** at `/ops/` — recent runs from `runs/**` frontmatter: per-run gap/window, entries published, sub-agent allocation, fetch failures, verification iterations + residuals, prompt version.
- **Trends dashboard** at [`/trends/`](https://ctipilot.ch/trends/) — weekly-bucketed cohort sparklines (ransomware, actively-exploited vulnerabilities, public-sector, OT/ICS, supply-chain, AI-abuse, Switzerland+Europe, nation-state) computed from entry metadata.
- **Print stylesheet** — `Cmd/Ctrl+P` produces a clean, link-annotated PDF for handover.
- **Light / dark / system theme toggle**, persisted per device.
- **Privacy-by-design analytics** — Umami Cloud (no cookies, no fingerprinting), aggregate counts only; `analytics.provider: "none"` in `config/branding.yaml` turns it off entirely. See [`docs/analytics.md`](docs/analytics.md).
- **SEO / machine-readability** — per-page `<title>` / meta description / canonical URL, per-page-type OpenGraph + Twitter cards (`og:type` `article` on entries and day briefs, `website` elsewhere; `article:published_time` from `discovered_at`, `article:modified_time` from `updated_at`), and schema.org **JSON-LD** on every page: `Article`/`TechArticle` per entry (dates, `keywords`, `about` → CVEs/entities), `WebSite` + `Organization` on the home page, `CollectionPage` + `ItemList` on brief and index pages, and a `BreadcrumbList` site-wide. Plus `sitemap.xml` (canonical indexable URLs only — the legacy `noindex` redirect stubs are excluded), a fully permissive `robots.txt` welcoming every crawler and AI agent, and `.well-known/security.txt`. The structured data helps both search engines surface rich results and AI answer engines ground responses in source-linked content.

## What this repo contains

```
.
├── entries/                   # THE content store — one file per verified finding
│   ├── README.md              # Contract pointer (docs/pipeline.md is normative)
│   └── YYYY-MM-DD/<slug>.md   # Frontmatter = full metadata (current state); body = analysis + dated update sections
├── entities/
│   ├── README.md              # Registry contract pointer
│   └── registry.yaml          # Global entity registry (actors, campaigns, malware, …)
├── runs/
│   ├── README.md              # Run-record contract pointer
│   └── YYYY-MM-DD/<run-id>.md # One per fire: telemetry frontmatter + verification notes
├── prompts/                   # Everything the routines load at runtime
│   ├── cti-run.md             # The intel-run master prompt (fired on the operator's cadence)
│   ├── quality-audit.md       # The quality-audit run (builds on cti-run.md)
│   ├── CHANGELOG.md           # Editorial-policy audit trail
│   ├── verification.md        # Fake-news / two-source verification policy
│   ├── entry-template.md      # Canonical entry + run-record skeletons
│   └── check-run-fixes.md     # How to fix common check_run.py FAILs
├── config/
│   ├── org-profile.yaml       # Organization profile: org/sector/region, watchlists, triage scheme, deployment
│   └── branding.yaml          # Site branding: identity, theme, logos, feeds, analytics
├── intel/
│   └── README.md              # Closed-source drop folder (intel/<date>/, no TLP gate, cited by reference)
├── sources/
│   └── sources.json           # Curated, dynamic CTI source list (~150 sources, tiered)
├── state/
│   ├── cves_seen.json         # Flat fast-lookup CVE index (dedup)
│   └── source_health.json     # Bounded source-accessibility history
├── tools/
│   ├── check_run.py           # Phase 5.5 mechanical gate (must exit 0 before commit)
│   ├── build_prior_coverage.py# Per-run dedup index from the entry store
│   ├── run_summary.py         # Compact state digest + rolling-24 h budget snapshot
│   ├── compose_prompts.py     # Renders org-profile.yaml into the ORG-PROFILE managed blocks
│   ├── fetch_source.py        # Bridge fetcher for hosts that 403 the routine UA
│   ├── migrate_briefs.py      # One-shot v2→v3 migration (kept for provenance)
│   ├── migrate_updates.py     # One-shot v3→v4 fold of update_of entries into their roots (provenance)
│   ├── source_candidates.py   # Cited-but-untracked publisher surfacing
│   └── source_health.py       # Recipe-level source accessibility probe
├── site/                      # GitHub Pages reader (static-site generator, stdlib-only)
│   ├── build.py               # SSG entrypoint — dynamic /live/, day pages, entry pages, feeds, ops
│   ├── content_model.py       # THE shared parser/validator for entries, registry, runs
│   ├── taxonomy.yaml          # Controlled vocabulary for entry frontmatter
│   ├── test_build.py          # Stdlib-only smoke tests
│   └── assets/                # CSS, JS (brief.js window renderer), vendored libs
├── docs/
│   ├── pipeline.md            # NORMATIVE data model (entries + changelog, registry, runs)
│   ├── architecture.md        # End-to-end map: what reads/writes what
│   ├── operating.md           # Operator runbook: setup, ops dashboard, troubleshooting
│   ├── routines.md            # Catalog of every routine + in-repo prompt
│   ├── audits/                # Quality-audit reports (one per audit fire)
│   ├── customization.md       # Downstream fork / rebrand guide
│   ├── private-deployment.md  # Host the whole stack org-internally
│   └── analytics.md           # What we measure, what we don't
├── .github/workflows/
│   ├── auto-merge-claude.yml  # Promotes pushes to claude/** branches onto main
│   ├── deploy-site.yml        # Build + deploy site/ to GitHub Pages
│   ├── source-health.yml      # Weekly-cron GitHub Action firing tools/source_health.py
│   └── compose-profile.yml    # Composes config/org-profile.yaml into the prompts on push
├── .claude/agents/
│   ├── cti-research.md        # Parallel research worker (S1–S4 + conditional S5)
│   └── cti-verification.md    # Cold-reader verifier (Claude Sonnet 5; F1–F18)
├── work/<run-id>/             # Per-run forensic artefacts, committed with each run
└── CNAME                      # Custom-domain marker for GitHub Pages → ctipilot.ch
```

For an end-to-end map of how every piece reads and writes data, see [`docs/architecture.md`](docs/architecture.md). For operator setup and the runbook, see [`docs/operating.md`](docs/operating.md).

## Customizing for your organization

The deployment is organization-parameterizable via [`config/org-profile.yaml`](config/org-profile.yaml): describe your organisation / sector / region (the shipped default is the Swiss public-sector deployment), list **products** and **suppliers** the research agents specifically sweep every run, define your own **vulnerability-triage categories** (every CVE-carrying entry then carries a structured `org_triage` rating in your scheme), set the **national-CERT single-source carve-out list** your deployment trusts, and the **policy/regulatory watch** the intel run's S2 (home region & sector) worker sweeps. `python3 tools/compose_prompts.py --write` renders the profile into the prompts and agent definitions (the `compose-profile` workflow does it on push). Watchlist matches only *sharpen* relevance — general threat-landscape coverage always stays primary (hard anti-overshoot rules; watchlist-driven entries carry `watchlist_hit: true` and the ≤ ⅓ guideline applies). See [`docs/operating.md`](docs/operating.md#customizing-the-organization-profile).

The **published site is equally parameterizable** via [`config/branding.yaml`](config/branding.yaml) + [`site/branding/`](site/branding/README.md): site name and wordmark, taglines, theme colors and fonts, logos and favicon, chart palettes, sector RSS slices, trend cohorts, and analytics (`analytics.provider: "none"` is a one-line tracking off switch that also strips the third-party origins from the CSP). The shipped config *is* the ctipilot.ch default and builds a byte-identical site. **Downstream forks customize only `config/*.yaml` + `site/branding/` + `CNAME` + this README and merge upstream conflict-free** — the full guide is [`docs/customization.md`](docs/customization.md).

## Operating principles (non-negotiable)

These principles are encoded in the prompts and enforced by quality gates on each run.

1. **Zero LLM knowledge.** Every fact in any entry comes from a source fetched in that run. Nothing from training data.
2. **Inline source links at the point of claim.** No bibliography. The reader can click through from the exact sentence; the frontmatter `sources[]` list and the body's inline links must agree.
3. **No IOCs.** No hashes, IP addresses, attacker-controlled domains/URLs, or rule code. Entries cover *knowledge* — TTPs, campaigns, actors, vulnerabilities, targeting, sectors, detection concepts. IOC distribution belongs elsewhere (e.g., MISP).
4. **No vanity metrics.** Skip "median dwell time", "X% YoY", and similar vendor-marketing numbers. Operational scoring (CVSS, EPSS, KEV status) is fine.
5. **Always English** (output). Sources may be in German / French / Italian / Polish; entries translate findings and cite originals by their native title with a brief English gloss.
6. **Two-source verification by default**, with carve-outs for a national CERT / government authority disclosing for its own jurisdiction and a victim's own filing about its own incident. Single-source entries carry a structured `verification` value (`single-source`, `single-source-national-cert`, `single-source-victim`) rendered as a reader-visible badge; contradictions are flagged, never silently resolved.
7. **No repetition across runs — one entry per finding.** Every run builds a prior-coverage index over the last 14 days of entries — **including entries earlier runs published the same day** — which the main agent loads in full (every brief's `summary`) into context, checking each candidate against them all; coverage older than 14 days is caught by the store-wide CVE index. A covered story never becomes a second entry: a material development is appended to the existing entry as a timestamped `updates[]` record (with its own body section), and the mechanical gate FAILs a new entry whose CVEs any existing entry already carries unless it declares that entry in `references[]`.
8. **Relevance discipline (no hardcoded volume) — sound *and* complete.** Entry volume follows a strict relevance/actionability gate, not a count — there is no per-run, per-day, or rolling-24 h target or ceiling. The brief is held to two properties of equal weight: **sound** — only relevant, accurate, actionable content (very low false positives, no marginal items); and **complete** — every genuinely-relevant in-window item is published (very low false negatives), so a reader relying on ctipilot.ch alone has no blind spot on anything that matters to their job. A dropped relevant item is as serious as an included marginal one. The window carries exactly the entries that clear the gate, however few or many; more runs mean lower latency, never more content (dedup guarantees it). A run that finds nothing publishes only its run record — a healthy outcome.
9. **Priority is the alert-fatigue control surface.** `critical` ⇔ a structured `immediate_action` block (mechanically enforced) and means "stop reading and act now"; `high` leads the window's TL;DR; `notable` is the standard item; `routine` is kept-for-awareness. A false `critical` trains readers to ignore the channel.
10. **One entity namespace.** Every named actor / campaign / malware / tool / incident / report resolves to a key in `entities/registry.yaml`; aliases are checked before anything new is registered; keys are permanent.
11. **Yearly / periodic threat reports get one dedicated entry**, then are never re-summarised — later coverage references the report's registry entity.
12. **Historical-context rule.** Deep-dive entries on topics with prior public reporting older than ~6 months open with a 3–5-sentence Background paragraph citing 2–3 prior reports.
13. **Recency is gap-derived and self-healing, with a 24 h floor.** Each run's window is computed from the previous run record (`window_hours = max(24, gap_hours + 2)`) — never narrower than a full day even when several fires land inside 24 h; a missed fire simply widens the next window. The underlying event's date is recorded as `event_date` so freshness is never misrepresented.
14. **One new candidate source per run, maximum.** A flood of new candidates is anomalous; overflow waits for the next run.

## The intel run

A scheduled Claude Code routine fires on whatever cadence the operator configured — **several times per working day is the intended pattern** (e.g. every 4–6 hours). The routine is given exactly one instruction: `Read prompts/cti-run.md and execute it.`

The recency window is **derived from the previous run record, not from a hardcoded schedule**: every fire computes `gap_hours` since the last record under `runs/` and covers at least a full day — the gap plus a 2-hour safety overlap, floored at 24 h (`window_hours = max(24, gap_hours + 2)`). This makes the system **self-healing** for missed fires — the next window simply widens — and **cadence-agnostic** — the operator can fire it 1× or 6× a day without touching the prompt. Entry-level dedup (the 14-day in-context prior-coverage load plus the store-wide CVE index) makes the wide, overlapping window harmless: a sub-daily fire re-scans the same 24 h and republishes only the genuinely new delta.

> **One-time setup** required for the routine to publish back to this repo: install the Claude GitHub App on the repo, leave **Allow unrestricted branch pushes** *off* (the routine pushes to `claude/**` only — the auto-merge workflow promotes), and enable Pages. Full instructions: [`docs/operating.md`](docs/operating.md).

Each fire walks through:

1. **Phase 0 — Preflight.** Compute the run id (`YYYY-MM-DDTHHMMZ-intel` — minute-precision, so multiple runs per day are first-class and a same-minute retry is idempotent). Build the prior-coverage index over the last 14 days of entries *including earlier runs today* (`tools/build_prior_coverage.py`) — the main agent loads it in full (every in-window brief) into context — and the compact state digest with the rolling-24 h coverage snapshot (`tools/run_summary.py`); read `entities/registry.yaml` + `site/taxonomy.yaml`; detect closed-source drops under `intel/`.
2. **Phase 1 — Parallel research.** Spawn four `cti-research` sub-agents with tiered source slices — (S1) Active Threats & Trending Vulnerabilities, (S2) Home Region & Sector, (S3) Research & Investigative Reporting, (S4) Incidents & Disclosures — plus a conditional S5 intake when intel drops exist. Every worker reads the prior-coverage index and the registry *before* fetching. Essential-tier sources (national CERTs, CISA, ENISA, …) are attempted every run; standard-tier sources rotate by staleness.
3. **Phase 2 — Verification & triage.** URL spot-checks, two-source / carve-out rule, fake-news guard, CVE verification on NVD/MITRE, the dedup decision (new entry vs update record on the existing entry vs drop), recency re-check, the relevance/actionability gate (drop anything that doesn't clear it, no matter the count), priority assignment.
4. **Phase 3 — Deep-dive selection.** Deep-dive treatment is reserved for an item that earns the long form (rare by construction, not by quota), with category rotation derived from the last 30 days of `deep_dive: true` entries.
5. **Phase 4 — Compose.** One `Write` per new finding — `entries/YYYY-MM-DD/<slug>.md`, strictly from the sub-agents' findings files (anti-embellishment rules; no enrichment from memory) — one appended changelog record + `## Update — <at>` section per existing entry with a material development, plus the run record `runs/YYYY-MM-DD/<run-id>.md`: telemetry frontmatter + verification & coverage notes body.
6. **Phase 5 — State update.** Register new entities (same commit as the entries that need them), sync `state/cves_seen.json`, run the source lifecycle on `sources/sources.json`, refresh `state/source_health.json`.
7. **Phase 5.5 — Mechanical gate.** `python3 tools/check_run.py <run-id>` must exit 0: schema/taxonomy/registry validation, the entry-lifecycle contract (changelog records ⇔ body sections, no silent edits), store-wide CVE dedup, rolling-24 h composition report (informational — no count is gated), `priority` ⇔ `immediate_action`, evidence binding, URL block-list + liveness, IOC scan, run-record completeness, site smoke tests. Fix recipes: [`prompts/check-run-fixes.md`](prompts/check-run-fixes.md).
8. **Phase 5.7 — Verifier loop (gatekeeper).** [`cti-verification`](.claude/agents/cti-verification.md) reads the run's new entries, every entry it updated, and the record cold; a **confirmed CLEAN — two consecutive CLEAN verdicts from independent cold passes — gates publish** (a first CLEAN triggers a confirmation pass). NEEDS_FIXES → remediate, re-run the gate, re-spawn fresh. **8-iteration cap with model rotation** — odd iterations Opus, even iterations the Sonnet-pinned [`cti-verification-alt`](.claude/agents/cti-verification-alt.md) — and a documented fail-open at the cap. Verification can drop entries; it never blocks the run record.
9. **Phase 6 — Commit & push the feature branch**; `auto-merge-claude.yml` promotes to `main` (auto-resolution: `state/*.json` + `entities/registry.yaml` → ours, `sources/sources.json` → theirs), then `deploy-site.yml` rebuilds the site. **Phase 7** polls the run record on `origin/main` and then `data/briefbook.json` for the run id — a pushed feature branch is not a published run.

Full walkthrough lives in the prompt itself ([`prompts/cti-run.md`](prompts/cti-run.md)). Architecture map: [`docs/architecture.md`](docs/architecture.md). Operator runbook: [`docs/operating.md`](docs/operating.md).

## The quality audit

A second routine fires on an operator-chosen cadence (weekly is typical; the prompt is cadence-agnostic and audits the window since its previous record): `Read prompts/quality-audit.md and execute it.` Where the intel run produces intelligence, the audit run audits *it* — institutionalized continuous improvement, modeled on the operator-directed full-store audit of 2026-07-11 ([`docs/audits/2026-07-11-intelligence-quality-audit.md`](docs/audits/2026-07-11-intelligence-quality-audit.md)). The audit prompt **builds on the intel-run prompt** — it `Read`s `cti-run.md` at runtime and defines only the divergent lens, so shared machinery can never copy-drift.

> Until 2026-08-27 a third, weekly strategic routine (`prompts/weekly-summary.md`) produced `horizon: strategic` synthesis entries rendered at `/weekly/`. It was retired by operator decision; its entries remain in the store as archived permalinks, and the ATT&CK-pin freshness duty it carried moved to the audit.

Each fire covers the window since the previous audit record (default 7 days, self-healing, 21-day cap) and asks the two questions the sound-AND-complete doctrine weighs equally: **soundness** — retrospective cold-reader truth passes re-fetch the primary sources behind every published entry and re-check every CVE id/CVSS (against the per-CVE authority), exploitation/KEV claim, version boundary, victim statement, attribution, evidence quote, ATT&CK id (against the pinned dataset) and classification; and **completeness** — independent research sub-agents re-research the window as if for the first time (including per-publisher research-blog listing sweeps, the discovery path CVE/KEV channels miss) and the returns are diffed against the store. On top of both: a systemic review (runaway runs, publish follow-through, reachable-but-unreadable sources, `actions[]`/priority/classification drift), re-checks of the previous audit's watch items, and effectiveness checks on its shipped fixes. The **first fire of each calendar month** also runs the priority-calibration review — the store's priority distribution against the verifier loop's F16 (priority-calibration) findings — to keep the notification channel honest.

Every confirmed defect is root-caused to a specific mechanism and the fix ships in the same run (prompts, tools, sources, agent definitions — under the versioning rule) or becomes a numbered operator recommendation. Output per fire: an audit report `docs/audits/<date>-quality-audit.md`, one run record (`-audit` run-id suffix), audit-recovered entries where a missed item still clears the inclusion gate, corrections and improvements appended to existing entries, and the fixes themselves. A clean audit is a healthy outcome and is reported as such — findings are never manufactured. A wrong published statement is fixed **in the entry that made it** — the erroneous text is corrected where it stands and a timestamped `correction` record explains what was wrong, what is right and the ground-truth source; added precision or sourcing ships as an `improvement` record. There is no separate exception ledger: the entry's own changelog is the audit trail.

## Source list and CVE index — autonomous

The repository is the agent's working memory. Both `sources/sources.json` and `state/cves_seen.json` are maintained by the runs with **no human review gate**. Every change appears in the run's git diff, the commit message, and the run record's `sources_changed[]` telemetry; that's the audit trail.

### Source lifecycle (all transitions autonomous)

- **Discovery → candidate.** When a sub-agent encounters a new high-quality publisher (primary source, editorial track record, in-scope) during research, it's added to `sources.json` with `status: "candidate"`. **At most one new candidate per run** — overflow waits for the next run.
- **Candidate → active.** A candidate is auto-promoted to `active` after **3 distinct runs** in which the source was successfully fetched *and* contributed content to a published entry.
- **Active → demoted (content axis only).** Demotion fires only on the **content axis**, never on the transport axis. After 3 consecutive `consecutive_quiet_periods` increments accompanied by a failed canonical-URL probe, OR after 5 consecutive `consecutive_fetch_failures` of code 404 (sustained 4xx-not-403/429), the source's `reliability` drops one tier and `status` becomes `demoted`. Sustained 403 / 429 / 503 / 5xx **never** demotes — that pattern means the publisher is blocking the agent's request shape, not that the source is dead. For those, the agent records an alternate-URL strategy in `notes` and keeps the source in rotation.
- **Demoted → active (recovery).** A demoted source returns to `active` only when the agent finds a working canonical URL during research and the recovered URL contributes content to an entry.
- **URL updates in place.** Any time a better canonical URL is found for an active source (publisher CMS migration, restructured advisories index), update `url` and append a dated note. The source `id` stays stable so historical references remain valid.

**No source deletion.** Demoted and tier-downgraded sources stay in the file as historical record.

On top of the lifecycle, every source carries a `tier`: the ~14 `essential` records (national CERTs, NCSC-CH, CERT-EU, ENISA, BSI, ANSSI, NCSC-UK, NCSC-NL, CERT-PL, CERT-AT, CISA) are attempted on **every** intel run — a miss is disclosed in the run record — while `standard` records rotate on a staleness ranking so nothing silently starves and nothing floods.

### CVE index — autonomous

The agent appends new CVE IDs, bumps `last_seen` on subsequent appearances, updates `title` or `primary_source_url` when better information emerges, and **removes** entries that turn out to be invalid (e.g., a CVE ID that does not resolve on NVD/MITRE). Removals are documented in the run's commit body.

The current list (~150 sources) covers: Swiss/EU national CERTs (NCSC-CH, GovCERT.ch, CERT-EU, ENISA, BSI, ANSSI, NCSC-UK, NCSC-NL, CERT.at, GovCERT.at, CERT-PL, AGID, CCN-CERT); Swiss security firms (Compass Security, scip AG, OneConsult, InfoGuard, Kudelski Security, PRODAFT); top-tier vendor TI (Mandiant/GTIG, Microsoft, CrowdStrike, Unit 42, Cisco Talos, Volexity, ESET, Kaspersky Securelist, Trend Micro, Check Point, Sophos X-Ops, Secureworks, Recorded Future Insikt, Sekoia, Group-IB, Elastic Security Labs, Huntress, Red Canary, The DFIR Report, Sygnia, Truesec, NCC Group, WithSecure Labs, IBM X-Force, Akamai, Cloudflare Cloudforce One, Trustwave SpiderLabs, Tenable, Rapid7); vulnerability research (CISA KEV, watchTowr Labs, Project Zero, ZDI, VulnCheck, GreyNoise, Shadowserver); OT/ICS (Dragos, SANS ICS); journalism (Krebs, Schneier, Inside IT, Le Monde Informatique, Malwarebytes, The Record, CyberScoop, BleepingComputer, SecurityWeek, Security Affairs, Help Net Security, SANS ISC, Dark Reading); breach trackers (SEC EDGAR 8-K, UK ICO, CNIL FR, EDPB); civil-society research (Citizen Lab); discovery (r/netsec).

## Reader engagement (privacy-by-design)

The site uses **Umami Cloud** for aggregate visitor counts so the operator can see whether the pipeline's output is being read. Umami is a privacy-by-design alternative to mainstream analytics:

- No cookies. No fingerprinting. No personal data persisted.
- Aggregates only: page URL, referrer host, country (IP discarded after lookup), and a daily-rotated hash for unique-visitor counting.
- Search-string parameters are excluded from collection.
- Block at the network layer if you don't want to be counted: `cloud.umami.is` in your browser, ad-blocker, or DNS resolver. The site keeps working without it.

The site's strict CSP allows only `'self'`, `https://cloud.umami.is` (the script), and `https://gateway.umami.is` (the beacon endpoint) for `script-src` / `connect-src` — no other third-party origin can run code or receive data from this page. Full disclosure at [`/about/docs/analytics/`](https://ctipilot.ch/about/docs/analytics/).

The pipeline's Phase 0 does **not** consume any engagement signal. Editorial weighting is purely verification + home-region/coverage-focus nexus + novelty per [`prompts/verification.md`](prompts/verification.md); what is read is not reflected in what is written.

## Security posture

This is a fully autonomous, self-evolving system: the agent edits its own prompts, mutates its own state, and publishes via the feature-branch + auto-merge chain. The defensive frame is "detect and correct", not "prevent at all costs". Highlights:

- **Phase 5.5 mechanical gate.** Before the verifier and before every commit, `tools/check_run.py` must exit 0: every entry's frontmatter parses and is schema- and taxonomy-valid, entity keys resolve in the registry, every changelog record pairs with its body section and `updated_at` mirrors the last one, no entry was edited without a record for the editing run, no store-wide CVE duplicates (unless declared in `references[]`), `priority` ⇔ `immediate_action` holds, evidence quotes are bound, no blocked/dead source URLs, no IOCs, the run record is complete, and the site smoke tests pass.
- **Adversarial verification loop.** An independent cold-reader sub-agent (Claude Sonnet 5, fresh spawn per iteration) re-fetches every URL and traces every claim before publish; the commit is gated on two consecutive CLEAN verdicts.
- **No silent edits.** A published entry changes only through a dated, attributed `updates[]` changelog record with a matching body section — `discovered_at`, `run_id` and the entry id never change, and the gate FAILs any edit without a record for the editing run, so the published record cannot be silently rewritten. Git carries the exact diff of every correction.
- **Feature-branch-only publishing.** Nothing writes to `main` except the auto-merge workflow; every routine commit is a reviewable diff.
- **Vendored library integrity.** `site/build.py` aborts on SHA-256 mismatch against [`site/assets/vendor/HASHES`](site/assets/vendor/HASHES).
- **Strict CSP** delivered via meta tag — no inline scripts; `script-src` / `connect-src` restricted to `'self'` plus the two Umami origins; no inline frames or forms.
- **Build-side Markdown sanitisation** with a pinned tag/URI-scheme allowlist. The build refuses any rendered output that would carry an event handler, a `javascript:` / `data:` URI, or a forbidden tag.
- **Site privacy guarantees:** no cookies, no fingerprinting, no third-party scripts other than Umami's privacy-by-design tracker.

## Verification policy

Entries explicitly defend against fake-news patterns common in CTI feeds: ransomware leak-site theatrics, hallucinated CVE numbers, AI-generated security blogspam, vendor PR dressed as research, re-runs of months-old news (the `event_date` field pins the real timeline), sweeping unbacked attribution, and Telegram/X-only sourcing.

See [`prompts/verification.md`](prompts/verification.md) for the full checklist and the `verification` frontmatter enum that surfaces the sourcing status of every entry.

## License / classification

The repository contains no IOCs and no operationally sensitive material — only public-source synthesis with links. **The pipeline applies no TLP or public/private filter**: everything the agents can read (including anything under [`intel/`](intel/README.md)) is fair game to process, so on the public deployment the control is simply what is committed to the repo. Each entry instead carries an explicit, configurable **classification** — the NATO Admiralty code (a source-reliability letter A–F plus an information-credibility number 1–6) for intelligence items, and the org's patch-triage rating (`org_triage`) for vulnerabilities. Source reliability in [`sources/sources.json`](sources/sources.json) uses the same Admiralty A–F scale. To keep material non-public, run the stack privately (private repo + internal hosting): see [`docs/private-deployment.md`](docs/private-deployment.md).
